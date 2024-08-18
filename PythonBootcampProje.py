import random

def tas_kagit_makas_MELIKE_SULTAN_CAN():

    # Karşılama
    print("Merhaba...\nTaş, Kağıt, Makas, Spock, Kertenkele Oyununa Hoş Geldiniz!")
    print("Kurallar: Taş, Kağıt, Makas, Spock ve Kertenkele seçeneklerinden birini seçin.")
    print(" - Taş, Makas'ı ve Kertenkele'yi yener.")
    print(" - Kağıt, Taş'ı ve Spock'ı yener.")
    print(" - Makas, Kağıt'ı ve Kertenkele'yi yener.")
    print(" - Spock, Taş'ı ve Makas'ı yener.")
    print(" - Kertenkele, Spock'ı ve Kağıt'ı yener.")
    print("İlk iki turu kazanan oyunun galibi olur.")
    print("Oyundan çıkmak için 'çıkış' yazınız.")

    choices = ["taş", "kağıt", "makas", "spock", "kertenkele"]
    
    # Sayaçlarımız
    oyun_sayisi = 0
    toplam_oyuncu_galibiyetleri = 0
    toplam_bilgisayar_galibiyetleri = 0

    # Oyun Başlangıcı
    while True:
        oyun_sayisi += 1
        oyuncu_tur_galibiyetleri = 0
        bilgisayar_tur_galibiyetleri = 0
        tur = 0

        while oyuncu_tur_galibiyetleri < 2 and bilgisayar_tur_galibiyetleri < 2:
            tur += 1
            print(f"\n{tur}. Tur")
            oyuncu_secim = input("Lütfen bir seçim yapın.\nTaş, Kağıt, Makas, Spock, Kertenkele : ").lower()
            
            if oyuncu_secim == 'çıkış':
                print("Oyundan çıktınız.")
                return

            if oyuncu_secim not in choices:
                print("Geçersiz seçim yaptınız, lütfen tekrar deneyin.")
                continue

            bilgisayar_secim = random.choice(choices)
            print(f"Bilgisayarın seçimi: {bilgisayar_secim}")

            if oyuncu_secim == bilgisayar_secim:
                print("Beraberlik!")
            elif (oyuncu_secim == "taş" and (bilgisayar_secim == "makas" or bilgisayar_secim == "kertenkele")) or \
                 (oyuncu_secim == "kağıt" and (bilgisayar_secim == "taş" or bilgisayar_secim == "spock")) or \
                 (oyuncu_secim == "makas" and (bilgisayar_secim == "kağıt" or bilgisayar_secim == "kertenkele")) or \
                 (oyuncu_secim == "spock" and (bilgisayar_secim == "taş" or bilgisayar_secim == "makas")) or \
                 (oyuncu_secim == "kertenkele" and (bilgisayar_secim == "spock" or bilgisayar_secim == "kağıt")):
                print("Bu turu kazandınız!")
                oyuncu_tur_galibiyetleri += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_tur_galibiyetleri += 1

            print(f"Durum: Oyuncu {oyuncu_tur_galibiyetleri} - {bilgisayar_tur_galibiyetleri} Bilgisayar")

        if oyuncu_tur_galibiyetleri == 2:
            print("\nTebrikler! Bu oyunu kazandınız!")
            toplam_oyuncu_galibiyetleri += 1
        else:
            print("\nBilgisayar bu oyunu kazandı!")
            toplam_bilgisayar_galibiyetleri += 1

        print(f"Oyun Durumu: Oyuncu {toplam_oyuncu_galibiyetleri} - {toplam_bilgisayar_galibiyetleri} Bilgisayar")

        devam = input("Başka bir oyun oynamak ister misiniz? (Evet/Hayır): ").lower()
        if devam != 'evet':
            print("Oyunu sonlandırdınız. Teşekkürler!")
            break
        
# Oyunumuzu başlatmak için fonksiyonu çağıralım.
tas_kagit_makas_MELIKE_SULTAN_CAN()
