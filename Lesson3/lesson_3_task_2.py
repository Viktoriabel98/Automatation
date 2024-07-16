from smartphone import Smartphone

catalog = [Smartphone("iPhone", "12PRO", "+79786754589"),
           Smartphone("Xiomi", "Note", "+79786544589"),
           Smartphone("Samsung", "Galaxy", "+79777754555"),
           Smartphone("Asus", "10", "+79786754509"),
           Smartphone("LG", "12", "+79786754675")]

for phone in catalog:
    print(f"{phone.mark} - {phone.model}. {phone.telnum}")