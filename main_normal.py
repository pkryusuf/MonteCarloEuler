from normal_class import TicToc, FindEuler

if __name__ == "__main__":

    tt = TicToc()
    find_euler = FindEuler()
    tt.tic()
    e = find_euler.random_numbers(10000000)

    print("E = %12.8f" % e)
    print("TIME = %.6f seconds" % (tt.toc()))
