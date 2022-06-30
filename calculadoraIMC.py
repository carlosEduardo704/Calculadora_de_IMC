import PySimpleGUI as Psg

# Funções para diminuir o tamanho do nome de alguns widgets.


def push():
    return Psg.Push()

# função que calcula o IMC


def calcula_imc(peso, altura):
    imc = peso/(altura**2)
    if imc < 18.5:
        return f'Seu Imc é de {imc:.2f}, Você está no índice: de Magreza!'
    elif 18.5 < imc < 24.9:
        return f'Seu Imc é de {imc:.2f}, Você está no índice: Normal!'
    elif 25 < imc < 29.9:
        return f'Seu Imc é de {imc:.2f}, Você está no índice de: Sobrepeso!'
    elif 30 < imc < 34.9:
        return f'Seu Imc é de {imc:.2f}, Você está no índice de: Obesidade Grau I!'
    elif 35 < imc < 39.9:
        return f'Seu Imc é de {imc:.2f}, Você está no índice de: Obseidade Grau II'
    elif imc > 40:
        return f'Seu Imc é de {imc:.2f}, Você está no índice de: Obseidade Grau III'
    else:
        return 'Infelizmente, não consegui calcular o seu imc!'

# ---------------------------------------------------JANELAS --------------------------------------------------------- #


def janela_inicio():
    Psg.theme('Black')
    layout = [
        [push(), Psg.Text('Calculadora de IMC!', font=('times', 40)), push()],
        [push(), Psg.Text('Qual seu peso?  ', font=('times', 25)), push(), Psg.InputText(key='peso', size=(20, 0)),
         push()],
        [push(), Psg.Text('Qual sua altura?', font=('times', 25)), push(), Psg.InputText(key='altura', size=(20, 0)),
         push()],
        [push(), Psg.Button('CALCULAR', font=('times', 25), button_color='Gray'), push()]
    ]
    return Psg.Window('CALCULADORA IMC', layout, size=(600, 300), finalize=True)

#5


def janela_erro_campos_vazios():
    Psg.theme('Black')
    layout = [
        [push(), Psg.Text('ERRO!', font=('times', 50)), push()],
        [push(), Psg.Text('Os campos não podem ficar vazios, por favor', font=('times', 20)), push()],
        [push(), Psg.Text('preencha todos os campos!', font=('times', 20)), push()],
        [push(), Psg.Button('VOLTAR', font=('times', 25), button_color='Gray'), push()]
    ]
    return Psg.Window('CALCULADORA IMC', layout, size=(600, 300), finalize=True)


def janela_erro_valor_incorreto():
    Psg.theme('Black')
    layout = [
        [push(), Psg.Text('ERRO!', font=('times', 50)), push()],
        [push(), Psg.Text('Somente números, por favor!', font=('times', 20)), push()],
        [push(), Psg.Button('VOLTAR', font=('times', 25), button_color='Gray'), push()]
    ]
    return Psg.Window('CALCULADORA IMC', layout, size=(600, 300), finalize=True)
# -------------------------------------------------------------------------------------------------------------------- #


erro = False  # Controla se os imputs do usuário possuem somente números.
# Criando as janelas
janelainicio, janelaerro = janela_inicio(), None

while True:
    janela_em_uso, evento, valor = Psg.read_all_windows()
    if evento == Psg.WIN_CLOSED:
        break
    if evento == 'CALCULAR':
        try:
            int(valor['peso'])
        except ValueError:
            janelainicio.close()
            janelaerro = janela_erro_valor_incorreto()
            erro = True
    if evento == 'CALCULAR' and (valor['peso'] == '' or valor['altura'] == ''):
        janelainicio.close()
        janelaerro = janela_erro_campos_vazios()
    elif evento == 'CALCULAR' and erro is False:  # só será executado, caso, não haja letras no input do usuário.
        Psg.popup(calcula_imc(float(valor['peso']), float(valor['altura'])), font=('times', 30))
    if evento == 'VOLTAR':
        janelaerro.hide()
        janelainicio = janela_inicio()

