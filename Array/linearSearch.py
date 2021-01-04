def linear_search(arr, count, num):
    for i in range(count):
        if(arr[i] == num):
            print("Number", num, "is at position",i+1)
    
        

arr = []
print("How many elements do you want to enter? ",end="")
count=int(input())
print("Enter Numbers:" )
for i in range(count):
    inp = int(input())
    arr.append(inp)


print("Entered array is :")
print(arr)

print("Which number you want to find? ",end="")
num= int(input())

linear_search(arr,count,num)

"""
Output:
How many elements do you want to enter? 5
Enter Numbers:
242
2425
23
4444
5454
Entered array is :
[242, 2425, 23, 4444, 5454]
Which number you want to find? 4444
Number 4444 is at position 4
"""
