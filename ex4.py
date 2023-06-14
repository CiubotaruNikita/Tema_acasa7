num =int(input("Introduci un număr prim: "))
flag = False
if num == 1:
    print(num, "nu este un număr prim")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
    if flag:
        print(num, "nu este un număr prim")
    else:
        print(num, "este un număr prim")