

# Bibliothèque
import pyxel # https://github.com/kitao/pyxel/blob/main/docs/README.fr.md
from datetime import datetime, timedelta

# Création de  l'objet
class Jeu:
    def __init__(self):
        # position initiale de la bulle à l'ouverture de la fenetre
        # (origine des positions : coin haut gauche)
        self.voiture_x = 100
        self.voiture_y = 150
        self.taille_voiture_x=35
        self.taille_voiture_y=60
        self.position_game_over=0
        self.taille_fenetre_x=200
        self.taille_fenetre_y=300
        self.time = datetime.now()
        self.vitesse=100
        
        # initialisation des bulles fantomes
        self.taille_bulle_fantome=5
        self.bidon_liste=[]

        self.essence=100
        self.vie = 1
        self.couleur = 0

        # liste de couleurs
        self.couleur_essence = [11,9,8]

        # taille de la fenetre 200x300 pixels
        # ne pas modifier
        pyxel.init(self.taille_fenetre_x, self.taille_fenetre_y, title="RUN CAR",fps=self.vitesse)
        # fps= vitesse de rafraichissement des images self.vitesse fois par seconde
  
        # chargement des images
        # pyxel.load("car.pyxres")

        """
        #création de la mélodie
        pyxel.sound(2).set(
            "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )
        """,
        # https://github.com/kitao/pyxel/blob/main/python/pyxel/examples/04_sound_api.py

        # On lance l’application Pyxel avec la fonction run qui crée
        # deux processus basés sur les méthodes draw() et update() :
        pyxel.run(self.update, self.draw)


    def voiture_deplacement(self):
        """déplacement avec les touches de directions"""
        if pyxel.btn(pyxel.KEY_RIGHT) and self.voiture_x<self.taille_fenetre_x:
            self.voiture_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.voiture_x>0:
            self.voiture_x += -1

    def bidon_creation(self):
        """création aléatoire des bidons"""
        # bidon 
        if datetime.now() > self.time + timedelta(seconds=0.4):
            self.bidon_liste.append([pyxel.rndi(0, self.taille_fenetre_x), 0,pyxel.rndi(0,14)])
            self.time = datetime.now()

            
    def bidon_deplacement(self):
        """déplacement des  bulles fantome vers le haut et suppression s'ils sortent du cadre"""              
        for bidon in self.bidon_liste:
            bidon[1] += 1 #vitesse de déplacement (p*p)
            if  bidon[1]>self.taille_fenetre_y:
                self.bidon_liste.remove(bidon)

    def collision_bidon(self):
        """disparition du vaisseau et d'un ennemi si contact"""
        for bidon_col in self.bidon_liste:
            if bidon_col[0] > self.voiture_x -(self.taille_voiture_x) and bidon_col[0] < self.voiture_x +(self.taille_voiture_x) and bidon_col[1] > self.voiture_y-(self.taille_voiture_y) and bidon_col[1] < self.voiture_y +(self.taille_voiture_y):
                self.bidon_liste.remove(bidon_col)
                # on remet l'essence à 100 (réservoir max)
                self.essence = 100
    
    # Fonction reserve d'essence
    def reserve_essence(self):
        if datetime.now() > self.time + timedelta(seconds=0.1):
            self.essence -= 1
            self.time = datetime.now()

    def alert_essence(self):
        if self.essence > 70:
            self.couleur = 0
        elif self.essence < 69 and self.essence > 35:
            self.couleur = 1
        elif self.essence < 34 and self.essence >= 0:
            self.couleur=2

        
            
    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        if self.essence > 0:
            """mise à jour des variables """
            # deplacement de ma voiture
            self.voiture_deplacement()
            # creation des bulles fantome
            self.bidon_creation()
            # mise a jour des positions des bulles fantome
            self.bidon_deplacement()
            # collision avec le bidon d'essence
            self.collision_bidon()
            # diminution de l'essence présente dans la voiture
            self.reserve_essence()
            # couleur alerte de la jauge d'essence
            self.alert_essence()



    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets """
        # vide la fenetre avec la couleur de fond 0
        pyxel.cls(0)
        # ma voiture
        pyxel.rect(self.voiture_x, self.voiture_y, self.taille_voiture_x, self.taille_voiture_y, 7)

        # bidon d'essence
        for bul_fant in self.bidon_liste:
            pyxel.circ(bul_fant[0], bul_fant[1], self.taille_bulle_fantome, bul_fant[2])

        # affichage de l'essence
        pyxel.rect(10, 7, 100, 14, 13) # fond de la jauge d'essence (rectangle)
        pyxel.rect(10, 7, self.essence, 14, self.couleur_essence[self.couleur]) # rectangle jauge essence
        pyxel.text(14,11, "Essence : " + str(self.essence) + "/100", 7) # texte du niveau d'essence.

        # Fin du jeu
        if self.vie == 0 or self.essence == 0:
            pyxel.text(self.taille_fenetre_x/2.4,self.taille_fenetre_y/2 - 20, 'JEU TERMINE', 10)

Jeu()
