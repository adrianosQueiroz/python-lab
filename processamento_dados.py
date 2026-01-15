def padronizar_texto(texto: str) -> str:
    """
    Remove espaços extras e coloca o texto em formato 'Title Case': primeira letra maiúscula.
    Útil para nomes de marcas, produtos ou nomes de clientes.
    """
    # .strip() remove espaços no início e fim
    # .title() coloca a primeira letra de cada palavra em maiúscula
    return texto.strip().title()


# Testes
print(padronizar_texto("   charm rio   "))       # Resultado: Charm Rio
