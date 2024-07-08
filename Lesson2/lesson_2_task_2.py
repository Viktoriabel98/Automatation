def is_year_leap(n): 
        if (n % 4 == 0):
            return(True)
        else: 
             return(False)
print(is_year_leap(int(input("Введите год: "))))

# год 2024
year = 2024
result = is_year_leap(year)
print(f"Год: {year}: {result}")
 

