age = input("Enter your age: ")
new_age = float(age) + 50
print(new_age)

def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars

print (currency_converter(100,1000))
