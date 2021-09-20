import threading

def print_args(x):
    print(x)

def main() :
    print("main begins")
    t1 = threading.Thread(target=print_args,args=("A") )# create
    t1.start()

    t2 = threading.Thread(target=print_args,args=("B") )# create
    t2.start()

    t1.join()#wait
    t2.join()
    print("main ends")

if __name__ == "main":
    main()