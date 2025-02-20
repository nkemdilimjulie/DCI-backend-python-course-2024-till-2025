# Django API - Blog api - 06: Iterators, Generators, and classic coroutines

> Learning Goals
> - Difference between Iterators & Iterables
> - Introduction of Generators
> - Introduction of classic Coroutines
> - Introduction of native Coroutines 
> - Understanding `async` and `await` constructs
> - Making asynchronous requests

**Last Session**

- Viewsets:
    - has the application logic for all 5 CRUD methods
- together with router we can create all CRUD endpoints for a distinct model
- to reduces our code in the views.py file significantly

```python
#views.py
class MyViewset(ModelViewsSet):
    queryset = MyModel.objects.all()
    serializer_class = MySerializer
    permission_classes = MyPersmission

#urls.py

router = SimpleRouter()
router.register("myentities", MyViewSet, basename='entities')

urlpatterns = router.urls

# urlpattern = [ 
#     path('myentities', MyListView.as_view(), name="entities-list"), 
#     path('myentities', MyDetailPutDestroyView.as_view(), name="entities-detail"), 
#     ]
```
- testing authentication:
    - with APITestCase

```python
class MyAPITestCase(ApiTestCase):

    def create_user_and_login(self):
        credentials = {'username': 'bob', 'password': 1234}
        user = User.objects.create_user(**credentials)
        self.client.login(**credentials)
        res = self.client.get('myentities/')
        self.assertEqual(res.status_code, 200)
```

## Iteration

- Iteration is fundamental to data processing:

    - programs apply computations to data series, from pixels to nucleotides

- If the data doesn’t fit in memory, we need to fetch the items lazily

    - one at a time and on demand.
      That’s what an iterator does.

- we will see how the Iterator design pattern is built into the Python language

- Every standard collection in Python is iterable.
- An iterable is an object that provides an iterator,

    - which Python uses to support operations like:
        - for loops
        - List, dict, and set comprehensions
        - Unpacking assignments
        - Construction of collection instances

- Let's explore iterables by implementing a `Sentence` class:

    - you give its constructor a string with some text,
      - and then you can iterate word by word.

- This will implement the `sequence protocol`,

   - and it’s iterable because all sequences are iterable

```python
import re

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text) # ['word1', 'word2', etc.]

    def __len__(self):
        return len(self.words)

    def __getitem__(self, index):
        return self.words[index]

sentence = Sentence("This is an example.")
print(len(sentence))
print(sentence[1])

for word in sentence:
    print(word)
```

- `__getitem__`(self, index): This method allows accessing individual words in the sentence using indexing
- `__len__`(self): This method returns the number of words in the sentence by returning the length of self.words.

## Why Sequences Are Iterable

- Whenever Python needs to iterate over an object x, it automatically calls `iter(x)`.

The iter built-in function:

1. Checks whether the object implements `__iter__`, and calls that to
   obtain an __iterator__.
2. If `__iter__` is not implemented, but `__getitem__` is, then
   iter() creates an __iterator__ that tries to fetch items by index, starting
   from 0 (zero).
3. If that fails, Python raises TypeError

*An iterator is an object that represents a stream of data. It keeps track of the current position and can fetch the next item in the sequence when requested.*

- That is why all Python sequences are iterable:
    - by definition, they all implement __getitem__.
- In fact, the standard sequences also implement __iter__, because iteration via __getitem__
   exists for backward compatibility

### Iterables Versus Iterators

`_iterable_`
- Any object from which the iter built-in function can obtain an iterator.
- Objects implementing an `__iter__` method returning an iterator are iterable.

- Sequences are always iterable, as are objects implementing a `__getitem__` method that accepts 0-based indexes.

Python obtains iterators from iterables.

**e.g. simple for loop iterating over a str**

The str 'ABC' is the iterable here.
behind the curtain is an iterator:
```python
s = 'ABC'
for char in s:
    print(char)
```

If there was no for statement and we had to emulate the for machinery by
hand with a while loop, this is what we’d have to write:

```python
s = 'ABC'

it = iter(s)

while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break

```

StopIteration signals that the iterator is exhausted.
This exception is
handled internally by the iter() built-in that is part of the logic of for
loops and other iteration contexts like list comprehensions, iterable
unpacking, etc.

Python’s standard interface for an iterator has two methods:

__next__
1. Returns the next item in the series
2. raising `StopIteration` if there are no more items.

__iter__
Returns self;
- this allows iterators to be used where an iterable is
    - expected, for example, in a for loop.

- we can see the iterator how it is built by by iter() from our sequence instance 

```python
import re

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text) # ['word1', 'word2', etc.]

    def __len__(self):
        return len(self.words)

    def __getitem__(self, index):
        return self.words[index]

s = Sentence("This is an example.")

it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) # raises stopIteration
print(list(it))
```

- Because the only methods required of an iterator are __next__ and __iter__,
    - there is no way to check whether there are remaining items,
    - other than to call next() and catch `StopIteration`.
- Also, it’s not possible to “reset” an iterator.
- If you need to start over, 
    - you need to call `iter()` on the iterable that built the iterator in the first place.

## Sentence Classes with __iter__

The next variations of Sentence implement the *standard iterable protocol*,
first by implementing the Iterator design pattern


### A Classic Iterator

```python
import re

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text) # ['word1', 'word2', etc.]

    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self

s = Sentence("This is an example.")
it = iter(s) 
# print(next(it)) # This
# print(next(it)) # is

for word in s:
    print(word)
```

- The SentenceIterator class has the necessary methods for iteration:

- __next__(self): Returns the next word, and raises a StopIteration exception when there are no more words.
- __iter__(self): Returns the iterator object itself


### Sentence Version 3: A Generator Function


```python
import re

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text) # ['word1', 'word2', etc.]

    def __iter__(self):
        for word in self.words:
            yield word


s = Sentence("This is an example.")
it = iter(s) 
# print(next(it)) # This
# print(next(it)) # is

for word in s:
    print(word)
```

__iter__(self):

- This method allows the Sentence object to be iterated over using a for loop.
- It yields each word from self.words, making the Sentence class iterable.
- The yield keyword turns this method into a generator, allowing lazy iteration over the words in the sentence

ow the iterator is in fact a __generator object__, _built automatically when the __iter__ method is called

**Generator functions return generator objects**

### How a Generator Works

Any Python function that has the yield keyword in its body is a generator function: 
a function which, when called, returns a generator object.

```python
def gen_123():
    yield 1
    yield 2
    yield 3

print(gen_123)
print(gen_123())

for i in gen_123():
    print(i)

g = gen_123()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
```

- we see `gen_123` is a function object.
- But when invoked, gen_123() returns a generator object
- Generator objects implement the Iterator interface, so they are also iterable.

- Because g is an iterator, calling next(g) fetches the next item produced by yield.

- generator are not returning 'normal' values
- Calling a generator function returns a generator
- A generator yields values
- A generator doesn’t “return” values in the usual way:


```python
def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

# for c in gen_AB():
#     print('-->',c)
g = gen_AB()
next(g)
next(g)
next(g)
```


#### Iterators vs Generators

__iterator__

- General term for any object that implements a __next__ method.
- Iterators are designed to produce data that is consumed by the client
    - code, i.e., the code that drives the iterator via a for loop or other iterative feature

__generator__

- An iterator built by the Python compiler.
- To create a generator, we don’t implement __next__.
- Instead, we use the `yield` keyword to make a generator function, 
    - which is a factory of generator objects.

- Generator objects provide __next__, so they are iterators.

- Since Python 3.5, we also have asynchronous generators declared with `async def`.


## Classic Coroutines

- classic coroutines are actually generators used in a different way
- And a coroutine object is physically a generator object
- Despite sharing the same underlying implementation
   - the use cases of generators and coroutines in Python are different

### Example: Coroutine to Compute a Running Average

```python
def averager():
    total = 0.0
    count = 0
    average = 0.0

    while True:
        term = yield average # Yield the current average
        print('from coroutine', average)
        total += term           # Add the new term to the total
        count += 1              
        average = total / count # Update the average


avg_gen = averager()

print(next(avg_gen))

print(avg_gen.send(10))
print(avg_gen.send(20))
print(avg_gen.send(30))
```


## Asynchronous Programming

- **Async** is a programming paradigm that allows for **concurrent** execution of tasks, typically in an event-driven model.
- **Concurrency** refers to managing multiple tasks at once, but not necessarily simultaneously.
- **Async** enables concurrency by allowing tasks to be paused (via `await`) /suspend (like the `yield`) and resumed without blocking the entire program, improving efficiency.

- However, **async** doesn't imply tasks are running at the same time
    - just that they are being managed in a non-blocking manner.

- Instead, the system switches between tasks, often quickly, making it appear as though they are running together.
- Concurrency is useful for managing multiple tasks that are logically independent and may spend time waiting for I/O operations, like file access or network communication.

- This allows the system to keep working on other tasks while waiting.

**Example**: A web server handling multiple requests at once by switching between them without waiting for each one to finish.


### Natives versus classic Coroutines

- *Classic coroutine*
    -  A generator function that consumes data sent to it via my_coro.send(data) calls, 
    and reads that data by using yield in an expression.

- *Native coroutine*
    - A coroutine function defined with `async def`.
    - You can delegate from a native coroutine to another native coroutine using the await keyword
    - The async def statement always defines a native coroutine, even if the await keyword is not used in its body.
    - The await keyword cannot be used outside of a native coroutine.

### An asyncio Example: Probing Domains

Imagine you plan to register
a domain using a Python keyword and the .dev suffix—for example:

http://await.dev

we can use using `asyncio` and `native coroutines` to check several domains concurrently

This is the output it produces:

```bash
$ python3 blog_dns.py
with.dev
+ elif.dev
+ def.dev
from.dev
else.dev
or.dev
if.dev
del.dev
+ as.dev
none.dev
pass.dev
true.dev
+ in.dev
+ for.dev
+ is.dev
+ and.dev
+ try.dev
+ not.dev
```

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

1. `probe` returns a tuple with the domain name and a boolean;
   - True means the domain is available
   - Returning the domain name will make it easier to display the results.

2. Get a reference to the `asyncio event loop` : `loop.getaddrinfo(…)` 
3. The `loop.getaddrinfo(…)` coroutine method returns
  
   - a five-part tuple of parameters to connect to the given address
   - In this example, we don’t need the result.
   - If we got it, the domain resolves;
   - getaddrinfo() is a method provided by Python's socket library (and exposed via asyncio for asynchronous operations)
   - It is used to perform a DNS lookup and get information about how to reach a specific domain over the network.

4. `main` must be a `coroutine`, so that we can use `await` in it.
5. `domain Generator` to yield domain names with the .dev suffix based on python keywords.
6. coros is a `list of coroutine` objects by invoking the probe coroutine with
7. `asyncio.as_completed` is a generator
    - that yields coroutines that return the results of the coroutines passed to it
    - in the order they are completed and
        - not in the order they were submitted.

8. the `await expression` will not block
    - we need it to get the result from coro.
9. `asyncio.run` starts the event loop and returns only when the event loop exits.
    - This is a common pattern for scripts that use asyncio:
   - implement main as a coroutine, and drive it with asyncio.run

- Using the syntax `await loop.getaddrinfo(...)` avoids blocking
   because `await` *suspends* the current coroutine object.
- For example, during the execution of the `probe('if.dev')` coroutine,

    - a new coroutine object is created by `getaddrinfo('if.dev', None)`.

- Awaiting it starts the low-level **addrinfo query** and

    - yields control back to the event loop,
    - not to the probe(‘if.dev’) coroutine, which is suspended.

- The event loop can then drive other pending coroutine objects, such as `probe('or.dev')`.
- When the event loop gets a response for the `getaddrinfo('if.dev', None) query`,
    - that specific coroutine object resumes and returns control back to the `probe('if.dev')`
    - which was suspended at await
    - and can now handle a possible exception and return the result tuple.

