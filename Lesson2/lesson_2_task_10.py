def bank():
    procent = 10
    n  = int(input("Сколько кладете на счет: "))
    y = int(input("На сколько лет хотите положить деньги: "))
    for x in range(y):
        n = int(n+procent*n/100)
        print ("Вы получите: ", n)
bank()
