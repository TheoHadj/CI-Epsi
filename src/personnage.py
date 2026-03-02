class Personnage:
    def __init__(self):
        self.points_de_vie = 10
        
    def get_points_vie(self):
        return self.points_de_vie

    def est_vivant(self):
        return self.points_de_vie > 0
    
    def subir_degats(self):
        self.points_de_vie -= 1