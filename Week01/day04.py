# Function basic syntax

# Global vs Local
x = 10
def show():
    print(x)
def change():
    global x
    x = 99
    print(x)
show()
change()