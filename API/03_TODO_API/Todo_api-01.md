# Todo API

we will build Todo API back-end that contains both a list API endpoint for all todos and dedicated endpoints for each individual todo. 

### Single Page Apps (SPAs)

SPAs are required for mobile apps that run on i0S or Android and is the dominant pattern for web apps that want to take advantage of JavaScript front-end frameworks/Libraries like `React, Vue, Angular`, and others.

There are multiple advantages to adopting a SPA approach. 

Developers can focus on their own area of expertise, typically either front-end or the back-end, but
rarely both. 

It allows for using testing and build tools suitable to the task at hand since building, testing, and deploying a Django project is quite different than doing the same for a JavaScript/React project.

And the forced separation removes the risk of coupling; it is not possible for front-end changes to break the back-end.

For large teams, SPAs make a lot of sense since there is already a built-in separation of tasks.

Even in smaller teams, the adoption cost of an SPA approach
is relatively small. 

The main risk of separating the back-end and the front-end is that it requires domain knowledge in both areas.

While Django is relatively
mature at this point the front-end ecosystem is decidedly not.

A solo developer should think carefully about whether the added complexity of a dedicated JavaScript front-end is worth it versus sprinkling JavaScript into existing Django templates with modern tools like:

- htmx (https://htmx.org/) or
- alpinjs (https://alpinejs.dev/)


### Initial Set Up

