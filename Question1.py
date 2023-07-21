a = 0

def b():
    global a
    a = c(a)
def c(a):
    return a + 2