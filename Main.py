from tkinter import *
import os.path
from functools import partial


class App:
    def __init__(self):
        self.ch0 = IntVar()
        self.ch1 = IntVar()
        self.ch2 = IntVar()
        self.ch3 = IntVar()
        self.ch4 = IntVar()
        self.ch5 = IntVar()
        self.ch6 = IntVar()
        self.t = 0
        self.amigos = inicio()
        for v in self.amigos:
            self.t += 1
        root.geometry(f'450x{50 + self.t * 100}')
        self.fonte = ("Arial", "29", "bold")
        self.fonte_a = ("Arial", "18")

        self.botao_add = Button(width=7, heigh=1, font=('Arial', '12'), text='Add.')
        self.botao_add['command'] = criar_add
        self.botao_add.place(x=360, y=10)

        self.botao_rem = Button(width=7, heigh=1, font=('Arial', '12'), text='Remover')
        self.botao_rem['command'] = self.colocar_b_rem
        self.botao_rem.place(x=250, y=10)

        self.can_rem = Button(width=7, heigh=1, font=('Arial', '12'), text='Cancelar')
        self.can_rem['command'] = App

        self.con_rem = Button(width=7, heigh=1, font=('Arial', '12'), text='Confirmar')
        self.con_rem['command'] = self.rem

        if self.t > 0:
            self.canva_amigo_0 = Canvas(width=450, heigh=100, bg='gray', highlightthickness=1,
                                        highlightbackground="black")
            self.canva_amigo_0.place(x=-2, y=50)
            self.label_amigo_0 = Label(width=2, heigh=2, font=self.fonte, background='white', fg='black')
            self.label_amigo_0['text'] = '1'
            self.label_amigo_0.place(x=-2, y=53)
            self.nome_amigo_0 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
            self.nome_amigo_0['text'] = self.amigos[0][0]
            self.nome_amigo_0.place(x=170, y=60)
            self.idade_amigo_0 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
            self.idade_amigo_0['text'] = f'{self.amigos[0][1]} anos'
            self.idade_amigo_0.place(x=55, y=115)
            self.num_amigo_0 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
            self.num_amigo_0['text'] = self.amigos[0][2]
            self.num_amigo_0.place(x=270, y=115)

            if self.t > 1:
                self.canva_amigo_1 = Canvas(width=450, heigh=100, bg='gray', bd=0, highlightthickness=1,
                                            highlightbackground="black")
                self.canva_amigo_1.place(x=-2, y=150)
                self.label_amigo_1 = Label(width=2, heigh=2, font=self.fonte, background='white', fg='black')
                self.label_amigo_1['text'] = '2'
                self.label_amigo_1.place(x=-2, y=153)
                self.nome_amigo_1 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
                self.nome_amigo_1['text'] = self.amigos[1][0]
                self.nome_amigo_1.place(x=170, y=160)
                self.idade_amigo_1 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
                self.idade_amigo_1['text'] = f'{self.amigos[1][1]} anos'
                self.idade_amigo_1.place(x=55, y=215)
                self.num_amigo_1 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
                self.num_amigo_1['text'] = self.amigos[1][2]
                self.num_amigo_1.place(x=270, y=215)

                if self.t > 2:
                    self.canva_amigo_2 = Canvas(width=450, heigh=100, bg='gray', bd=0, highlightthickness=1,
                                                highlightbackground="black")
                    self.canva_amigo_2.place(x=-2, y=250)
                    self.label_amigo_2 = Label(width=2, heigh=2, font=self.fonte, background='white', fg='black')
                    self.label_amigo_2['text'] = '3'
                    self.label_amigo_2.place(x=-2, y=253)
                    self.nome_amigo_2 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
                    self.nome_amigo_2['text'] = self.amigos[2][0]
                    self.nome_amigo_2.place(x=170, y=260)
                    self.idade_amigo_2 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
                    self.idade_amigo_2['text'] = f'{self.amigos[2][1]} anos'
                    self.idade_amigo_2.place(x=55, y=315)
                    self.num_amigo_2 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
                    self.num_amigo_2['text'] = self.amigos[2][2]
                    self.num_amigo_2.place(x=270, y=315)

                    if self.t > 3:
                        self.canva_amigo_3 = Canvas(width=450, heigh=100, bg='gray', bd=0, highlightthickness=1,
                                                    highlightbackground="black")
                        self.canva_amigo_3.place(x=-2, y=350)
                        self.label_amigo_3 = Label(width=2, heigh=2, font=self.fonte, background='white', fg='black')
                        self.label_amigo_3['text'] = '4'
                        self.label_amigo_3.place(x=-2, y=352)
                        self.nome_amigo_3 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
                        self.nome_amigo_3['text'] = self.amigos[3][0]
                        self.nome_amigo_3.place(x=170, y=360)
                        self.idade_amigo_3 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
                        self.idade_amigo_3['text'] = f'{self.amigos[3][1]} anos'
                        self.idade_amigo_3.place(x=55, y=415)
                        self.num_amigo_3 = Label(width=10, heigh=1, font=self.fonte_a, background='gray', fg='black')
                        self.num_amigo_3['text'] = self.amigos[3][2]
                        self.num_amigo_3.place(x=270, y=415)

                        if self.t > 4:
                            self.canva_amigo_4 = Canvas(width=450, heigh=100, bg='gray', highlightthickness=1,
                                                        highlightbackground="black")
                            self.canva_amigo_4.place(x=-2, y=450)
                            self.label_amigo_4 = Label(width=2, heigh=2, font=self.fonte, bg='white', fg='black')
                            self.label_amigo_4['text'] = '5'
                            self.label_amigo_4.place(x=-2, y=453)
                            self.nome_amigo_4 = Label(width=10, heigh=1, font=self.fonte_a, bg='gray', fg='black')
                            self.nome_amigo_4['text'] = self.amigos[4][0]
                            self.nome_amigo_4.place(x=170, y=460)
                            self.idade_amigo_4 = Label(width=10, heigh=1, font=self.fonte_a, bg='gray', fg='black')
                            self.idade_amigo_4['text'] = f'{self.amigos[4][1]} anos'
                            self.idade_amigo_4.place(x=55, y=515)
                            self.num_amigo_4 = Label(width=10, heigh=1, font=self.fonte_a, bg='gray', fg='black')
                            self.num_amigo_4['text'] = self.amigos[4][2]
                            self.num_amigo_4.place(x=270, y=515)

                            if self.t > 5:
                                self.canva_amigo_5 = Canvas(width=450, heigh=100, bg='gray', highlightthickness=1,
                                                            highlightbackground="black")
                                self.canva_amigo_5.place(x=-2, y=550)
                                self.label_amigo_5 = Label(width=2, heigh=2, font=self.fonte, bg='white', fg='black')
                                self.label_amigo_5['text'] = '6'
                                self.label_amigo_5.place(x=-2, y=553)
                                self.nome_amigo_5 = Label(width=10, heigh=1, font=self.fonte_a, bg='gray', fg='black')
                                self.nome_amigo_5['text'] = self.amigos[5][0]
                                self.nome_amigo_5.place(x=170, y=560)
                                self.idade_amigo_5 = Label(width=10, heigh=1, font=self.fonte_a, bg='gray', fg='black')
                                self.idade_amigo_5['text'] = f'{self.amigos[5][1]} anos'
                                self.idade_amigo_5.place(x=55, y=615)
                                self.num_amigo_5 = Label(width=10, heigh=1, font=self.fonte_a, bg='gray', fg='black')
                                self.num_amigo_5['text'] = self.amigos[5][2]
                                self.num_amigo_5.place(x=270, y=615)

                                if self.t > 6:
                                    self.canva_amigo_6 = Canvas(width=450, heigh=100, bg='gray', bd=0,
                                                                highlightthickness=1, highlightbackground="black")
                                    self.canva_amigo_6.place(x=-2, y=650)
                                    self.label_amigo_6 = Label(width=2, heigh=2, font=self.fonte, bg='white',
                                                               fg='black')
                                    self.label_amigo_6['text'] = '7'
                                    self.label_amigo_6.place(x=-2, y=653)
                                    self.nome_amigo_6 = Label(width=10, heigh=1, font=self.fonte_a, bg='gray',
                                                              fg='black')
                                    self.nome_amigo_6['text'] = self.amigos[6][0]
                                    self.nome_amigo_6.place(x=170, y=660)
                                    self.idade_amigo_6 = Label(width=10, heigh=1, font=self.fonte_a, bg='gray',
                                                               fg='black')
                                    self.idade_amigo_6['text'] = f'{self.amigos[6][1]} anos'
                                    self.idade_amigo_6.place(x=55, y=715)
                                    self.num_amigo_6 = Label(width=10, heigh=1, font=self.fonte_a, bg='gray',
                                                             fg='black')
                                    self.num_amigo_6['text'] = self.amigos[6][2]
                                    self.num_amigo_6.place(x=270, y=715)

        self.rem_0 = Checkbutton(variable=self.ch0, onvalue=1, offvalue=0)
        self.rem_1 = Checkbutton(variable=self.ch1, onvalue=1, offvalue=0)
        self.rem_2 = Checkbutton(variable=self.ch2, onvalue=1, offvalue=0)
        self.rem_3 = Checkbutton(variable=self.ch3, onvalue=1, offvalue=0)
        self.rem_4 = Checkbutton(variable=self.ch4, onvalue=1, offvalue=0)
        self.rem_5 = Checkbutton(variable=self.ch5, onvalue=1, offvalue=0)
        self.rem_6 = Checkbutton(variable=self.ch6, onvalue=1, offvalue=0)

    def colocar_b_rem(self):

        self.botao_add.place_forget()
        self.botao_rem.place_forget()

        self.can_rem.place(x=250, y=10)
        self.con_rem.place(x=360, y=10)

        if self.t > 0:
            self.rem_0.place(x=420, y=52)

            if self.t > 1:
                self.rem_1.place(x=420, y=152)

                if self.t > 2:
                    self.rem_2.place(x=420, y=252)

                    if self.t > 3:
                        self.rem_3.place(x=420, y=352)

                        if self.t > 4:
                            self.rem_4.place(x=420, y=452)

                            if self.t > 5:
                                self.rem_5.place(x=420, y=552)

                                if self.t > 6:
                                    self.rem_6.place(x=420, y=652)

    def rem(self):
        filename = f'{os.path.abspath(os.path.dirname(__file__))}\list.txt'
        lista = [(0, self.ch0.get()), (1, self.ch1.get()), (2, self.ch2.get()), (3, self.ch3.get()),
                 (4, self.ch4.get()), (5, self.ch5.get()), (6, self.ch6.get())]
        v = 0

        for i in lista:
            if i[1] == 1:
                if self.t == 1:
                    file = open(filename, 'w')
                    file.writelines('')
                    file.close()

                else:
                    file = open(filename, 'r')
                    conteudo = file.readlines()
                    file.close()

                    conteudo = conteudo[:i[0]-v]+conteudo[i[0]+1-v:]
                    u1, u2, u3, u4 = conteudo[-1].split(',')
                    ult = f'{u1},{u2},{u3},'
                    conteudo.remove(conteudo[-1])
                    conteudo.append(ult)

                    file = open(filename, 'w')
                    file.writelines(conteudo)
                    file.close()
                    v = v + 1

        App()


def criar_add():
    newWindow = Toplevel(root)
    newWindow.title('Adicionar')
    newWindow.geometry('300x150')
    newWindow.resizable(False, False)

    fonte = ('Arial', 12)

    nome = Entry(newWindow, font=fonte)
    l_nome = Label(newWindow, font=fonte, text='Nome:')
    idade = Entry(newWindow, font=fonte)
    l_idade = Label(newWindow, font=fonte, text='Idade:')
    num = Entry(newWindow, font=fonte)
    l_num = Label(newWindow, font=fonte, text='Número:')

    botao_con = Button(newWindow, text='Adicionar', command=partial(add, nome, idade, num, newWindow))
    botao_can = Button(newWindow, text='Cancelar', command=newWindow.destroy)

    nome.place(x=80, y=22)
    l_nome.place(x=25, y=20)
    idade.place(x=80, y=52)
    l_idade.place(x=25, y=50)
    num.place(x=80, y=82)
    l_num.place(x=15, y=80)

    botao_con.place(x=150, y=120)
    botao_can.place(x=90, y=120)


def add(nome_, idade_, num_, n):
    nome = nome_.get()
    idade = idade_.get()
    num = num_.get()

    filename = f'{os.path.abspath(os.path.dirname(__file__))}\list.txt'

    file = open(filename, 'r')
    conteudo = file.readlines()
    file.close()

    if not conteudo:
        conteudo.append(f'{nome},{idade},{num},')
    else:
        conteudo.append("\n" + f'{nome},{idade},{num},')

    file = open(filename, 'w')
    file.writelines(conteudo)
    file.close()

    App()
    n.destroy()


def inicio():
    filename = f'{os.path.abspath(os.path.dirname(__file__))}\list.txt'
    filecontent = list()
    file = open(filename, "r")

    for fileline in file:
        filecontent.append(fileline.split(","))

    file.close()
    return filecontent


root = Tk()
root.config(bg="coral4")
root.title('Friends')
root.resizable(False, False)
App()
root.mainloop()
