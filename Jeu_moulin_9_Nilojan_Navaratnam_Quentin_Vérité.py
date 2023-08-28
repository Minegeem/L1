from fltk import*
from graphique_Nilojan_Navaratnam_Quentin_Vérité import*

def creation_plateau():
    """
    
    Création de la liste de liste
    
    """
    lst=[]
    for i in range(7):
        if i==0 or i==6:
            lst.append([True,None,None,True,None,None,True])
        elif i==1 or i==5:
            lst.append([None,True,None,True,None,True,None])
        elif i==2 or i==4:
            lst.append([None,None,True,True,True,None,None])
        else:
            lst.append([True,True,True,None,True,True,True])
    return lst

def pion_possible(ligne,colonne,lst,joueur,taille,lst1,lst2):
    '''
    
    Regarde si on peut poser un pion 
    
    '''
    x,i,j=point_valable(ligne,colonne,lst1,lst2,taille)
    if lst[i][j]=="Black" or lst[i][j]=="White" or lst[i][j]==None or x==False:
        print(f"Choisissez un autre endroit joueur {joueur}.")
        ev=attend_ev()
        x,i,j=pion_possible(abscisse(ev),ordonnee(ev),lst,joueur,taille,lst1,lst2)
    return (True,i,j)

def point_valable(x,y,lst1,lst2,taille): 
    '''
    
    point valable sur le plateau (graphique)
    
    '''
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            if lst1[i][j]-taille/100<x and x<lst1[i][j]+taille/100 and lst2[i][j]-taille/100<y and y<lst2[i][j]+taille/100:
                return True,i,j
    ev=attend_ev()
    x,i,j=point_valable(abscisse(ev),ordonnee(ev),lst1,lst2,taille)
    return True,i,j

def pose_pion(ligne,colonne,plateau_compresser,lst1,lst2,joueur,taille,x):
    '''
    
    Permet de poser un pion en echangeant les 
    
    '''
    if x==True:
        plateau_compresser[ligne][colonne]=joueur
       
def pose_joueur(taille,lst_complete1,lst_complete2,joueur_actuelle):
    '''
    
    Crée le plateau et permet de poser les 18 premiers pion
    
    '''
    plateau=creation_plateau()
    lst_compresser=liste_compresser(plateau)
    for i in range(18):
        if joueur_actuelle==0:
            print("C'est au joueur Noirs")
            ev = attend_ev()
            ty = type_ev(ev)
            if ty == 'Quitte':
                return lst_compresser,10
            x,i,j=pion_possible(abscisse(ev),ordonnee(ev),lst_compresser,"Black",taille,lst_complete1,lst_complete2)
            pose_pion(i,j,lst_compresser,lst_complete1,lst_complete2,"Black",taille,x)
            jeton(taille,lst_compresser,lst_complete1,lst_complete2)
            fin=moulin(lst_compresser,i,j,lst_complete1,lst_complete2,taille)
            if fin==10:
                return lst_compresser,10
            mise_a_jour()
            joueur_actuelle=1
        else:
            print("C'est au joueur Blancs")
            ev=attend_ev()
            ty = type_ev(ev)
            if ty == 'Quitte':
                return lst_compresser,10
            x,i,j=pion_possible(abscisse(ev),ordonnee(ev),lst_compresser,"White",taille,lst_complete1,lst_complete2)
            pose_pion(i,j,lst_compresser,lst_complete1,lst_complete2,"White",taille,x)
            jeton(taille,lst_compresser,lst_complete1,lst_complete2)
            fin=moulin(lst_compresser,i,j,lst_complete1,lst_complete2,taille)
            if fin==10:
                return lst_compresser,10
            mise_a_jour()
            joueur_actuelle=0
    return lst_compresser,4
            

def deplacement_joueur(joueur,plateau,lst1,lst2,taille):
    '''
    
    Pose les question pour deplacer et deplace le pion en appelant des fonctions
    
    '''
    print(f"quel pion voulez vous deplacer joueur {joueur}")
    ev1=attend_ev()
    ty = type_ev(ev1)
    if ty == 'Quitte':
        return 0,0,10
    x,i,j=point_valable(abscisse(ev1),ordonnee(ev1),lst1,lst2,taille)
    while plateau[i][j]!=joueur:
        ev1=attend_ev()
        ty = type_ev(ev1)
        if ty == 'Quitte':
            return 0,0,10
        x,i,j=point_valable(abscisse(ev1),ordonnee(ev1),lst1,lst2,taille)
    print(f"Choisissez l'endroit ou deplacer votre pion joueur {joueur}")
    
    ev2=attend_ev()
    ty = type_ev(ev2)
    if ty == 'Quitte':
        return 0,0,10
    pp,k,l=pion_possible(abscisse(ev2),ordonnee(ev2),plateau,joueur,taille,lst1,lst2)
    while pp!=True:
        ev2=attend_ev()
        ty = type_ev(ev2)
        if ty == 'Quitte':
            return 0,0,10
        pp,k,l=pion_possible(abscisse(ev2),ordonnee(ev2),plateau,joueur,taille,lst1,lst2)
    
    dec_plateau=decompresse_liste(plateau)
    ligne1,colonne1=changement_coord(i,j)
    ligne2,colonne2=changement_coord(k,l)
    
    pointb,pointw=saut(plateau)
    if pointb>3 and joueur=="Black" or pointw>3 and joueur=="White":
        dl=deplacement_possible_ligne(ligne1,colonne1,ligne2,colonne2,dec_plateau)
        dc=deplacement_possible_colonne(ligne1,colonne1,ligne2,colonne2,dec_plateau)
    else:
        dl=True
        dc=True
        
    
    couleur=plateau[i][j]
    
    if couleur==joueur and dl==True or dc==True:
        plateau[i][j]=True
        plateau[k][l]=joueur
        enlever_pion(plateau,joueur,lst1,lst2,taille,i,j,"deplacement")
        jeton(taille,plateau,lst1,lst2)
        mise_a_jour()
        return k,l,4
    else:
        deplacement_joueur(joueur,plateau,lst1,lst2,taille)

def deplacement_possible_ligne(ligne1,colonne1,ligne2,colonne2,plateau):
    if ligne1==0 or ligne1==6:
        if ligne1==ligne2 and colonne2==colonne1+3 or colonne2==colonne1-3:
            return True
        else:
            return False
    elif ligne1==5 or ligne1==1:
        if ligne1==ligne2 and colonne2==colonne1+2 or colonne2==colonne1-2:
            return True
        else:
            return False
    else:
        if ligne1==ligne2 and colonne2==colonne1+1 or colonne2==colonne1-1:
            return True
        else:
            return False

def deplacement_possible_colonne(ligne1,colonne1,ligne2,colonne2,plateau):
    if colonne1==0 or colonne1==6:
        if colonne1==colonne2 and ligne2==ligne1+3 or ligne2==ligne1-3:
            return True
        else:
            return False
    elif colonne1==5 or colonne1==1:
        if colonne1==colonne2 and ligne2==ligne1+2 or ligne2==ligne1-2:
            return True
        else:
            return False
    else:
        if colonne1==colonne2 and ligne2==ligne1+1 or ligne2==ligne1-1:
            return True
        else:
            return False

def saut(plateau):
    pointb=0
    pointw=0
    for i in range(len(plateau)):
        for elem in plateau[i]:
            if elem=="Black":
                pointb+=1
    for i in range(len(plateau)):
        for elem in plateau[i]:
            if elem=="White":
                pointw+=1
    return pointb,pointw

def enlever_pion(plateau,joueur,lst1,lst2,taille,ligne,colonne,ou):
    coord=plateau[ligne][colonne]
    if coord==joueur and coord!=True and coord!=None and ou=="moulin":
        plateau[ligne][colonne]=True
        efface(f'{ligne},{colonne}')
        mise_a_jour()
    elif coord==True and coord!=None and ou=="deplacement":
        plateau[ligne][colonne]=True
        efface(f'{ligne},{colonne}')
        mise_a_jour()
    else:
        ev=attend_ev()
        x,ligne,colonne=point_valable(abscisse(ev),ordonnee(ev),lst1,lst2,taille)
        enlever_pion(plateau,joueur,lst1,lst2,taille,ligne,colonne,ou)

def moulin_ligne(plateau,i,j):
    '''
    
    tout les moulins possible ligne
    
    '''
    if i==3 and j>=0 and j<3:
        if plateau[3][1]==plateau[3][0] and plateau[3][1]==plateau[3][2] and plateau[3][2]=="White":
            return "Blancs"
        elif plateau[3][1]==plateau[3][0] and plateau[3][1]==plateau[3][2] and plateau[3][2]=="Black":
            return "Noirs"
        
    elif i==3 and j<6 and j>=3:
        if plateau[3][3]==plateau[3][4] and plateau[3][4]==plateau[3][5] and plateau[3][5]=="White":
            return "Blancs"
        elif plateau[3][3]==plateau[3][4] and plateau[3][4]==plateau[3][5] and plateau[3][5]=="Black":
            return "Noirs"
        
    else:
        if True in plateau[i]:
            return None
        if "White" and not "Black" in plateau[i]:
            return"Blancs"
        if "Black" and not "White" in plateau[i]:
            return"Noirs"
    

def moulin_colonne(plateau,i,j):
    '''
    
    tout les moulins possible colonne
    
    '''
    b=0
    w=0
    plateau_dec=decompresse_liste(plateau)
    i,j=changement_coord(i,j)
    if j==3 and i>=0 and i<3:
        if plateau_dec[1][3]==plateau_dec[0][3] and plateau_dec[0][3]==plateau_dec[2][3] and plateau_dec[0][3]=="White":
            return "Blancs"
        elif plateau_dec[1][3]==plateau_dec[0][3] and plateau_dec[0][3]==plateau_dec[2][3] and plateau_dec[0][3]=="Black":
            return "Noirs"
    elif j==3 and i>=4 and i<7:
        if plateau_dec[5][3]==plateau_dec[4][3] and plateau_dec[4][3]==plateau_dec[6][3] and plateau_dec[6][3]=="White":
            return "Blancs"
        if plateau_dec[5][3]==plateau_dec[4][3] and plateau_dec[4][3]==plateau_dec[6][3] and plateau_dec[6][3]=="Black":
            return "Noirs"
    
    
    elif j==0 or j==1 or j==2:
        i=0
        for i in range(7):
            if plateau_dec[i][j]==None:
                continue
            elif plateau_dec[i][j]==True:
                return None
            elif plateau_dec[i][j]=="Black":
                b+=1
            else:
                w+=1
        if b==3:
            return "Noirs"
        elif w==3:
            return "Blancs"
        else:
            return None
    else:
        i=0
        for i in range(7):
            if plateau_dec[i][j]==None:
                continue
            elif plateau_dec[i][j]==True:
                return None
            elif plateau_dec[i][j]=="Black":
                b+=1
            else:
                w+=1
        if b==3:
            return "Noirs"
        elif w==3:
            return "Blancs"
        else:
            return None
    
def moulin(plateau,i,j,lst1,lst2,taille):
    '''
    
    programme regroupent tout les moulins possible (ligne et colonne)
    
    '''
    moulinc=moulin_colonne(plateau,i,j)
    moulinl=moulin_ligne(plateau,i,j)
    if moulinc=="Blancs" :
        print(f"Choisissez un pion a enlever joueur Blancs")
        ev=attend_ev()
        x,ligne,colonne=point_valable(abscisse(ev),ordonnee(ev),lst1,lst2,taille)
        enlever_pion(plateau,"Black",lst1,lst2,taille,ligne,colonne,"moulin")
    if moulinl=="Blancs":
        print(f"Choisissez un pion a enlever joueur Blancs")
        ev=attend_ev()
        x,ligne,colonne=point_valable(abscisse(ev),ordonnee(ev),lst1,lst2,taille)
        enlever_pion(plateau,"Black",lst1,lst2,taille,ligne,colonne,"moulin")
    if moulinc=="Noirs" :
        print(f"Choisissez un pion a enlever joueur Noirs")
        ev=attend_ev()
        x,ligne,colonne=point_valable(abscisse(ev),ordonnee(ev),lst1,lst2,taille)
        enlever_pion(plateau,"White",lst1,lst2,taille,ligne,colonne,"moulin")
    if moulinl=="Noirs":
        print(f"Choisissez un pion a enlever joueur Noirs")
        ev=attend_ev()
        x,ligne,colonne=point_valable(abscisse(ev),ordonnee(ev),lst1,lst2,taille)
        enlever_pion(plateau,"White",lst1,lst2,taille,ligne,colonne,"moulin")

def liste_compresser(plateau):
    '''
    
    liste sans les None
    
    '''
    plateau_compresser=[]
    for i in range(7):
        lst1=[]
        for elem in plateau[i]:
            if elem!=None:
                lst1.append(elem)
        plateau_compresser.append(lst1)
    
    return plateau_compresser

def taille():
    '''
    
    programme permettant de transferer la taille dans different fichier py
    
    '''
    taille=int(input("Choisissez une taille."))
    return taille

def jeton(taille,lst_compresser,lst_point1,lst_point2):
    '''

   crée les cercle en fonction de la couleur de la liste de liste

    ''' 
    for i in range(len(lst_compresser)) :
        for j in range(len(lst_compresser[i])):
            if lst_compresser[i][j]=="Black":
                cercle(lst_point1[i][j],lst_point2[i][j],taille/50,couleur='black',remplissage='black',epaisseur=1,tag=f'{i},{j}')
                mise_a_jour()
            elif lst_compresser[i][j]=="White":
                cercle(lst_point1[i][j],lst_point2[i][j],taille/50,couleur='black',remplissage='white',epaisseur=1,tag=f'{i},{j}')
                mise_a_jour()
            else:
                continue

def decompresse_liste(plateauc):
    plateau=[]
    for i in range(len(plateauc)):
        lst=[]
        for elem in plateauc[i]:
            lst.append(elem)
        plateau.append(lst)
            
    for i in range(len(plateau)):
        if i==0 or i==6:
            plateau[i].insert(1,None)
            plateau[i].insert(1,None)
            plateau[i].insert(4,None)
            plateau[i].insert(4,None)
        elif i==1 or i==5:
            plateau[i].insert(0,None)
            plateau[i].insert(-1,None)
            plateau[i].insert(2,None)
            plateau[i].insert(6,None)
        elif i==2 or i==4:
            plateau[i].insert(0,None)
            plateau[i].insert(0,None)
            plateau[i].insert(5,None)
            plateau[i].insert(5,None)
        else:
            plateau[i].insert(3,None)
    return plateau

def changement_coord(i,j):
    if i==0 or i==6:
            if j==0:
                return i,j
            if j==1:
                return i,3
            if j==2:
                return i,6
    elif i==1 or i==5:
        if j==0:
            return i,1
        if j==1:
            return i,3
        if j==2:
            return i,5
    elif i==2 or i==4:
        if j==0:
            return i,2
        if j==1:
            return i,3
        if j==2:
            return i,4
    else:
        if j==3:
            return i,4
        elif j==4:
            return i,5
        elif j==5:
            return i,6
        else:
            return i,j