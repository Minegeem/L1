from graphique_Nilojan_Navaratnam_Quentin_Vérité import*
from Jeu_moulin_9_Nilojan_Navaratnam_Quentin_Vérité import*
from random import randint

def jeux(plateau,lst1,lst2,taille,joueur_actuelle):
    
    jouer=True
    while jouer:
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
        if pointw<3 or pointb<3:
            return 0
        if joueur_actuelle==0:
            i,j,fin=deplacement_joueur("Black",plateau,lst1,lst2,taille)
            if fin==10:
                return 10
            fin=moulin(plateau,i,j,lst1,lst2,taille)
            joueur_actuelle=1
        else:
            i,j,fin=deplacement_joueur("White",plateau,lst1,lst2,taille)
            if fin==10:
                return 10
            fin=moulin(plateau,i,j,lst1,lst2,taille)
            joueur_actuelle=0
    

taille=taille()
cree_fenetre(taille,taille)
bordure=(taille-40)/7
joueur_actuelle=randint(0,1)
rotation=0




if __name__ == '__main__':
    page=True
    while page:
        if rotation==0:
            button1=ecran_daccueil(taille)
            ev=attend_ev()
            ty = type_ev(ev)
            if ty == 'Quitte':
                ferme_fenetre()
                page = False
            elif abscisse(ev) >taille/2-100 and ordonnee(ev) >taille/2-60 and abscisse(ev) <taille/2+40 and ordonnee(ev)<taille/2+30:
                rotation=1
                jouer=True
            
        else:
            jouer = True
            fin=''
            plateau_graph(bordure,taille)
            lst_complete1,lst_complete2=point_plateau(bordure,taille)
            mise_a_jour()
            plateau,fin=pose_joueur(taille,lst_complete1,lst_complete2,joueur_actuelle)
            while jouer:
                mise_a_jour()
                ev = donne_ev()
                ty = type_ev(ev)
                if ty == 'Quitte' :
                    ferme_fenetre()
                    jouer = False
                    page = False
                fin=jeux(plateau,lst_complete1,lst_complete2,taille,joueur_actuelle)
                if fin==0:
                    jouer=False
                    rotation=0
                if fin==10:
                    ferme_fenetre()
                    jouer = False
                    page = False
        
        

    
