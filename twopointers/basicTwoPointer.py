## use two pointers to check if the array has duplicate elements 
#3 since I'm not in a function, print True if a duplicate is present else print false
## (yes I know you can use a hashamp I just want to practice traversing an array)

#        0  1  2  3  4  5  6  7  8
array = [1, 2, 3, 3, 4, 5, 6, 7, 7]

### what if we did a current pointer then looked at the next value 
### instead?

curr = 0
next = curr + 1

res = set()

## ok it solved half of the problem 
## how does it get the other duplicate??? I'll think this over
for i in array:
    if array[curr] == array[next]:
        res.add((curr, next))
        
    else:
        curr += 1
        next += 1

print(res)

    


'''
left = 0
right = 1

while left <= right:
    if array[left] == array[right]:
        print("True, there is a duplicate present")
        print(left, right)
    else:
        print('not duplicates')
        print(left, right)
        left += 1 
        right += 1

        break
    
while left >= right:
    if array[left] == array[right]:
        print("True, there is a duplicate present")
    else:
        print('not duplicates')
        left += 1
        right += 1

    break
'''


