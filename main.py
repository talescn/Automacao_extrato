import pyautogui
import time
import pandas as pd
import pdfplumber
import pytesseract
from PIL import Image
import re
import pygetwindow as gw
import calendar
from datetime import datetime
import pyperclip

# Configure o caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def navegar_para_baixa_entradas():
    """Navega até a seção de baixa de entradas no sistema."""
    pyautogui.click(x=315, y=55)  # Clica no menu "Parcelas a Pagar"
    time.sleep(1)
    pyautogui.click(x=322, y=253) 
    time.sleep(1)
    pyautogui.click(x=596, y=254) 
    time.sleep(1)

# Dicionário de meses para conversão de número para nome
meses = {
    "1": "Janeiro",
    "2": "Fevereiro",
    "3": "Março",
    "4": "Abril",
    "5": "Maio",
    "6": "Junho",
    "7": "Julho",
    "8": "Agosto",
    "9": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro"
}

# Solicita o mês de importação ao usuário
print("Digite o Mês de importação (1-12):")
mes_numero = input().strip()

# Define o ano atual (pode ser ajustado para datetime.now().year)
ano_atual = 2024

# Verifica se o mês é válido e calcula a data de vencimento
if mes_numero in meses:
    mes_nome = meses[mes_numero]
    ultimo_dia = calendar.monthrange(ano_atual, int(mes_numero))[1]  # Obtém o último dia do mês
    data_vencimento = f"{ultimo_dia}/{mes_numero.zfill(2)}/{ano_atual}"  # Formata a data de vencimento
else:
    print("Número do mês inválido. Por favor, insira um número entre 1 e 12.")

def capturar_valor_parcela():
    """Captura o valor da parcela a partir da interface gráfica."""
    # Clicar nas datas no campo vencimento 
    pyautogui.click(x=237, y=379)
    pyautogui.write(f"01/{mes_numero.zfill(2)}/{ano_atual}")  # Escreve a data formatada
    time.sleep(2)
    pyautogui.click(x=477, y=377)  # Ajuste as coordenadas conforme necessário
    pyautogui.write(data_vencimento)  # Escreve a data de vencimento
    time.sleep(2)

    # Clicar no botão de buscar
    pyautogui.click(x=900, y=755)
    time.sleep(2)

    # Selecionar e copiar o texto
    pyautogui.click(x=1020, y=340)
    time.sleep(2)
    pyautogui.rightClick(x=410, y=343)
    pyautogui.click(x=463, y=409)
    time.sleep(2)
    
    # Obter o texto da área de transferência
    valor_texto = pyperclip.paste()
    print(f"Texto copiado: {valor_texto}")  # Verifique o texto copiado
    
    # Processar o texto copiado
    match = re.search(r'(\d+,\d{2})', valor_texto)
    if match:
        return float(match.group(1).replace(',', '.'))
    else:
        print("Erro ao capturar valor da parcela.")
    return None

def extrair_valores_extrato(pdf_path):
    """Extrai valores de um extrato em PDF."""
    valores_extrato = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                matches = re.findall(r'(\d+,\d{2})', text)
                for match in matches:
                    valores_extrato.append(float(match.replace(',', '.')))
    return valores_extrato

def verificar_pagamento(valor_parcela, valores_extrato):
    """Verifica se o valor da parcela está presente nos valores do extrato."""
    return valor_parcela in valores_extrato

def lancar_baixa(valor_parcela):
    """Lança a baixa do pagamento no sistema."""
    pyautogui.click(x=789, y=487)  # Campo do valor pago
    time.sleep(1)
    pyautogui.click(x=605, y=395)
    time.sleep(1)
    
    # Formata o valor da parcela com vírgula
    valor_parcela_formatado = f"{valor_parcela:.2f}".replace('.', ',')
    pyautogui.write(valor_parcela_formatado)
    pyautogui.press('tab')
    time.sleep(1)

    pyautogui.click(x=791, y=763)  # Campo novo lançamento contábil
    time.sleep(1)
    pyautogui.doubleClick(x=607, y=593)  # Campo do banco
    time.sleep(1)

    pyautogui.write('574')
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(x=1000, y=300)  # Botão de confirmar
    time.sleep(2)

def automatizar_baixa(pdf_path):
    """Automatiza o processo de baixa de pagamentos."""
    navegar_para_baixa_entradas()
    
    valor_parcela = capturar_valor_parcela()
    if valor_parcela:
        print(f"Valor da parcela: {valor_parcela}")

        valores_extrato = extrair_valores_extrato(pdf_path)
        if verificar_pagamento(valor_parcela, valores_extrato):
            print("Pagamento encontrado! Lançando baixa...")
            lancar_baixa(valor_parcela)
        else:
            print("Nenhum pagamento correspondente encontrado.")
    else:
        print("Erro ao capturar valor da parcela.")

# Título do aplicativo para ativação da janela
titulo_aplicativo = "Domínio Escrita Fiscal"

# Obtém a janela do aplicativo
janelas = gw.getWindowsWithTitle(titulo_aplicativo)
if janelas:
    janela_obj = janelas[0]
    print(f"Encontrado: {janela_obj.title}")
    
    # Aguarde um pouco antes de ativar
    time.sleep(2)
    
    try:
        janela_obj.activate()
        print("Janela ativada com sucesso!")
    except Exception as e:
        print(f"Erro ao ativar janela: {e}")
else:
    print("Janela não encontrada.")

# Aguarde um pouco para garantir que a janela está ativa
time.sleep(2)

# Chamar a automação
automatizar_baixa(r'Y:\Intranet\0363 - Empório SLX Ltda - ME\EXTRATOS E COMPROVANTES\2024\10\4 - Extrato Mensal_Outubro2024At.pdf')
