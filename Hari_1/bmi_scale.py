berat = float (input ("masukan berat badan (kg):"))
tinggi_cm = float (input ("masukan tinggi badan (m):"))

tinggi_m = tinggi_cm / 100


#cara hitung BMi

bmi = berat / (tinggi_m ** 2) 
print ("BMI anda adalah :{bmi :.2f} bmi")


#menentukan kategori bmi

if bmi < 18.5 :
    print ("kategori : berat badan kurang")
elif bmi < 18.5 and bmi < 25 :
    print ("kategori : berat badan normal")
elif bmi < 25 and bmi < 30 :
    print("kategori : berat badan berlebih")
