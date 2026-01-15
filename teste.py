


def media_invest (precos: list, qtde: int) -> float:
    """"
    Essa função traz as médias dos valores de acordo com a janela
    """

    if len(precos) < qtde:
        return 0.0
    
    ult_valores = precos[-qtde:]
    media = sum(ult_valores) / qtde
    return media



periodo = 4
precos_bitcoin = [10, 20, 30, 40, 10, 5, 9]

print(f"A média do Bitcoin nos últimos {periodo} períodos foi de R$ {media_invest(precos_bitcoin, periodo)} reais")





