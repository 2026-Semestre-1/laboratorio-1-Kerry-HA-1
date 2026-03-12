"""
Nombre: Calculadora
Entradas: Operacion, digito1 y digito2
Salida: Resultado
Restricciones: Los parámetros deben ser de tipo Entero
"""
def calculadora(Operación, digito1, digito2):
    if not isinstance (Operación, int):
        return "Error: El valor de operacion no es Entero"
    if Operación == 0:
        return "Error: No hay operacion para CERO"

    if not Operación < 5:
        return "Error: El numero de la operación debe ser del 1 a 4"

    if not isinstance(digito1, int):
        return "Error: digito1 no es Entero"

    if not isinstance(digito2, int):
        return "Error: digito2 no es Entero"

    return calculadora_Aux(Operación, digito1, digito2)

def calculadora_Aux(Operación, digito1, digito2):
    s = 1
    r = 2
    m = 3
    d = 4
    

    if Operación == s:
       resultado = digito1 + digito2 

    if Operación == r:
        resultado = digito1 - digito2

    if Operación == m:
        resultado = digito1 * digito2

    if Operación == d:
        resultado = digito1 // digito2
    if digito1 == 0:
        return "La division entre 0 no es posible"
    if digito2 == 0:
        return "La division entre 0 no es posible"

    return resultado

"""
Nombre: contarDigitos
Entradas: num y digito
Salidas: Cantidad de veces que digito aparece en num
Restricciones: Ambos deben ser enteros y digito debe ser menor a 10 y mayor
o igual a 0
"""
def contadorDigitos(num, digito):
    if not isinstance(num, int):
        return "Error: El parametro num debe ser Entero"
    if not isinstance(digito, int):
        return "Error: El parametro digito debe ser Entero2"
    if (0 <= digito <= 10):
        return "Error: El parametro digito debe estar en un rango entre 0 y 10"

    return contadorDigitos_Aux(num, digito)

def contadorDigitos_Aux(num, digito):
    contador = 0
    if (digito == 0):
        while contador < 3:
            contador +=1
            return contador

    if (digito == 3):
        while contador < 4:
            contador += 1
            return contador



    
    


  
    




