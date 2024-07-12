from address import Address
from mailing import Mailing

to_address = Address("299038", "Севастополь", "Большая Морская", "52", "30")
from_address = Address("299035","Краснодар", "Красная", "78", "10")
mailing = Mailing(to_address, from_address, "1500", "TN5664789")
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat},"
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.city}"
      f"{mailing.to_address.house}, {mailing.from_address.flat}. Стоимость {mailing.cost} рублей")