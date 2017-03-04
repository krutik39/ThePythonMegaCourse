def cel2fah(cel):
    if cel < -273.15:
        print ("Invalid Temperature")
    else:
        fah = (((cel*9)/5)+32)
        return fah

print (cel2fah(-300))
