from my_module import my_age, str_
from my_package import my_age as aux_age


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')


if True:
    # set instructiuni
    pass
    if False:
        pass
    print('something')

print('my_module.my_age', my_age)
print('my_module.str_', str_)

my_int = 7
print('my_int', my_int)

my_float=6.444
print('my_float', my_float, type(my_float))

my_complex=3+5j
print('my_complex', my_complex, type(my_complex))

my_complex_from_int=complex(my_int)
my_int_from_float=int(my_float)
my_float_from_int=float(my_int)
print('my_complex_from_int', my_complex_from_int, type(my_complex_from_int))
print('my_int_from_float', my_int_from_float, type(my_int_from_float))
print('my_float_from_int', my_float_from_int, type(my_float_from_int))

# Python None is...
# and or not , is, is not - operatori
# print(7 is 7)
print([1, 2] is [1, 2])  # se afla la locatii de memorie diferite in coada si de aceea este fals

# in si not in - operatori de apartenenta
# === - egalitate completa (in Javascript) verifica atat tipul de date cat si valoarea
# 7=='7' va da true, dar 7==='7' va da false
# str(7)=='7' sau 7==int(7)

# print(isinstance(a, type(b)) and isinstance(b, type(a)) and a == b)
# print(a == b)  # false because they are different types
a = 7
b = 7
print(a is b, id(a), id(b))  # afiseaza adresa in memorie

c = [1, 2]
d = [1, 2]
print(c is d, id(c), id(d))
# ord() - ASCII
# ' ' == " "
escape_character = 'hhfidjsif \' fhddjhd'  # ' - can be used as a character within the string


