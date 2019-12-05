#import bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import bdSist

#Criar Nossa Janela
janela = Tk()
janela.title("PySistLogin ")
janela.geometry("600x300")
janela.configure(background = "white")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9)
janela.iconbitmap(default="imagens/LogoIcon.ico")

#Logo
logo = PhotoImage(file = "imagens/6f4724ed14bf65cfc214d287aae55e99a.png")

#Width
LeftFrame = Frame(janela, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

logoLabel = Label(LeftFrame, image = logo, bg= "MIDNIGHTBLUE")
logoLabel.place(x = 50, y = 100)

UserLabel = Label(RightFrame, text = "User", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg = "white")
UserLabel.place(x = 5, y = 5)
userEntry = ttk.Entry(RightFrame,width=30)
userEntry.place(x = 150, y = 15)

passLabel = Label(RightFrame, text = "Senha", font=("Century Gothic",20), bg ="MIDNIGHTBLUE",fg = "white")
passLabel.place(x = 5, y = 45)
passEntry = ttk.Entry(RightFrame, width = 30, show="*")
passEntry.place(x = 150, y = 55)

def login():

    User = userEntry.get()
    Pass = passEntry.get()

    bdSist.cur.execute("""
    SELECT * FROM Users 
    WHERE (User = ? AND Password = ?)
    """,(User,Pass))
    print("LOGADO")
    verificador = bdSist.cur.fetchone()

    try:
        if((User in verificador) and (Pass in verificador)):
            messagebox.showinfo(title ="Login Info", message = "Acesso Comfirmado. Bem Vindo!!!")
    except:
        messagebox.showinfo(title ="Login Info", message = "Acesso Negado.")

#Botões
LoginButton = ttk.Button(RightFrame, text = "Login", width = 10, command = login)
LoginButton.place(x = 150, y = 95)

def register():
    LoginButton.place(x = 5000)
    RegistButton.place(x = 5000)

    userNomeLabel = Label(RightFrame,text = "Nome", font=("Century Gothic",20), bg ="MIDNIGHTBLUE",fg = "white")
    userNomeLabel.place(x = 5, y = 85)
    userNomeEntry = Entry(RightFrame, width=30)
    userNomeEntry.place(x = 150, y = 95)

    emailLabel = Label(RightFrame,text = "Email", font=("Century Gothic",20), bg ="MIDNIGHTBLUE",fg = "white")
    emailLabel.place(x = 5, y = 125)
    emailEntry = Entry(RightFrame, width=30)
    emailEntry.place(x = 150, y = 135)

    def cadastarBd():

        Name = userNomeEntry.get()
        User = userEntry.get()
        Pass = passEntry.get()
        Email = emailEntry.get()

        if(Name == "" or User == "" or Pass == "" or Email == ""):
            messagebox.showerror(title="Erro!!!", message="Campos obrigatorios vazios.")
        else:
            bdSist.cur.execute("""
            INSERT INTO users(Name, Email, User, Password) VALUES(?,?,?,?)
            """, (Name, Email, User, Pass))
            bdSist.conn.commit()
            messagebox.showinfo(title="Acessando Informações de cadastro", 
            message="Cadastrado com Sucesso")
    
    Registar = ttk.Button(RightFrame, text="Registar", width = 10, command=cadastarBd)
    Registar.place(x = 150, y = 175)
    
    def backMenu():
        #Voltar para tela Login removendo os Wigets de cadastro
        userNomeLabel.place(x = 5000)
        userNomeEntry.place(x = 5000)
        emailLabel.place(x = 5000)
        emailEntry.place(x = 5000)
        Registar.place(x = 5000)
        Back.place(x = 5000)
        #trazendo de volta os botôes de Login
        LoginButton.place(x = 150)
        RegistButton.place(x = 265)

    Back = ttk.Button(RightFrame, text="Voltar", width = 10, command = backMenu)
    Back.place(x = 265, y = 175)

RegistButton = ttk.Button(RightFrame, text = "Registar", width = 10, command = register)
RegistButton.place(x = 265, y = 95)
janela.mainloop()