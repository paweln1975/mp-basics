from threading import Thread, Lock
from _thread import interrupt_main
from time import sleep
import sys
from signal import signal
from signal import SIGINT

product_price = 0
product_name = ""
number_of_changes = 0
lock = Lock()


def set_price(name, price, delay):
    global product_price, product_name
    while True:
        lock.acquire()
        product_price = price
        product_name = name
        lock.release()


def check_price():
    global product_price, product_name, number_of_changes
    prev_product_name = product_name
    prev_product_price = product_price
    while True:
        lock.acquire()
        current_product_name = product_name
        current_product_price = product_price
        lock.release()

        if prev_product_price != current_product_price or prev_product_name != current_product_name:
            number_of_changes += 1
            # print(f'Current product name={current_product_name} and price={current_product_price}')
            prev_product_name = current_product_name
            prev_product_price = current_product_price


products = [
    ("Shirt", 5, 0.1),
    ("Jeans", 10, 0.2)
]

t_check = Thread(target=check_price, daemon=True)
t_check.start()

t1 = Thread(target=set_price, args=products[0], daemon=True)
t2 = Thread(target=set_price, args=products[1], daemon=True)

t1.start()
t2.start()


# task executed in a new thread
def task():
    # block for a moment
    sleep(10)
    # interrupt the main thread
    print('Interrupting main thread now')
    interrupt_main()


# handle single
def handle_sigint(signalnum, frame):
    # terminate
    print(f'Main interrupted! Exiting. Number of changes: {number_of_changes}')
    sys.exit()


# register the signal handler for this process
signal(SIGINT, handle_sigint)
# start the new thread
thread = Thread(target=task)
thread.start()

# wait around
while True:
    sleep(1)
