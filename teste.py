import unittest

from dojo_pedra_papel_tesoura import jokenpo

class Test_teste(unittest.TestCase):
    def test_pedra_empata_com_pedra(self):
        resultado = jokenpo('pedra', 'pedra')
        self.assertEquals(resultado, 'empata')

    def test_pedra_ganha_de_tesoura(self):
        resultado = jokenpo('pedra', 'tesoura')
        self.assertEquals(resultado, 'ganha')

    def test_pedra_perde_com_papel(self):
        resultado = jokenpo('pedra', 'papel')
        self.assertEquals(resultado, 'perde')
   
    def test_papel_ganha_pedra(self):
        resultado = jokenpo('papel','pedra')
        self.assertEquals(resultado,'ganha')

    def test_papel_empata_com_papel(self):
        resultado = jokenpo('papel', 'papel')
        self.assertEquals(resultado, 'empata')

    def test_papel_perde_tesoura(self):
        resultado = jokenpo('papel', 'tesoura')
        self.assertEquals(resultado, 'perde')

    def test_tesoura_empata_com_tesoura(self):
        resultado = jokenpo('tesoura', 'tesoura')
        self.assertEquals(resultado, 'empata')
    

if __name__ == '__main__':
    unittest.main()
