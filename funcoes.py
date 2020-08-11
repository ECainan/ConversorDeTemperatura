

def fercel(temp):
    f = (1.8 * temp) + 32
    return f

def celfer(temp):
    c = (temp-32)/1.8
    return c

def kelcel(temp):
    c = temp - 273
    return c

def celkel(temp):
    k = temp + 273
    return k

def kelfer(temp):
    f = (temp*1.8) - 459.67
    return f

def ferkel(temp):
    k = (temp + 459.67) * (5/9)
    return k