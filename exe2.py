# aircraft class with variables:
class aircraft:
    x = 0
    y = 0
    acceleration_constant = 1
# Methods to inc. and dec. x and y
    def __init__(self, x, y, acceleration_constant):
        self.x = x
        self.y = y

def move_left(x):
    x-=1
    return x

def move_right(x):
    x+=1
    return x

def move_up(y):
    y+=1
    return y

def move_down(y):
    y-=1
    return y

# Creating a single instance of the Aircraft class
p1=aircraft(0, 0, 1)

# Moving the aircraft
x = p1.x
y = p1.y

x  = move_left(x)
y = move_up(y)

for i in range(4):
    x = move_right(x)

for i in range(6):
    y  = move_down(y)

# Final co-ordinates of the aircraft
print("x co-ordinate:",x,"\ny co-ordinate:",y)
