import sys


class Hangman:
    aranan_kelime = ""
    yanlis_hakki = 7
    dogru_karakterler = list()
    yanlis_sayisi = 0
    adam = [[" " for i in range(3)] for i in range(4)]

    def __init__(self):
        pass

    def get_kelime(self):
        self.aranan_kelime = input("Bulunmasını istediğiniz kelimeyi giriniz :")
        self.dogru_karakterler = ['_' for i in range(len(self.aranan_kelime))]

    def karsilastir_karakter(self, tahmin):
        sayac = 0

        if tahmin not in self.aranan_kelime:
            self.yanlis_sayisi += 1
        else:
            for harf in self.aranan_kelime:
                if tahmin == harf:
                    self.dogru_karakterler[sayac] = harf

                sayac += 1

    def yaz_kelimeleri(self):
        for character in self.dogru_karakterler:
            print(character, end=" ")
        print()

    def oyunu_baslat(self):

        while self.yanlis_hakki - self.yanlis_sayisi:
            self.oyun_bitti_mi()
            print("Haklar:", self.yanlis_hakki - self.yanlis_sayisi)
            tahmin_karakteri = input("Tahmin:")
            self.karsilastir_karakter(tahmin_karakteri)
            self.adam_ciz()
            self.yaz_kelimeleri()

        else:
            print("Tahmin hakkınız bitmiştir. Adam asıldı.")
            sys.exit()

    def oyun_bitti_mi(self):
        if "_" not in self.dogru_karakterler:
            print("Tebrikler ! Bildiniz.")
            sys.exit()

    def adam_ciz(self):
        print("yanlis sayisi :", self.yanlis_sayisi)
        if self.yanlis_sayisi == 1:
            self.adam[0][1] = "o"
        if self.yanlis_sayisi == 2:
            self.adam[1][0] = "/"
        if self.yanlis_sayisi == 3:
            self.adam[1][2] = "\\"
        if self.yanlis_sayisi == 4:
            self.adam[1][1] = "|"
        if self.yanlis_sayisi == 5:
            self.adam[2][1] = "|"
        if self.yanlis_sayisi == 6:
            self.adam[3][0] = "/"
        if self.yanlis_sayisi == 7:
            self.adam[3][2] = "\\"
        for i in range(len(self.adam)):
            for j in range(len(self.adam[0])):
                print(self.adam[i][j], end=' ')
            print()


hangman = Hangman()
hangman.get_kelime()
hangman.oyunu_baslat()
