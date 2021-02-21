def prime_first(sayi):
    if sayi > 1:
        kontrol = True
        for i in range(2, sayi):
            if sayi % i == 0:
                kontrol = False
                break
        if kontrol == True:
            print(sayi)


def prime_second(sayi):
    if sayi > 1:
        kontrol = True
        for i in range(2, sayi):
            if sayi % i == 0:
                kontrol = False
                break
        if kontrol == True:
            print(sayi)


for i in range(0, 1000):
    if i < 500:
        prime_first(i)
    else:
        prime_second(i)
