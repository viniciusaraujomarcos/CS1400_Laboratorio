"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""
#comecei fazer o programa e vou colocar a mensagemd e boa vindas.
# TODO #1:
# Imprime un mensaje de bienvenida al programa de comidas de Latinoamérica.
print("bienvenido al programa de comidas de Latinoamérica")
# TODO #2:
# Aqui estou preparando o menu.
# Muestra al usuario una lista de al menos 5 opciones de comidas para elegir.
print(" menu")
print("galinhada $10")
print("feijoada $20")
print("lasanha $30")
print("churrasco $40")
print("PF de posto $50")
# TODO #3:
# Guarda lo que el usuario escribió en una variable llamada `comida`.
#usando lower para q nao haja divergencia na variavel.
# Aqui estou dando a opcao de escolha ao cliente.
comida = input("qual comida vai a querer?\n").lower()
#
# TODO #4:
# Convierte lo ingresado a minúsculas para asegurar la comparación correcta.

# TODO #5:
# Usa una  if / elif / else para verificar la comida elegida.
# Imprime un mensaje con el país de origen para cada comida.
#estou usando as variables para que o cliente receba uma menssagem de acordo com a escolha dele.
if comida == "galinhada":
    print ("uma deliciosa galinhada saindo.")
elif comida == "feijoada":
    print("essa e muito boa.")
elif comida == "lasanha":
    print(" esse prato e maravilhosolasanha.")
elif comida == "churrasco":
    print("esse e verdadeeiramente brasileiro.")
elif comida == "PF de posto":
    print("esta muito barato esse.")
else:
    print("te darei mais uns minutos para decidir.")
    
## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""
