
# http://www.codeskulptor.org/#user39_5PqX3jJTBCIXiLi_14.py

# Quiz 4a, Question 3
my_list = ["This", "course", "is", "great"]
print my_list[1:3]

print

# Quiz 4a, Question 4
# Odd, then the two parts should have lengths n and n+1.
my_list1 = [1,2,3,4,5]
print my_list1[0 : len(my_list1) // 2] 
print my_list1[len(my_list1) // 2 : len(my_list1)]

print 

# Even, then the two parts should each have length n.
my_list2 = [1,2,3,4,5,6]
print my_list2[0 : len(my_list2) // 2] 
print my_list2[len(my_list2) // 2 : len(my_list2)]

print 

# Quiz 4a, Question 5
radius = 2
a = [4, 7]
b = [2, 9]
dist = ( (a[0] - b[0])**2 + (a[1] - b[1])**2 )**0.5 - radius
print round(dist, 4) 

### Result
['course', 'is']

[1, 2]
[3, 4, 5]

[1, 2, 3]
[4, 5, 6]

0.8284
