
def jokenpo(jogo_1, jogo_2):
    if (jogo_1 == jogo_2 ):
        return 'empata'

    situacoes_ganha = [
        ('papel', 'pedra'),
        ('pedra', 'tesoura'),
        ('tesoura', 'papel')
    ]

    situacoes_perde = [(jogo_2, jogo_1) 
                        for jogo_1, jogo_2
                        in situacoes_ganha]

    if (jogo_1, jogo_2) in situacoes_ganha:
        return 'ganha'

    if (jogo_1, jogo_2) in situacoes_perde:
        return 'perde'

    return 'empate'
