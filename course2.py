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

my_float = 6.444
print('my_float', my_float, type(my_float))

my_complex = 3+5j
print('my_complex', my_complex, type(my_complex))

my_complex_from_int=complex(my_int)
my_int_from_float=int(my_float)
my_float_from_int=float(my_int)
print('my_complex_from_int', my_complex_from_int, type(my_complex_from_int))
print('my_int_from_float', my_int_from_float, type(my_int_from_float))
print('my_float_from_int', my_float_from_int, type(my_float_from_int))

# Python None is...
# and or not , is, is not - operators
# print(7 is 7)
print([1, 2] is [1, 2])  # are found at different memory locations

# in si not in - belonging operators
# === - complete equality (in Javascript) checks the type and the value
# 7=='7' va da true, dar 7==='7' va da false
# str(7)=='7' sau 7==int(7)

# print(isinstance(a, type(b)) and isinstance(b, type(a)) and a == b)
# print(a == b)  # false because they are different types
a = 7
b = 7
print(a is b, id(a), id(b))  # prints the address from the memory

c = [1, 2]
d = [1, 2]
print(c is d, id(c), id(d))
# ord() - ASCII
# ' ' == " "
escape_character = 'hhfidjsif \' fhddjhd'  # ' - can be used as a character within the string

print(r'linia 1\nlinia2\nlinia2\n')  # rawstring
print(R'linia 1\nlinia2\nlinia2\n')

price = 10.00
name = 'Hamburger'
msg = 'Top product: {0}  costs only ${1:.2f}'.format(name, price)  # formatting from a database, 0 = placeholder 0
msg = 'Top product: {my_placeholder1} costs only ${my_placeholder2:.2f}'.format(my_placeholder1=name, my_placeholder2 = price)
msg = 'Top product: {name}  costs only ${price:.2f}'.format(name=name, price=price)
print(msg)

my_list = [1, 2, True, 'abc']
# 0 1 2 3
# -4 -3 -2 -1 #indexes in the list
print(my_list)
print(2 in my_list)  # true
print(my_list[0])  # 1
print(my_list[-4])  # 1
new_list = my_list[:-1:2]  # -1 element will not be part of the new list, 2 is the step
print(len(my_list))
print(new_list)
new_list = my_list[1:1:2]
print(new_list)

my_list[2] = False
print(my_list)

my_list[2] = ['a', [1, 2], 4, 5, 6]
print(my_list[2][1][1])  # prints 2

rev_list = my_list[::-1]  # creates the list in reverse
print(rev_list)
# tuples - lists that cannot be modified; uses less memory - 24 bits for a tuple, 40 bits for a list = IMMUTABLE

tuple_list = [1, 2, 3]
print(tuple_list)  # [1, 2, 3]
tuple_list = tuple (tuple_list)
print(tuple_list)  # (1, 2, 3)

my_dict = {'a': 12, 'b': 12, 3: 22, 'b':100, 'abc': 15}  # b will have the last occurrence of key
print(my_dict)
print(my_dict['a'])
print(my_dict.get['abc', 'my default value'])
print( )
if 'a' in my_dict:
    print("a not in my_dict")