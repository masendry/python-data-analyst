import json


data = {
    "nama depan" : "Totok",
    "nama belakang" : "Winarko",
    "umur" : "55",
    "alamat" : "Pakem",
    "hobby" : "Karaoke"
}

print(json.dumps(data, indent=4))
print(data["alamat"])

data["alamat"] = "Jogja"

print("\nsetelah diubah")
print(data["alamat"])


BigData = [
    {
    "nama depan" : "Angela",
    "nama belakang" : "Brown",
    "umur" : "33",
    "alamat" : "Brooklyn",
    "hobby" : "Menyanyi"
},
{
    "nama depan" : "James",
    "nama belakang" : "Masiani",
    "umur" : "29",
    "alamat" : "Oldtraford",
    "hobby" : "Sepakbola"
},
{
    "nama depan" : "Sigit",
    "nama belakang" : "Bonar",
    "umur" : "44",
    "alamat" : "Ketandan",
    "hobby" : "Mancing"
},
{
    "nama depan" : "Ani",
    "nama belakang" : "Ananda",
    "umur" : "25",
    "alamat" : "Sosrowijayan",
    "hobby" : "Renang"
}
]

BigData.append (
    {
    "nama depan" : "Wahyudi",
    "nama belakang" : "Waluyo",
    "umur" : "35",
    "alamat" : "Kota Gede",
    "hobby" : "Touring"
}
)

print(json.dumps(BigData,indent=4))