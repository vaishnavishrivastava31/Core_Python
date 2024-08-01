import threading

def hello():
    for i in range(5):
        print('hello',i)

def hi():
    for i in range(5):
        print('hi',i)

hello_thread = threading.Thread(target = hello)
hi_thread = threading.Thread(target = hi)
hello_thread.start()
hi_thread.start()