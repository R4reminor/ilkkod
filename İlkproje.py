
modern_kelime_sozluk = {"Lol":"kahka atmak", "cringe":"utandirici"}




cevap = input("hangi kelimenin tanimini ogrenmek istiyorsun?")


if cevap.lower() in modern_kelime_sozluk:
    print(modern_kelime_sozluk[cevap])

else:
    print("kelime sozlukte yok")
