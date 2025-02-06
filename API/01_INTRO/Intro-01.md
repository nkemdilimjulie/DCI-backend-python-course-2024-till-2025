# Django API - 01: Intro to restful API

> Learning Goals
>- Web API
>- HTTP, Web, Internet
>- Status Codes
>- Restful API
>- we will use traditional Django code (library app with book model) and add API functionality

**Last Session**

- Django Authentication:
    - django.contrib.auth  --> is django's build-in app we can use to setup an authentication system for our users
    - routes    
        - login: we justed needed to provide the template for the form
        - signup: we had to create our own View by using an CreateView: we used `UserCreationForm` 
            - we got the form django.contrib.auth.forms

        ```python
            class SignUpView(CreateView):

                form_class = UserCreationForm
                success_url = reverse_lazy('login')
                template_name = 'signedup.html'
        ```        
        - logout

Where did we specified the redirect after a successful login and logout?

```python
# settings.py
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
```

- urls.py (main)

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path("admin/", admin.site.urls),
path("accounts/", include("django.contrib.auth.urls")),
path("accounts/", include("accounts.urls")), # we used that only for the SignupView 
                                             # in the apps urls.py   path("signup/", SignUpView.as_view(), name="signup"),
path("", include("blog.urls")),
]
```

How can we now protect our routes?

- LoginRequiredMixin
- Middleware

## Web APIs

Before we start building our own web APIs with Django let's recap how the web works. 
After all, a “web API” literally sits on top of the existing architecture of the world wide web and relies on a host of technologies including HTTP, TCP/IP, and more.

### World Wide Web

The Internet is a system of interconnected computer networks 
that has existed since at least the 1960s. 

However, the internet’s early usage was restricted to a small number of isolated networks, 
- largely U.S. government, 
- military (with the intention of creating a decentralized communication network that could withstand potential military disruptions)
- or research labs/unis, that exchanged information electronically. 

- In Europe, the biggest internet node was located at CERN 
    - (EuropeanOrganization for Nuclear Research) in Geneva, Switzerland, which operates the largest particle physics laboratory in the world.

- These experiments generate enormous quantities of data that need to be shared remotely with scientists all around the world.

- Compared with today, though, overall internet usage in the 1980s was miniscule. 

- Most people did not have access to it or even understood why it mattered.

- A small number of internet nodes powered all the traffic and the computers using it were primarily within the same, small networks.

- This all changed in 1989 when a research scientist at CERN, Tim Berners-Lee, invented HTTP and ushered in the modern World Wide Web. 
    - Berners-Lee proposed a system that would allow researchers to share documents and information across different computers/networks 
        - which ultimately led to the creation of the World Wide Web.

His great insight was that the existing hypertext system, where text displayed on a computer screen contained links (hyperlinks) to other documents, could be moved onto the internet.

His invention, Hypertext Transfer Protocol (HTTP), was the first standard, universal way to share documents over the internet. 

It ushered in the concept of web pages:

discrete documents with a URL, links, and resources such as images, audio, or video.

Today, when most people think of “the internet,” they think of the World Wide Web, which is now the primary way that billions of people and computers communicate online.

### URLs

- A URL (Uniform Resource Locator) is the address of a resource on the internet.

- For example, the Google homepage lives at `https://www.google.com`.

- Since web communication occurs via HTTP request/responses are known more formally as HTTP requests and HTTP responses.
- Within a given URL are also several discrete components.

- The first part, **https**, refers to the **scheme** used.
- It tells the web browser how to access resources at the location. 
- For a website this is typically **http or https**, but
    - it could also be **ftp** for files, **smtp** for email, and so on.
- **www.google.com**, is the hostname or the actual name of the site.
- Every URL contains a scheme and a host.
- Many webpages also contain an optional path, too. 
- If you go to the homepage for Python at https://www.python.org and click on the link for the 
    - `About` page you'll be redirected to https://www.python.org/about/. 
    - The **/about/** piece is the path. 

In summary, every URL like https://python.org/about/ has three potential parts: 

- a scheme - https
- a hostname - www.python.org
- and an (optional) path - /about/

### Internet Protocol Suite

Once we know the actual URL of a resource, a whole collection of other technologies must work properly (together) to connect the client with the server and load an actual webpage. 

This is broadly referred to as the internet protocol suite. 

First the browser needs to find the desired
server, somewhere, on the vast internet. 

It uses a domain name service (DNS) to translate the domain name “google.com” into an IP address 
which is a unique sequence of numbers representing every connected device on the internet.

Domain names are used because it is easier for humans to remember a
domain name like “google.com” than an IP address like “172.217.164.68”.


After the browser has the IP address for a given domain, it needs a way to set up a consistent connection with the desired server. 

This happens via the Transmission Control Protocol (TCP)  which provides reliable, ordered, and error-checked delivery of bytes between two application.

To establish a TCP connection between two computers, a three-way “handshake” occurs between the client and server:

1. The client sends a SYN (packet) asking to establish a connection
2. The server responds with a SYN- ACK acknowledging the request and passing a connection parameter
3. The client sends an ACK back to the server confirming the connection

Once the TCP connection is established, the two computers can start communicating via HTTP

### HTTP Verbs

What are the most comman HTTP verbs?

CRUD HTTP Verbs
Create <---> POST
Read   <---> GET
Update <---> PUT/PATCH
Delete <---> DELETE

- Every webpage contains both an address (the URL) as well as a list of approved actions known as HTTP verbs.
- So far we’ve mainly talked about getting a web page, but it’s also possible to create, edit, and delete content.

Consider the Facebook website. 

- After logging in, you can read your timeline, create a new post, or edit/delete an existing one. 
- These four actions Create-Read-Update-Delete are known colloquially as “CRUD”
    - and represent the overwhelming majority of actions taken online.

- The HTTP protocol contains a number of request methods that can be used while requesting information from a server.


### Endpoints

- A `traditional website` consists of web pages with HTML, CSS, images, JavaScript, and more. 
- There is a dedicated URL, such as example.com/1/, for each page. 

- A `web API` also relies on URLs and a corresponding one might be example.com/api/1/,
     - but instead of serving up web pages consumable by humans it produces API endpoints.
- An endpoints contains data, typically in the JSON format, and also a list of available actions (HTTP verbs).
- For example, we could create the following API endpoints for a new website called mysite.

https://www.mysite.com/api/users # GET returns all users
https://www.mysite.com/api/users/<id> # GET returns a single user

- In the first endpoint, /api/users, an available GET request returns a list of all available users.
- This type of endpoint which returns multiple data resources is known as a `collection`.

- The second endpoint, /api/users/<id>, represents a single user.

- A GET request returns information about just that one user.
- If we added a POST to the first endpoint we could create a new user, while adding DELETE to the second endpoint would allow us to delete a single user.

- for example look at https://fakestoreapi.com/

### HTTP

What is the main purpose of HTTP?

- HTTP is a request-response protocol between two computers that have an existing TCP connection.
    - enables the communication between a web client (such as a browser) and a web server

- Typically a client is a web browser but it could also be an iOS app or really any internet-connected device.

Every HTTP message consists of a **status line, headers, and optional body data**.

For example, here is a sample **HTTP message** that a browser might send to request the Google homepage located at 
https://www.google.com.

```bash
GET / HTTP/1.1
Host: google.com
Accept_Language: en-US
```
The top line is known as the **request line**
The two subsequent lines are **HTTP headers**: 
Host is the domain name and Accept_Language is the language to use, in this case American English.
There are many HTTP headers available.

HTTP messages also have an optional third section, known as the body, however we only see a body message with HTTP responses containing data.

For simplicity, let’s assume that the Google homepage only contained the HTML “Hello, World!” This is what the **HTTP response** message from a Google
server might look like.

```bash
HTTP/1.1 200 OK
Date: Mon, 24 Jan 2022 23:26:07 GMT
Server: gws
Accept-Ranges: bytes
Content-Length: 13
Content-Type: text/html; charset=UTF-8
Hello, world!
```
The next five lines are HTTP headers. 
And finally, after a line break, there is our actual body content of “Hello, world!”.

Every HTTP message, whether a request or response, therefore has the following format:

```shell
Response/request line
Headers. ..
(optional) Body
```

### Status Codes

Once your web browser has executed an HTTP Request on a URL there is no guarantee things will actually work! 


Thus there is a quite lengthy list of HTTP Status Codes available to accompany each HTTP response.

You can tell the general type of status code based on the following system:

- 2xx Success - the action requested by the client was received, understood, and accepted
- 3xx Redirection
- 4xx Client Error -there was an error, typically a bad URL request by the client
- 5xx Server Error -the server failed to resolve a request

the most common ones such as 200 (OK), 201 (Created), 301 (Moved Permanently), 404 (Not Found), and 500 (Server Error).


The important thing to remember is that, generally speaking, there are only four potential outcomes to any given HTTP request: 

- it worked (2xx), 
- it was redirected somehow (3xx), 
- the client made an error (4xx), or 
- the server made an error (5xx).

### REST

- Representational State Transfer (REST) is an architecture first proposed in 2000 by Roy Fielding in his dissertation thesis. 
- It is an approach to building APIs on top of the web, which means on top of the HTTP protocol.
- Entire books have been written on what makes an API actually RESTful or not.
- But there are three main traits that we will focus on here

Every RESTful API:
- is stateless, like HTTP
- supports common HTTP verbs (GET, POST, PUT, DELETE, etc.) 
- returns data in either the JSON or XML format

Any RESTful API must, at a minimum, have these three principles.

The standard is important because it provides a consistent way to both design and consume web APIs.

### Library Website

Django REST Framework works alongside the Django web framework to create web APIs
We cannot build a web API with only Django Rest Framework.

It always must be added to a project after Django itself has been installed and configured.

We will review the similarities and differences between traditional Django and Django REST Framework. 

The most important takeaway is that Django creates websites containing webpages, while Django REST Framework creates web APIs which are a collection of URL endpoints containing available HTTP verbs that return JSON.

To illustrate these concepts, we will build out a basic Library website with traditional Django and then extend it into a web API with Django REST
Framework.