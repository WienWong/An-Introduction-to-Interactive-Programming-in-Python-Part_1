
# Ex1 for expressions
# Compute the number of feet corresponding to a number of miles.

###################################################
# Miles to feet conversion formula
# Student should enter statement on the next line.
feetpermile = 5280
miles = 13
feet2miles = feetpermile * miles
print feet2miles
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#68640

# Compute the number of seconds in a given number of hours, minutes, and seconds.

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter statement on the next line.

hours = 7
minutes = 21
seconds = 37
tot = hours * 3600 + minutes * 60 + seconds
print tot
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#26497

# Compute the length of a rectangle's perimeter, given its width and height.

###################################################
# Rectangle perimeter formula
# Student should enter statement on the next line.
w = 4
h = 7
print 2* w + 2* h

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#22

# Compute the area of a rectangle, given its width and height.

###################################################
# Rectangle area formula
# Student should enter statement on the next line.

w = 4
h = 7
print "Area of a rectangle is " + str(w * h)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#28

# Compute the circumference of a circle, given the length of its radius.

###################################################
# Circle circumference formula
# Student should enter statement on the next line.

radius = 8
pi = 3.14
circumference = 2 * pi * radius
print circumference
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#50.24

# Compute the area of a circle, given the length of its radius.

###################################################
# Circle area formula
# Student should enter statement on the next line.

radius = 8
pi = 3.14
area = pi * radius**2
print area

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#200.96

# Compute the future value of a given present value, annual rate, and number of years.

###################################################
# Future value formula
# Student should enter statement on the next line.

interest = 0.07
year = 10
value = 1000
print value*(1 + interest)**10

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#1967.15135729

# Compute a name tag, given the first and last name.

###################################################
# Name tag formula
# Student should enter statement on the next line.

print "My name is " + "Joe " + "Warren" + "."
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#My name is Joe Warren.

# Compute the statement about a person's name and age, given the person's name and age.

###################################################
# Name and age formula
# Student should enter statement on the next line.

print "Joe Warren is " + str(52) + " years old."
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 52 years old.

# Compute the distance between the points (x0, y0) and (x1, y1).

###################################################
# Distance formula
# Student should enter statement on the next line.

# Hint: You need to use the power operation ** .
import math
x = [2, 2]
y = [5, 6]
dist = math.sqrt( (x[0] - y[0])**2 + (x[1] - y[1])**2 )
print dist
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#5.0

