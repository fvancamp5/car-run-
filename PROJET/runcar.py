

# Bibliothèque
import pyxel # https://github.com/kitao/pyxel/blob/main/docs/README.fr.md

# Création de  l'objet
class Jeu:
    def __init__(self):
        # position initiale de la bulle à l'ouverture de la fenetre
        # (origine des positions : coin haut gauche)
        self.bulle_x = 100
        self.bulle_y = 150
        self.taille_ma_bulle=10
        self.taille_fenetre_x=200
        self.taille_fenetre_y=300
        self.vitesse=100

        # taille de la fenetre 200x300 pixels
        # ne pas modifier
        pyxel.init(self.taille_fenetre_x, self.taille_fenetre_y, title="Challenge NSI",fps=self.vitesse)
        # fps= vitesse de rafraichissement des images self.vitesse fois par seconde
  
        # chargement des images
        pyxel.load("car.pyxres")

        # On lance l’application Pyxel avec la fonction run qui crée
        # deux processus basés sur les méthodes draw() et update() :
        pyxel.run(self.update, self.draw)


    def bulle_deplacement(self):
        """déplacement avec les touches de directions"""
        if pyxel.btn(pyxel.KEY_RIGHT) and self.bulle_x<self.taille_fenetre_x:
            self.bulle_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.bulle_x>0:
            self.bulle_x += -1
        if pyxel.btn(pyxel.KEY_DOWN) and self.bulle_y<self.taille_fenetre_y :
            self.bulle_y += 1
        if pyxel.btn(pyxel.KEY_UP) and self.bulle_y>0:
            self.bulle_y += -1

        
            
            
    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """mise à jour des variables """
        # deplacement de ma bulle
        self.bulle_deplacement()
        
    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets """
        # vide la fenetre avec la couleur de fond 0
        pyxel.cls(0)
        # ma bulle
        pyxel.circ(self.bulle_x, self.bulle_y, self.taille_ma_bulle, 14)

Jeu()
