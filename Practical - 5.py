list1 = [1,2,3,4,5,6,7,8,9,10]
print("List = ",list1)
size = len(list1)
def binary_search(x):
    print("BINARY SEARCHING")
    low = 0
    high = len(list1) - 1
    mid = 0
    while low <= high: 
        mid = (high + low) // 2
        if list1[mid] < x: 
            low = mid + 1
        elif list1[mid] > x: 
            high = mid - 1
        else: 
            return mid 
    return "None it not in the list"

def linear_search(n):
	print("LINEAR SEARCHING")
	if n not in list1:
		print(n,"not in the list")
	else:
		for i in range(size):
			if list1[i]==n:
				print("index of ", n," is ",i)
				
n = input("Enter (L) for Linear search and  (B) for Binary search :")
if n=="L" or n=="l":
	y = int(input("Enter a no. from the given list1 "))
	linear_search(y)
elif n=="B" or n=="b":
	y = int(input("Enter a no. from the given list1 "))
	print("index of ",y," is ",binary_search(y))
else:
	print("Invalid input")
