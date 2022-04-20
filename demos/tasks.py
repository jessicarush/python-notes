# This demo file goes with the instructions in queues.py

import time

def example(seconds):
    print('Starting task...')
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print('Task completed.')