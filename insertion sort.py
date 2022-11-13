#insertion sort

arr=[95,65,7,-2,48]
n=len(arr)
for i in range (1,n):
    l=arr[i]
    j=i-1
    while j>=0 and l < arr[j]:
        arr[j+1] = arr[j]
        j-=1
        arr[j+1] = l

print("Sorted array is : ",arr)







