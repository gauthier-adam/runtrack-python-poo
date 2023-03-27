class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = None

    def vieillir(self):
        self.age += 1
        print("l'age de l'animal",self.age,"ans")

    def afficherTout(self):
        return f"{self.prenom} a {self.age} ans"
    
    def nommer(self, nom):
        self.prenom = nom
        print(self.prenom)

Napoleon = Animal()
Napoleon.vieillir()
Napoleon.nommer("napoleon")
print(Napoleon.afficherTout())