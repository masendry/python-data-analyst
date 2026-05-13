index = [0, 1, 2, 3, 4, 5, 6]
nama = ["Alice", "Bob", "Angelo", "Mulyadi", "Bendot", "Lupek"]
nilai =["80", "65", "90", "100", "35", "55"]

nama_slice_3_tengah = nama[1:3] #['Bob', 'Angelo']
nilai_slice_3_tengah = nilai[1:3] #['65', '90']

print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#INSERT (memasukan dimanapun)
nama_slice_3_tengah.insert(1, "Dwi")
nilai_slice_3_tengah.insert(1, "22")
print("\n")
print("INSERT")
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#APPEND (menambahkan/memunculkan dibelakang)
nama_slice_3_tengah.append("Zara")
nilai_slice_3_tengah.append("91")
print("\n")
print("APPEND")
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#SORT (mengurutkan nilai dari terendah ke paling tinggi)
nama_slice_3_tengah.sort()
nilai_slice_3_tengah.sort()
print("\n")
print("SORT")
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#REVERSE (membalimk urutan dari paling belakang)
nama_slice_3_tengah.reverse()
nilai_slice_3_tengah.reverse()
print("\n")
print("REVERSE")
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)

#POP (menghilangkan bagian terakhir dari data/urutan)
nama_slice_3_tengah.pop()
nilai_slice_3_tengah.pop()
print("\n")
print("POP")
print(nama_slice_3_tengah)
print(nilai_slice_3_tengah)


#print(nama)
#print(nilai)

# PrRINT DENGAN INDEX
    #print("\n")
    #print("Print dengan index")
    #print(f"Nama: {nama[1]}, memperoleh nilai {nilai[0]}")

#for z in range(len(nama)):
   # print(f"Nama: {nama[z]}, memperoleh nilai {nilai[z]}")


