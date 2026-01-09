name = "Pranav".lower()
letters = [letter for letter in name]
print(letters)

double_list = [num*2 for num in range(1,10)]

print(double_list)

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names = [name for name in names if len(name)<=4 ]
long_names = [name.upper() for name in names if len(name)>5]
print(short_names)
print(long_names)
