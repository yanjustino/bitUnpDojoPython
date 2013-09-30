
def jokenpo(jogo_1, jogo_2):
    if (jogo_1 == jogo_2 ):
        return 'empata'

    situacoes_ganha = [
        ('papel', 'pedra'),
        ('pedra', 'tesoura'),
        ('tesoura', 'papel')
    ]

    situacoes_perde = [(jogo2, jogo1)
                        for jogo1, jogo2
                        in situacoes_ganha]

    if (jogo_1, jogo_2) in situacoes_ganha:
        return 'ganha'

    if (jogo_1, jogo_2) in situacoes_perde:
        return 'perde'

print jokenpo('pedra', 'pedra')
print jokenpo('pedra', 'tesoura')
print jokenpo('tesoura', 'pedra')
