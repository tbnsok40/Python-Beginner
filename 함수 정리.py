def hello():
    print("Hello, lim")
    print("Maestro of S/W")

hello()

def hello(name):
    print("Hello, %s" %name)
    print("Maestro of S/W")

hello("성후")
print()

def print_sum(a,b):
    print(a + b)

def print_product(a, b):
    print(a * b)

def print_residue(a, b):
    print(a % b)

def print_average(x, y, z):
    print((x + y + z) / 3)

print_sum(4, 2)
print_product(3, 4)
print_residue(13, 3)
print_average(5, 10, 15)
print()

def print_profile(name, age):
    print(name)
    print(age)

my_name = "LIm"
my_age = 26

print(my_name, my_age)
print()

def next_number(n):
    m = n + 1
    print(m)

next_number(3)
def print_full_name(f_name, l_name):
    print(l_name, f_name)
print_full_name("윤수", "이")