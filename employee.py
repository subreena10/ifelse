age=int(input("Enter your age:"))
sex=input("Enter 'M','F':")
marital_status=input(" married  'Y','N':")
if sex=='F':
    print("she will work only in urban areas.")
elif sex=='M' & age>=20 and age<=40:
    print("he may work any where.")
elif sex=='M' & age>=40 and age<=60:
    print("he will work in urban areas.")
else:
    print("Error.")