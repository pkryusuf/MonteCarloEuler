import time
import random


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindEuler:
    def __init__(self):
        self.count = 0
        self.index = 0

    def random_numbers(self, x):
        for _ in range(x):
            sum_of_randoms = 0
            self.count += 1
            while True:
                sum_of_randoms += random.random()
                self.index += 1
                if sum_of_randoms >= 1:
                    break
        return self.index / self.count
