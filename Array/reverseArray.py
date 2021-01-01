#Program to reverse an array

def reverseArray(arr):
    print(arr[::-1])


print("Enter length of your array: ",end="")
len = int(input())
arr = []
print("Enter your array:")
for i in range(len):
    inp = input()
    arr.append(inp)


print("Entered array is ",end="")
print(arr)
print("Reversed array is ",end="")
reverseArray(arr)


"""
Output:

Enter length of your array: 6
Enter your array:
123
789
abc
xyz
???
1b4
Entered array is ['123', '789', 'abc', 'xyz', '???', '1b4']
Reversed array is ['1b4', '???', 'xyz', 'abc', '789', '123']
"""