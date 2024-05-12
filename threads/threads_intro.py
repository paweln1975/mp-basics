from datetime import datetime
from time import sleep
from threading import Thread


def print_hello(thread, name, delay=0):
    sleep(delay)
    print(
        f"{thread} ---> Hello {name}. The time is: \
            \t{datetime.now().strftime("%H:%M:%S.%f")}"
    )


t1 = Thread(target=print_hello, args=("t1", "Pawel"))
t2 = Thread(target=print_hello, args=("t2", "Monika"))
t1.start()
t2.start()

t1 = Thread(target=print_hello, args=("t1", "Pawel", 0.5))
t2 = Thread(target=print_hello, args=("t2", "Monika"))
t1.start()
t2.start()
