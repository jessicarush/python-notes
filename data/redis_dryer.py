# import redis
#
# conn = redis.Redis()
# print('Dryer is starting')
#
# while True:
#     msg = conn.blpop('dishes')
#     if not msg:
#         break
#     val = msg[1].decode('utf-8')
#     if val == 'quit':
#         break
#     print('dried', val)
#
# print('Dryer is done')



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
