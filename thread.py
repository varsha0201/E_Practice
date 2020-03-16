import time
import _thread

def thread_test(name, wait):
    i =0
    while i<=3:
        time.sleep(wait)
        print("Running %s\n" %name)
        i =i+1

    print("%s has finished excution" %name)

if __name__ == "__main__":
    _thread.start_new_thread(thread_test,("First thread", 1))
    _thread.start_new_thread(thread_test,("Second thread", 2))
    _thread.start_new_thread(thread_test,("Third Thread", 3))
