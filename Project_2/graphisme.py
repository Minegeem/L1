from fltk import*

def salle(taille: float,i: int,j: int):
    """
    dessine une salle

    """
    rectangle(i*taille,j*taille,i*taille+taille,j*taille+taille,"white","white")
    rectangle(i*taille,j*taille,i*taille+1/3*taille,j*taille+1/3*taille,"black","black")
    rectangle(i*taille+1/3*taille,j*taille+2/3*taille,i*taille,j*taille+taille,"black","black")
    rectangle(i*taille+2/3*taille,j*taille+1/3*taille,i*taille+taille,j*taille,"black","black")
    rectangle(i*taille+2/3*taille,j*taille+2/3*taille,i*taille+taille,j*taille+taille,"black","black")
    rectangle(i*taille+1/6*taille,j*taille+1/6*taille,i*taille+5/6*taille,j*taille+5/6*taille,"white","white")
    mise_a_jour()
    
def porte(ferme: tuple , taille: float, i: int, j: int):
    """
    
    dessine les portes fermer
    
    """
    if ferme[0]!=True:
        rectangle(i*taille, j*taille, i*taille+taille, j*taille+1/6*taille, "black", "black", 1, f"portehaut({i},{j})")             #porte haut
    if ferme[1]!=True:
        rectangle(i*taille+5/6*taille,j*taille,i*taille+ taille,j*taille+ taille, "black", "black", 1, f"portedroite({i},{j})")     #porte droit
    if ferme[2]!=True:
        rectangle(i*taille+taille, j*taille+5/6*taille, i*taille, j*taille+taille, "black", "black", 1, f"portebas({i},{j})")       #porte bas
    if ferme[3]!=True:
        rectangle(i*taille, j*taille, i*taille+1/6*taille, j*taille+taille, "black", "black", 1, f"portegauche({i},{j})")           #porte gauche

def ecran_daccueil(taille: int):
    """
    
    Ecran d'accueil
    
    """
    image(taille/2,taille/2,"./media/fond_accueil.png")                                                                                 #fond d'ecran
    rectangle(9*taille/25-2,19*taille/50-2,31*taille/50+2,14*taille/25+2,couleur='black', remplissage='black')                          #button Level-2
    rectangle(9*taille/25,19*taille/50,31*taille/50,14*taille/25,couleur='mediumslateblue', remplissage='mediumslateblue')              #button Level
    #rectangle(14*taille/50-2,126*taille/200-2,7*taille/10+2,162*taille/200+2,couleur='black', remplissage='black')                      #button Parametre-2
    #rectangle(14*taille/50,126*taille/200,7*taille/10,162*taille/200,couleur='mediumslateblue', remplissage='mediumslateblue')          #button Parametre
    texte(21*taille/50, 22*taille/50, "Level",couleur='pink',ancrage='nw', police='Arial', taille=int(taille/20))                       #txt Level
    #texte(17*taille/50, 138*taille/200, "Parametre",couleur='pink',ancrage='nw', police='Helvetica', taille=int(taille/20))             #txt Parametre
    texte(46*taille/200, taille/10, "Wall is you",couleur='black',ancrage='nw', police='Helvetica', taille=int(taille/12))              #txt Nom jeu
    mise_a_jour()   

def ecran_fin(resultat: str, taille: int):
    rectangle(1/6*taille,1/4*taille,taille-1/6*taille,taille-1/4*taille,couleur='black', remplissage='black')
    texte(taille/2, taille/2, resultat,couleur='white',ancrage='center', police='Arial', taille=int(taille/10))
    return

def ecran_level(taille: int):
    """
    
    crée l'écran avec les bouton pour les niveaux
    
    """
    image(taille/2,taille/2,"./media/fond_parametre.png")                                             #fond d'ecran
    rectangle(1/8*taille,1/4*taille,350*taille/800,300*taille/800,couleur='black', remplissage='navajowhite')                              #button Level
    rectangle(450*taille/800,1/4*taille,7*taille/8,300*taille/800,couleur='black', remplissage='tan')  
    rectangle(1/8*taille,1/2*taille,35*taille/80,5*taille/8,couleur='black', remplissage='darkkhaki')  
    rectangle(450*taille/800,1/2*taille,7*taille/8,5*taille/8,couleur='black', remplissage='olivedrab')  
    rectangle(1/8*taille,3/4*taille,35*taille/80,7*taille/8,couleur='black', remplissage='forestgreen')  
    rectangle(450*taille/800,3/4*taille,7*taille/8,7*taille/8,couleur='black', remplissage='darkolivegreen')  
    texte(1/8*taille+30,1/4*taille+20, "Level 1",couleur='black',ancrage='nw', police='Helvetica', taille=int(taille/20))               #txt Level_1
    texte(1/8*taille+380,1/4*taille+20, "Level 2",couleur='black',ancrage='nw', police='Helvetica', taille=int(taille/20))              #txt Level_2
    texte(1/8*taille+30,1/4*taille+220, "Level 3",couleur='black',ancrage='nw', police='Helvetica', taille=int(taille/20))              #txt Level_3
    texte(1/8*taille+380,1/4*taille+220, "Level 4",couleur='black',ancrage='nw', police='Helvetica', taille=int(taille/20))             #txt Level_4
    texte(1/8*taille+30,1/4*taille+420, "Level 5",couleur='black',ancrage='nw', police='Helvetica', taille=int(taille/20))              #txt Level_5
    texte(1/8*taille+380,1/4*taille+420, "Level 6",couleur='black',ancrage='nw', police='Helvetica', taille=int(taille/20))             #txt Level_6
    texte(46*taille/200+100, taille/10, "Levels",couleur='black',ancrage='nw', police='Helvetica', taille=int(taille/12))               #txt Levels
    mise_a_jour()   
    
def dragongraph(dragons: list[dict],donjon: list[list[tuple]],taille: int):
    """
    
    mets les images et le niveau des dragons
    
    """
    
    for dragon in dragons:
        
        if dragon["position"] == None:
            #image(a*taille/len(donjon)+(taille/len(donjon))/2,b*taille/len(donjon[0])+(taille/len(donjon[0]))/2,"./media/ganondorf.png", int((taille/len(donjon[0]))/3), int((taille/len(donjon[0]))/3),"center")
            continue
        else:
            (a,b) = dragon["position"]
            niv = dragon["niveau"]
            image(a*taille/len(donjon)+(taille/len(donjon))/2,b*taille/len(donjon[0])+(taille/len(donjon[0]))/2,"./media/ganondorf.png", int((taille/len(donjon[0]))/3), int((taille/len(donjon[0]))/3),"center", tag="dragon")
            rectangle(a*taille/len(donjon)+(taille/len(donjon))/2+10*taille/800,b*taille/len(donjon[0])+(taille/len(donjon[0]))/2-20*taille/800,a*taille/len(donjon[0])+(taille/len(donjon[0]))/2+20*taille/800,b*taille/len(donjon[0])+(taille/len(donjon[0]))/2-35*taille/800,"black","black", tag="dragon")
            texte(a*taille/len(donjon)+(taille/len(donjon))/2+12*taille/800,b*taille/len(donjon[0])+(taille/len(donjon[0]))/2-33*taille/800, f"{niv}",couleur='white',ancrage='nw', police='Helvetica', taille=int(taille/90), tag="dragon")
            

def aventuriergraph(aventurier: dict,donjon: list[list[tuple]],taille: int):
    """
    
    mets l'aventurier et le niveau de l'aventurier
    
    """
    (a,b)=aventurier["position"]
    niv=aventurier["niveau"]
    image(a*taille/len(donjon)+(taille/len(donjon))/2,b*taille/len(donjon[0])+(taille/len(donjon[0]))/2,"./media/link.png", int(30), int(37),"center","aventurier")
    rectangle(a*taille/len(donjon)+(taille/len(donjon))/2-15*taille/800,b*taille/len(donjon[0])+(taille/len(donjon[0]))/2-25*taille/800,a*taille/len(donjon[0])+(taille/len(donjon[0]))/2-5*taille/800,b*taille/len(donjon[0])+(taille/len(donjon[0]))/2-40*taille/800,"black","black",1,"aventurier")
    texte(a*taille/len(donjon)+(taille/len(donjon))/2-13*taille/800, b*taille/len(donjon[0])+(taille/len(donjon[0]))/2-39*taille/800, f"{niv}",couleur='white',ancrage='nw', police='Helvetica', taille=int(taille/90), tag="aventurier")

def plateau(donjon: list[list[tuple]], taille: float = 800):
    """
    
    crée le plateau a partir de la liste de liste initiale
    
    """
    for i in range(len(donjon)):
        for j in range(len(donjon[i])):
            salle(taille,i,j)
            porte(donjon[i][j],taille,i,j)
            
def trait_rouge(chemin: list[tuple], donjon: list[list[tuple]], taille: float = 800):
    """
    
    crée le trait rouge qui relie le chemin entre l'aventurier et le dragon
    
    """
    for i in range(len(chemin)-1):
        ligne(chemin[i][0]*taille/len(donjon)+(taille/len(donjon))/2, chemin[i][1]*taille/len(donjon)+(taille/len(donjon))/2, chemin[i+1][0]*taille/len(donjon)+(taille/len(donjon))/2, chemin[i+1][1]*taille/len(donjon)+(taille/len(donjon))/2, couleur = "red", epaisseur = 2, tag = "trait_rouge")
        mise_a_jour()

