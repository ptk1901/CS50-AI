list = { 1 , 2 , 3 , 4 }
list2 = {2,3,4}
list3 = {1,2,3,4}
list4 = {1,2,4}
list5 = {1,2,3,4}
set1 = set(list)
set2 = set(list2)
set3 = set(list3)
set4 = set(list4)
set5 = set(list5)

setnew = set()
cellz = {3,2}
difference = set1-set2
print(difference)
setnew = setnew.union(difference)
difference = set1-set3
setnew = setnew.union(difference)
difference = set1-set4
setnew = setnew.union(difference)
difference = set1-set5
setnew = setnew.union(difference)
cell = set(cellz)
number = 10
for row in range(-1,2):
    print(number-row)

print(setnew)
print(set1)






    

#12345
#123789
#45