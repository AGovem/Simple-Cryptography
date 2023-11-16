import os 
from cryptography.fernet import Fernet
import time

running_dir = os.getcwd()

menü = """
		MENÜ

	0) ANAHTAR OLUŞTUR 

	1) Yazı Şifrele
	2) Yazı Şifre Çöz
	
	3) Dosya Şifrele
	4) Dosya Şifre Çöz

	5) Klasör Şifrele
	6) Klasör Şifre Çöz

	q) Çıkış



	!!!!! Daha Önce Oluşturmadıysan İlk Anahtar Oluştur ve Sakın Kaybetme. Kaybetmen Halinde Dosyalara Bir Daha Ulaşamazsın !!!!!

"""

def write_key():
	# random parola üretir ve dosyaya yazar"

	key = Fernet.generate_key()

	with open(anahtar,"wb") as key_file:
		key_file.write(key)

def load_key():
    # Loads the key from the current directory named `key.key`
    return open(anahtar, "rb").read()



def şifrele(Dosya_Adı , Anahtar):

	f = Fernet(Anahtar)

	with open(Dosya_Adı , "rb") as Dosya:

		dosya_verisi = Dosya.read()

	şifreli_veri = f.encrypt(dosya_verisi)

	with open(Dosya_Adı , "wb") as şifreli_dosya:

		şifreli_dosya.write(şifreli_veri)

def çöz(Dosya_Adı , Anahtar):

	f = Fernet(Anahtar)

	with open(Dosya_Adı , "rb") as dosya:

		çözülecek_dosya = dosya.read()

	çözülmüş = f.decrypt(çözülecek_dosya)

	with open(Dosya_Adı , "wb") as çözülmüş_veri:

		çözülmüş_veri.write(çözülmüş)



print("\nBoş Bırakırsanız Bu Klasöre 'key.key' Adı İle Oluşturulacak.")
print("Menüye Dönmek İçin 'n' ye Basın.\n")

a_yolu = input("Anahtarınızın Oluşturulacağı\\Bulunduğu Klasörün Yolu : ")
adı = input("Anahtar Dosyanızın Adı: ")

if a_yolu.upper() == "N" or adı.upper() == "N":
	anahtar = running_dir+"\\"+"key.key"
	input("Enter'a Basın")

if bool(a_yolu) == False:
	a_yolu = running_dir
else:
	a_yolu = a_yolu

if bool(adı) == False:
	adı = "key"
else:
	adı = adı

anahtar = a_yolu+"\\"+adı+".key"

while True:

	print(menü)
	a = input("Yapacağınız İşlem No. : ")


	if a == "0":  #Anahtar oluşturuyor
		write_key()
		time.sleep(0.5)
		print(f"""\nAnahtarınız '{anahtar}' Noktasına Oluşturuldu :D 

					
				!!!! SAKIN KAYBETME !!!!""")
		time.sleep(4)
	
	elif a == "1":    # Yazı şifreliyor
		key = load_key()
		f = Fernet(key)
		m = input("Şifrelenecek Metin (dönüş için 'n') : ").encode()
		
		if m == b"n" or m == b"N":
			input("Enter'a Basın")

		else:
			şifreli = f.encrypt(m)
			print("\nŞifrelenmiş Metin >>>>>", şifreli)
			time.sleep(1)
	
	elif a == "2":    # Yazı çözüyor
		key = load_key()
		f = Fernet(key)
		m = input("Şifreli Metin (dönüş için 'n') : ").encode()
		
		if m == b"n" or m == b"N":
			input("Enter'a Basın")

		else:
			çöz = f.decrypt(m)
			print("Çözümleniyor")
			for i in range(3):
				print(".")
				time.sleep(1)
			print("\nÇözülen Metin >>>>>", çöz)
			time.sleep(2)
	
	elif a == "3":     # Dosya şifreliyor
		key = load_key()
		f = Fernet(key)
		y = input("Şifrelenecek Dosya Yolu (dönüş için 'n') : ")

		if y == b"n" or y == b"N":
			input("Enter'a Basın")

		else:
			şifrele(y,key)
			print("\nDosya Başarıyla Şifrelendi :D")
			time.sleep(2)
	
	elif a == "4":      # Dosya çözme
		key = load_key()
		f = Fernet(key)
		y = input("Çözülecek Dosya Yolu (dönüş için 'n') : ")

		if y == b"n" or y == b"N":
			input("Enter'a Basın")
		
		else:	
			çöz(y,key)
			print("\nDosya Çözme Başarılı :D")
			time.sleep(2)

	elif a == "5":       # Klasör Şifreliyor

		c = input("Klasörün İçindeki TÜM DOSYALAR Şifrelenecek. Devam Etmek İstiyor Musun? y/n : ")
		
		if c == "y" or c == "Y":

			DosyaYolu = input("Şifrelenecek Klasörün Yolunu Yazın : ")
			dosya = os.listdir(DosyaYolu)


			key = load_key()
			f = Fernet(key)
			
			s = 0 #dosya.index("dfg.txt")
			for i in dosya:
														#print(dosya[s])
				a = dosya[s]
				j = DosyaYolu+"\\"+a
				name,extension = os.path.splitext(a)
														#print(extension)
				if extension != b'.py' and extension != b".key":# and extension != "py":
					şifrele(j, key)
				s = s+1
			
			print("Encrypting...")
			time.sleep(1.5)
			print("\nEncryption Successful :D")
			time.sleep(1)

		elif c == "n" or c == "N":
			input("Menüye Dönmek İçin Enter'a Basın.")


	elif a == "6":       # Klasör Çözüyor

		m = input("Menüye Dönmek İster Misin? y/n : ")

		if m == "y" or m == "Y":
			input("Enter'a Basın")

		else:
			DosyaYolu = input("Çözülecek Klasörün Yolunu Yazın : ")
			dosya = os.listdir(DosyaYolu)

			key = load_key()
			f = Fernet(key)
			
			s = 0
			for i in dosya:
				
				a = dosya[s]
				j = DosyaYolu+"\\"+a
				isim,uzantı = os.path.splitext(a)

				if uzantı != b".py" and uzantı != b".key":
					çöz(j, key)
				s += 1

			print("Decrypting...")
			time.sleep(0.5)
			print("Decryption Successful :D")
			time.sleep(1)


	elif a == "q" or a == "Q":
		quit()

	else:
		input("Bir Şeyler Yanlış Oldu!!! Ana Menüye Dönmek İçin Enter'a Bas")