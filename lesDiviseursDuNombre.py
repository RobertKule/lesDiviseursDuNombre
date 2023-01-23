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
	
#ma fenetre principale
fen=Tk()#ma fenetre
fen["bg"]="white"
#le cadre du programme
cad=Frame(fen,bg="white")
#le label d'introduction'
l=Label(fen,text="Welcome in this application\n",bg="white",fg="cyan",font=("Arial",14,"bold"))
lab=Label(cad,font=("Arial",14,"bold"),text="Entrez un nombre : ")
#la variable de entry
entre=Entry(cad,font=("Arial",14,"bold"),bg="cyan",fg="white")
#le bouton de l'execution'
executer=Button(fen,bg="green",font=("Arial",14,"bold"), text="Execute",command=go)
#le résultant
lresu=Label(fen,bg="white", text="",font=("Arial",12,"bold"))
#les fausses valeurs de diviseurs
#on ajoute nos widgets
l.pack()
cad.pack()#ajout qu cadre
lab.pack(side=LEFT)
entre.pack(side=RIGHT)
meni=Menu(fen,bg='cyan',fg='white',font=("Arial",14,"bold"))

meni.add_cascade(label='\tDevelopped by Robert KULE')
fen.config(menu=meni)
executer.pack(fill=X)
lresu.pack()

fen.mainloop()