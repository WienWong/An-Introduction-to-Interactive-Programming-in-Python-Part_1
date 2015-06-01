
# Quiz 1
import math
import random

# Question 2
p = True
q = True
print not (p or not q)

p = True
q = False
print not (p or not q)

p = False
q = True
print not (p or not q)

p = False
q = False
print not (p or not q)
print


# Question 3
def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"
    
print do_stuff()
print


# Question 4
n = 123
print n % 100
print n % 10
print (n % 100 - n % 10)
print (n % 100 - n % 10) / 10

print (n // 10)
print (n // 10) % 10

print (n % 10) / 10

print((n - n % 10) % 100) / 10

print(n - n % 10) / 10
print


# Question 5
print random.randrange(0, 10) # 0-9
print random.randint(0, 10)   # 0-10
print


# Question 6
print -5*0**5 + 69* 0**2 - 47 
print -5*1**5 + 69* 1**2 - 47 
print -5*2**5 + 69* 2**2 - 47 
print -5*3**5 + 69* 3**2 - 47 
print


# Question 7
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    # Put your code here.
    return present_value*(1 + rate_per_period)**periods

print future_value(500, .04, 10, 10) # should return 745.317442824.
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
print


# Question 8
def area_of_polygon(n_sides, length_of_eachside):
    print 0.25 * n_sides * length_of_eachside**2 / math.tan(math.pi/n_sides)

area_of_polygon(7,3)
print
    
    
# Question 9
def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

print max_of_3(5, 8, 3)
print


# Question 10
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2)**(0.5)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)
