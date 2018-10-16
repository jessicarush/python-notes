'''Queues'''


# Queues are peculiar data structures because, like sets, their functionality
# can be handled entirely using lists. However, while lists are extremely
# versatile, they are not always the most efficient data structor for container
# operations. If a program is using a small dataset (hundreds or thousands of
# elements), then lists will probably be ok. However, if you need to scale your
# data into the millions, you may need a more efficient container. Python
# provides three types of queue data structures in its queue module. All
# utilize the same API, but differ in both behavior and structure.


# FIFO queues (first in, first out)
# -----------------------------------------------------------------------------
# These are typically used as a sort of communication medium when one or more
# objects is producing data and one or more other objects is consuming the
# data in some way, probably at a different rate. Think of a messaging
# application that is receiving messages from the network, but can only
# display one message at a time to the user. The other messages can be
# buffered in a queue in the order they are received.

# The Queue class is a good choice when you don't need to access any data
# inside the data structure except the next object to be consumed. They have a
# very simple API. The primary methods are put() and get(). Both accept
# optional arguments to govern what happens if the operation can't successfully
# complete because the queue is either empty (can't get) or full (can't put).
# The default behavior is to block or idly wait until the Queue object has
# data or room available. You can have it raise exceptions instead by passing
# the block=False parameter or have it wait a defined amount of time before
# raising an exception by passing a timeout parameter.

# The Queue class also has methods to check whether the Queue is full() or
# empty() and a few more methods to deal with concurrent access.

from queue import Queue

q = Queue(maxsize=5)

q.put('one')
q.put('two')
q.put('three')
q.put('four')
q.put('five')
# q.put('six', timeout=5)  # raise Full, queue.Full
print('full: ', q.full())

q.get()
q.get()
q.get()
q.get()
last = q.get()
# q.get(block=False)  # raise Empty, queue.Empty
print('last: ', last)
print('empty: ', q.empty())

# full:  True
# last:  five
# empty:  True


# LIFO queues (last in, first out)
# -----------------------------------------------------------------------------
# These queues are more frequently called stacks (think of a stack of papers
# where you can only access the top-most paper). Traditionally, operations on
# stacks are names push and pop, but since python uses the same API as for
# FIFO queues, we use put() and get() still, but they'll both operate off the
# top of the stack.

from queue import LifoQueue

stack = LifoQueue(maxsize=5)

stack.put('one')
stack.put('two')
stack.put('three')
stack.put('four')
stack.put('five')
# stack.put('six', timeout=5)  # raise Full, queue.Full
print('full: ', stack.full())

stack.get()
stack.get()
stack.get()
stack.get()
last = stack.get()
# q.get(block=False)  # raise Empty, queue.Empty
print('last: ', last)
print('empty: ', stack.empty())

# full:  True
# last:  one
# empty:  True


# SimpleQueue
# -----------------------------------------------------------------------------
# New to python 3.7 are SimpleQueues which are unbounded FIFO queues.
# Simple queues lack advanced functionality such as task tracking.


# deques (double-ended queue)
# -----------------------------------------------------------------------------
# Deques (from collections.deque) are a more advanced, extended versions of a
# queue that supports adding and removing items from both ends.

from collections import deque

d = deque('abcdefg')

print(d)
print('length: ', len(d))
print('left end: ', d[0])
print('right end: ', d[-1])
print('pop left: ', d.popleft())
print('pop right: ', d.pop())
print('pop left: ', d.popleft())
print('pop right: ', d.pop())
print('removed: ', d.remove('c'))
d.append('right')
d.appendleft('left')
print('appended: ', d)
d.extend('456')
d.extendleft('321')
print('extended :', d)

# deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# length:  7
# left end:  a
# right end:  g
# pop left:  a
# pop right:  g
# pop left:  b
# pop right:  f
# removed:  None
# appended:  deque(['left', 'd', 'e', 'right'])
# extended : deque(['1', '2', '3', 'left', 'd', 'e', 'right', '4', '5', '6'])


def palindrome(word):
    d = deque(word)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

palindrome('racecar')   # returns True
palindrome('radar')     # returns True
palindrome('maam')      # returns True
palindrome('what')      # returns False

# The example above is just an example. If you wanted to actually check for
# palindromes you could also do:

def palindrome_better(word):
    return word == word[::-1]


# Queues and threads
# -----------------------------------------------------------------------------
# Queues are 'thread-safe' so, for example, you can have a deque be consumed
# from both ends at the same time from separate threads. woah.

import threading
import time

candle = deque(range(5))

def burn(end, source):
    while True:
        try:
            next = source()
        except IndexError:
            break
        else:
            print('{:>6}: {}'.format(end, next))
            time.sleep(0.1)
    print('{:>6}: done.'.format(end))
    return

left = threading.Thread(target=burn, args=('Left', candle.popleft))
right = threading.Thread(target=burn, args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()

#  Left: 0
# Right: 4
#  Left: 1
# Right: 3
#  Left: 2
# Right: done.
#  Left: done.


# Priority Queues
# -----------------------------------------------------------------------------
# The priority queue enforces a very different style of ordering from the
# previous queue implementations. Once again, they follow the exact same get()
# and put() API, but instead of relying on the order that items arrive to
# determine when they should be returned, the most "important" item is
# returned. By convention, the most important, or highest priority item is the
# one that sorts lowest using the less than operator.

# A common convention is to store tuples, where the first element in the tuple
# is the priority, and the second is the data. Another common method is to
# implement the __lt__ special method. Note that it's perfectly acceptable to
# have multiple elements with the same priority but there will be no
# guarantees on which will be returned first.

from queue import PriorityQueue

heap = PriorityQueue()
heap.put((2, 'medium-level task'))
heap.put((1, 'important task 1'))
heap.put((3, 'low-level task'))
heap.put((1, 'important task 2'))

while not heap.empty():
    print(heap.get())

# (1, 'important task 1')
# (1, 'important task 2')
# (2, 'medium-level task')
# (3, 'low-level task')


# Task Queues
# -----------------------------------------------------------------------------
# Task queues provide a convenient solution for an application to request the
# execution of a task by a worker process. Worker processes run independently
# of the application and can even be located on a different system. The
# communication between the application and the workers is done through a
# message queue. The application submits a job, and then monitors its progress
# by interacting with the queue.

# The most popular task queue for Python is Celery. This is a fairly
# sophisticated package that has many options and supports several message
# queues.

# http://www.celeryproject.org/
# https://blog.miguelgrinberg.com/post/using-celery-with-flask

# Another popular Python task queue is Redis Queue or just RQ, which sacrifices
# some flexibility, such as only supporting a Redis message queue, but in
# exchange it is much simpler to set up than Celery.

# http://python-rq.org/


# RQ (task queues)
# ----------------------------------------------------------------------------
# The communication between an application and RQ workers is going to be
# carried out in a Redis message queue, so you need to have a Redis server
# running. See also: noSQL_datastores.py, networks.py, concurrency.py

# $ pip install rq
# $ redis-server

# Example task (app/tasks.py):

import time

def example(seconds):
    print('Starting task...')
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print('Task completed.')

# Run an RQ worker:

# $ rq worker test

# The worker process is now connected to Redis, and watching for any jobs that
# may be assigned to it on a queue named 'test'. In cases where you
# want multiple workers to have more throughput, all you need to do is run
# more instances of rq worker, all connected to the same queue. Then when a
# job shows up in the queue, any of the available worker processes will pick
# it up. In a production environment you will probably want to have at least
# as many workers as available CPUs.

# Execute the tasks:

# In another terminal window, start a python shell session.

# >>> from redis import Redis
# >>> import rq
# >>> q = rq.Queue('test', connection=Redis.from_url('redis://localhost:6379'))
# OR
# >>> q = rq.Queue('test', connection=Redis())
# >>> job = q.enqueue('app.tasks.example', 23)
# >>> job.get_id()
# >>> job.is_finished

# Back in the first terminal window, where the worker is listening, you should
# see it run example function above and then wait.

# The Queue class from RQ represents the task queue as seen from the
# application side. The arguments it takes are the queue name, and a Redis
# connection object, which in this case we initialize with a default URL.
# If you have your Redis server running on a different host or port number,
# you'll need to use a different URL.

# The enqueue() method on the queue is used to add a job to the queue. The
# first argument is the name of the task you want to execute, given directly
# as a function object, or as an import string. I find the string option much
# more convenient, as that makes it unnecessary to import the function on the
# application's side. Any remaining arguments given to enqueue() are going to
# be passed to the function running in the worker.

# The job.get_id() method can be used to obtain the unique identifier assigned
# to the task. The job.is_finished expression will report False until its
# done, then True. Test it!

# Once the function completes, the worker goes back to waiting for new jobs,
# so you can repeat the enqueue() call with different arguments if you want to
# experiment more. The data that is stored in the queue regarding a task will
# stay there for some time (500 seconds by default), but eventually will be
# removed. This is important, the task queue does not preserve a history of
# executed jobs.

# Normally, for a long running task, you will want some sort of progress
# information to be made available to the application, which in turn can show
# it to the user. RQ supports this by using the meta attribute of the job
# object. Here's the example tasks expanded out to include this:

# Example task (app/tasks.py):

import time
from rq import get_current_job

def example(seconds):
    job = get_current_job()
    print('Starting task...')
    for i in range(seconds):
        job.meta['progress'] = 100.0 * i / seconds
        job.save_meta()
        print(i)
        time.sleep(1)
    job.meta['progress'] = 100
    job.save_meta()
    print('Task completed.')

# This new version of example() uses RQ's get_current_job() function to get a
# job instance, which is similar to the one returned to the application when
# it submits the task. The meta attribute of the job object is a dictionary
# where the task can write any custom data that it wants to communicate to the
# application. In this example, We're writing a 'progress' item that represents
# the percentage of completion of the task. Each time the progress is updated
# we call job.save_meta() to instruct RQ to write the data to Redis, where the
# application can find it.

# We can run this new task an monitor its progress like this:

# >>> job = q.enqueue('app.tasks.example', 23)
# >>> job.meta
# {}
# >>> job.refresh()
# >>> job.meta
# {'progress': 69.56521739130434}
# >>> job.refresh()
# >>> job.meta
# {'progress': 100}
# >>> job.is_finished
# True

# The refresh() method needs to be invoked for the contents to be updated
# from Redis.
