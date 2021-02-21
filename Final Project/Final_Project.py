class Tarifler:

    def __init__(self, tarif_ismi):
        self.tarif_ismi = tarif_ismi

    def basla(self):
        print("\nTarif İsmi:", self.tarif_ismi)

    def ac_ocak(self):
        print("Ocağı aç.")

    def ekle_tuz(self):
        print("Tuz ekle.")

    def ekle_su(self, bardak="Uygun sayida"):
        print(f"{bardak} bardak su ekle")

    def hazirla_servise(self):
        print("Servise hazırla")


class PirincPilavi(Tarifler):
    def __init__(self, tarif_ismi):
        super().__init__(tarif_ismi)

    def pirinci_yika(self):
        print("pirinci bol suyla yıka, 30 dk suda beklet.")

    def tereyagi_erit(self):
        print("tencerede 3 yemek kaşığı tereyağı erit.")

    def suyu_süz(self):
        print("pirincin suyunu süz")

    def yagda_kavur(self):
        print("pirinci yağda kavur")

    def pisir(self):
        print("ocakta pişir")

    def yap(self):
        self.basla()
        self.pirinci_yika()
        self.tereyagi_erit()
        self.suyu_süz()
        self.yagda_kavur()
        self.ekle_su()
        self.ekle_tuz()
        self.pisir()
        self.hazirla_servise()


class FirikPilavi(Tarifler):
    def __init__(self, tarif_ismi):
        super().__init__(tarif_ismi)

    def sogan_dogra(self):
        print("2 ortaboy soğanı küp küp doğra")

    def sogan_kavur_yagda(self):
        print("içerisine 2 su bardağı firik,1 su bardağı pilavlık bulgur koyup yağda kavur")

    def ekle_salca(self):
        print("2 tatlı kaşığı salça ekle")

    def tavuk_koy(self):
        print("haşlayıp dilimlenen tavuğu pilavın içine ekle.")

    def nohut_ekle(self):
        print("haşlanmış nohutu içerisine ekle.")

    def kaynat(self):
        print("kısık ateşte kaynatıp, pişir")

    def sosu_ekle(self):
        print("yarım su bardağı sıvı yağı kızartıp karabiber ekle ")

    def sosu_pilava_ekle(self):
        print("sosu pilava ekle")

    def yap(self):
        self.basla()
        self.ac_ocak()
        self.sogan_dogra()
        self.sogan_kavur_yagda()
        self.ekle_salca()
        self.ekle_su(6)  # buraya su ekle gelicek
        self.tavuk_koy()
        self.nohut_ekle()
        self.kaynat()
        self.sosu_ekle()
        self.sosu_pilava_ekle()
        self.hazirla_servise()


class MercimekCorbasi(Tarifler):
    def __init__(self, tarif_ismi):
        super().__init__(tarif_ismi)

    def ekle_yag(self):
        print("tencereye 3 yemek kaşığı yağ ekle.")

    def kavur_sogan(self):
        print("İri doğranmış 1 adet büyük soğanı sıvı yağ ile birlikte kavur.")

    def un_ekle(self):
        print("Kavrulan soğanlara 1 yemek kaşığı unu ekle ve kavurmaya devam et")

    def ekle(self):
        print(
            "Tuz, karabiber ve bol suda yıkadıktan sonra suyunu süzdürdüğünüz 1,5 su bardağı mercimeği de ilave et ve son kez güzelce karıştır")

    def su_ekle(self):
        print("6 su bardağı sıcak suyu da tencereye ilave edin.")

    def pisir(self):
        print("40 dakika pişir")

    def yap(self):
        self.basla()
        self.ekle_yag()
        self.kavur_sogan()
        self.un_ekle()
        self.ekle()
        self.ekle_su(6)
        self.pisir()
        self.hazirla_servise()


secim = ' '
while secim != '4':
    print("\nÖğrenmek istediğiniz tarifi seçiniz.")
    print("1. Pirinç pilavi tarifi")
    print("2. Firik pilavi tarifi")
    print("3. Mercimek çorbası tarifi")
    print("4. Çıkış")

    secim = input("Secim :")

    if secim == "1":
        pirinc_pilavi = PirincPilavi("pirinç pilavi")
        pirinc_pilavi.yap()
    elif secim == "2":
        firik_pilavi = FirikPilavi("Firik pilavi")
        firik_pilavi.yap()
    elif secim == "3":
        mercimek_corbasi = MercimekCorbasi("Mercimek corbasi")
        mercimek_corbasi.yap()
    elif secim == "4":
        exit()
    else:
        print("Gecersiz giriş.\n")
