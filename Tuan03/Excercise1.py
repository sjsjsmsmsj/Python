def task1():
    print('* ' * 13)
    print('* ' * 7)
    print('* ' * 26)
def task2(n):
    for i in range (n):
        if i == 0 or i == n - 1:
            print("* " * 2*n)
        else:
            print("* " + "  " * 2 *(n - 1) + '*')
def task3(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")
task1()
print()
task2(5)
print()
task3(5)