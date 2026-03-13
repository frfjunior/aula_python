from time import sleep


b = 1
x = 2

while b < 10:
    x = x + 1 + b
    sleep(2)
    print(x)
