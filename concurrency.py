# Concurrency and Networks

# Normally we run programs in one place (on a single machine) and one line at a 
# time (sequential). Concurrency is running more than one thing at at time. 
# Distributed computing or Networking is running in more than one place.

# Concurrency: https://docs.python.org/3/library/concurrency.html

# In terms computing of wait times, there are two main concepts:

# CPU bound means the program is bottlenecked by the CPU, or central processing
# unit, while I/O bound means the program is bottlenecked by I/O, or
# input/output, such as reading or writing to disk, network, etc. In general,
# when optimizing computer programs, one tries to seek out the bottleneck and
# eliminate it.

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

# Some platforms implement both concurrency and asynchronousness and others
# just implement asynchronousness.

# On a single machine, if you want to perform multiple tasks as fast as
# possible, you want to make them independent. Slow tasks shouldn’t block all
# the others.

# If you needed to resize an image, your web server code could call a separate,
# dedicated image resizing process to run asynchronously and concurrently. It
# could scale your application horizontally by invoking multiple resizing
# processes.

    # Vertical Scaling - improving the capabilities of a node/server
    # Horizontal Scaling - increasing the number of nodes/servers. The capacity 
    # of each individual does not change, but its load is decreased by sharing.

# The trick is getting them all to work with one another. Any shared control or
# state means that there will be bottlenecks, failures, more things that can go
# wrong. There are methods to help you deal with complexities:

# Queues

# A queue is like a list: things are added at one end and taken away from the
# other. The most common is referred to as FIFO (first in, first out). Also: a
# sequence of work objects that are waiting to be processed. 

... more to come
