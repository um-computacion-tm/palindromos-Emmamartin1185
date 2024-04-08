import unittest

def es_palindrome(palabra):
    
    palabra = palabra.replace(" ", "").lower()

    for i in range(len(palabra)):
        palabra2 = palabra[::-1]
        if palabra[i] != palabra2[i]:
            return False
    return True


def obtener_cantidad_de_palabras_palindrome(lista):
     contador = 0
     for palabra in lista:
         if es_palindrome(palabra):
          contador = contador +1
     return contador


class TestCantidadDePalabrasPalindromes(unittest.TestCase):
    def test_cantidad_de_palabras_palindromes_simple(self):
        lista = ["ala"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 1)

    def test_cantidad_de_palabras_palindromes_con_2(self):
        lista = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_3(self):
        lista = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_4(self):
        lista = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 2)

    def test_cantidad_de_palabras_palindromes_con_5(self):
        lista = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 3)



    def test_cantidad_de_palabras_palindromes_complejo(self):
        lista = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 4)

    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        lista = [
            "ala",
            "neuquen",
            "hola",
            "programacion",
            "palap",
            "neu  quen",
            "agita falsos usos la fatiga",
            "presidente de la camara de diputados: martin menem",
        ]
        resultado = obtener_cantidad_de_palabras_palindrome(lista)
        self.assertEqual(resultado, 5) 

unittest.main()