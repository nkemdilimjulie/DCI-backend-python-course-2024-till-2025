# Django API - Blog - 4: CRUD with Viewsets & Routers & Tests

> Learning Goals
>- Understanding and implementing Viewset and Routers
>- Test (with & without Login)

**Last Session**
- Authentication: 

What is the difference between Authorization and Authentication?
- Authorization is more about privileges (=`permissions`)
- `Authentication` is about Login and being recognized as a User by the backend system
    - depending what user is logged in different privileges are granted

- Authentication options:
    1. session based authentication
        - relies on cookies 
            - in a session cookie the session id is stored
            - in our django database we have a session table
                - here session objects are stored (== row)
                - each session object has a unique session id
    2. basic authentication
        - here we use a username and password for each request
            - it is encoded in our response header: `Authorization`
                - e.g. `piet3:6pS3s.xA!4sqhpk` would be encoded to `cGlldDM6NnBTM3MueEEhNHNxaHBr`
                - therefore the complete header would like like `Authorization: Basic cGlldDM6NnBTM3MueEEhNHNxa`
                - Warning: the password is only encoded but not encrypted
                - if you only would use HTTP instead of HTTPS everyone could spy on your login credentials        
    3. Token based authentication:
        - user can obtain a Token during login
        - instead of sending our credentials every time with each request; we just can send our token
        3. 2. JWT authentication 

# Viewsets and Routers

Viewsets and routers are tools within Django REST Framework that can speed-up API development.
- a single viewset can replace multiple related views.
- router can automatically generate URLSs


### User endpoints

Currently we have the following API endpoints in our project.

|Endpoint |HTTP Verb|
|------|-----|
|/ |GET |
|/:pk/ |GET |
| /rest-auth/login | POST |
| /rest-auth/logout | POST |


Let's now add two additional endpoints to list all users and individual
users. 

steps:
- new serializer class for the model
- new views for each endpoint
- new URL routes for each endpoint

### Serializer

```python
# posts/serializers.py
from django.contrib.auth import get_user_model # new
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "created_at",)

class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)
```

By using get_user_model we ensure that we are referring to the correct user model, whether it is the default User or a custom user model


### Views

```python
# posts/views.py
from django.contrib.auth import get_user_model # new
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer # new

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
```

- there is quite a bit of repetition here

### Urls

```python
# posts/urls.py
from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail # new

urlpatterns = [
    path("users/", UserList.as_view()), # new
    path("users/<int:pk>/", UserDetail.as_view()), # new
    path("", PostList.as_view()),
    path("<int:pk>/", PostDetail.as_view()),
]
```

### Viewsets

A viewset is a way to combine the logic for multiple related views into a single class.

```python
# posts/views.py
from django.contrib.auth import get_user_model
from rest_framework import viewsets # new
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
```

- we no longer have to repeat the same queryset and serializer_class for each view

### Routers

- Routers work directly with viewsets
- automatically generate URL patterns

```python
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register("posts", PostViewSet, basename="posts")  # Register PostViewSet
router.register("users", UserViewSet, basename="users")  # Register UserViewSet

# No need for path-based views since we're using viewsets
urlpatterns = router.urls

```
### Permissions

- Any authenticated user can add a new user on the User List page
- there are no explicit permissions for UserViewSet.

- we want to restrict access to superusers only.

```python
# posts/views.py
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser # new
from .models import Post
 from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer ‘

class PostViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser] # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
```

### Conclusion

- Viewsets and routers are a powerful abstraction that reduce the amount of code
- the decision of when to add viewsets and routers to your project is subjective.

- start with views and URLs
- As your API grows in complexity if you find yourself repeating the same endpoint patterns over and over again, then look to viewsets and routers

### Tests

Let's test a variety of important scenarios:

1. Accessing the list of posts without being authenticated.
2. Accessing the list of posts as a regular authenticated user.
3. Accessing the list of posts as an admin user.

```python
    User.objects.create_user(username="...", email="...", password="...") # hashes the password
    User.objects.create(username="...", email="...", password="...") # we would need to hash the password before

    User.objects.create_superuser(username="...", email="...", password="...") # sets is_staff to true

```

```python
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post

User = get_user_model()

# class BlogTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create_user(
#             username="testuser",
#             email="bla@gmail.com",
#             password="secret",
#         )

#         cls.post = Post.objects.create(
#             author=cls.user,
#             title="A good title",
#             body="Nice body content",
#         )

#     def test_post_model(self):
#         self.assertEqual(self.post.author.username, 'testuser')

class PostAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="user",
            password="secret",
        )
        cls.admin_user = User.objects.create_superuser(
            username="admin",
            password="adminpassword",
        )

        cls.post = Post.objects.create(
            title='Sample Post',
            body='Sample Body',
            author=cls.user,
        )

        cls.post_list_url = reverse('posts-list')
        cls.post_detail_url = reverse('posts-detail', kwargs={'pk': 
                                cls.post.pk})

    def test_list_unauthenticated(self):
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_authenticated(self):
        self.client.login(username='user', password='secret')
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_admin(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_detail_unauthenticated(self):
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_detail_authenticated(self):
        self.client.login(username='user', password='secret')
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_creation_as_authenticated(self):
        self.client.login(username='user', password='secret')
        response = self.client.post(
            self.post_list_url,
            {'title': 'New Post', 'body': 'New Content', 'author': self.user.id}
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.last().author, self.user)

    def test_update_post_authenticated_not_author(self):
        another_user = User.objects.create_user(username='anotheruser', password='1234')
        self.client.login(username='anotheruser', password='1234')
        update_data = {'title': 'Updated t.', 'body': 'updated b.', 'author': another_user.id}
        response = self.client.put(
            self.post_detail_url,
            update_data,
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
```