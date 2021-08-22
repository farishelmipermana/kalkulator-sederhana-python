# Program membuat kalkulator sederhana yang dapat menambah, mengurangi, mengalikan dan membagi menggunakan fungsi
# Fungsi ini menambahkan dua angka
def add(x, y):
   return x + y
# Fungsi ini mengurangi dua angka
def subtract(x, y):
   return x - y
# Fungsi ini mengalikan dua angka
def multiply(x, y):
   return x * y
# Fungsi ini membagi dua bilangan
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# membuat input dari pengguna
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
