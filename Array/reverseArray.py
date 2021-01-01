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