jogada_c1 = "pedra"
jogada_c2 = "pedra"

ganhador = None

if jogada_c1 == jogada_c2:
    msg = "Empate"

match jogada_c1:
    case "pedra":
        if jogada_c2 == "papel":
            msg == "Jogador 2 ganhou"
        if jogada_c2 == "tesoura":
            msg == "Jogador 1 ganhou"
    case "papel":
        if jogada_c2 == "pedra":
            msg == "Jogador 1 ganhou"
        if jogada_c2 == "tesoura":
            msg == "Jogador 2 ganhou"
    case "tesoura":
        if jogada_c2 == "pedra":
            msg == "Jogador 2 ganhou"
        if jogada_c2 == "papel":
            msg == "Jogador 1 ganhou"