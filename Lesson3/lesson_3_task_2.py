from smartphone import Smartphone

catalog = []

Tel1 = Smartphone("iPhone", "12PRO", "+79786754589")
Tel2 = Smartphone("Xiomi", "Note", "+79786544589") 
Tel3 = Smartphone("Samsung", "Galaxy", "+79777754555")
Tel4 = Smartphone("Asus", "10", "+79786754509")
Tel5 = Smartphone("LG", "12", "+79786754675")

catalog.append(Tel1)
catalog.append(Tel2)
catalog.append(Tel3)
catalog.append(Tel4)
catalog.append(Tel5)

for phone in catalog:
    print(f"{phone.marka} - {phone.model}. {phone.number}")