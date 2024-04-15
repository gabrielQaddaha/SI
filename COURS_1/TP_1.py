import json
import os
import sys

class Livre:
    def __init__(self, nom, tag, image):
        self.nom = nom
        self.tag = tag
        self.image = image
    
        
class Bibliotheque:
    def __init__(self):
        self.livres = []
    
    def ajouter_livre(self, livre):
        self.livres.append(livre)
    
    def supprimer_livre(self, nom):
        for livre in self.livres:
            if livre.nom == nom:
                self.livres.remove(livre)
    
    def lister_livres(self):
        if not self.livres:
            print("Aucun livre dans la bibliothèque.")
        else:
            for livre in self.livres:
                print(livre.nom, "\n")
                print(f"       Tag : {livre.tag}")
                print(f"       Image : {livre.image}\n")
    
    def detail_livre(self, nom):
        for livre in self.livres:
            if livre.nom == nom:
                print(livre)
    
    def sauvegarder(self):
        with open("bibliotheque.json", "w") as f:
            json.dump([livre.__dict__ for livre in self.livres], f)
    
    def charger(self):
        if os.path.exists("bibliotheque.json"):
            with open("bibliotheque.json", "r") as f:
                data = json.load(f)
                self.livres = [Livre(livre["nom"], livre["tag"], livre["image"]) for livre in data]

def menu():
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Lister les livres")
    print("4. Détail d'un livre")
    print("5. Sauvegarder")
    print("6. Charger")
    print("7. Quitter")
    choix = input("Votre choix : ")
    return choix

def main():
    bibliotheque = Bibliotheque()
    bibliotheque.charger()
    
    while True:
        choix = menu()
        
        if choix == "1":
            nom = input("Nom : ")
            tag = input("Tag : ")
            image = input("Image : ")
            livre = Livre(nom, tag, image)
            bibliotheque.ajouter_livre(livre)
        elif choix == "2":
            nom = input("Nom : ")
            bibliotheque.supprimer_livre(nom)
        elif choix == "3":
            bibliotheque.lister_livres()
        elif choix == "4":
            nom = input("Nom : ")
            bibliotheque.detail_livre(nom)
        elif choix == "5":
            bibliotheque.sauvegarder()
        elif choix == "6":
            bibliotheque.charger()
        elif choix == "7":
            sys.exit(0)
        else:
            print("Choix invalide")

if __name__ == "__main__":
    main()
