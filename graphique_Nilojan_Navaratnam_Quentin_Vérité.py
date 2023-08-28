from fltk import*
from Jeu_moulin_9_Nilojan_Navaratnam_Quentin_Vérité import*


def plateau_graph(bordure,taille):
    '''

    création du plateau (graphique)

    '''
    
    rectangle(0,0,taille,taille,couleur='DarkGoldenrod4', remplissage='DarkGoldenrod4')
    rectangle(20,20,taille-20,taille-20,couleur='black', remplissage='', epaisseur=taille/100)
    rectangle(bordure+20,bordure+20,taille-bordure-20,taille-bordure-20,couleur='black', remplissage='', epaisseur=taille/100)
    ligne(20, taille/2, 2*bordure+20, taille/2, couleur='black', epaisseur=taille/100)
    ligne(taille/2, 20, taille/2, 2*bordure+20, couleur='black', epaisseur=taille/100)
    ligne(taille-20, taille/2, taille-2*bordure-20, taille/2, couleur='black', epaisseur=taille/100)
    ligne(taille/2, taille-20, taille/2, taille-2*bordure-20, couleur='black', epaisseur=taille/100)
    rectangle(2*bordure+20,2*bordure+20,taille-2*bordure-20,taille-2*bordure-20,couleur='black', remplissage='', epaisseur=taille/100)

def point_plateau(bordure,taille):
    '''

    creation de tout les points du plateau + mise en liste de liste leurs coordonnées

    '''
    lst1=[]
    lst2=[]
    lst_complete1=[]
    lst_complete2=[]
    for i in range(3):
        point(20+i*bordure,20+i*bordure,couleur='black', epaisseur=taille/100)
        lst1.append(20+i*bordure)
        lst2.append(20+i*bordure)
        mise_a_jour()
        
        point(taille/2,20+i*bordure,couleur='black', epaisseur=taille/100)
        lst1.append(taille/2)
        lst2.append(20+i*bordure)
        mise_a_jour()
        
        point(taille-20-i*bordure,20+i*bordure,couleur='black', epaisseur=taille/100)
        lst1.append(taille-20-i*bordure)
        lst2.append(20+i*bordure)
        mise_a_jour()
        lst_complete1.append(lst1)
        lst_complete2.append(lst2)
        lst1=[]
        lst2=[]
    for i in range(3):
        point(20+i*bordure,taille/2,couleur='black', epaisseur=taille/100)
        lst1.append(20+i*bordure)
        lst2.append(taille/2)
        mise_a_jour()

        point(taille-20-i*bordure,taille/2,couleur='black', epaisseur=taille/100)
        lst1.append(taille-20-i*bordure)
        lst2.append(taille/2)
        mise_a_jour()
    lst_complete1.append(lst1)
    lst_complete2.append(lst2)
    lst1=[]
    lst2=[]
    for i in range(3):
        point(20+i*bordure,taille-20-i*bordure,couleur='black', epaisseur=taille/100)
        lst1.append(20+i*bordure)
        lst2.append(taille-20-i*bordure)
        mise_a_jour()
        
        
        point(taille-taille/2,taille-20-i*bordure,couleur='black', epaisseur=taille/100)
        lst1.append(taille-taille/2)
        lst2.append(taille-20-i*bordure)
        mise_a_jour()
        
        
        point(taille-20-i*bordure,taille-20-i*bordure,couleur='black', epaisseur=taille/100)
        lst1.append(taille-20-i*bordure)
        lst2.append(taille-20-i*bordure)
        mise_a_jour()
        lst_complete1.append(lst1)
        lst_complete2.append(lst2)
        lst1=[]
        lst2=[]
    lst_complete1[4],lst_complete1[6]=lst_complete1[6],lst_complete1[4]
    lst_complete1[3][1],lst_complete1[3][2]=lst_complete1[3][2],lst_complete1[3][1]
    lst_complete1[3][2],lst_complete1[3][4]=lst_complete1[3][4],lst_complete1[3][2]
    lst_complete1[3][3],lst_complete1[3][5]=lst_complete1[3][5],lst_complete1[3][3]
    lst_complete1[3][4],lst_complete1[3][5]=lst_complete1[3][5],lst_complete1[3][4]

    lst_complete2[4],lst_complete2[6]=lst_complete2[6],lst_complete2[4]
    lst_complete2[3][1],lst_complete2[3][2]=lst_complete2[3][2],lst_complete2[3][1]
    lst_complete2[3][2],lst_complete2[3][4]=lst_complete2[3][4],lst_complete2[3][2]
    lst_complete2[3][3],lst_complete2[3][5]=lst_complete2[3][5],lst_complete2[3][3]
    lst_complete2[3][4],lst_complete2[3][5]=lst_complete2[3][5],lst_complete2[3][4]
    
    
    return lst_complete1,lst_complete2

def ecran_daccueil(taille):
    rectangle(0,0,taille,taille,couleur='cyan', remplissage='cyan')
    button1=rectangle(taille/2-70,taille/2-60,taille/2+70,taille/2+30,couleur='gray', remplissage='gray')
    texte(taille/2-40, taille/2-30, "Jouer",couleur='white')
    texte(taille/4, taille/10, "Jeu du Moulin",couleur='black',ancrage='nw', police='Helvetica', taille=48)
    mise_a_jour()
    return button1
