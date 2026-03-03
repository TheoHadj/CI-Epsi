class Combat:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2

    def lancer(self):
        attaquant = self.joueur1
        defenseur = self.joueur2

        while self.joueur1.est_vivant() and self.joueur2.est_vivant():
            attaquant.attaquer(defenseur)
            attaquant, defenseur = defenseur, attaquant

        if self.joueur1.est_vivant():
            return self.joueur1
        return self.joueur2
