import unittest
import cambia_texto_unitest

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "hola mundo"
        resultado = cambia_texto.todo_mayuscula(palabra)
        self.assertEqual(resultado, "Hola Mundo")

if __name__ ==    "__main__":
    unittest.main()