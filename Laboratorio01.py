"""
Nombre: calcularRenta
Entradas: Salario mensual, porcentaje
Salidad: Salario menos el porcentaje de impuestos
"""
def calcularRenta(n):
    if not (isinstance(n,int)):
        return "Error: El valor debe ser Entero"

    if (n < 0):
        return "Error: El valor debe ser mayor a CERO"

    
    if (isinstance(n,int)):
        if (n < 817000):
            return 0

    if (isinstance(n,int)):
        if(1226000 >= n > 817000):
            resultado = ((n - 817000) * 10/100)
            return resultado                    
    if(isinstance(n,int)):
        if (n > 1226000):
            resultado = ((n - 1226000) * 15/100) + 40900
            return resultado
"""
Nombre: contarDigitos
Entrada: num
Salidas : digitos
"""
def contarDigitos(num):
    if not isinstance(num, int):
        return "Error: num debe ser Entero"
    elif (num < 0):
        num *= -1
    elif num == 0:
        return 1

    return contarDigitos_Aux(num)

def contarDigitos_Aux(num):
    digitos = 0

    while num != 0:
        num //= 10
        digitos += 1

    return digitos



"""
Nombre: contadordigitos_V2
Entradas: num, digito
Salidad: numero de veces que aparece el digito
"""
def contadorDigitos_V2(num,digito):
    if not isinstance(num,int):
        return "Error: num debe ser Entero"

    if not isinstance(digito, int):
        return "Error: digito debe ser Entero"

    if(digito > 10):
        return "Error: digito debe ser menor a 10"

    return contadorDigitos_V2_Aux(num, digito)

def contadorDigitos_V2_Aux(num, digito):
     num = abs(num)
    if num == 0 and digito == 0:
        return 1

    contador = 0
    while num > 0:
        ultimo = num % 10
        if ultimo == digito:
            contador += 1
        num //= 10
    return contador

    return(contadorDigitos_V2(102039480, 0))  
    return(contadorDigitos_V2(132033483, 3))
    return(contadorDigitos_V2(0, 0))          
    return(contadorDigitos_V2(-100, 1))   




     
        

    

    
