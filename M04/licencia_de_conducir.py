#Marco
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
#
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
 #
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
 #
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
 #
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""
# iniciando o programa dz de rotina.
print("Boa tarde! bem vindo ao DMV")
print("Vamos da inicio ao seu processo de habilitacao.")
idade = int(input("quantos anos vc tem? "))
if idade < 18:
    print("Vai pra casa e espera completar sua maior idade. voce precisa de 18 ou mais para poder ter uma habilitacao")
# adicionando o else para continuar o programa caso o sujeito seja maior de 18 anos.
else:

  print("Me de aqui sua habilitacao.")
  seguranca = input("Ta usando sinto de seguranca? (sim/nao)").lower()
  sono = input("Voce durmiu menos de 4 horas esta noite? (sim/nao)").lower()
  oculos = input("esqueceu seus oculos? brigou com eles foi ?").lower()
#adicionando as condicionais.
  if seguranca == "sim" and sono == "nao" and oculos == "nao":
     print("Pode seguir sua viagem.")
  elif oculos == "sim" or sono == "sim":
    print("entrega as chaves.")
  elif not seguranca == "sim":
     print("coloque o sinto antes de sair.")
  else:
     print("Chame o uber")
  