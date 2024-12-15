"""
bytes type training
>>> import sys; sys.tracebacklimit = 0
"""

chinese_hello = bytes('你好，世界', encoding='utf-8')
print(chinese_hello)

chinese_hello_enc = '你好，世界'.encode('utf-8')
print(chinese_hello_enc == chinese_hello)

chinese_hello_dec = chinese_hello_enc.decode('utf-8')
print(chinese_hello_dec)

int_to_bytes = bytes([104, 105])
print(int_to_bytes)

zero_bytes = bytes(4)
print(zero_bytes)

first_number = (1024).to_bytes(2, byteorder='big')
second_number = (1024).to_bytes(2, byteorder='little')
print(first_number, second_number)

number_1024 = int.from_bytes(first_number, byteorder='big')
print(number_1024)

