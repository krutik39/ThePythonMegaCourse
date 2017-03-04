# def cel2fah(cel):
#         if cel < -273.15:
#             print ("Invalid Temperature")
#         else:
#             fah = (((cel*9)/5)+32)
#             return fah
# print (cel2fah(-300))
# temperatures = [10,-20,-289,100]
def temps(l1):
    for i in l1:
        if i < -273.15:
            print("Invalid Temperature")
        else:
            j = (((i*9)/5)+32)
            print (j)
print (temps([10,-20,-289,100]))
