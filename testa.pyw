import time
import os
import time
import datetime, random
from tkinter import ttk
from tkinter import *


def atendimento():
    lista= enderc.get()
    nomeuser= nome1.get()
    numero= nume1.get()
    chamado= cham1.get()
    textogr= text1.get("1.0",'end-1c')
    #print(lista)
    #print(nomeuser)
    #print(numero)
    #print(chamado)
    #print(textogr)
    mensagem = '\n'
    if lista == 'LIGACAO':
        textf.insert(END, 'Efetuando tentativa de contato para o(s) número(s): %s' %(numero))

    if lista == 'PAUSA USER':
        textf.insert(END, '''Prezado(a) Sr.(a) %s,

Informamos que foi realizada tentativa de contato telefônico para o número (88)99711-2949 com objetivo de dar prosseguimento ao tratamento do seu chamado, porém não obtivemos sucesso.

Para agilizar seu atendimento ou caso o chamado já tenha sido atendido, por favor entrar em contato conosco através do telefone (85) 3366.2966 ou do portal CATINET https://cati.tjce.jus.br/assystnet/''' %(nomeuser))

    if lista == 'INICIAR ATENDIMENTO':
         textf.insert(END, 'Pendência sanada após informações recebida do(a) senhor(a) %s, atendimento retomado. ' %(nomeuser))

    if lista == 'FINALIZAR':
        textf.insert(END, '''Prezado Sr.(a). %s, informo que sua solicitação está sendo encerrada pelo motivo descrito abaixo:

( ) solicitação não faz parte do escopo de atendimento da CATI;
(x) solucionado sem intervenção da CATI; %s
( ) encerrando para correção de categoria e registrando um novo chamado de nº: ______
( ) Outros. Descrever:

Canais de Atendimento:
Tel. (85) 3366.2966, CATINET ( https://cati.tjce.jus.br/assystnet/)''' %(nomeuser, textogr))
    if lista == 'RESOLVIDO':
        textf.insert(END, '''Acompanhado do(a) usuário(a) %s, foi realizado o procedimento abaixo:

Descrever ação tomada: Feito a Instalação %s, procedimento realizado com sucesso.

Testado pelo usuário?
(x) Sim
( ) Não. Conclusão da solicitação pendente de testes do usuário. ''' %(nomeuser, textogr))
    if lista == 'INF RCBUSER':
        textf.insert(END, 'Pendência sanada após informações recebida do(a) senhor(a) %s, atendimento retomado. ' %(nomeuser))
    else:
        print('')



    #textf.insert(END, mensagem)
    
    


root = Tk()
root.title('CATI WEB')
root.geometry('700x480')
#root.configure(background='#71a6ff')


#######################################################
label2 = Label(root ,text = "PROCEDIMENTO")
label2.pack()
listEndrc=["LIGACAO","PAUSA USER","INICIAR ATENDIMENTO", "RESOLVIDO", "FINALIZAR", "INF RCBUSER"]
enderc=ttk.Combobox(root,values=listEndrc)
enderc.set("")
enderc.pack()

nome1 = Label(root,text = "Nome").pack()
nome1 = Entry(root)
nome1.pack()

label1 = Label(root,text = "Número").pack()
nume1 = Entry(root)
nume1.pack()

label1 = Label(root,text = "Chamado").pack()
cham1 = Entry(root)
cham1.pack()

label3 = Label(root,text = "Texto").pack()
text1 = Text(root,height=5, width=20)
text1.pack()

textf = Text(root,height=8, width=100, font=(("Arial"),10), foreground="blue")
textf.pack()

buton = Button(root, text="Iniciar", command= atendimento)
buton.pack()


root.mainloop()

