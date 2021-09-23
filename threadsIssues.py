import threading

COUNT =0

def calculate_count(arg):
    print("{}:begin".format(arg))
    global COUNT
    for _ in range(1000000):
        COUNT = COUNT +1
    print("{}:ends".format(arg))

def main():
    print("main begin:COUNT = {}".format(COUNT))
    t1 = threading.Thread(target=calculate_count, args=("t1",))#creating of threads
    t2 = threading.Thread(target=calculate_count, args=("t2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("main dont: COUNT = {}".format(COUNT))

if __name__ == "__main__":
    main()

    # mutex or mutual exclusion can be used to oveercome issue
