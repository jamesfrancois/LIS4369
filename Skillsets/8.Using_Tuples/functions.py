def get_requirements():
   
    print("Developer: James S. Francois")
    print("Python Loops")
    print("\nProgram Requirements:\n"
    +"1. Tuples (Python data structure): *immutable* (cannot be changed!), ordered sequence of elements.\n"
    +"2. Tuples are immutable/unchangeable--that is, cannot insert, update, delete.\n"
    +"3. Create tuple using parentheses (tuple): my_tuplel = (cherries, apples, bananas, oranges)"
    +"4. Create tuple (packing), that is, *without* using parentheses (aka tuple packing): my_tuple2 = 1, 2, three, four\n"
    +"5. Python tuple (unpacking), that is, assign values from tuple to sequence of variables: fruit1, fruit2, fruit3, fruit4 = my_tuple1"
    +"6. Create a program that mirrors the following IPO (input/process/output) format.")

get_requirements()
tuple1= ('cherries', 'apples', 'bananas', 'oranges')
tuple2= 1, 2, 'one','two'

print('Print tuple1')
print(tuple1)
print()

print('Print tuple2')
print(tuple2)
print()

cherries, apples, bananas, oranges = tuple1
print('tuple1 unpacking')
print(f'{cherries} {apples} {bananas} {oranges}')
print()

print('Print 3rd element in tuple2 (one)')
print(tuple2[2])
print()

print('Print slice of tuple (second and third element)')
print(tuple2[1:3])
print()

print('reasign tuple2 using parenthesis')
tuple2 = (1,2,3,4)
'''tuple_to_list = list(tuple2)
for item in tuple_to_list[2:]:
    tuple_to_list.remove(item)
tuple_to_list.append('adding')
tuple_to_list.append('this')
list_to_tuple = tuple(tuple_to_list)'''
print(tuple2)
print()

print('Reasign tuple2 using packing')
tuple2 = 'one', 'two', 'three', 'four'
'''tuple2 = list(tuple2)
tuple2.clear()
tuple2 = 1, 2, 'repacking', 'tuple'
tuple2 = tuple(tuple2)'''
print(tuple2)
print()

print('number of elements in tuple1:',len(tuple1))
print()
print('Print the type of tuple1:', type(tuple1))