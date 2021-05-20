# declare a list containing the elements listed: 7, 8, 9, 2, 3, 1, 4, 10, 5, 6
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# print an ordered list
sorted_asc = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
sorted_asc.sort()
print("list sorted asc:", sorted_asc)

# print a list ordered desc
sorted_desc = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
sorted_desc.sort(reverse=True)
print("list sorted desc:", sorted_desc)

# print the even numbers from the list using SLICE
print("even numbers from my list:", sorted_asc[1::2])

# print the odd numbers from the list using SLICE
print("odd numbers from my list:", sorted_asc[::2])

# print the multiples of 3 from the list
print("multiples of 3:", sorted_asc[2::3])


