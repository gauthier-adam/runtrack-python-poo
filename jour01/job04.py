class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print ("je m'appelle", self.nom,self.prenom)

personne1 = Personne ("adam","gauthier")
personne1.SePresenter()