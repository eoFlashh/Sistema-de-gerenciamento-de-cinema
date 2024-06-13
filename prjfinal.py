import prjfun as fun
import customtkinter as tk

accountmode = 9
account_logged = None

file = fun.alllines('ProjetoCine.txt')

if file:
    accounts = dict(eval(file[0]))
    allfilms = list(eval(file[1]))
    tickets = list(eval(file[2]))
else:
    print('Arquivo de backup não contém nada salvo.')
    accounts = {}
    allfilms = []
    tickets = []


print(accounts)
print(allfilms)
print(tickets)
# Front
root = tk.CTk()
root.title("Cinema")
root.geometry("720x480")
tk.set_appearance_mode('dark')

container = tk.CTkFrame(root)
container.pack()

mainframe = tk.CTkFrame(container, fg_color='#242424')
authframe = tk.CTkFrame(container, fg_color='#242424')
registerframe = tk.CTkFrame(container, fg_color='#242424')
buyfilmframe = tk.CTkFrame(container, fg_color='#242424')
adminframe = tk.CTkFrame(container, fg_color='#242424')
regfilmframe = tk.CTkFrame(container, fg_color='#242424')
searchfilmframe = tk.CTkFrame(container, fg_color='#242424')
modifyfilmframe = tk.CTkFrame(container, fg_color='#242424')
deletefilmframe = tk.CTkFrame(container, fg_color='#242424')
listticketsframe = tk.CTkFrame(container, fg_color='#242424')

for frame in (mainframe, authframe, registerframe, adminframe, buyfilmframe, regfilmframe, searchfilmframe,
              modifyfilmframe, deletefilmframe, listticketsframe):
    frame.grid(row=0, column=0, sticky="nsew")

# Main-Menu
title = tk.CTkLabel(mainframe, text="Cinema", font=("Arial Black", 14))
title.pack(padx=10, pady=10)
buybutton = tk.CTkButton(mainframe, text="Comprar Ticket", fg_color="#DB3E39", hover_color="#821D1A",
                         command=lambda: fun.show_frameuser(buyfilmframe))
buybutton.pack(padx=5, pady=5)
adminbutton = tk.CTkButton(mainframe, text="Painel admin", fg_color="#DB3E39", hover_color="#821D1A",
                           command=lambda: fun.show_frameadmin(adminframe))
adminbutton.pack(padx=10, pady=10)
authbutton = tk.CTkButton(mainframe, text="Logar-se", fg_color="#DB3E39", hover_color="#821D1A",
                          command=lambda: fun.show_frame(authframe))
authbutton.pack(padx=5, pady=5)
registerbutton = tk.CTkButton(mainframe, text="Registre-se", fg_color="#DB3E39", hover_color="#821D1A",
                              command=lambda: fun.show_frame(registerframe))
registerbutton.pack(padx=10, pady=10)

# Auth
title = tk.CTkLabel(authframe, text="Autenticação", font=("Arial Black", 14))
title.pack(padx=10, pady=10)
user_aut = tk.CTkEntry(authframe, placeholder_text="Digite seu usuário")
user_aut.pack(padx=5, pady=5)
password_aut = tk.CTkEntry(authframe, placeholder_text="Digite sua senha")
password_aut.pack(padx=5, pady=5)
login = tk.CTkButton(authframe, text="Logar-se", fg_color="#DB3E39", hover_color="#821D1A",
                     command=lambda: fun.auth(user_aut, password_aut, accounts, auth_stats,))
login.pack(padx=10, pady=10)
back = tk.CTkButton(authframe, text="Voltar", fg_color="#DB3E39", hover_color="#821D1A",
                    command=lambda: fun.show_frame(mainframe))
back.pack(padx=5, pady=5)
auth_stats = tk.CTkLabel(authframe, text="")
auth_stats.pack(padx=5, pady=5)

# Register
title = tk.CTkLabel(registerframe, text="Registrar", font=("Arial Black", 14))
title.pack(padx=10, pady=10)
user_reg = tk.CTkEntry(registerframe, placeholder_text="Digite seu usuário")
user_reg.pack(padx=5, pady=5)
password_reg = tk.CTkEntry(registerframe, placeholder_text="Digite sua senha")
password_reg.pack(padx=5, pady=5)
admin = tk.CTkCheckBox(registerframe, text="Admin", fg_color="#DB3E39", hover_color="#821D1A")
admin.pack(padx=5, pady=5)
regbutton = tk.CTkButton(registerframe, text="Registrar-se", fg_color="#DB3E39", hover_color="#821D1A",
                         command=lambda: fun.register(user_reg, password_reg, admin, register_stats, accounts))
regbutton.pack(padx=10, pady=10)
backbutton = tk.CTkButton(registerframe, text="Voltar", fg_color="#DB3E39", hover_color="#821D1A",
                          command=lambda: fun.show_frame(mainframe))
backbutton.pack(padx=5, pady=5)
register_stats = tk.CTkLabel(registerframe, text="")
register_stats.pack(padx=5, pady=5)

# Buy-Film
title = tk.CTkLabel(buyfilmframe, text="Comprar ingresso", font=("Arial Black", 14))
title.pack(padx=10, pady=10)
choosefilm = tk.CTkEntry(buyfilmframe, placeholder_text="Filtrar por filme")
choosefilm.pack(padx=5, pady=5)
textbuybox = tk.CTkTextbox(buyfilmframe, height=225, width=500, state=tk.DISABLED)
textbuybox.pack(padx=10, pady=10)
buybutton = tk.CTkButton(buyfilmframe, text="Comprar", fg_color="#DB3E39", hover_color="#821D1A",
                         command=lambda: fun.buyticket(choosefilm, textbuybox, tickets, allfilms))
buybutton.pack(padx=5, pady=5)
searchbuy = tk.CTkButton(buyfilmframe, text="Procurar filme", fg_color="#DB3E39", hover_color="#821D1A",
                         command=lambda: fun.searchfilms(choosefilm, textbuybox, allfilms))
searchbuy.pack(padx=10, pady=10)
usertickets = tk.CTkButton(buyfilmframe, text="Listar ingressos", fg_color="#DB3E39", hover_color="#821D1A",
                           command=lambda: fun.userlistticket(textbuybox, tickets))
usertickets.pack(padx=5, pady=5)
leaveclient = tk.CTkButton(buyfilmframe, text="Sair", fg_color="#DB3E39", hover_color="#821D1A",
                           command=lambda: fun.leave_textbox(mainframe, textbuybox))
leaveclient.pack(padx=10, pady=10)

# Admin-Panel
title = tk.CTkLabel(adminframe, text="Painel ADMIN", font=("Arial Black", 14))
title.pack(padx=10, pady=10)
registerfilm = tk.CTkButton(adminframe, text="Cadastrar filme", command=lambda: fun.show_frame(regfilmframe))
registerfilm.pack(padx=10, pady=10)
searchfilm = tk.CTkButton(adminframe, text="Buscar filmes", command=lambda: fun.show_frame(searchfilmframe))
searchfilm.pack(padx=5, pady=5)
modifyfilm = tk.CTkButton(adminframe, text="Modificar filme",
                          command=lambda: fun.show_frame(modifyfilmframe))
modifyfilm.pack(padx=10, pady=10)
deletefilm = tk.CTkButton(adminframe, text="Deletar filme",
                          command=lambda: fun.show_frame(deletefilmframe))
deletefilm.pack(padx=5, pady=5)
listtickets = tk.CTkButton(adminframe, text="Listar ingressos",
                           command=lambda: fun.show_frame(listticketsframe))
listtickets.pack(padx=10, pady=10)
leaveadm = tk.CTkButton(adminframe, text="Sair", fg_color="#DB3E39", hover_color="#821D1A",
                        command=lambda: fun.show_frame(mainframe))
leaveadm.pack(padx=5, pady=5)

# Register-Films
title = tk.CTkLabel(regfilmframe, text="Cadastrar filme", font=("Arial Black", 14))
title.pack(padx=10, pady=10)
filmname = tk.CTkEntry(regfilmframe, placeholder_text="Digite o nome do filme")
filmname.pack(padx=5, pady=5)
filmhour = tk.CTkEntry(regfilmframe, placeholder_text="Digite o horário")
filmhour.pack(padx=5, pady=5)
filmroom = tk.CTkEntry(regfilmframe, placeholder_text="Digite a sala")
filmroom.pack(padx=5, pady=5)
filmprice = tk.CTkEntry(regfilmframe, placeholder_text="Digite o valor")
filmprice.pack(padx=5, pady=5)
number_label = tk.CTkLabel(regfilmframe, text="Número de cadeiras: 1")
number_label.pack(pady=0)
slider = tk.CTkSlider(regfilmframe, from_=1, to=100, number_of_steps=99,
                      command=lambda value: fun.on_slider_change(value, number_label))
slider.pack(pady=5, padx=5)
slider.set(1)
confirmcreate = tk.CTkButton(regfilmframe, text="Confirmar",
                             command=lambda: fun.createfilm(filmname, filmhour, filmroom, filmprice, slider, allfilms,
                                                            created_stats))
confirmcreate.pack(padx=10, pady=10)
back = tk.CTkButton(regfilmframe, text="Voltar", fg_color="#DB3E39", hover_color="#821D1A",
                    command=lambda: fun.show_frameadmin(adminframe))
back.pack(padx=5, pady=5)
created_stats = tk.CTkLabel(regfilmframe, text="")
created_stats.pack(padx=5, pady=5)

# Search-Film
title = tk.CTkLabel(searchfilmframe, text="Lista de filmes:", font=("Arial Black", 14))
title.pack(padx=10, pady=10)
searchname = tk.CTkEntry(searchfilmframe, placeholder_text="Buscar por nome")
searchname.pack(padx=5, pady=5)
textbox = tk.CTkTextbox(searchfilmframe, height=225, width=500, state=tk.DISABLED)
textbox.pack(padx=5, pady=5)
searchbutton = tk.CTkButton(searchfilmframe, text="Buscar",
                            command=lambda: fun.admsearch(searchname, textbox, allfilms))
searchbutton.pack(padx=10, pady=10)
showall = tk.CTkButton(searchfilmframe, text="Mostrar todos",
                       command=lambda: fun.admsearch(None, textbox, allfilms))
showall.pack(padx=5, pady=5)
back = tk.CTkButton(searchfilmframe, text="Voltar", fg_color="#DB3E39", hover_color="#821D1A",
                    command=lambda: fun.show_frameadmin(adminframe))
back.pack(padx=10, pady=10)

# Modify-Film
title = tk.CTkLabel(modifyfilmframe, text="Modificar filme", font=("Arial Black", 14))
title.pack(padx=10, pady=10)
choosemodifyfilm = tk.CTkEntry(modifyfilmframe, placeholder_text="Nome atual do filme",
                               fg_color="#565B5E", border_color="#FFFFFF", text_color="#FFFFFF")
choosemodifyfilm.pack(padx=5, pady=5)
newfilmname = tk.CTkEntry(modifyfilmframe, placeholder_text="Novo nome")
newfilmname.pack(padx=10, pady=10)
newfilmhour = tk.CTkEntry(modifyfilmframe, placeholder_text="Novo horário")
newfilmhour.pack(padx=5, pady=5)
newfilmroom = tk.CTkEntry(modifyfilmframe, placeholder_text="Nova sala")
newfilmroom.pack(padx=10, pady=10)
newfilmprice = tk.CTkEntry(modifyfilmframe, placeholder_text="Novo preço")
newfilmprice.pack(padx=5, pady=5)
number_label2 = tk.CTkLabel(modifyfilmframe, text="Número de cadeiras: 1")
number_label2.pack(pady=0)
slider2 = tk.CTkSlider(modifyfilmframe, from_=1, to=100, number_of_steps=99,
                       command=lambda value: fun.on_slider_change(value, number_label2))
slider2.pack(pady=5, padx=5)
slider2.set(1)
confirmmodify = tk.CTkButton(modifyfilmframe, text="Confirmar", command=lambda: fun.modifyedfilm(choosemodifyfilm, newfilmname, newfilmhour, newfilmroom, newfilmprice, slider2, allfilms, modify_stats))
confirmmodify.pack(padx=10, pady=10)
back = tk.CTkButton(modifyfilmframe, text="Voltar", fg_color="#DB3E39", hover_color="#821D1A",
                    command=lambda: fun.show_frameadmin(adminframe))
back.pack(padx=5, pady=5)
modify_stats = tk.CTkLabel(modifyfilmframe, text="")
modify_stats.pack(padx=10, pady=10)

# Delete-Film
title = tk.CTkLabel(deletefilmframe, text="Deletar filme", font=("Arial Black", 14))
title.pack(padx=10, pady=10)
choosedeletefilm = tk.CTkEntry(deletefilmframe, placeholder_text="Nome do filme", fg_color="#565B5E",
                               border_color="#FFFFFF", text_color="#FFFFFF")
choosedeletefilm.pack(padx=5, pady=5)
confirmdelete = tk.CTkButton(deletefilmframe, text="Confirmar", command=lambda: fun.deletefilm(choosedeletefilm,
                                                                                               delete_stats, allfilms))
confirmdelete.pack(padx=10, pady=10)
back = tk.CTkButton(deletefilmframe, text="Voltar", fg_color="#DB3E39", hover_color="#821D1A",
                    command=lambda: fun.show_frameadmin(adminframe))
back.pack(padx=5, pady=5)
delete_stats = tk.CTkLabel(deletefilmframe, text="")
delete_stats.pack(padx=10, pady=10)

# List-Tickets
title = tk.CTkLabel(listticketsframe, text="Listar tickets", font=("Arial Black", 14))
title.pack(padx=10, pady=10)
ticketsname = tk.CTkEntry(listticketsframe, placeholder_text="Filtrar por filme")
ticketsname.pack(padx=5, pady=5)
ticketstextbox = tk.CTkTextbox(listticketsframe, height=225, width=500, state=tk.DISABLED)
ticketstextbox.pack(padx=5, pady=5)
searchbutton = tk.CTkButton(listticketsframe, text="Buscar",
                            command=lambda: fun.listtickets(ticketsname, ticketstextbox, tickets))
searchbutton.pack(padx=10, pady=10)
showalltickets = tk.CTkButton(listticketsframe, text="Mostrar todos",
                       command=lambda: fun.listtickets(None, ticketstextbox, tickets))
showalltickets.pack(padx=5, pady=5)
back = tk.CTkButton(listticketsframe, text="Voltar", fg_color="#DB3E39", hover_color="#821D1A",
                    command=lambda: fun.show_frameadmin(adminframe))
back.pack(padx=10, pady=10)

fun.show_frame(mainframe)
root.mainloop()
