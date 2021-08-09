# 1. Wap to demonstrate different number data types in python

a = 10
b = 11.5
c = 2.05j

print("a is",type(a))
print("b is",type(b))
print("c is",type(c))

#2. WAP to perform different arithmetic problems between two numbers

a=int(input("enter a"))
b=int(input("enter b"))
print("addition",a+b)
print("substraction",a-b)
print("multiplication",a*b)
print("division",a/b)
print("modulus",a%b)
print("exponential",a**b)
print("floor division",a//b)

#3. Write a program to create, concatenate and print a string and accessing sub-string from a given string.

s1=input("Enter the first string:")
s2=input("Enter the second string")
print(s1)
print(s2)
print("Concatenation", s1+s2)
print("substring",s2[1:4])

#4. Python program to check if the list contains three consecutive common numbers in Python

#Example 1 : Only one occurrence of a 3 consecutively occurring element.

arr = [4, 0, 0, 0, 3, 8]
size = len(arr)
for i in range(size - 2):

    if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
        print(arr[i])

#Example 2 : Multiple occurrences of 3 consecutively occurring elements.

arr = [1, 1, 1, 64, 23, 64, 22, 22, 22]
size = len(arr)

for i in range(size - 2):

    if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
        print(arr[i])

# 5. Python program to find common elements in three lists using sets

def IntersectionOfSets(arr1, arr2, arr3):

    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)
    set1 = s1.intersection(s2)
    result_set = set1.intersection(s3)
    final_list = list(result_set)
    print(final_list)

if __name__ == '__main__':
    # Elements in Array1
    arr1 = [1, 5, 10, 20, 40, 80, 100, 0]

    # Elements in Array2
    arr2 = [6, 7, 20, 80, 100, 0]

    # Elements in Array3
    arr3 = [3, 4, 15, 20, 0, 30, 70, 80, 120]

    IntersectionOfSets(arr1, arr2, arr3)