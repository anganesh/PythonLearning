import turtle
import calendar

a = 5
print(a)

b="hello"
print(b)

ganesh_turtle = turtle.Turtle()

def square(): 
  ganesh_turtle.forward(100)
  ganesh_turtle.right(90)
  ganesh_turtle.forward(100)
  ganesh_turtle.right(90)
  ganesh_turtle.forward(100)
  ganesh_turtle.right(90)
  ganesh_turtle.forward(100)

square()

ganesh_turtle.forward(100)
square()

print(calendar.weekheader(3))
print
print(calendar.firstweekday())

print(calendar.month(2020,5))

print(calendar.monthcalendar(2020,5))

print(calendar.calendar(2020))

day_of_the_week = calendar.weekday(2020,05,11)

print(day_of_the_week)

is_leap = calendar.isleap(2020)

print(is_leap) 








