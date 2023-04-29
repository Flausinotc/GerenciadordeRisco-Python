import PySimpleGUI as sg

sg.theme('Reddit')  # Define o tema da janela

layout = [  # Define a estrutura da janela
    [sg.Text('Digite o valor aportado:')],
    [sg.InputText(key='aporte')],
    [sg.Text('Digite o lucro desejado:')],
    [sg.InputText(key='lucro')],
    [sg.Button('Calcular')],
    [sg.Text(size=(40,1), key='resultado')],
    [sg.Text(size=(40,1), key='resultado2')]
]

window = sg.Window('Calculadora de Stop Loss', layout)  # Cria a janela

while True:  # Loop de eventos
    event, values = window.read()  # Lê os eventos e valores
    if event == sg.WIN_CLOSED:  # Se o usuário fechar a janela
        break  # Encerra o loop
    if event == 'Calcular':  # Se o usuário clicar em "Calcular"
        aporte = float(values['aporte'])
        lucro = float(values['lucro'])
        stop = lucro/2
        res = aporte/4
        window['resultado'].update("O stop loss ideal é de R$ {:.2f}".format(stop))
        window['resultado2'].update("A perda máxima permitida é de R$ {:.2f}".format(res))

window.close()  # Fecha a janela ao encerrar o programa
