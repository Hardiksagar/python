class aircraft:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def move_left(x):
    x -= 1
    return x

def move_right(x):
    x += 1
    return x

def move_up(y):
    y += 1
    return y

def move_down(y):
    y -= 1
    return y

# Creating a multiple instance of the Aircraft class
p1 = aircraft(0, 0)
p2 = aircraft(2, 2)
p3 = aircraft(3, 3)
p4 = aircraft(4, 4)
p5 = aircraft(5, 5)

for i in range(2):
    x1 = move_left(p1.x)
    y2 = move_up(p2.y)
    x3 = move_left(p3.x)
    x4 = move_right(p4.x)
    x5 = move_left(p5.x)

for i in range(1):
    y1 = move_down(p1.y)
    x2 = move_right(p2.x)
    y4 = move_up(p4.y)
    y5 = move_down(p5.y)

for i in range(3):
    y3 = move_down(p3.y)
    x4 = move_right(x4)
    y4 = move_up(y4)

# Final co-ordinates of the aircraft
print("x-coordinate of Aircraft#1 :",x1,"\ny-coordinate of Aircraft#1 :",y1)
print("x-coordinate of Aircraft#2 :",x2,"\ny-coordinate of Aircraft#2 :",y2)
print("x-coordinate of Aircraft#3 :",x3,"\ny-coordinate of Aircraft#3:",y3)
print("x-coordinate of Aircraft#4 :",x4,"\ny-coordinate of Aircraft#5 :",y4)
print("x-coordinate of Aircraft#5 :",x5,"\ny-coordinate of Aircraft#5:",y5)
