__author__ = 'Avi'

# from multiprocessing import Process, Queue, Pool, Manager
import multiprocessing as multi
from Queue import Empty
import os
import time
from random import random
from collections import Counter

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name

def worker(num, q):
    """thread worker function"""
    q.put(num)
    # print 'process id:', os.getpid()
    print 'Worker id:', os.getpid(), '-', num
    return


def worker2(in_q):
    """thread worker function"""
    out_l = []
    while True:
        try:
            num = in_q.get(False)
        except Empty:
            break
        # time.sleep(random()*0.5)
        out_l.append((num,os.getpid()))
        # print 'Worker id:', os.getpid(), '-', num
    print 'Worker id:', os.getpid(), '- out,', 'len(list):', len(out_l)
    return out_l


def callback1(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.extend(result)


def worker1(in_q, out_q):
    """thread worker function"""
    # while True:
    while True:
        try:
            num = in_q.get(False)
        except Empty:
            break
        # time.sleep(random()*0.5)
        out_q.put((num,os.getpid()))
        # print 'Worker id:', os.getpid(), '-', num
    print 'Worker id:', os.getpid(), '- out,', 'qsize', out_q.qsize()
    return

if __name__ == '__main__':
    # jobs = []
    # res = 0
    # q_res = multi.Queue()
    # for i in range(5):
    #     p = multi.Process(target=worker, args=(i,q_res))
    #     jobs.append(p)
    #     p.start()
    #     # p.join()

    # print res
    # print 'Queue size:', q_res.qsize()
    # for job in jobs:
    #     job.join()
    # print 'Queue size:', q_res.qsize()
    # while not q_res.empty():
    #     res += q_res.get()
    # print 'res:', res
    load = 10000
    manager = multi.Manager()
    print
    print 'Self made pool:'
    q_in = manager.Queue()
    [q_in.put(x) for x in range(load)]
    print 'Input Queue size:', q_in.qsize()
    q_out = manager.Queue()
    num_of_procs = multi.cpu_count()
    pool = []
    for i in range(num_of_procs):
        pool.append(multi.Process(target=worker1, args=(q_in, q_out)))
        pool[i].start()
    print "Pool:", len(pool)
    for process in pool:
        process.join()

    print 'Input Queue size:', q_in.qsize()
    print 'Output Queue size:', q_out.qsize()
    process_list = []
    while not q_out.empty():
        entry = q_out.get()
        process_list.append(entry[1])
        # print entry
    print Counter(process_list)

    print
    print 'Managed:'
    q_in = manager.Queue()
    [q_in.put(x) for x in range(load)]
    print 'Input Queue size:', q_in.qsize()
    q_out = manager.Queue()
    pool = multi.Pool()
    print 'Pool:', pool._processes
    for process in range(pool._processes):
        workers = pool.apply_async(worker1, (q_in, q_out))
    pool.close()
    pool.join()

    print 'Input Queue size:', q_in.qsize()
    print 'Output Queue size:', q_out.qsize()
    process_list = []
    while not q_out.empty():
        entry = q_out.get()
        process_list.append(entry[1])
        # print entry
    print Counter(process_list)

    print
    print 'Managed (callback):'
    result_list = []
    manager = multi.Manager()
    q_in = manager.Queue()
    [q_in.put(x) for x in range(load)]
    print 'Input Queue size:', q_in.qsize()
    q_out = manager.Queue()
    pool = multi.Pool()
    print 'Pool:', pool._processes
    for process in range(pool._processes):
        workers = pool.apply_async(worker2, (q_in, ), callback = callback1)
    pool.close()
    pool.join()

    print 'Input Queue size:', q_in.qsize()
    print 'Output list size:', len(result_list)
    # print result_list
    print Counter([x[1] for x in result_list])

    # raw_input("Press Enter to continue...")
    # info('main line')
    # p = Process(target=f, args=('bob',))
    # p.start()
    # p.join()
