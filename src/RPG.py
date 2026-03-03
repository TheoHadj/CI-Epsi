#def main():
 #   print("Hello, World!")
  #  print("Hello, World!")


    
#if(__name__ == "__main__"):
#    main()
class Personnage:
    def __init__(self):
        self.hp = 10

     def attaquer(self, autre):
        if not self.est_vivant():
            return
        if not autre.est_vivant():
            return

        autre.hp -= 1

    def est_vivant(self):
        return self.hp > 0

