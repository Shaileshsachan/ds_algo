numbers = [10, 20, 30, 40, 50]

print(numbers[0])
numbers[1] = 'shailesh'
print(numbers)

for _ in numbers:
    print(_)

max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print(max)


from array import *

print(dir(array))

array1 = array('i', [10, 20, 30, 40, 50])

for i in array1:
    print(i)

print(array1[0])
print(array1[2])

array1.insert(8, 60)

array1.insert(-1, 70)
print(array1)
for i in array1:
    print(i)

array1 = array('i', [10, 20, 30, 40, 50])

array1.remove(40)

for i in array1:
    print(i)

print(array1.index(50))

array1[3] = 100
for i in array1:
    print(i)
