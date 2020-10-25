#Name: Aarya Vira
#Roll No: 374

a = str(input("Enter the string  l for Linear Search , b For Binary Search: "))
pos = -1
list = [0,1,2,3,4,5,6,7,8,45,72]
if a == 'b':
    def search(list,n):
        l = 0
        u = len(list)-1
        while l <=u:
            mid = (l+u)//2

            if list[mid] == n:
                globals()['pos']= mid
                return True
            else:
                if list[mid]<n:
                    l = mid+1
                else:
                    u = mid-1
        return False            
    
    list.sort()
    n= int(input("Enter the numbers for binary  search : "))
    if search(list, n):
        print("Number Found ")
    else:
        print("Not Found ")
elif a == 'l':
    #pos = -1
    def search(list ,n):
        i = 0

        while i < len(list):
            if list[i] == n:
                return True
            i = i+1

        return False

    list.sort()
    n= int(input("Enter the numbers for linear search : "))
    if search(list ,n):
        print("Number found ")
    else:
        print("not found")
    
else:
    print("enter valid input")
