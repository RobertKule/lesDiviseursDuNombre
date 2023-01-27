from tkinter import*
#la méthode go
def go():
	texte=entre.get()
	if texte:
		i=1
		try:
			nbre=int(texte)
		except :
			entre['bg']='red'
		else:
			entre["fg"]="green"
			lresu["fg"]="green"
			lresu["text"]="Les diviseurs du nombre {} sont : \n".format(nbre)
			for i in range(1,nbre+1):
				if not nbre%i:
					lresu["text"]=lresu["text"]+"\n"+str(i)
	else:
		lresu["fg"]="red"
		lresu["text"]="!!! Tapez d'abord une valeur svp\nCar la valeur tapée est vide"
#la fonction de la couleur
def  CouleurBleue():#verte
        fen["bg"]="blue"
        l["bg"]="blue"
        lab["bg"]="blue"
        lresu["bg"]="blue"
def  CouleurBlanche():#blanche
        fen["bg"]="white"
        l["bg"]="white"
        lab["bg"]="white"
        lresu["bg"]="white"
def  CouleurGrise():#grise
        fen["bg"]="gray"
        l["bg"]="gray"
        lab["bg"]="gray"
        lresu["bg"]="gray"
        
def  CouleurJaune():#Jaune
        fen["bg"]="yellow"
        l["bg"]="yellow"
        lab["bg"]="yellow"
        lresu["bg"]="yellow"
def maPhoto():
        lb=Label(text="Ecce omo",image=PhotoImage(file="kla.png"))
        lb.pack(side=BOTTOM)
#ma fenetre principale
fen=Tk()#ma fenetre
fen["bg"]="white"
#le cadre du programme
cad=Frame(fen,bg="white",height="20",width="200")
#le label d'introduction'
l=Label(fen,text="Welcome in this application\n",bg=fen["bg"],fg="cyan",font=("Arial",14,"bold"))
lab=Label(cad,font=("Arial",14,"bold"),text="Entrez un nombre : ")
#la variable de entry
entre=Entry(cad,font=("Arial",14,"bold"),bg="cyan",fg="white")
#le bouton de l'execution'
executer=Button(fen,bg="green",width="10",font=("Arial",14,"bold"), text="Execute",command=go)
#le résultant
lresu=Label(fen,bg="white", text="",font=("Arial",12,"bold"))
#Mon menu
meni=Menu(fen, bg="cyan")
#le menu de la couleur
couleur=Menu(meni,tearoff=0)
couleur.add_command(label="Blanche",command=CouleurBlanche)#couleur verte
couleur.add_command(label="Bleue",command=CouleurBleue)#couleur bleue
couleur.add_command(label="Grise",command=CouleurGrise)#couleur verte
couleur.add_command(label="Jaune",command=CouleurJaune)#couleur verte

meni.add_cascade(label="Couleur",menu=couleur)
meni.add_command(label='Developped by Robert KULE',command=maPhoto)
fen.config(menu=meni)


#on ajoute nos widgets
l.pack()#label intro
cad.pack(side=TOP)#ajout qu cadre
lab.pack(side=LEFT,fill=X)
entre.pack(side=RIGHT)
fen.resizable(width=False,height=True)
executer.pack(side=TOP)
lresu.pack()

fen.mainloop()
