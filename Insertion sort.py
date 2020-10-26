import sys
import os
# This is insertion sort
print("Insertion sort")

# Enter number for a list. For Example "1 2 3 4 5 6 7 8 9"
list = list(map(int, input().split()))


# Check number duplication
for i in range(0 , len(list)-1):
    check_num = list[i]
    for j in range(i+1,len(list)):
        if check_num == list[j]:
            print("Number Duplicated. Program terminated.")
            os._exit(0)

# Sorting start
print("Before sorting : ",  list )

for i in range(1,len(list)) : 
    
    for j in range (0,i):
        
        if list[i] < list[j] :

            temp = list[j]
            list[j] = list[i]
            list[i] = temp
        else :
            continue

    print("   routine-",i," : ",list)

print("Sorting complete : ",list)







    






