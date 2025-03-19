   # Automação de Baixa de Pagamentos

   Este projeto é uma automação de processos financeiros utilizando Python, projetada para facilitar a baixa de pagamentos em um sistema específico. A automação interage com a interface gráfica do usuário (GUI) para navegar até a seção de baixa de entradas, capturar valores de parcelas, extrair valores de extratos em PDF e verificar se os pagamentos foram realizados. Se um pagamento correspondente for encontrado, o sistema lança a baixa automaticamente.

   ## Funcionalidades Principais

   - **Navegação Automatizada**: Utiliza a biblioteca `pyautogui` para simular cliques e entradas de teclado, navegando automaticamente pelo sistema financeiro.
   - **Captura de Valores**: Captura valores de parcelas diretamente da interface do sistema e os processa para verificação.
   - **Extração de Dados de PDF**: Utiliza `pdfplumber` para extrair valores de extratos bancários em PDF, facilitando a comparação com os valores das parcelas.
   - **Verificação de Pagamentos**: Compara os valores capturados com os valores extraídos dos extratos para verificar se os pagamentos foram realizados.
   - **Lançamento de Baixa**: Se um pagamento correspondente for encontrado, a automação lança a baixa do pagamento no sistema.
   - **Ativação de Janela**: Utiliza `pygetwindow` para ativar a janela do aplicativo necessário antes de iniciar a automação.

   ## Tecnologias Utilizadas

   - **Python**: Linguagem de programação principal para a automação.
   - **PyAutoGUI**: Para automação de GUI.
   - **PyGetWindow**: Para manipulação de janelas de aplicativos.
   - **PDFPlumber**: Para extração de texto de PDFs.
   - **Pytesseract**: Para OCR, se necessário.
   - **Pandas**: Para manipulação de dados, se necessário.
   - **Pyperclip**: Para manipulação da área de transferência.

   Este projeto é ideal para empresas que precisam automatizar a baixa de pagamentos de forma eficiente, reduzindo erros manuais e economizando tempo.