import time
from threading import Thread


def print_hello(thread, name, delay=0):
    time.sleep(delay)
    print(
        f"{thread} ---> Hello {name}. The time is: \
            \t{time.strftime("%H:%M:%S", time.localtime())}"
    )


t1 = Thread(target=print_hello, args=("t1", "Pawel"))
t2 = Thread(target=print_hello, args=("t2", "Monika"))
t1.start()
t2.start()

t1 = Thread(target=print_hello, args=("t1", "Pawel", 0.5))
t2 = Thread(target=print_hello, args=("t2", "Monika"))
t1.start()
t2.start()