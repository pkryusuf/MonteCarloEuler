from numba_class import TicToc, FindEuler

if __name__ == "__main__":

    for _ in range(3):
        tt = TicToc()
        find_euler = FindEuler()
        tt.tic()
        find_euler.random_numbers_static(10000000)
        e = find_euler.find_E()
        print("E = %12.8f" % e)
        print("TIME = %.6f seconds" % (tt.toc()))
