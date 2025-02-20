# Django API - Blog api - 06: Iterators, Generators, and classic coroutines

> Learning Goals
> - Understanding `async` and `await` constructs
> - Making asynchronous requests

### Yesterday's asynchronous DNS check
**Native Corouine**
```python
import asyncio
import socket
from keyword import kwlist # ['False', 'None', 'True', 'and', etc.]

async def probe(domain):
    loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(domain, None)
        return (domain, False)
    except socket.gaierror:
        return (domain, True)

async def main():
    domains = [ f'{kw}.dev'.lower() for kw in kwlist ] # can either be a list or a generator
    coros = [ probe(domain) for domain in domains]
    for coros in asyncio.as_completed(coros):
        domain, found = await coros
        mark = '+' if found else ' '
        print(f'{mark} {domain}')

asyncio.run(main())

```

## Asynchronous classic coroutines

we could have also used classic coroutines to do the same we did yesterday:


```python
import asyncio
import socket
from keyword import kwlist

# Classic coroutine using 'yield' and 'yield from'
@asyncio.coroutine
def probe(domain):
    loop = asyncio.get_running_loop()
    try:
        # Use 'yield from' to await the result of getaddrinfo
        result = yield from loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return (domain, False)
    return (domain, True)

# Main function with classic coroutine
@asyncio.coroutine
def main():
    domains = [f'{kw}.dev'.lower() for kw in kwlist]  # domain generator
    coros = [probe(domain) for domain in domains]  # List of classic coroutine tasks
    
    for coro in asyncio.as_completed(coros):
        # Use 'yield from' to get results as they complete
        domain, found = yield from coro
        mark = '+' if found else ' '
        print(f'{mark} {domain}')

asyncio.run(main())

```

remarks:

- The @asyncio.coroutine decorator for classic coroutines and generator-based
   coroutines was deprecated in Python 3.8 and is scheduled for removal in Python 3.11

So far, we’ve seen `asyncio.as_completed` and `await` applied
to coroutines.
But they handle any awaitable object.

### New Concept: Awaitable

- The `for` keyword works with iterables.
- The await keyword works with awaitables.

There are three main types of awaitable objects:

1. A `native coroutine object`, which you get by calling a `native coroutine function`
2. An `asyncio.Task`, which you usually get by passing a coroutine object to `asyncio.create_task()`
3. `Futures`: Normally there is no need to create Future objects at the application level code.

## asyncio.Tasks

Tasks are used to schedule coroutines concurrently.

Consider:

Awaiting on a coroutine. The following snippet of code will print “hello” after waiting for 1 second, and then print “world” after waiting for another 2 seconds:

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

```

- above's example is not running asynchronous/concurrently
- let's fix that with `asynico.Task`s 

When a coroutine is wrapped into a Task with functions like `asyncio.create_task()` 
the coroutine is automatically scheduled to run soon.

Let’s modify the above example and run two say_after coroutines concurrently:

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(2, 'hello'))
    task2 = asyncio.create_task(say_after(1, 'world'))
    
    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

## Asynchronous  Requests: Version1

```python
import asyncio
import httpx

async def fetch_url(url, client):
    response = await client.get(url)
    print(url, len(response.text))
    return url, response.text

async def main():

    urls = [
        "https://www.example.com",
        "https://httpbin.org/get",
        "https://www.python.org",       
    ]

    client = httpx.AsyncClient()

    task1 = asyncio.create_task(fetch_url(urls[0], client))
    task2 = asyncio.create_task(fetch_url(urls[1], client))
    task3 = asyncio.create_task(fetch_url(urls[2], client))

    response1 = await task1
    print('Main res1:', len(response1[1]))
    response2 = await task2
    print('Main res2:', len(response2[1]))
    response3 = await task3
    print('Main res2:', len(response2[1]))

asyncio.run(main())

```

## Asynchronous  Requests: Version2

```python
import asyncio
import httpx

async def fetch_url(url, client):
    response = await client.get(url)
    return url, response.text

async def main():

    urls = [
        "https://www.example.com",
        "https://httpbin.org/get",
        "https://www.python.org",       
    ]

    client = httpx.AsyncClient()

    tasks = [fetch_url(url, client) for url in urls]
    
    for completed_task in asyncio.as_completed(tasks):
        response = await completed_task
        print(f"Response length: {len(response[1])} of {response[0]}\n")


asyncio.run(main())

```

- we use `asyncio.as_completed(tasks)` to get an iterator that yields each task's result as soon as it finishes.
- This allows us to handle the responses in the order they are completed, rather than the order in which they were started.
- Your code sits between the asyncio library and the asynchronous libraries you are using, such as HTTPX.

- In an asynchronous program, a user’s function starts the event loop, scheduling an initial coroutine with asyncio.run.
- Each user’s coroutine drives the next with an await expression,
    - forming a channel that enables communication between a library like HTTPX and the event loop.

- `await` borrows most of its implementation from `yield from`, 
    - which also makes `.send` calls to drive coroutines.
- The await chain eventually reaches a low-level awaitable, which returns a generator
- The low-level awaitables and generators at the end of these `await chains` are implemented deep into the libraries

- Using functions like `asyncio.gather` and `asyncio.create_task`, you can start multiple concurrent await channels, enabling concurrent execution of multiple I/O operations driven by a single event loop

## Asynchronous  Requests: Version3

```python
import asyncio
import httpx

async def fetch_url(url, client):
    response = await client.get(url)
    return url, len(response.text)

async def main():

    urls = [
        "https://www.example.com",
        "https://httpbin.org/get",
        "https://www.python.org",       
    ]

    client = httpx.AsyncClient()

    tasks = [fetch_url(url, client) for url in urls]
    
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())

```