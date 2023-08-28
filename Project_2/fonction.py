from fltk import *
from graphisme import*
#(haut ,droit ,bas ,gauche)

def pivot(dungeon : list[list[tuple]], position : tuple):
    """
    
    fait pivoter la porte vers la droite
    
    """
    (x,y) = position
    room = dungeon[x][y]
    haut = room[0]
    droite = room[1]
    bas = room[2]
    gauche = room[3]
    dungeon[x][y] = (gauche, haut, droite, bas)
    return dungeon

def connect(dungeon : list[list[tuple]], position1 : tuple, position2 : tuple):
    """
    
    regarde si il y'a un passage entre de position
    
    """
    (x,y) = position1
    (a,b) = position2

    room1 = dungeon[x][y]
    room2 = dungeon[a][b]

    if room1[1] == room2[3] == True and x+1 == a and y == b :
        return True
    if room1[3] == room2[1] == True and x-1 == a and y == b:
        return True
    if room1[2] == room2[0] == True and y+1 == b and x == a:
        return True
    if room1[0] == room2[2] == True and y-1 == b and x == a:
        return True
    return False

def voisins(donjon : list[list[tuple]], position : tuple):
    """
    
    regarde les case voisines

    """
    coord = []
    nb_lignes = len(donjon)
    nb_colonnes = len(donjon[0])

    for direction in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        voisin_ligne = position[0] + direction[0]
        voisin_colonne = position[1] + direction[1]
        if 0 <= voisin_ligne < nb_lignes and 0 <= voisin_colonne < nb_colonnes:
            coord.append((voisin_ligne, voisin_colonne))
    return coord


def intention(dungeon : list[list[tuple]], position : tuple, dragon : dict, visite : list):
    """
    
    cherche un chemin menant au dragon donné.
    
    """
    voisine = voisins(dungeon,position)
    for waypon in voisine:
        if position == dragon["position"]:
            niveau = dragon["niveau"]
            visite.append(position)
            return [(visite, niveau)]
        if  len(visite) != 1 and position in visite:
            return [(visite, 0)]
        reponse = connect(dungeon, position, waypon)
        
        if reponse:
            if visite == [] or visite[-1] != position:
                visite.append(position)
            [(chemin, maxniveau)] = intention(dungeon, waypon, dragon, visite)
            if maxniveau > 0:
                return [(chemin, maxniveau)]
            chemin.pop()
    if 'chemin' in locals():
        return [(chemin, maxniveau)]
    else:
        return [([],0)]
    
def comparer(solution : list[tuple], dragons: list[dict]):
    """
    
    compare les chemins pour aller au dragon et supprime celle qui ne fonctionne pas ex: un chemin passant par un autre dragon.
    
    """
    delete = []
    for sol in solution:    
        for dragon in dragons:
                if dragon["position"] in sol[0] and dragon["position"] != sol[0][-1]:
                    delete.append(sol)
    for i in range(len(solution)):
        if solution[i] in delete:
            solution.pop(i)
            solution.append(([],0))
    niveaumax = 0
    cheminmax=[]
    for (chemin, niveau) in solution:
        if niveau > niveaumax:
            niveaumax, cheminmax = niveau, chemin
    return (cheminmax,niveaumax)

def rencontre (aventurier: dict, dragon : dict):
    """
    
    regarde si il y'a une rencontre entre le joueur et un dragon
    
    """
    if aventurier["niveau"]>=dragon["niveau"]:
        aventurier["niveau"]+=1
        dragon["position"]=None
        return aventurier, dragon
    else :
        aventurier["niveau"] = None
        return aventurier, dragon

def appliquer_chemin(aventurier : dict, dragons : list[dict], chemin : tuple):
    """
    
    applique le chemin
    
    """
    for elem in chemin:
        if elem == dragons["position"]:
            return rencontre(aventurier,dragons)
        else : 
            aventurier["position"]=elem

def fin_partie(aventurier : dict, dragons : list[dict]):
    """
    
    regarde s'il y'a une fin de partie
    
    """
    for dragon in dragons:
        if dragon["position"] != None:
            return 0
    if aventurier["niveau"] == None:
        return -1
    return 1

def charger(fichier : str):
    """
    
    Chargement du fichier texte en liste de liste et crée les dictionnaire des dragon et de l'aventurier
    
    ╔╔
    ╔╔
    A 0 3 
    D 3 4 1

    ===>
    aventurier {"position": (0,3), "niveau": 1},
    [dragon = {"position": (3,4), "niveau": 1}],
    [[(False,True,True,False),(False,True,True,False)],[(False,True,True,False),(False,True,True,False)]]

    """
    tableau= {
        "╔" : (False,True,True,False),
        "╗" : (False,False,True,True),
        "╚" : (True,True,False,False),
        "╝" : (True,False,False,True),
        "═" : (False,True,False,True),
        "║" : (True,False,True,False),
        "╠" : (True,True,True,False),
        "╣" : (True,False,True,True),
        "╦" : (False,True,True,True),
        "╩" : (True,True,False,True),
        "╨" : (True,False,False,False),
        "╡" : (False,False,False,True),
        "╥" : (False,False,True,False),
        "╞" : (False,True,False,False),
        "╬" : (True,True,True,True),
        " " :(False,False,False,False)
    }
    fic = open(fichier, "r",encoding = "utf-8")
    dragons = []
    donjon = []
    for ligne in fic:
        lig = []
        if ligne[0] == "A":
            aventurier = {
                'position' : (int(ligne[2]),int(ligne[4])),
                'niveau' : 1
            }
            continue
        if ligne[0] == "D":
            dragon = {
                'position' : (int(ligne[2]),int(ligne[4])),
                'niveau' : int(ligne[-2])
            }
            dragons.append(dragon)
            continue
        for elem in ligne:
            if elem == "\n":
                continue
            lig.append(tableau[elem])
        donjon.append(lig)
        
    if isinstance(aventurier,dict):
        return (aventurier,dragons,donjon)
    fic.close()



def jeux(fichier: str, taille: int = 800):
    """
    
    L'agencement de toute les fonctions pour crée le jeu
    
    """
    (aventurier, dragons, donjon) = charger(f"./maps/{fichier}.txt")
    longeur = taille/len(donjon[0])
    plateau(donjon, longeur)
    dragongraph(dragons,donjon,taille)
    aventuriergraph(aventurier,donjon,taille)
    jouer = True
    while jouer:
        
        ev = attend_ev()
        ty = type_ev(ev)
        if ty == 'Quitte':
            jouer = False
            return "ecran_level"
        if ty == "ClicGauche":
            for i in range (len(donjon)):
                for j in range (len(donjon[0])):
                    if abscisse(ev) > i*longeur and ordonnee(ev) > j*longeur and abscisse(ev) < i*longeur+longeur and ordonnee(ev) < j*longeur+longeur:
                        donjon = pivot(donjon,(i,j))
                        efface(f"portehaut({i},{j})")
                        efface(f"portedroite({i},{j})")
                        efface(f"portebas({i},{j})")
                        efface(f"portegauche({i},{j})")
                        porte(donjon[i][j],longeur,i,j)
                        mise_a_jour()
        if ty == "Touche" and rep[0] != []:
            for elem in rep[0]:
                efface("aventurier")
                aventurier["position"] = elem
                aventuriergraph(aventurier, donjon, taille)
                efface('trait_rouge')
                mise_a_jour()
                attend_ev()
            for dragon in dragons:
                if dragon["position"] == aventurier["position"]:
                    aventurier, drag = rencontre(aventurier, dragon)
                    efface("aventurier")
                    aventuriergraph(aventurier, donjon, taille)
                    mise_a_jour()
                    dragon = drag
                    if aventurier["niveau"] == None:
                        ecran_fin("Defaite", taille)
                        attend_ev()
                        jouer = False
                        return "ecran_level"
                    if dragon["position"] == None:
                        efface("dragon")
                        dragongraph(dragons, donjon, taille)
                        mise_a_jour()


        solution = []
        for dragon in dragons:
            sol = intention(donjon, aventurier["position"], dragon, visite = [])
            solution += sol
        rep = comparer(solution, dragons)
        efface("trait_rouge")
        if rep[0] != []:
            trait_rouge(rep[0], donjon, taille)
        cpt = 0
        for dragon in dragons:
            if dragon["position"] != None:
                continue
            else:
                cpt += 1
            if cpt == 3:
                ecran_fin("Victoire", taille)
                attend_ev()
                jouer = False
                return "ecran_level"


