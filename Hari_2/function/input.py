import aritmatika as f

berat = float (input ("masukan berat badan (kg):"))
tinggi_m = float (input ("masukan tinggi badan (m):"))

bmi = f.bmi(berat, tinggi_m)
print("BMI kamu :", bmi)

f.bmi_check(bmi)

#print(f.add(10, 6))