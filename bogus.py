def countdown(n):
    print("counting down from", n)
    while n >= 0:
        print(n)
        new_value = yield n
        if new_value:
            n = new_value
        else:
            n -= 1


c = countdown(5)
for n in c:
    if n == 5:
        c.send(3)
