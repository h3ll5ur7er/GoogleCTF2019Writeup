from hashlib import md5
from random import randint as rng, choice
import string
from threading import Thread, RLock
from collections import deque
from time import sleep
from math import ceil

string_prefix = "flagrom-"
thread_pool_size = 7
max_tries = 10000000
max_tries_seq = 1000000000000000000000000
log_frequency = 10000000
numeric_max_value = 999999999999999999999999999999999
alphabetic_characters = string.ascii_lowercase + string.ascii_uppercase
parallel_operations_to_schedule = 1000 * thread_pool_size
alphabetic_max_length = 32

class WorkerThread(Thread):
    def __init__(self, idx, *a, **kw):
        super().__init__()
        self.lock = RLock()
        self.queue = deque()
        self.running = None
        self.idle = True
        self.idx = idx

    def run(self, *a, **kw):
        print("starting worker thread ", self.idx)
        self.running = True
        while self.running:
            if len(self.queue) == 0:
                self.idle = True
                sleep(0.2)
            else:
                self.idle = False
                with self.lock:
                    task = self.queue.popleft()
                task()

    def enqueue(self, *tasks):
        print("scheduling ", len(tasks), " tasks on thread ", self.idx)
        self.idle = False
        with self.lock:
            for task in tasks:
                self.queue.append(task)

    def stop(self):
        self.running = False

class ThreadPool:
    def __init__(self, size):
        self.size = size
        self.threads = [WorkerThread(i) for i in range(self.size)]
        for thread in self.threads:
            thread.start()

    def schedule_tasks(self, *tasks):
        task_count = len(tasks)
        tasks_per_group = ceil(task_count/self.size)
        print("scheduling {} tasks per thread".format(tasks_per_group))
        task_groups = [tasks[i*tasks_per_group:(i+1)*tasks_per_group] for i in range(self.size)]
        for i in range(self.size):
            self.threads[i].enqueue(*task_groups[i])

    def stop(self):
        for thread in self.threads:
            thread.stop()

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = alphabetic_characters
    s = ""
    for i in range(stringLength):
        s+=letters[rng(0, len(letters)-1)]
    return s

def alphabetic_worker_task(pool, candidate, candidate_prefix, hash_prefix):
    def task():
        candidate = candidate_prefix + candidate
        the_hash = md5(candidate.encode("ascii")).hexdigest()
        if the_hash.startswith(hash_prefix):
            print("found matching hash: ", the_hash)
            print("found matching string: ", candidate)
            if pool is not None:
                pool.stop()
            else:
                exit(0)
    return task

def numeric_worker_task(pool, candidate, candidate_prefix, hash_prefix):
    candidate = candidate_prefix + str(candidate)
    the_hash = md5(candidate.encode("ascii")).hexdigest()
    if the_hash.startswith(hash_prefix):
        print("found matching hash: ", the_hash)
        print("found matching string: ", candidate)
        if pool is not None:
            pool.stop()
        else:
            exit(0)

def alphabetic(md5_prefix):
    for i in range(max_tries_seq):
        if i%log_frequency == 0:
            print("--- ", i, " ---")
        str_len = rng(7, alphabetic_max_length)
        s = string_prefix + randomString(str_len)
        
        alphabetic_worker_task(None, s, string_prefix, md5_prefix)

def numeric(md5_prefix):
    for i in range(max_tries_seq):
        if i%log_frequency == 0:
            print("--- ", i, " ---")
        s = string_prefix + str(rng(1, numeric_max_value))
        
        numeric_worker_task(None, s, string_prefix, md5_prefix)

def alphabetic_parallel(md5_prefix):
    try:
        pool = ThreadPool(thread_pool_size)
        pool.schedule_tasks(*[lambda: alphabetic_worker_task(pool,  randomString(rng(1, alphabetic_max_length)),string_prefix, md5_prefix) for i in range(max_tries)])
    except:
        pool.stop()


def numeric_parallel(md5_prefix):
    try:
        pool = ThreadPool(thread_pool_size)
        while 1:
            tasks = [lambda: numeric_worker_task(pool, rng(1, numeric_max_value),string_prefix, md5_prefix) for i in range(max_tries)]
            pool.schedule_tasks(*tasks)
            while not all([t.idle for t in pool.threads]):
                pass
    except:
        pool.stop()

def main(*args):
    if len(args) != 1:
        print("usage: python hashfinder.py md5_prefix")
        exit(1)
    # alphabetic(args[0])
    numeric(args[0])
    #numeric_parallel(args[0])

if __name__ == "__main__":
    from sys import argv
    main(*argv[1:])
