'''Concurrency and Networks'''

# Normally we run programs in one place (on a single machine) and one line at
# a time (sequential). Concurrency is running more than one thing at a time.
# Distributed computing or Networking is running in more than one place.

# Concurrency: https://docs.python.org/3/library/concurrency.html


# CPU bound, I/O bound
# -----------------------------------------------------------------------------
# In terms of computing wait times, there are two main concepts:

# CPU bound means the program is bottlenecked by the CPU, or central processing
# unit, while I/O bound means the program is bottlenecked by input/output such
# as reading or writing to disk, network, etc. In general, when optimizing
# computer programs, one tries to seek out the bottleneck and eliminate it.

# Assume we have one CPU bound process and many I/O bound processes. As the
# processes flow around the system, the following scenario may result. The
# CPU-bound process will get and hold the CPU. During this time, all the other
# processes will finish their I/O and will move into the ready queue, waiting
# for the CPU. While the processes wait in the ready queue, the I/O devices are
# idle. Eventually, the CPU-bound process finishes its CPU burst and moves to
# an I/O device. All the I/O-bound processes, which have short CPU bursts,
# execute quickly and move back to the I/O queues. At this point, the CPU sits
# idle. The CPU-bound process will then move back to the ready queue and be
# allocated the CPU. Again, all the I/O processes end up waiting in the ready
# queue until the CPU-bound process is done. There is a convoy effect as all
# the other processes wait for the one big process to get off the CPU. This
# effect results in lower CPU and device utilization than might be possible if
# the shorter processes were allowed to go first.


# Asynchronous
# -----------------------------------------------------------------------------
# Synchronous - the next task begins when the previous task has been completed
# Asynchronous - the ability to not stop and wait on a task which depends on an
# external system, like reading a file, a database, or loading data from the
# internet and continue with the next tasks. When the external system is
# finished it's part, the program can go back to it to complete the task.

# Asynchronous methods run in parallel but on the same thread.

# Asynchronousity only helps reduce processing times when an external system is
# involved. When it comes to the parts of a task that are handled by the
# program itself, the only way to reduce the time is with concurrency... which
# is having more than one task running parallel in separate threads.

# Some platforms implement both concurrency and asynchronousity and others
# just implement asynchronousity. On a single machine, if you want to perform
# multiple tasks as fast as possible, you want to make them independent. Slow
# tasks shouldn't block all the others.

# If you needed to resize an image, your web server code could call a separate,
# dedicated image resizing process to run asynchronously and concurrently. It
# could scale your application "horizontally" by invoking multiple resizing
# processes.

    # Vertical Scaling - improving the capabilities of a node/server
    # Horizontal Scaling - increasing the number of nodes/servers. The capacity
    # of each individual does not change, but its load is decreased by sharing.

# The trick is getting them all to work with one another. Any shared control or
# state means that there will be bottlenecks, failures, more things that can go
# wrong. There are methods to help you deal with complexities:


# Queues
# -----------------------------------------------------------------------------
# Queues are used by both threads and multiprocesses. They can be thought of
# like the thread's inbox. They contain a sequence of work objects that are
# waiting to be processed. Queues are generally shared between two or more
# threads or processes.

# Queues for "distributed task management" are often called work, job or task
# queues. These can be handled in a synchronous or asynchronous way. For
# example, in the analogy of washing dishes, washers wait for a dish to handle,
# and then wait for another worker, the dryer, to give it to (synchronous) or,
# dishes are stacked between workers with different paces, and everyone keeps
# working (asynchronous).

# A queue is like a list: things are added at one end and taken away from the
# other. The most common is referred to as FIFO (first in, first out). However,
# emergency tasks may be assigned a LIFO (last in, first out). You can
# implement queues in many ways. The standard library contains a
# multiprocessing module which contains a queue function. There's also a queue
# module and a threading module.

# see also: queues.py


# Multiprocesses
# -----------------------------------------------------------------------------
# Multiprocesses take advantage of the CPUs ability to utilize multiple CPUs.
# Threads cannot do this because the OS treats them as one process. That being
# said, multiprocesses hog more resources in terms of memory.

# In the following example, the queue looks like a simple iterator, producing a
# series of dishes. It actually starts up it's own separate process along with
# the communication between washer and dryer. Queue, SimpleQueue, JoinableQueue
# are FIFO queues modeled on the queue.Queue class in the standard library.

import multiprocessing as mp

def washer(dishes, queue):
    for dish in dishes:
        print('washing', dish, 'dish')
        queue.put(dish) # adds to the queue

def dryer(queue):
    while True:
        dish = queue.get() # pulls from the queue or waits if nothing there
        print('drying', dish, 'dish')
        queue.task_done()  # see below

dish_queue = mp.JoinableQueue()
dryer_process = mp.Process(target=dryer, args=(dish_queue,))
dryer_process.daemon = True # see below
dryer_process.start()

dishes = ['salad', 'bread', 'main', 'side', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()  # see below (note that dish_queue is its own process)

# washing salad dish
# washing bread dish
# washing main dish
# drying salad dish
# washing side dish
# washing dessert dish
# drying bread dish
# drying main dish
# drying side dish
# drying dessert dish

# JoinableQueue and the final join() method let the washer know that all the
# dishes have been dried. If you use JoinableQueue then you must call
# JoinableQueue.task_done() for each task removed from the queue or else the
# semaphore used to count the number of unfinished tasks may eventually
# overflow, raising an exception.

# (In computer science, a semaphore is a variable or abstract data type used to
# control access to a common resource by multiple processes in a concurrent
# system such as a multiprogramming operating system.)


# Daemon Processes
# -----------------------------------------------------------------------------
# By default the main program will not exit until all of the children have
# exited. There are times however when starting a background process that runs
# without blocking the main program from exiting is useful, such as in services
# where there may not be an easy way to interrupt the worker, or where letting
# it die in the middle of its work does not lose or corrupt data (for example,
# a task that generates “heart beats” for a service monitoring tool).

# This is called a daemon process. The daemon process is terminated
# automatically before the main program exits, to avoid leaving orphaned
# processes running. To mark a process as a daemon, set its daemon attribute
# with a boolean value. The default is for processes to not be daemons, so
# passing True turns the daemon mode on.

# In the example above, if we don't set dryer_process.daemon = True, the main
# program will never be allowed to exit because the dryer function is forever
# waiting for new items to be added to the queue.

# https://pymotw.com/3/multiprocessing/basics.html
# https://docs.python.org/3.6/library/multiprocessing.html


# .join()
# -----------------------------------------------------------------------------
# To wait until a process has completed its work and exited, we use the join
# method. This method can be applied to anything that it a process or a thread.

# This example does a better job of specifically demonstrating what join()
# does. Without join, the main program will start "new_process", sleep for 2
# seconds and then move on to the rest of the code. With join, the program will
# wait until new_process has finished before moving on.

import multiprocessing as mp
import time

def countdown():
    for i in range(0,10):
        print("tick {}".format(i))
        time.sleep(1)

new_process = mp.Process(target=countdown)
new_process.start()

time.sleep(2)

# new_process.join()

print("ok, our main loop can run again!")

# In the dishwasher multiprocessing example above, we used .join() on a queue,
# which has it's own unique process going on behind the scenes that we need to
# wait for before exiting from the main program. If in that example we removed
# the join, we'd see the dishes not get a chance to dry because the program
# exits. Alternatively though, if you also remove .daemon = True on the
# dryer_process, the queue will have time to finish its job because the
# dryer_process now blocks the main program from ever exiting.


# Threading
# -----------------------------------------------------------------------------
# A thread runs within a process and has access to everything within that
# process. For example, __main__ runs in a process and has/is one thread.
# A thread is usually something that runs in a loop forever.

# The concept of blocking is when your main program is stuck waiting for
# I/O bound things. As noted above in multiprocessing, Join is used to make
# the main thread wait for other threads to finish (if you don't, when main
# dies/ends, it kills everything else).

import threading

def info(arg):
    print('Thread: {}, is: {}'.format(threading.current_thread(), arg))

if __name__ == '__main__':
    info('Main Program')
    for n in range(5):
        p = threading.Thread(target=info, args=('function {}'.format(n),))
        p.start()

# Thread: <_MainThread(MainThread, started 140735277539328)>, is: Main Program
# Thread: <Thread(Thread-1, started 123145312813056)>, is: function 0
# Thread: <Thread(Thread-2, started 123145312813056)>, is: function 1
# Thread: <Thread(Thread-3, started 123145312813056)>, is: function 2
# Thread: <Thread(Thread-4, started 123145312813056)>, is: function 3
# Thread: <Thread(Thread-5, started 123145312813056)>, is: function 4

# To reproduce the process-based dish example from above:

import threading
import queue
import time

def washer(dishes, queue):
    for dish in dishes:
        print('washing', dish, 'dish')
        time.sleep(1)
        queue.put(dish)

def dryer(queue):
    while True:
        dish = queue.get()
        print('drying', dish, 'dish')
        time.sleep(2)
        queue.task_done()

dish_queue = queue.Queue()

for n in range(2):
    dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
    dryer_thread.start()

dishes = ['salad', 'bread', 'main', 'side', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()

# washing salad dish
# washing bread dish
# drying salad dish
# washing main dish
# drying bread dish
# washing side dish
# drying main dish
# washing dessert dish
# drying side dish
# drying dessert dish

# NOTE: control c to end this in command line

# One difference between multiprocessing and threading is that threading does
# not have a terminate() function. There's no easy way to end a running thread
# because it can apparently cause all sorts of problems in your code. That
# being said, there are ways... You can have an 'event object' that has a
# set method. All the threads are looping while the event is not set. When the
# event becomes set, they end.

# It should be noted that threads can be dangerous. They can potentially cause
# bugs that are very hard to find. It is said that to use threads, all the code
# in the program and in the external libraries that it uses, must be
# 'thread-safe'. In the examples above, the threads didn't share any global
# variables, so they could run independently without breaking anything.

# In short, threads can be useful and safe when global data is not involved.
# They can be particularly useful for saving time while waiting for some I/O
# operation to complete. In these cases they don't have to fight over data,
# because each has completely separate variables. But threads do sometimes have
# good reason to change global data (to divide up the work). The usual way to
# share data safely is to apply a software 'lock' before modifying a variable
# in a thread.

# It's always a good idea to have something blocking in your looping thread,
# even if is something like time.sleep(0.1). This kind of blocking element
# basically lets the program move on and run the next task(s). The sleep time
# essentially lets you put priority on certain threads. A sleep of 0.1 says
# this thread is super important, check back often as opposed to one that's
# set to sleep for 5 seconds.

# A queue.get() is another example of blocking code and is actually a far
# better method than sleep(). If a queue is empty, the .get() method will wait
# where it is and tell the main program to go ahead and move on to to other
# tasks. It sits and waits at the .get() line until something shows up in the
# queue. When it does, the main program will return priority to the getting
# thread. In summary, think of .get() as .get_or_wait(). If there's nothing
# left in the queue, the getting thread will force the program to move
# past it onto something else and check back later.

# In general, use threads for I/O bound problems and use processes, networking,
# or events for CPU bound problems

# https://pymotw.com/3/threading/index.html
# https://docs.python.org/3/library/threading.html


# Event-driven frameworks
# -----------------------------------------------------------------------------
# An alternative to separate threads and process is event-based programming.
# An event-based program runs a central event loop, doles out any tasks and
# repeats the loop.

# In an event-driven application, there is generally a main loop that listens
# for events, and then triggers a callback function when one of those events
# is detected. In embedded systems the same may be achieved using hardware
# interrupts instead of a constantly running main loop.

# some popular event-driven, asynchronous frameworks:

# http://circuitsframework.com/
# https://twistedmatrix.com/trac/
# http://www.tornadoweb.org/en/stable/  # * mentioned by Twelve-Factor App


# asyncio
# -----------------------------------------------------------------------------
# The asyncio module provides tools for building concurrent applications using
# coroutines (think of coroutines like co-functions, it allows you to control
# many functions running side by side). While threading implements concurrency
# through application threads and multiprocessing implements it through system
# processes, asyncio uses a single-threaded, single-process approach in which
# parts of the application cooperate to switch tasks (functions) explicitly at
# optimal times.

# https://pymotw.com/3/asyncio/index.html
# https://docs.python.org/3/library/asyncio.html


# Queues across Networks
# -----------------------------------------------------------------------------
# This example uses a Redis server. The Redis list acts as the queue. In theory,
# clients would talk to the server via TCP. One or more provider clients pushes
# messages onto one end of the list and one or more client workers watch the
# list with a blocking pop operation. If the list is empty, they wait until a
# message arrives.

# File 1 - redis_washer.py:

import redis

conn = redis.Redis()
print('Washer is starting')
dishes = ['salad', 'bread', 'main', 'side', 'dessert']

for dish in dishes:
    msg = dish.encode('utf-8')
    conn.rpush('dishes', msg)
    print('washed', dish)

conn.rpush('dishes', 'quit')
print('Washer is done')

# File 2 - redis_dryer.py:

import redis

conn = redis.Redis()
print('Dryer is starting')

while True:
    msg = conn.blpop('dishes')
    if not msg:
        break
    val = msg[1].decode('utf-8')
    if val == 'quit':
        break
    print('dried', val)

print('Dryer is done')

# launch Redis server: redis-server

# Start the dryer, and then the washer using '&'. This puts the first program
# in the background and keeps it running:

# $ python3 redis_dryer.py &
# $ python3 redis_washer.py

# Washer is starting
# washed salad
# dried salad
# washed bread
# washed main
# dried bread
# washed side
# dried main
# washed dessert
# dried side
# Washer is done
# dried dessert
# Dryer is done

# As soon as dish IDs started arriving at Redis from the washer process, the
# dryer process starts pulling them back out. Each dish ID is a number except
# the final 'sentinel' value, 'quit'. When the dryer process reads that quit
# dish ID, it quits. You can use a sentinel like this to indicate something
# special from the data stream itself (in this case–that we're done). Otherwise
# there would need to be a lot more program logic.

# Here's a modified dryer that creates multiple dryer processes and adds a
# timeout for each dryer, rather than using a sentinel.

# Alternate File 2 - redis_dryers.py:

def dryer():
    import redis
    import os
    import time
    conn = redis.Redis()
    pid = os.getpid()
    timeout = 20
    print('Dryer process {} is starting'.format(pid))

    while True:
        msg = conn.blpop('dishes', timeout)
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val == 'quit':
            break
        print('{} dried {}'.format(pid, val))
        time.sleep(0.1)
    print('dryer process {} is done'.format(pid))

import multiprocessing
DRYERS = 3
for num in range(DRYERS):
    p = multiprocessing.Process(target=dryer)
    p.start()

# One process reads the quit ID and quits, but the other two linger for
# 20 seconds, then timeout and quit. After the last dryer subprocess quits,
# the main dryer program should end. # BUG: but sometimes it doesn't!

# don't forget to shutdown the server: redis-cli shutdown


# Final Note on Queues
# -----------------------------------------------------------------------------
# Some techniques relating to queues:

# – Fire and forget
#       Just pass things into the queue and don't worry about the consequences.
# – Request-reply
#       The washer receives an acknowledgement from the dryer for each dish in
#       the pipeline.
# – Back pressure or throttling:
#       This technique directs a fast worker to take it easy if someone
#       downstream can't keep up.

# In real systems, you need to be careful that each process or thread is
# keeping up with demand. You might add new tasks to a 'pending' list and let a
# worker process pop the latest message to a 'working' list. When the message
# is done, it's removed from the working list and added to the completed list.
# This lets you know what tasks have failed or are taking too long. You can do
# this kind of thing with Redis yourself or use a system that someone else has
# already written and tested (some of which use Redis):

# http://python-rq.org/
# http://www.celeryproject.org/
# https://github.com/andyet/thoonk.py
