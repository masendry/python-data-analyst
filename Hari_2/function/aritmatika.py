def add(a=None, b=None): 
    if a == None or b == None:
        print("parameter tidak lengkap")
        return

    total = a + b
    return total

def substract(a=None, b=None):
    if a == None or b == None:
        print("print tidak lengkap")

print(add())

jumlah = add(10, 5)
    
print(f"hasil dari penjumlahan 10 tambah 5 = {jumlah}")

def bmi(berat, tinggi_m):
    bmi = berat / (tinggi_m ** 2)
    return bmi


def bmi_check(bmi):
    if bmi < 18.5 :
        print ("kategori : Kurang Berat Badan")
    elif bmi > 18.5 and bmi < 25 :
        print ("kategori : Normal")
    elif bmi > 25 and bmi < 30 :
        print("kategori : Kelebihan Berat Badan")
    elif bmi >30 :
        print("kategori : Obesitas")
