#-*- coding:UTF-8 -*-

"""
Programa Criado Por  Dhelbegor Vredesbyrd e Lario dos Santos Diniz 
"""

from ttk import *
from Tkinter import *
import tkMessageBox
import tkFileDialog,os
import ttk


def center(win):
    #funçao para centralizar
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width 
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

class compiler:
    def __init__(self,janela):
        self.filename=''
        self.janela = janela
        self.janela.resizable(width=False, height=False)
        self.janela.title('Cx Compilar')

        font1=('Copperplate Gothic Bold', '53')
        font2 = ('Arial','14')
        font3 = ('Arial','12')

        #==========================Frames==============================#
        base=LabelFrame(self.janela, bg='Blue')
        base.grid()
        caixa=LabelFrame(base)
        caixa.grid(row=1, column=1, padx=5, pady=5)
        caixa2=LabelFrame(base)
        caixa2.grid(row=2, column=1, sticky=N+W, padx=5, pady=5)
        caixa3=LabelFrame(base)
        caixa3.grid(row=2, column=1, sticky=N+E, padx=5, pady=5)
        #=========================Widigets=============================#
        #Logo
        Label(caixa, text='CX COMPILAR', font=font1).grid()
        #arquivo fonte
        Label(caixa2, text='Arquivo.py:', font=font2).grid(row=1, sticky=E)
        self.AR_entrada=Entry(caixa2, font=font2, borderwidth=3, relief=GROOVE, state=DISABLED)
        self.AR_entrada.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        
        #Descriçao
        Label(caixa2, text='Descrição:', font=font2).grid(row=5, sticky=E)
        self.D_entrada=Entry(caixa2, font=font2, borderwidth=3, relief=GROOVE)
        self.D_entrada.grid(row=5, column=1, padx=5, pady=5, sticky=W)
        
        #Nome
        Label(caixa2, text='Nome:', font=font2).grid(row=6, sticky=E)
        self.N_entrada=Entry(caixa2, font=font2, borderwidth=3, relief=GROOVE)
        self.N_entrada.grid(row=6, column=1, padx=5, pady=5, sticky=W)
        
        #Verçao
        Label(caixa2, text='Versão:', font=font2).grid(row=7, sticky=E)
        self.V_entrada=Entry(caixa2, font=font2, width=9, borderwidth=3, relief=GROOVE)
        self.V_entrada.grid(row=7, column=1, padx=5, pady=5, sticky=W)
        
        #executaveis
        Label(caixa2, text='Executavel:', font=font2).grid(row=8, sticky=E)
        
        executaveis = ['Win32GUI','']
        self.EX=ttk.Combobox(caixa2, font=font2, width=9)
        self.EX["values"] = executaveis
        self.EX.current(0)
        self.EX.bind("<<ComboboxSelected>>")
        self.EX.grid(row=8 , column=1,padx=4, pady=4, sticky=W)
        
        #botoes procurar..
        Button(caixa2,text='Procurar',width=8, borderwidth=3,
               font=font3,command=self.proc_arpy).grid(row=1,column=2, padx=5, pady=5)
       
        #Botoes
        self.botao_com=Button(caixa3,text='Compilar',width=8, borderwidth=3, font=font2, command=self.Compilar)
        self.botao_com.grid(row=1, padx=5, pady=5)
        self.botao_Pro=Button(caixa3,text='Ajuda',width=8, borderwidth=3, font=font2, command=self.ajuda)
        self.botao_Pro.grid(row=2, padx=5, pady=5)
        
    def Compilar(self):
        result = tkMessageBox.askquestion("Compilar", "Você tem certeza que quer compilar?\ntudo que estiver na pasta build sera substituido.", icon='question')
        if result == 'yes':   
            if self.filename == '':
                tkMessageBox.showerror("Erro de Preenchimento", "Selecione o codigo a ser compilado")
            elif self.D_entrada.get() == '':
                tkMessageBox.showerror("Erro de Preenchimento", "Forneça uma descrição")
            elif self.N_entrada.get() == '':
                tkMessageBox.showerror("Erro de Preenchimento", "Forneça um Nome")
            elif self.V_entrada.get() == '':
                tkMessageBox.showerror("Erro de Preenchimento", "Forneça uma versão (ponto Flutuante)")
            else:
                try:
                    float(self.V_entrada.get())
                    escrever="""from cx_Freeze import setup, Executable
        
setup(
    name = "%s",
    version = "%s",
    descriptiom = "%s",
    executables = [Executable("%s", base = "%s")])
                            """ %(self.N_entrada.get(),self.V_entrada.get(),self.D_entrada.get(),self.filename, self.EX.get())
                    abertura=open('setup.py','w')
                    abertura.write(escrever)
                    abertura.close()
                    os.system('rd build /s /q')
                    os.system('python setup.py build')
                    os.startfile('build')
                
                except ValueError:
                    tkMessageBox.showerror("Erro de Preenchimento", "Forneça uma versão (ponto Flutuante)")
        else:
            pass           
    def ajuda(self):
        a="""O Cx_Compilar é uma interface gráfica simples para empacotar programas utilizando o modulo cx_freeze.\n
Ela possui as opções mais simples para o empacotamento.
Para opções mais completas utilizar linha de códigos e ver a documentação do cx_freeze.
Você precisa ter o modulo cx_freeze instalado no seu computador.\n
Tutorial:
1 – Aperte em “Procurar” e encontre o código python que você quer empacotar.
2 – Preencha o campo descrição.
3 – Preencha o campo nome.
4 – Preencha o campo versão.
6 – Pressione o botão compilar. Uma janela perguntando se você tem certeza irá aparecer, confirme caso esteja tudo certo.
7 – Uma janela se abrirá mostrando a pasta do executável criada.

Autores:
Dhelbegor Vredesbyrd: dhelbegor@gmail.com
Lario Diniz: lariodiniz@gmail.com
"""
        tkMessageBox.showinfo("Ajuda", a)

    def proc_arpy(self):
        jan=Tk()
        jan.withdraw()    
        self.filename = tkFileDialog.askopenfilename(parent=jan,title='Adicionar.')
        try:
            self.AR_entrada['state']=NORMAL
            self.AR_entrada.delete(0, END)
            self.AR_entrada.insert(0, str(self.filename.split('/')[-1]))
            self.AR_entrada['state']=DISABLED
            self.AR_entrada['state']='readonly'

        except IOError:
                pass


raiz=Tk()
compiler(raiz)
center(raiz)
raiz.mainloop()
