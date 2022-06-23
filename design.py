import PySimpleGUI as Psg

layout = [
    [Psg.Push(), Psg.Text('Calculadora de IMC!', font='Arial, 25'), Psg.Push()],
    [Psg.Text('Qual seu peso?', font='Arial, 15'), Psg.InputText(key='userpeso')],
    [Psg.Text('Qual sua altura?', font='Arial, 15'), Psg.InputText(key='useraltura')],
    [Psg.Text('Resultado!', font='Arial, 15'), Psg.Push(), Psg.Text(f'{imc_zerado}')],
    [Psg.Push(), Psg.Button('CALCULAR'), Psg.Push()]
]


janela_em_uso = Psg.Window('CALCULADORA DE IMC', layout, size=(600, 600))

while True:
    evento, valor = janela_em_uso.read()
    if evento == Psg.WIN_CLOSED:
        break

