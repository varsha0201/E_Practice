# python program to illustarate the concept
# of threading
# importing the threading module
import threading

def print_cube(num):
    print("Cube: {}".format(num*num*num))

def print_square(num):
    print("Square: {}".format(num*num))

if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target= print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    # staring thread 1
    t1.start()

    # staring thread 2
    t2.start()

    # wait until thread 1 is completly excuted
    t1.join()

    # wait until thread 2 is completly excuted
    t2.join()

    # Both thread completly excuted
    print("Done")
