#Exercice:
#creer un dossier nommé TpRappelJanvier2024 contenant les fichiers python
#mesfonctions.py et application.py 
#le fichier mesfonctions.py contient les fonctions suivantes:
#-->Une fonction de saisie des informations d'un candidat
#-->Une fonction de creation d'un fichier de candidat qui utilise la fonction precedente
#-->Une fonction qui affiche le contenu du fichier de candidat
#-->Une fonction qui ajoute des candidats dans le fichier
#-->Une fonction qui transfert dans une liste les candidats du fichier puis affiche
#le nombre de candidat de la liste et les candidats dont le nombre de parrain est >=60000
#-->Une fonction pour le menu

#Le fichier application.py va appeler la fonction menu qui est dans mesfonctions.py

#Un candidat est caracterisé par son code, son nom , son prenom, le nom de son parti ou coallission politique
#le nombre de parrain obtenu , son sexe et sa fonction


def saisieCandidat():
    code=input("Entrer le code du candidat : ")
    nom=input("Entrer le nom du candidat : ")
    prenom=input("Entrer le prenom du candidat : ")
    pp=input("Entrer le parti ou coallission du candidat : ")
    sexe=input("Entrer le sexe du candidat : ")
    fonction=input("Entrer la fonction du candidat : ")
    np=int(input("Entrer le nombre de parrain du candidat : "))
    candidat=code+" : "+nom+" : "+prenom+" : "+pp+" : "+sexe+" : "+fonction+" : "+str(np)+"\n"
    return candidat

#c=saisieCandidat()
#print(c)


def creationFichierCandidat():
#ouverture du fichier en mode ecriture    
    fc=open("listeCandidat.txt","w")
    n=int(input("entrer le nombre de candidat a ajouter dans le fichier : "))
    for i in range(1,n+1):
        print("*"*15)
        c=saisieCandidat()
        fc.write(c)
        print("le candidat",c," est ajouté dans le fichier")
    fc.close() #tout fichier ouvert doit etre fermé a la fin

#creationFichierCandidat()

#read() permet de lire une ligne et readline() permet de lire une ligne et va sur la ligne suivante
#readlines()permet de lire tout le fichier
    
def afficheFichierCandidat():
    fc=open("listeCandidat.txt","r")
    candidats=fc.readlines()
    if len(candidats)==0:
        print("le fichier de candidat est vide")
    else:
        print("la liste des candidats est ")
        for c in candidats:
            can=c.split(":")
            for ca in can:
                print(ca,end="  ")
    fc.close()

#afficheFichierCandidat()



def ajoutCandidat():
#ouverture du fichier en mode ecriture    
    fc=open("listeCandidat.txt","a")
    n=int(input("entrer le nombre de candidat a ajouter dans le fichier : "))
    for i in range(1,n+1):
        print("*"*15)
        c=saisieCandidat()
        fc.write(c)
        print("le candidat",c," est ajouté dans le fichier")
    fc.close()

#ajoutCandidat()
#afficheFichierCandidat()



def transfertCandidat():
    fc=open("listeCandidat.txt","r")
    candidats=fc.readlines()
    if len(candidats)==0:
        print("le fichier de candidat est vide")
    else:
#split() permet de delimiter les chaines mais faut lui donner le caractere de separation        
        for c in candidats:
            nbp=int(c.split(" : ")[6])
            nomPrenomcandidat=c.split(" : ")[1]+" "+c.split(" : ")[2]
            if nbp >=60000:
                print("le candidat", nomPrenomcandidat," a validé son parrainage")
    fc.close()

transfertCandidat()          
def menu():
    while True:
        print(" - "*15)
        print("\t MENU")
        print("1 - Creation fichier candidat")
        print("2 - Affiche fichier candidat")
        print("3 - Ajout dans le fichier candidat")
        print("4 - Liste de candidat ayant valider le parrainnage")
        print("5 - Quitter")
        print("6 - Faites votre choix : ",end="")
        choix=int(input(""))
        if choix==1:
            creationFichierCandidat()
        elif choix==2:
            afficheFichierCandidat() 
        elif choix==3:
            ajoutCandidat()
        elif choix==4:
            transfertCandidat()
        elif choix==5:
            print("Au revoir")
            break
        else:
            print("Le choix n'existe pas")
        
#menu()           
            




















  
