from PyQt5 import uic, QtWidgets

regra = True

# Função para resetar tela após calculo ou erro de expressão

def validacao():
    if regra == False:
        tela.ln_dados.setText("")
    elif tela.ln_dados.text() == "Expressão mal formada!":
        tela.ln_dados.setText("")

###########################################################

# Fuções dos botões para concatenar dados do campo text com valores ou operações

def ponto():
    global regra
    validacao()
    memoria = (tela.ln_dados.text() + ",")
    tela.ln_dados.setText(memoria)    
    regra = True
    

def zero():
    global regra
    validacao()
    memoria = tela.ln_dados.text() + "0"
    tela.ln_dados.setText(memoria)    
    regra = True

def um():
    global regra
    validacao()
    memoria = tela.ln_dados.text() + "1"
    tela.ln_dados.setText(memoria)
    regra = True

def dois():
    global regra
    validacao()
    memoria = tela.ln_dados.text() + "2"
    tela.ln_dados.setText(memoria)
    regra = True

def tres():
    global regra
    validacao()
    memoria = tela.ln_dados.text() + "3"
    tela.ln_dados.setText(memoria)
    regra = True

def quatro():
    global regra
    validacao()
    memoria = tela.ln_dados.text() + "4"
    tela.ln_dados.setText(memoria)
    regra = True

def cinco():
    global regra
    validacao()
    memoria = tela.ln_dados.text() + "5"
    tela.ln_dados.setText(memoria)
    regra = True

def seis():
    global regra
    validacao()
    memoria = tela.ln_dados.text() + "6"
    tela.ln_dados.setText(memoria)
    regra = True

def sete():
    global regra
    validacao() 
    memoria = tela.ln_dados.text() + "7"
    tela.ln_dados.setText(memoria)
    regra = True

def oito():
    global regra
    validacao()
    memoria = tela.ln_dados.text() + "8"
    tela.ln_dados.setText(memoria)
    regra = True

def nove():
    global regra
    validacao()
    memoria = tela.ln_dados.text() + "9"
    tela.ln_dados.setText(memoria)
    regra = True

def subtracao():
    global regra
    memoria = tela.ln_dados.text() + "-"
    tela.ln_dados.setText(memoria)
    regra = True

def adicao():
    global regra     
    memoria = tela.ln_dados.text() + "+"
    tela.ln_dados.setText(memoria)
    regra = True

def multiplicacao():
    global regra     
    memoria = tela.ln_dados.text() + "*"
    tela.ln_dados.setText(memoria)
    regra = True

def multip():
    global regra     
    memoria = tela.ln_dados.text() + "*"
    tela.ln_dados.setText(memoria)
    regra = True

def divis():
    global regra    
    memoria = tela.ln_dados.text() + "/"
    tela.ln_dados.setText(memoria)
    regra = True

###########################################################

# Função que limpa campo text

def c_limpar():
    tela.ln_dados.setText("")

###########################################################   

# Função que valida e realiza o calculo

def calcular():
    try:
        global regra
        if tela.ln_dados.text() == "":
            tela.ln_dados.setText("0")        
            regra = False
        else: 
            expressao = tela.ln_dados.text().replace(",", "X").replace(".", "").replace("X", ".")
            resultado = eval(expressao)
            tela.ln_dados.setText(f'{resultado:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))        
            regra = False
    except:
        tela.ln_dados.setText("Expressão mal formada!")

###########################################################        


app = QtWidgets.QApplication([])
tela = uic.loadUi("calc.ui")

tela.bt_ponto.clicked.connect(ponto)
tela.bt_zero.clicked.connect(zero)
tela.bt_um.clicked.connect(um)
tela.bt_dois.clicked.connect(dois)
tela.bt_tres.clicked.connect(tres)
tela.bt_quatro.clicked.connect(quatro)
tela.bt_cinco.clicked.connect(cinco)
tela.bt_seis.clicked.connect(seis)
tela.bt_sete.clicked.connect(sete)
tela.bt_oito.clicked.connect(oito)
tela.bt_nove.clicked.connect(nove)
tela.bt_sub.clicked.connect(subtracao)
tela.bt_soma.clicked.connect(adicao)
tela.bt_mult.clicked.connect(multip)
tela.bt_div.clicked.connect(divis)
tela.bt_c.clicked.connect(c_limpar)
tela.bt_calcular.clicked.connect(calcular)

tela.show()
app.exec()