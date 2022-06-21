import PySimpleGUI as psg

layout = [
    [psg.Text(), psg.InputText()],
    [psg.Text(), psg.InputText()],
    [psg.Text(), psg.InputText()],
    [psg.Button()]
]

layout_calcular = [
    [psg.Text(), psg.InputText()],
    [psg.Text(), psg.InputText()],
    [psg.Text(), psg.InputText()],
    [psg.Button()]
]

janela_em_uso = psg.Window('CALCULADORA DE IMC', layout)

while 1:
    evento, valor = janela_em_uso.read()
    if evento == psg.WIN_CLOSED:
        break

