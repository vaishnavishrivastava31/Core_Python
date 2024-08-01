import threading
import time

def first_thread():
    print("Hello Ram")
    time.sleep(1)
    print("Bye Ram")

def second_thread():
    print("Hello Shyam")
    print("Bye Shyam")

t1 = threading.Thread(target=first_thread)
t2 = threading.Thread(target=second_thread)

t1.start()
t2.start()