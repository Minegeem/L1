from fonction import*
from graphisme import*


taille = 800
cree_fenetre(taille,taille)
rotation = "ecran_accueil"
if __name__ == '__main__':
    page = True
    
    while page:
        page_level = True
        page_accueil = True
        if rotation == "ecran_accueil":
            ecran_daccueil(taille)
            while page_accueil:
                ev = attend_ev()
                ty = type_ev(ev)
                if ty == 'Quitte':
                    ferme_fenetre()
                    page_accueil = False
                    page = False
                elif abscisse(ev) > 9*taille/25 and ordonnee(ev) > 19*taille/50 and abscisse(ev) < 31*taille/50 and ordonnee(ev) < 14*taille/25:
                    rotation = "ecran_level"
                    page_accueil = False
                    continue
                """elif abscisse(ev) > 14*taille/50 and ordonnee(ev) > 126*taille/200 and abscisse(ev) < 7*taille/10 and ordonnee(ev) < 162*taille/200:
                    rotation = "Parametre"
                    page_accueil = False
                    continue"""
        elif rotation == "ecran_level":
            ecran_level(taille)
            while page_level:
                ev = attend_ev()
                ty = type_ev(ev)
                if ty == 'Quitte':
                    rotation = "ecran_accueil" 
                    page_level = False
                    continue  
                elif abscisse(ev) > 1/8*taille and ordonnee(ev) > 1/4*taille and abscisse(ev) < 350*taille/800 and ordonnee(ev) < 300*taille/800:
                    rotation = jeux("map1")
                    page_level = False
                    continue
                elif abscisse(ev) > 450*taille/800 and ordonnee(ev) > 1/4*taille and abscisse(ev) < 7*taille/8 and ordonnee(ev) < 300*taille/800:
                    rotation = jeux("map2")
                    page_level = False
                    continue
                elif abscisse(ev) > 1/8*taille and ordonnee(ev) > 1/2*taille and abscisse(ev) < 35*taille/80 and ordonnee(ev) < 5*taille/8:
                    rotation = jeux("map3")
                    page_level = False
                    continue
                elif abscisse(ev) > 450*taille/800 and ordonnee(ev) > 1/2*taille and abscisse(ev) < 7*taille/8 and ordonnee(ev) < 5*taille/8:
                    rotation = jeux("map4")
                    page_level = False
                    continue
                elif abscisse(ev) > 1/8*taille and ordonnee(ev) > 3/4*taille and abscisse(ev) < 35*taille/80 and ordonnee(ev) < 7*taille/8:
                    rotation = jeux("map5")
                    page_level = False
                    continue
                elif abscisse(ev) > 450*taille/800 and ordonnee(ev) > 3/4*taille and abscisse(ev) < 7*taille/8 and ordonnee(ev) < 7*taille/8:
                    rotation = jeux("map6")
                    page_level = False
                    continue
        """elif rotation == "Parametre":
            ecran_parametre(taille)
            ev = attend_ev()
            ty = type_ev(ev)
            if ty == 'Quitte':
                rotation == "ecran_accueil" """
 