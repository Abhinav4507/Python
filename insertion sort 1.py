arr=[]
n=int(input("Enter no of elements : "))

for i in range (0,n):
    ele=int(input("Enter Element : "))
    arr.append(ele)
print("List before sorting : ",arr)

for i in range (1,n):
    l=arr[i]
    j=i-1
    while j>=0 and l < arr[j]:
        arr[j+1] = arr[j]
        j-=1
        arr[j+1] = l

print("Sorted array is : ",arr)