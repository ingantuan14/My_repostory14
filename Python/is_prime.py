
# The next code is a prime numbers detector:
# Try and see if a number is prime or not
# if the input is not an integer, you'll get an alert!


def is_prime(numero: int) -> bool:
  reference = numero
  while numero > 2:
      numero -= 1 
      div = reference % numero
      if div == 0:
        return False
  return True

def captadatos(): 
  numero = input('Escriba un numero para saber si es primo:_ ')
  if not numero:
    print('Campo vacio')
    return False
  else:
    try:
      numero = int(numero)
      return(numero)
    except: 
      print('valor introducido no es valido, debe ser un numero entero')
      return False

if __name__ == '__main__': 
  numero = captadatos()
  if numero:
    answer = is_prime(numero)
    if answer:
      text = 'es un numero primo'
    else:
      text = 'no es un numero primo'
    print(f'El numero {numero} {text} ')
  else:
    print('Intente de nuevo')