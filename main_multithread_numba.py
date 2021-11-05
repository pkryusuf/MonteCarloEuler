import os
from threading import Thread
from numba_class import TicToc, FindEuler

if __name__ == "__main__":

    for _ in range(3):
        tt = TicToc()
        find_euler = FindEuler()
        threads = []
        found_e = []
        n = int(10000000/12)

        tt.tic()

        for i in range(os.cpu_count()):
            found_e.append(FindEuler())
            threads.append(Thread(target=found_e[i].random_numbers_static, args=(n,)))
#           print("Started thread number #%d" % i)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        count = 0
        index = 0
        for find_e in found_e:
            count += find_e.count
            index += find_e.index

        print("E = %12.8f" % (index / count))
        print("TIME = %.6f seconds" % (tt.toc()))

