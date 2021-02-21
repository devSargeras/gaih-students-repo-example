try:
    kisi_sayisi = 2
    grades = [[0 for i in range(3)] for j in range(kisi_sayisi)]
    ad_soyad = [[0 for i in range(2)] for j in range(kisi_sayisi)]

    for i in range(kisi_sayisi):
        for j in range(3):
            if j == 0:
                grades[i][j] = int(input(f"{i + 1}. öğrencinin midterm notunu girin:"))
            if j == 1:
                grades[i][j] = int(input(f"{i + 1}. öğrencinin final notunu girin:"))
            if j == 2:
                grades[i][j] = int(input(f"{i + 1}. öğrencinin homework notunu girin:"))
        for k in range(2):
            if k == 0:
                ad_soyad[i][k] = (input(f"{i + 1}. öğrencinin ismini girin:"))
            if k == 1:
                ad_soyad[i][k] = (input(f"{i + 1}. öğrencinin soyismini girin:"))
    info = dict()
    max_not = 0
    max_kisi = tuple()
    for i in range(kisi_sayisi):
        note = (grades[i][0] + grades[i][1] + grades[i][2]) / 3
        isim_soyisim = (ad_soyad[i][0], ad_soyad[i][1])
        info[(isim_soyisim)] = note
        if max_not < note:
            max_not = note
            max_kisi = (ad_soyad[i][0], ad_soyad[i][1])
    print(info)
    sortedList = sorted(info.values())
    print("Sıralama:", sortedList)
    print("Tebrikler:", max_kisi)
except:
    print("Hatayla karşılaşıldı.")
