
modern_kelime_sozluk = {"Lol":"kahka atmak", "cringe":"utandirici","ROFL ":"bir şakaya karşılık cevap",}




cevap = input("hangi kelimenin tanimini ogrenmek istiyorsun?")


if cevap.lower() in modern_kelime_sozluk:
    print(modern_kelime_sozluk[cevap])

else:
    print("kelime sozlukte yok")
