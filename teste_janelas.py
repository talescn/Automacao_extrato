import pygetwindow as gw

# Obter todos os títulos de janelas abertas
janelas = gw.getAllTitles()

# Imprimir todos os títulos
for janela in janelas:
    print(janela)