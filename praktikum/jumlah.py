word = "Hallo dunia"


def HitungKalimat(kalimat):
    jumlah = 0
    for i in kalimat:
        jumlah += 1
    return jumlah


print("Terdapat", HitungKalimat(word), "karakter")
