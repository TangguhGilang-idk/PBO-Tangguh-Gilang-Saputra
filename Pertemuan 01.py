#Fundamentals
nama_pengguna = 'Gilang'

print(nama_pengguna)

nama_pengguna = 'Gilang'
print(nama_pengguna)

nama_pengguna = 'Aku'

print(nama_pengguna)

integer_number = 5
float_number = 5.9

new_number = integer_number * float_number

print("Value:",new_number)
print("Data Type:",type(new_number))

num_string = '3'
num_integer = 7

print("Data type of num_string before Type Casting:",type(num_string))

num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))

print('Selamat Pagi!', end= ' ')

print('Hari ini cerah.')

num = input('Masukkan Angka: ')

print('Kamu memasukkan Angka:', num)

print('Type data dari angka tersebut:', type(num))

x = 3
y = 5
print('x > y  is',x>y)
print('x < y  is',x<y)
print('x == y is',x==y)
print('x != y is',x!=y)
print('x >= y is',x>=y)
print('x <= y is',x<=y)

x1 = 2
y1 = 2
x2 = 'Halo'
y2 = 'Halo'
x3 = [6, 7, 8]
y3 = [6, 7, 8]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

#Flow Control
x = int(input("Enter x: "))
y = int(input("Enter y: "))

result = (x < y)
print(f"x < y ---> {result}")

result = (x <= y)
print(f"x <= y ---> {result}")

result = (x < 10)
print(f"x < 10 ---> {result}")

result = (x <= 10)
print(f"x <= 10 ---> {result}")

age = int(input("Masukkan Umur: "))
citizen = input("Orang Indonesia (ya/tidak)?: ")

result = (age >= 18) and (citizen == "ya")
print(result)

age = int(input("Maukkan Umur: "))

if age >= 18:
    print("Kamu Diizinkan Masuk Website Ini.")
else:
    print("Kamu Tidak Diizinkan Masuk Website Ini.")
print("Program Selesai.")

models = ["Claude", "ChatGPT", "Opus"]

for model in models:
    print(model)
    print("---")

numbers = [0, 1, 2, 3, 4, 5]

for num in numbers:
    print(f"Processing: {num}")
    print(f"Done with: {num}")

print('All done')

number = float(input("Masukkan Angka: "))

while number >= 0.0:
    print(number)

    number = float(input("Masukkan angka lain: "))

while True:
    number = int(input("Masukkan Angka: "))
    if number == 0:
        break
    print(number)

number = int(input("Masukkan Angka: "))
for i in range(0, 4):

    if i == number:
        break
    print(i)

for i in range(1, 11):

    if i % 2 == 0:
        continue
    print(i)

is_valid = True

if is_valid:
    pass
else:
    print("Login gagal.")

#Data Types
num1 = int(2.3)
print(num1)

num2 = int(-2.8)
print(num2)

num3 = float(5)
print(num3)

num4 = complex('3+5j')
print(num4) 

import random

print(random.randrange(0, 10))

list1 = ['a', 'b', 'c', 'd', 'e']

print(random.choice(list1))

random.shuffle(list1)

print(list1)

print(random.random())

languages = ["HTML", "Javascript", "Python"]

print(f"languages[0] = {languages[0]}")

print(f"languages[2] = {languages[2]}")

cart = ["Handphone", "Kipas Angin", "Televisi"]

cart.append("Laptop")

print(cart)


# empty tuple
my_tuple = ()

# tuple having integers
my_tuple = (1, 2, 3)

my_tuple = (1, "Halo", 3.4)

my_tuple = ("kucing", [8, 4, 6], (1, 2, 3))

my_tuple = 3, 4.6, "tikus"
a, b, c = my_tuple

model = 'Gilang'

print(model[0]) 

print(model[4])

model = 'Gilang'

print(model[-1])

print(model[-4]) 

numbers = {0, 1, 2, 3}

print('Set asli:',numbers)

numbers.add(4)

print('Set yang diperbarui:', numbers) 

languages = {'Swift', 'Java', 'Python'}

print('Set asli:',languages)

removedValue = languages.discard('Java')

print('Set setelah dihapus():', languages)

country_capitals = {
  "Indonesia": "Jakarta", 
  "Malaysia": "Kuala Lumpur", 
  "Brunei Darussalam": "Bandar Seri Begawan",
}

print(country_capitals["Indonesia"])     
print(country_capitals["Brunei Darussalam"])  

country_capitals = {
  "Indonesia": "Jakarta",
  "Malaysia": "Kuala Lumpur",
  "Brunei Darussalam": "Bandar Seri Begawan",
}

del country_capitals["Indonesia"]

print(country_capitals)