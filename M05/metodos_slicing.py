#Marcos Alves oct 01.2026
# Conteo descendente
#Contagem Reversa com range() pronto e funcionando.
num = int(input("Introduce el número inicial: "))
"""
for i in range(num, 0, -1):
    print("Conteo:", i)
"""
    # Conteo descendente
num = int(input("Introduce el número inicial: "))

for i in range(num, -1, -2):
    print("Conteo:", i)
# 1. Ejecuta el programa e introduce 10. Al observar la consola, ¿en qué número comenzó la cuenta y en cuál terminó?

#Inicio:10 Fin: 1

# 2. ¿Por qué es necesario que el parámetro step (paso) sea un número negativo al realizar un conteo descendente?
#para que el conteo se realice en orden inverso.
# 3. ¿Por qué el valor final se configuró en 0 si queríamos que el conteo se detuviera en el número 1?
#Porque el número que ponemos al final no cuenta; siempre se refiere a un número anterior.
#Práctica de Sección:
# 4. Modifica el código para que cuente hacia atrás de 2 en 2, comenzando desde el número elegido por el usuario y deteniéndose exactamente en el 0 (inclusive). Escribe la línea de tu range() modificada:

#Respuesta: range( _______ , _______ , _______ )