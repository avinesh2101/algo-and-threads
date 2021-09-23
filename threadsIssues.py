import threading

COUNT = 0

# crititcal section :-The critical section in a code segment where the shared variables can be accessed.
def calculate_count(arg):
    print("{}:begin".format(arg))
    global COUNT
    for _ in range(1000000):
        COUNT = COUNT +1
    print("{}:ends".format(arg))

def main():
    print("main begin:COUNT = {}".format(COUNT))
    t1 = threading.Thread(target=calculate_count, args=("t1",))#creation of threads
    t2 = threading.Thread(target=calculate_count, args=("t2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("main dont: COUNT = {}".format(COUNT))

if __name__ == "__main__":
    main()
# race condition occurs here and both threads access shared variable at same time Then the first thread and second thread perform their operations on the value, and they race to see which thread can write the value last to the shared variable.
# mutex or mutual exclusion can be used to oveercome this
