'''Misc examples from the Standard Library'''


# https://docs.python.org/3/library/index.html

# -----------------------------------------------------------------------------
# threading
# -----------------------------------------------------------------------------
# This module constructs higher-level threading interfaces on top of the lower
# level _thread module.

import threading

threading_dir = [m for m in dir(threading) if m[0] != '_']

print(threading_dir)
# ['Barrier', 'BoundedSemaphore', 'BrokenBarrierError', 'Condition', 'Event',
# 'ExceptHookArgs', 'Lock', 'RLock', 'Semaphore', 'TIMEOUT_MAX', 'Thread',
# 'ThreadError', 'Timer', 'WeakSet', 'activeCount', 'active_count',
# 'currentThread', 'current_thread', 'enumerate', 'excepthook', 'get_ident',
# 'get_native_id', 'local', 'main_thread', 'setprofile', 'settrace',
# 'stack_size']


# threading.Timer()
# -----------------------------------------------------------------------------

from threading import Timer


def do_something():
    print('doing something...')


t = Timer(10.0, do_something)

t.start()
# will print 'doing something...' after 10 seconds. The rest of the code will
# have time to run first.


# -----------------------------------------------------------------------------
# string
# -----------------------------------------------------------------------------
# A modulle for common string operations.

import string

string_dir = [m for m in dir(string) if m[0] != '_']

print(string_dir)
# ['Formatter', 'Template', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase',
# 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation',
# 'whitespace']

print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)
# 0123456789
print(string.hexdigits)
# 0123456789abcdefABCDEF
print(string.octdigits)
# 01234567
print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace)
#  \t\n\r\x0b\x0c
print(string.printable)
# all of the above

# For example, here I'm using string.digits to clean up a string:
device_name = 'invchg123'
device_type = device_name.rstrip(string.digits)
print(device_type)
# invchg


# string.capwords()
# -----------------------------------------------------------------------------
# capwords() from the string library does a better job of capitalizing:

from string import capwords

example = "I'm super fun."

print(example.title())    # I'M Super Fun.
print(capwords(example))  # I'm Super Fun.


# -----------------------------------------------------------------------------
# random
# -----------------------------------------------------------------------------
# This module implements psuedo-random number generators for various
# distributions.

import random

random_dir = [m for m in dir(random) if m[0] != '_']

print(random_dir)
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST',
# 'SystemRandom', 'TWOPI', 'betavariate', 'choice', 'choices', 'expovariate',
# 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate',
# 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample',
# 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate',
# 'weibullvariate']


# random.choice()
# -----------------------------------------------------------------------------

import random
import string


def random_string(n):
    '''Produces a string of 'n' random ascii letters and digits'''
    s = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(s)


test = random_string(20)

print(test)
# 40Sfk7NFmRjecSSezU9M

# random.choice() takes any sequence. In python, a sequence is and orderd set
# like a list, tuple or string. If you wanted to get a random item from another
# data type like a dictionary, simply convert it to a list. For example:

colors = {
    'aliceblue': '#f0f8ff',
    'antiquewhite': '#faebd7',
    'aqua': '#00ffff'
    }

name, hexvalue = random.choice(list(colors.items()))

print(name, hexvalue)
# antiquewhite #faebd7


# random.random()
# -----------------------------------------------------------------------------
# Gives you a random float between 0 and 1

random_zero_to_one = random.random()

print(f'random.random() gave me: {random_zero_to_one}')
# random.random() gave me: 0.11438855280701565


# random.randint()
# -----------------------------------------------------------------------------
# Gives you a random integer between two values

ri = random.randint(0, 255)

print(ri)
# 206


# random.randbytes()
# -----------------------------------------------------------------------------
# Gives you a random number of bytes (new in Python 3.9)

rb = random.randbytes(4)

print(rb)
# b'=k\xbf4'


# random.range()
# -----------------------------------------------------------------------------
# Returns a random element from range(start, stop, step). This is equivalent to
# choice(range(start, stop, step)), but doesn't actually build a range object.

rr = random.randrange(0, 100, 5)

print(rr)
# 75


# random.sample()
# -----------------------------------------------------------------------------
# Returns a list of 'k' unique elements from a list.

animals = ['dog', 'cat', 'goat', 'chicken', 'squirrel', 'stoat', 'bird']

rs = random.sample(animals, k=3)

print(rs)
# ['stoat', 'goat', 'dog']


# -----------------------------------------------------------------------------
# secrets
# -----------------------------------------------------------------------------
# The secrets module is used for generating cryptographically strong random
# numbers suitable for managing data such as passwords, account authentication,
# security tokens, and related secrets. In particular, secrets should be used
# in preference to the default pseudo-random number generator in the random
# module, which is designed for modelling and simulation, not security or
# cryptography.

# https://docs.python.org/3/library/secrets.html

import secrets

secrets_dir = [m for m in dir(secrets) if m[0] != '_']

print(secrets_dir)
# ['DEFAULT_ENTROPY', 'SystemRandom', 'base64', 'binascii', 'choice',
# 'compare_digest', 'os', 'randbelow', 'randbits', 'token_bytes', 'token_hex',
# 'token_urlsafe']


# -----------------------------------------------------------------------------
# collections
# -----------------------------------------------------------------------------
# This module implements specialized container datatypes providing alternatives
# to the general purpose built-in containers: dict, list, set, tuple.

import collections

collections_dir = [m for m in dir(collections) if m[0] != '_']

print(collections_dir)
# ['ChainMap', 'Counter', 'OrderedDict', 'UserDict', 'UserList', 'UserString',
# 'defaultdict', 'deque', 'namedtuple']

# See queues.py for deque example
# See dictionaries.py for OrderedDict, defaultdict examples
# See tuples.py for namedtuple example


# collections.Counter()
# -----------------------------------------------------------------------------

from collections import Counter

jellybeans = ['red', 'red', 'orange', 'red', 'green', 'green']
jb_counter = Counter(jellybeans)

print(jb_counter)
# Counter({'red': 3, 'green': 2, 'orange': 1})

# most_common() returns all elements in descending order or just the top
# count if optional value passed in:

print(jb_counter.most_common(1))
# [('red', 3)]

# combine, find difference and find intersection of counters using +, -, &

jellybeans1 = ['red', 'red', 'orange', 'red', 'green', 'green']
jellybeans2 = ['black', 'red', 'yellow', 'yellow']

jb_counter1 = Counter(jellybeans1)
jb_counter2 = Counter(jellybeans2)

print(type(jb_counter1))
# <class 'collections.Counter'>

print(jb_counter1 + jb_counter2)
# Counter({'red': 4, 'green': 2, 'yellow': 2, 'orange': 1, 'black': 1})

print(jb_counter1 - jb_counter2)
# Counter({'red': 2, 'green': 2, 'orange': 1})

print(jb_counter2 - jb_counter1)
# Counter({'yellow': 2, 'black': 1})

print(jb_counter1 & jb_counter2)
# Counter({'red': 1})


# -----------------------------------------------------------------------------
# itertools
# -----------------------------------------------------------------------------
# This module contains functions that create iterators for efficient looping.
# itertools are special purpose iterator functions. Each returns one item at
# a time when called within a for loop and remembers its state between calls.

import itertools

itertools_dir = [m for m in dir(itertools) if m[0] != '_']

print(itertools_dir)
# ['accumulate', 'chain', 'combinations', 'combinations_with_replacement',
# 'compress', 'count', 'cycle', 'dropwhile', 'filterfalse', 'groupby',
# 'islice', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee',
# 'zip_longest']


# itertools.chain()
# -----------------------------------------------------------------------------
# chain() – runs through its arguments as if they were a single iterable

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)
    # 1, 2, a, b


# itertools.cycle()
# -----------------------------------------------------------------------------
# cycle() – is an infinite iterator, cycling through its arguments forever:

# for item in itertools.cycle([1, 2]):
#     print(item)


# itertools.accumulate()
# -----------------------------------------------------------------------------
# accumulate() – calculates accumulated values. By default, the sum:

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)
    # 1, 3, 6, 10

# you can provide a function as a second argument to accumulate().
# this will be used instead of addition. The function should take two
# arguments and return a single result.

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
    # 1, 2, 6, 24


# -----------------------------------------------------------------------------
# os
# -----------------------------------------------------------------------------
# This module provides a portable way of using oerating system dependent
# functionality. If you just want to read or write a file see open(), if you
# want to manipulate paths, see the os.path module, and if you want to read all
# the lines in all the files on the command line see the fileinput module. For
# creating temporary files and directories see the tempfile module, and for
# high-level file and directory handling see the shutil module.

import os

os_dir = [m for m in dir(os) if m[0] != '_']

print(os_dir)
# ['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry',
# 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST',
# 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE',
# 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE',
# 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'MutableMapping',
# 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT',
# 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_EXLOCK', 'O_NDELAY', 'O_NOCTTY',
# 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_SHLOCK', 'O_SYNC',
# 'O_TRUNC', 'O_WRONLY', 'POSIX_SPAWN_CLOSE', 'POSIX_SPAWN_DUP2',
# 'POSIX_SPAWN_OPEN', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL',
# 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike',
# 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD',
# 'RTLD_NOW', 'R_OK', 'SCHED_FIFO', 'SCHED_OTHER', 'SCHED_RR', 'SEEK_CUR',
# 'SEEK_DATA', 'SEEK_END', 'SEEK_HOLE', 'SEEK_SET', 'ST_NOSUID', 'ST_RDONLY',
# 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS',
# 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG',
# 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'X_OK',
# 'abc', 'abort', 'access', 'altsep', 'chdir', 'chflags', 'chmod', 'chown',
# 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'cpu_count',
# 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2',
# 'environ', 'environb', 'error', 'execl', 'execle', 'execlp', 'execlpe',
# 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod',
# 'fchown', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode', 'fsencode',
# 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'fwalk', 'get_blocking',
# 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb',
# 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist',
# 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid',
# 'getppid', 'getpriority', 'getsid', 'getuid', 'initgroups', 'isatty', 'kill',
# 'killpg', 'lchflags', 'lchmod', 'lchown', 'linesep', 'link', 'listdir',
# 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 'mkdir',
# 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path',
# 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'popen', 'posix_spawn',
# 'posix_spawnp', 'pread', 'putenv', 'pwrite', 'read', 'readlink',
# 'readv','register_at_fork', 'remove', 'removedirs', 'rename', 'renames',
# 'replace','rmdir', 'scandir', 'sched_get_priority_max', 'sched_get_priority_min',
# 'sched_yield', 'sendfile', 'sep', 'set_blocking', 'set_inheritable',
# 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp',
# 'setpriority', 'setregid', 'setreuid', 'setsid', 'setuid', 'spawnl',
# 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp',
# 'spawnvpe', 'st', 'stat', 'stat_result', 'statvfs', 'statvfs_result',
# 'strerror', 'supports_bytes_environ', 'supports_dir_fd',
# 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks',
# 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp',
# 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate',
# 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv',
# 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitpid', 'walk', 'write',
# 'writev']


# os.system()
# -----------------------------------------------------------------------------
# os.system is a simple way to run a shell command, for example to following
# will print the contents of the current directory:

import os

os.system('ls -alh')


# os.walk()
# -----------------------------------------------------------------------------
# os.walk recursively visits each directory from the root, and for each one,
# returns a tuple. The first item in the tuple is a string containing the
# current directory (path). Next is a list of all the directories in the
# current directory (directories). The last item in the tuple is a list
# containing all the file names (files). Note: os.walk is a generator. If you
# add an input to pause the loop, you can get a sense of how its drilling down
# and through the root directory.

import os

# Put the directory path here:
root = 'data/music'

# for path, directories, files in os.walk(root, topdown=True):
#     print(path)
#     print(directories)
#     for f in files:
#         print('\t', f)

# Use split() and splittext() to strip out the information you want.
# split() breaks a string into a tuple, splitext() will remove file extensions

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)                        # <--path is a string
        # data/music/Beatles/Sgt. Pepper's Lonely Hearts Club Band
        first_split = os.path.split(path)
        print(first_split)                 # <--first_split is a tuple
        # ('data/music/Beatles', "Sgt. Pepper's Lonely Hearts Club Band")
        print(first_split[1])              # <--contains the album name
        # Sgt. Pepper's Lonely Hearts Club Band
        second_split = os.path.split(first_split[0])
        print(second_split)                # <--second_split is a tuple
        # ('data/music', 'Beatles')
        print(second_split[1])             # <--contains the artist name
        # Beatles

        for f in files:                    # <--f is a string, files is a list
            f = os.path.splitext(f)        # f is now a tuple
            print(f)
            # ('13 - A Day In The Life', '.emp3')
            f = f[0].split(' - ')          # f is now a list
            print(f)
            # ['13', 'A Day In The Life']
        print('-' * 50)

# Using this you could easily create a database or structured file format,
# pulling out the specific bits of information.


# -----------------------------------------------------------------------------
# difflib
# -----------------------------------------------------------------------------
# the difflib module contains tools for comparing and working with differences
# between sequences. It's especially useful for comparing text.

import difflib

difflib_dir = [m for m in dir(difflib) if m[0] != '_']

print(difflib_dir)
# ['Differ', 'HtmlDiff', 'IS_CHARACTER_JUNK', 'IS_LINE_JUNK', 'Match',
# 'SequenceMatcher', 'context_diff', 'diff_bytes', 'get_close_matches',
# 'ndiff', 'restore', 'unified_diff']


# difflib.SequenceMatcher()
# -----------------------------------------------------------------------------
# This example uses the SequenceMatcher class and its .ratio() method:

from difflib import SequenceMatcher

test = SequenceMatcher(None, 'rain', 'rainn')
print(type(test))
# <class 'difflib.SequenceMatcher'>
print(test.ratio())
# 0.8888888888888888

test = SequenceMatcher(None, 'rain', 'Rainn')
print(test.ratio())
# 0.6666666666666666

test = SequenceMatcher(None, ' rain', 'r a i n n ')
print(test.ratio())
# 5333333333333333

# The ratio method returns the similarity between two strings on a scale of 0–1.
# Note, it is case sensitive. Extra characters such as spaces and '\n' also
# count. The None argument is where you can specify which characters should be
# ignored (junk).


# difflib.get_close_matches()
# -----------------------------------------------------------------------------

from difflib import get_close_matches

# get_close_matches(word, possibilities, n=3, cutoff=0.6)
#    - Use SequenceMatcher to return list of the best "good enough" matches.
#    - word is the sequence your trying to match (typically a string).
#    - possibilities is a list of sequences to match word against
#      (typically a list of strings).
#    - Optional arg n (default 3) is the maximum number of close matches to
#      return. n must be > 0.
#    - Optional arg ration cutoff (default 0.6) is a float in [0, 1].
#      Possibilities that don't score at least that similar to word are ignored

possibilities = ['train', 'car', 'grain', 'moose', 'rain', 'ball']

print(get_close_matches('rainn', possibilities))
# ['rain', 'train', 'grain']
print(get_close_matches('rainn', possibilities, n=1))
# ['rain']


# -----------------------------------------------------------------------------
# operator
# -----------------------------------------------------------------------------
# This module exports a set of efficient functions corresponsing to the
# instrinsic operators of Python. For example operator.add(a, b) is equivalent
# to a + b.

import operator

operator_dir = [m for m in dir(operator) if m[0] != '_']

print(operator_dir)
# ['abs', 'add', 'and_', 'attrgetter', 'concat', 'contains', 'countOf',
# 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt', 'iadd', 'iand',
# 'iconcat', 'ifloordiv', 'ilshift', 'imatmul', 'imod', 'imul', 'index',
# 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift', 'is_', 'is_not',
# 'isub', 'itemgetter', 'itruediv', 'ixor', 'le', 'length_hint', 'lshift',
# 'lt', 'matmul', 'methodcaller', 'mod', 'mul', 'ne', 'neg', 'not_', 'or_',
# 'pos', 'pow', 'rshift', 'setitem', 'sub', 'truediv', 'truth', 'xor']


# operator.itemgetter()
# -----------------------------------------------------------------------------
# This method allows us to sort lists of dictionaries or tuples by something
# other than their first value. For example:

from operator import itemgetter
from pprint import pprint

l = [('bob', 50), ('mary', 45), ('rick', 72), ('jane', 28)]

l.sort(key=itemgetter(1))

print(l)
# [('jane', 28), ('mary', 45), ('bob', 50), ('rick', 72)]

l = [{'id': 6, 'username': 'bob', 'email': 'bob@email.com'},
     {'id': 1, 'username': 'zed', 'email': 'zed@email.com'},
     {'id': 4, 'username': 'jane', 'email': 'jane@email.com'}]

l.sort(key=itemgetter('username'), reverse=True)

pprint(l)
# [{'email': 'zed@email.com', 'id': 1, 'username': 'zed'},
#  {'email': 'jane@email.com', 'id': 4, 'username': 'jane'},
#  {'email': 'bob@email.com', 'id': 6, 'username': 'bob'}]


# -----------------------------------------------------------------------------
# sys
# -----------------------------------------------------------------------------
# This module provides access to some variables used or maintained by the
# interpreter and to functions that interact strongly with the interpreter.

import sys

sys_dir = [m for m in dir(sys) if m[0] != '_']

print(sys_dir)
# ['abiflags', 'addaudithook', 'api_version', 'argv', 'audit',
# 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names',
# 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook',
# 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable',
# 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks',
# 'get_coroutine_origin_tracking_depth', 'getallocatedblocks',
# 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
# 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
# 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
# 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
# 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules',
# 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix',
# 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth',
# 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
# 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info',
# 'unraisablehook', 'version', 'version_info', 'warnoptions']


# sys.argv
# -----------------------------------------------------------------------------
# This variable is a list of all the arguments passed in the command line.
# The first item will be the filename invoked with python, for example:

# $ python3 standard_library.py

import sys

print(f'sys.argv is {sys.argv}')
# sys.argv is ['/Users/jessicarush/Documents/Coding/Python/github_python/standard_library.py']

# Any additional variables passed in the command line can be accessed using
# list index syntax. For example:

# $ python3 standard_library.py hello

# print(f'sys.argv[1] is {sys.argv[1]} and is {type(sys.argv[1])}')
# sys.argv[1] is hello and is <class 'str'>


# -----------------------------------------------------------------------------
# zoneinfo
# -----------------------------------------------------------------------------
# This module was added in Python 3.9. The zoneinfo module brings support for
# the IANA time zone database to the standard library. It adds
# zoneinfo.ZoneInfo, a concrete datetime.tzinfo implementation backed by the
# system’s time zone data.

import zoneinfo

zoneinfo_dir = [m for m in dir(zoneinfo) if m[0] != '_']

print(zoneinfo_dir)
# TODO


# zoneinfo.ZoneInfo
# -----------------------------------------------------------------------------

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Daylight Savings
dt = datetime(2021, 10, 31, 12, tzinfo=ZoneInfo('America/Vancouver'))

print(dt)
# 2021-10-31 12:00:00-07:00
print(dt.tzname())
# 'PDT'

# Standard time
dt += timedelta(days=7)

print(dt)
# 2020-11-07 12:00:00-08:00
print(dt.tzname())
# PST

# https://www.python.org/dev/peps/pep-0615/
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones


# -----------------------------------------------------------------------------
# graphlib
# -----------------------------------------------------------------------------
# This module was added in Python 3.9. This new module, graphlib contains the
# graphlib.TopologicalSorter class to offer functionality to perform topological
# sorting of graphs.

# https://docs.python.org/3/library/graphlib.html#module-graphlib

import graphlib

graphlib_dir = [m for m in dir(graphlib) if m[0] != '_']

print(graphlib_dir)
# TODO
