import os

# deklarasi variabel
opsi = ''
nomor = []
hasil = 0. 
i = 0

os.system('clear')	# clear
# start perulangan ke-1
while(True):
	print(" ______________________________")
	print("|                              |")
	print("|	   Kalkulator	       |")
	print("|______________________________|")
			
	# inputan nomor awal
	print(" Masukkan Nomor : ")
	nomor.insert(0, float(input("  ")))
	
	# hasil awal = nomor awal
	hasil = nomor[0]
	os.system('clear')	

	# start perulangan while ke-2
	while(opsi != 'q'):
		print(" ______________________________")
		print("|                              |")
		print("|	   Kalkulator	       |")
		print("|______________________________|")
		
		# keterangan opsi
		print("--------------------------------")
		print(" Keterangan Opsi : ")
		print(" ( + ) Penjumlahan ")
		print(" ( - ) Pengurangan ")
		print(" ( * ) Perkalian ")
		print(" ( / ) Pembagian ")
		print(" ( ^ ) Pangkat ")
		print(" ( r ) Akar ")
		print(" ( = ) Hasil ")
		print(" ( c ) Reset ")
		print(" ( q ) Keluar ")
		print("--------------------------------")
		print(" ")

		# inputan opsi
		opsi = input(" Pilih opsi : ")
		os.system('clear')
		
		# bagian penjumlahan
		if(opsi == '+'):
			print(" ______________________________")
			print("|                              |")
			print("|	   Kalkulator	       |")
			print("|______________________________|")
			
			i += 1
			# input nomor ke i
			print(" Masukkan Nomor : ")
			nomor.insert(i, float(input("  ")))
			os.system('clear')
			
			# proses penjumlahan
			# untuk nomor[2],dst
			if(i > 1):
				hasil += nomor[i]
			# untuk nomor[0] dan nomor[1]
			else:
				hasil = nomor[0] + nomor[i]
		
		# bagian pengurangan		
		elif(opsi == '-'):
			print(" ______________________________")
			print("|                              |")
			print("|	   Kalkulator	       |")
			print("|______________________________|")
			
			i += 1
			# input nomor ke i
			print(" Masukkan Nomor : ")
			nomor.insert(i, float(input("  ")))
			os.system('clear')
			
			# proses pengurangan
			# untuk nomor[2],dst
			if(i > 1):
				hasil -= nomor[i]
			# untuk nomor[0] dan nomor[1]
			else:
				hasil = nomor[0] - nomor[i]
		
		# bagian perkalian
		elif(opsi == '*'):
			print(" ______________________________")
			print("|                              |")
			print("|	   Kalkulator	       |")
			print("|______________________________|")
			
			i += 1
			# input nomor ke i
			print(" Masukkan Nomor : ")
			nomor.insert(i, float(input("  ")))
			os.system('clear')
			
			# proses perkalian
			# untuk nomor[2],dst
			if(i > 1):
				hasil *= nomor[i]
			# untuk nomor[0] dan nomor[1]
			else:
				hasil = nomor[0] * nomor[i]
		
		# bagian pembagian
		elif(opsi == '/'):
			print(" ______________________________")
			print("|                              |")
			print("|	   Kalkulator	       |")
			print("|______________________________|")
			
			i += 1
			# input nomor ke i
			print(" Masukkan Nomor : ")
			nomor.insert(i, float(input("  ")))
			os.system('clear')
			
			# proses pembagian
			# jika nomor ke-i = 0
			if(float(nomor[i] == 0. )):
				# menampilkan hasil
				print(" Hasil : ")
				print("  Tidak Terdefinisi ")
				
				input("Press Enter to Continue ... ")	# pause	
				os.system('clear')
			# jika nomor != 0
			else:
				# untuk nomor[2],dst
				if(i > 1):
					hasil /= nomor[i]
				# untuk nomor[0] dan nomor[1]
				else:
					hasil = nomor[0] / nomor[i]
					
		# bagian bilangan pangkat			
		elif(opsi == '^'):
			print(" ______________________________")
			print("|                              |")
			print("|	   Kalkulator	       |")
			print("|______________________________|")
			
			# input pangkat
			print(" Masukkan Pangkat : ")
			pangkat = float(input("  "))
			os.system('clear')
			
			# proses pencarian bilangan berpangkat
			# jika melakukan ini kesekian kalinya
			if(i > 0):
				hasil **= pangkat
			# untuk nomor awal
			else:

				hasil = nomor[0] ** pangkat
		
		# bagian akar pangkat dari bilangan
		elif(opsi == 'r'):
			print(" ______________________________")
			print("|                              |")
			print("|	   Kalkulator	       |")
			print("|______________________________|")
			
			# input akar pangkat
			print(" Masukkan Akar Pangkat : ")
			akar_pangkat = float(input("  "))
			os.system('clear')
			
			# proses pencarian akar pangkat dari bilangan
			# jika melakukan ini kesekian kalinya
			if(i > 0):
				hasil **= (1/akar_pangkat)
			# untuk nomor awal
			else:

				hasil = nomor[0] ** (1/akar_pangkat)
				 
		# bagian hasil
		elif(opsi == '='):
			print(" ______________________________")
			print("|                              |")
			print("|	   Kalkulator	       |")
			print("|______________________________|")
			
			# menampilkan hasil
			print(" Hasil : ")
			print("  ", hasil)
			print(" ")
			
			input("Press Enter to Continue ... ")	
			os.system('clear')
		
		# bagian reset	
		elif(opsi == 'c'):
			break
	# end perulangan while ke-2
	
	# bagian keluar
	if(opsi == 'q'):
		break						
# end perulangan while ke-1

print(" ")
print(" Terima Kasih Telah Menggunakan Layanan ini! ")
print(" ")

input("Press Enter to Continue ... ")		
os.system('clear')				

