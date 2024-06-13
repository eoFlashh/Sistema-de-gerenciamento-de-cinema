import customtkinter as tk
import random


def alllines(file1: str):
    archive = open(file1, 'r')
    lines = archive.readlines()
    archive.close()
    return lines


def writelines(file1: str, line: int, text):
    if isinstance(file1, str) and isinstance(line, int):
        archive = open(file1, 'r')
        lines = archive.readlines()
        lines[line] = str(text) + '\n'
        archive = open(file1, 'w')
        archive.writelines(lines)
        archive.close()
        alllines(file1)
        return lines
    else:
        return 'Parâmetros inválidos'


def on_slider_change(value, label):
    label.configure(text=f"Número de cadeiras: {int(value)}")


def validation(entry: str):
    if len(entry) >= 3:
        return True
    else:
        return False


def show_frame(frame):
    frame.tkraise()


def show_frameadmin(frame):
    global accountmode
    if accountmode == 1:
        frame.tkraise()
    else:
        print('Sem acesso')


def show_frameuser(frame):
    global accountmode
    if accountmode == 0:
        frame.tkraise()
    else:
        print('Sem acesso')


def leave_textbox(frame, box):
    frame.tkraise()
    box.configure(state=tk.NORMAL)
    box.delete("1.0", tk.END)
    box.configure(state=tk.DISABLED)


def auth(userinputbutton, passwordinputbutton, usersdict: dict, statslabel):
    global accountmode, account_logged
    userinput = userinputbutton.get()
    passwordinput = passwordinputbutton.get()
    if validation(userinput) and validation(passwordinput):
        if userinput in usersdict:
            if usersdict[userinput][0] == passwordinput:
                print(usersdict)
                print(userinput)
                print(passwordinput)
                statslabel.configure(text="Logado com sucesso")
                accountmode = usersdict[userinput][1]
                account_logged = userinput
                print(accountmode)
                print(account_logged)
            else:
                statslabel.configure(text="Senha inválida.")
        else:
            statslabel.configure(text="Usuário inexistente.")


def register(userinputbutton, passwordinputbutton, admincheckbox, statslabel, accounts):
    global file
    username = userinputbutton.get()
    user_password = passwordinputbutton.get()
    choose_mode = admincheckbox.get()
    if validation(username) and validation(user_password):
        if username in accounts:
            statslabel.configure(text="Usuário já existente!")
        else:
            accounts[username] = [user_password, choose_mode]
            statslabel.configure(text="Conta criada com sucesso!")
            writelines('ProjetoCine.txt', 0, accounts)
            file = alllines('ProjetoCine.txt')
            print(file[0])
            print(accounts)


def ticketverify(list1: list, item: str):
    boovar = False
    for x in range(len(list1)):
        if list1[x][0] == item:
            boovar = True
    return boovar


def buyticket(entry, box, ticketlist, filmslist):
    global file
    buy = entry.get()
    buyboo = False
    box.configure(state=tk.NORMAL)
    box.delete("1.0", tk.END)
    box.configure(state=tk.DISABLED)
    userticket = str(random.randint(100000, 999999))
    while ticketverify(ticketlist, userticket):
        userticket = str(random.randint(100000, 999999))

    for x in range(len(filmslist)):
        if filmslist[x][0] == buy:
            if int(filmslist[x][4]) > 0:
                buyboo = True
                filmslist[x][4] = str(int(filmslist[x][4]) - 1)

                box.configure(state=tk.NORMAL)
                box.insert(tk.END, "Informações do filme:\n\nHorário: " + filmslist[x][1] + "\nSala: " + filmslist[x][
                    2] + f"\nCadeiras restantes: {filmslist[x][4]}" + "\nPreço à ser pago: " + filmslist[x][3] +
                           "\n\nSeu ticket: " + f"#{userticket}#")
                box.configure(state=tk.DISABLED)

                ticketlist.append([userticket, account_logged, buy])
                writelines("ProjetoCine.txt", 2, ticketlist)
                writelines("ProjetoCine.txt", 1, filmslist)

                file = alllines("ProjetoCine.txt")
                print(file[2])
            else:
                buyboo = True
                box.configure(state=tk.NORMAL)
                box.insert(tk.END, "Não há ingressos disponíveis para este filme.")
                box.configure(state=tk.DISABLED)
            break
    if buyboo is False:
        box.configure(state=tk.NORMAL)
        box.insert(tk.END, "Não encontramos o filme que você quer comprar.")
        box.configure(state=tk.DISABLED)


def searchfilms(entry, box, filmslist):
    search = entry.get()
    box.configure(state=tk.NORMAL)
    box.delete("1.0", tk.END)
    box.configure(state=tk.DISABLED)
    searchboo = False
    for x in filmslist:
        if x[0].count(search) > 0:
            searchboo = True
            box.configure(state=tk.NORMAL)
            box.insert(tk.END, "Filme: " + x[0] + "\nHorário: " + x[1] + "\nSala: " + x[2] + f"\nCadeiras restantes: "
                                                                                             f"{x[4]}"
                       + "\nPreço do ingresso: " + x[3] + "\n\n")
            box.configure(state=tk.DISABLED)
    if searchboo is False:
        box.configure(state=tk.NORMAL)
        box.insert(tk.END, "Nenhum filme encontrado.")
        box.configure(state=tk.DISABLED)


def userlistticket(box, ticketlist):
    global account_logged
    print(ticketlist)
    searchboo = False
    box.configure(state=tk.NORMAL)
    box.delete("1.0", tk.END)
    box.configure(state=tk.DISABLED)
    for x in ticketlist:
        if x[1] == account_logged:
            searchboo = True
            box.configure(state=tk.NORMAL)
            box.insert(tk.END, f"Ingresso: #{x[0]}# \n Filme: {x[2]}\n\n")
            box.configure(state=tk.DISABLED)
    if searchboo is False:
        box.configure(state=tk.NORMAL)
        box.insert(tk.END, "Nenhum ingresso encontrado.")
        box.configure(state=tk.DISABLED)


def createfilm(nameentry, hourentry, roomentry, priceentry, slotsentry, filmslist, stats):
    global file
    name = nameentry.get()
    hour = hourentry.get()
    room = roomentry.get()
    price = priceentry.get()
    slots = str(int(slotsentry.get()))
    filmeboo = True
    if len(filmslist) > 0:
        for x in range(len(filmslist)):
            if name == filmslist[x][0]:
                filmeboo = False
                print('Esse filme já existe.')
                stats.configure(text="Esse filme já existe.")
                break
            elif hour == filmslist[x][1] and room == filmslist[x][2]:
                filmeboo = False
                print('Essa sala estará ocupada.')
                stats.configure(text="Essa sala estará ocupada.")
                break
        if filmeboo is True:
            print('filme criado')
            filmslist.append([name, hour, room, price, slots])
            print(filmslist)
            stats.configure(text="Filme criado com sucesso!")

            writelines("ProjetoCine.txt", 1, filmslist)
            file = alllines("ProjetoCine.txt")
            print(file[1])
    else:
        filmslist.append([name, hour, room, price, slots])
        print(filmslist)
        print('lista vazia')
        stats.configure(text="Filme criado com sucesso!")

        writelines("ProjetoCine.txt", 1, filmslist)
        file = alllines("ProjetoCine.txt")
        print(file[1])


def admsearch(entry, box, filmslist):
    if entry:
        search = entry.get()
    else:
        search = ""
    box.configure(state=tk.NORMAL)
    box.delete("1.0", tk.END)
    box.configure(state=tk.DISABLED)
    searchboo = False
    for x in filmslist:
        if x[0].count(search) > 0:
            searchboo = True
            box.configure(state=tk.NORMAL)
            box.insert(tk.END, f"Filme: " + x[0] + "\nHorário: " + x[1] + "\nSala: " + x[2] + "\nPreço do ingresso: " +
                       x[3] + "\n\n")
            box.configure(state=tk.DISABLED)
    if searchboo is False:
        box.configure(state=tk.NORMAL)
        box.insert(tk.END, "Nenhum filme encontrado.")
        box.configure(state=tk.DISABLED)


def modifyedfilm(entryname, enewname, enewhour, enewroom, enewprice, enewslots, filmslist, stats):
    global file
    modifyfilm = entryname.get()
    newname = enewname.get()
    newhour = enewhour.get()
    newroom = enewroom.get()
    newprice = enewprice.get()
    newslots = str(int(enewslots.get()))
    for x in filmslist:
        print(x)
        if x[0] == modifyfilm:
            x[0] = newname
            x[1] = newhour
            x[2] = newroom
            x[3] = newprice
            x[4] = newslots
            stats.configure(text="Filme modificado com sucesso!")
            writelines("ProjetoCine.txt", 1, filmslist)
            file = alllines("ProjetoCine.txt")
            break
        else:
            stats.configure(text="Nenhum filme encontrado com esse nome.")


def deletefilm(entry, stats, filmlist):
    global file
    name = entry.get()
    for x in range(len(filmlist)):
        if filmlist[x][0] == name:
            del filmlist[x]
            stats.configure(text="Filme deletado com sucesso!")
            writelines("ProjetoCine.txt", 1, filmlist)
            file = alllines("ProjetoCine.txt")
            print(file[1])
            break
        else:
            stats.configure(text="Nenhum filme encontrado com esse nome.")


def listtickets(entry, box, ticketlist):
    searchboo = False
    box.configure(state=tk.NORMAL)
    box.delete("1.0", tk.END)
    box.configure(state=tk.DISABLED)
    if entry:
        name = entry.get()
        for x in ticketlist:
            if name == x[2]:
                searchboo = True
                box.configure(state=tk.NORMAL)
                box.insert(tk.END, f"Ingresso: #{x[0]}#\n Cliente: {x[1]}\n Filme: {x[2]}\n\n")
                box.configure(state=tk.DISABLED)
    else:
        for x in ticketlist:
            searchboo = True
            box.configure(state=tk.NORMAL)
            box.insert(tk.END, f"Ingresso: #{x[0]}#\n Cliente: {x[1]}\n Filme: {x[2]}\n\n")
            box.configure(state=tk.DISABLED)
    if searchboo is False:
        box.configure(state=tk.NORMAL)
        box.insert(tk.END, "Nenhum ingresso encontrado.")
        box.configure(state=tk.DISABLED)