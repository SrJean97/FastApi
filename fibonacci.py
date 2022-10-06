def fibbonacci_func(posicion : int) : 
    a = 1
    b = 1
    if posicion == 1 :
        return 1
    elif posicion == 2 :
        return 1
    else :
        for i in range(posicion) :
            pos = a + b
            b = a
            a = pos 
            return a