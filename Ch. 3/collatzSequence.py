# Write your code here :-)
def collatz(number):
    global x
    if number % 2 == 0:
        x = number // 2
        return print(x)
    elif number % 2 == 1:
        x = 3 * number + 1
        return print(x)

try:
    print('Input integer')
    x = int(input())
    while x != 1:
        collatz(x)
except ValueError:
    print('Must enter integer')

