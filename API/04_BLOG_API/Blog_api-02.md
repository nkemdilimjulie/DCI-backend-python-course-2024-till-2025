# Django API - Blog - 2: Permissions & Testing

>Learning Goals
>- Understanding django restful persission system
    >- project-level permissions
    >- custom permissions
>- test our project


**Last Session**
- AbstractUser
    - we can import it from `django.contrib.auth.models`
    - inherits all columns from the standard User model in django
- CustomUser
    - here we can add more columns to the (Custom)User model
- in the settings we can swap the User model with the CustomUser used for authentication:
```python
AUTH_USER_MODEL = "accounts.CustomUser"
```

- in order to add our CustomUser to the Admin Page we needed:
    - UserCreationForm
    - UserChangeForm
- these forms we inherited from `django.contrib.auth.forms`
- we had also to use the  AdminClass from django's `auth` app:
    - here we can define e.g. columns are display in admin's listview 

- we created CRUD endpoints:
    - RetrieveUpdateDestroyAPIView --> instead of defining 3 Views and urlpattern
                                --> we just needed 1 View/urlpattern
    - ListCreateAPIView --> instead of 2 we needed only 1

# Permissions
Django REST Framework ships with several out-of-the-box permissions settings that we can use to secure our API These can be applied at a project-level (1), a view-level (2), or at any individual model level(3).


### Project-Level Permissions

Django REST Framework has a host of configurations that are namespaced inside a single Django setting called REST_FRAMEWORK. 

```python
# django_project/settings.py
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated", # new
    ],
}
```

There are actually four built-in project-level permissions settings we can use:
- `AllowAny` - any user, authenticated or not, has full access
- `IsAuthenticated` - only authenticated, registered users have access
- `IsAdminUser` - only admins/superusers have access
- `IsAuthenticatedOrReadOnly` - unauthorized users can view any page, but only authenticated users have write, edit, or delete privileges

### Add Log In and Log Out

how can our new user log in to the browsable API? 

We can do it by updating our project-level URLconf.

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/vi/", include("posts.urls")),
    path("api-auth/", include("rest_framework.urls")), # new
]
```

When we navigate to our browsable API at http://127.0.0.1:8000/api/v1/, then there is a subtle change: a “Log in” link in the upper right corner. 


### View-Level Permissions

Permissions can be added at the view-level too for more granular control. 

Let's update our PostDetail view so that only admin users can view it. 


If we do this correctly, a logged out user can’t view the API at all, a logged-in user can view the list page, but only an admin can see the detail page.

In the posts/views.py file import permissions from Django REST Framework and then add a permission_classes field to PostDetail that sets it to IsAdminUser.

```python
# posts/views.py
from rest_framework import generics, permissions # new
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

hat’s all we need, to add view-level permission.

Refresh the browsable API at http://127.0.0.1:8000/api/v1/ and the Post List page is still viewable if we are logged-in as normal user.

However if you navigate to http://127.0.0.1:8000/api/v1/1/ to see the Post Detail page an HTTP 403 Forbidden status code is displayed.

If you log out of the browsable admin and then log in with your admin account the Post Detail page will still be visible. 

So we have effectively applied a view-level permission.

### Custom Permissions

Here is the actual source code which is available on Github:

```python

class BasePermission:
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
        """
        Return “True’ if permission is granted, ‘False' otherwise. 
        """
        return True

    def has_object_permission(self, request, view, obj)
        """
        Return “True’ if permission is granted, ‘False' otherwise.
        """
        return True
```

For a custom permission class you can override one or both of these methods. 

has_permission works on list views while detail views execute both:
- first has_permission and then, if that passes, has_object_permission.

It is **strongly advised** to always set both methods explicitly because each defaults to True, meaning they will allow access implicitly unless set explicitly.

In our case, we want only the author of a blog post to have write permissions to edit or delete it. 

We also want to restrict read-only list view to authenticated users. 

To do this we'll create a new file called posts/permissions.py and fill it with the following code:

```python
# posts/permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request so we'll always
        # allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
```

We import permissions at the top and then create a custom class IsAuthorOrReadOnly which extends BasePermission. 

The first method, has_permission, requires that a user be logged in, or authenticated, in order to have access. 

The second method, has_object_permission, allows read-only requests but limits write permissions to only the author of the blog post. 

We access the author field via obj.author and the current user with request.user.

in the views.py file we can remove the permissions import because we will swap out PostDetail’s permissions
IsAdminUser in favor of importing our custom IsAuthorOrReadOnly permission. 

```python
# posts/views.py
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```
And we're done.

To create only posts for the currently logged-in user you can change the code as follows:

```python
#posts/views.py
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer

class PostList(ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    # permission_classes = (permissions.IsAdminUser,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

```

To display only post of the currently logged-in user if not superuser:

```python
from rest_framework.generics import (ListCreateAPIView,
                            RetrieveUpdateDestroyAPIView)
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer

class PostList(ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(author=self.request.user)
```