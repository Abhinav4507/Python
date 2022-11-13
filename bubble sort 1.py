#program which takes an array as an input and arrange it in ascending order using bubble sort
 
arr=[]
n=int(input("Enter no of elements : "))

for i in range (0,n):
    ele=int(input("Enter Element : "))
    arr.append(ele)
print("List before sorting : ",arr)

for i in range (n-1):
    for j in range (0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1], arr[j]

print("List after sorting : ", arr)
