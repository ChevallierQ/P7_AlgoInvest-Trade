from csv import reader as read
from itertools import combinations as combi
from tqdm import tqdm
from os import system as sys

class BruteForce:
    '''
        Classe principale de l'algorithme brute force.
    '''

    def __init__(self):
        '''
            Initialisation de la classe et de ses variables, 
            test, ouverture et lecture du fichier csv.
        '''
        try:
            with open('data/action.csv', newline='') as data_csv:
                data_action = read(data_csv, delimiter=',', quotechar='|')
                liste_action = []
                for i in data_action:
                    liste_action.append([i[0], float(i[1]), float(i[2])])
        except FileNotFoundError:
            print("La base de données csv n'a pas été trouvée.")
        self.actions = liste_action
        self.limite_achat = 500
        self.benefices = 0
        self.meilleur_combinaison = []

    def calcul_prix_actions(self, combinaison):
        '''
            Fonction calculant le prix d'un groupe d'action.
            argument -> liste
            retourn -> float (somme des prix)
        '''
        calcul = []
        for i in combinaison:
            calcul.append(i[1])
        calcul = sum(calcul)
        return calcul

    def calcul_benefices(self, combinaison):
        '''
            Fonction calculant le benefice d'une action en fonction de son prix
            et de son pourcentage de rentabilité.
            argument -> list
            retourn -> float (somme des benefices)
        '''
        calcul = []
        for i in combinaison:
            calcul.append((i[2]*i[1])/100)
        calcul = sum(calcul)
        return calcul

    def resultats(self, *arg):
        '''
            Fonction affichant le resultat final en forme.
            arguments -> list, list
        '''
        prix = self.calcul_prix_actions(arg[0])
        benefices = "{:.2f}".format(arg[1])
        combinaison = arg[0]
        print("\n")
        print("=====================================================================")
        print("=======================La meilleur combinaison=======================")
        print("=====================================================================")
        print(f"\n\nPour {prix}$, vous pouvez gagnez au bout de 2 ans {benefices}$\navec la combinaison d'actions suivante :\n")
        for i in combinaison:
            print(f"Action n°{i[0]}, coût {i[1]}$.")
        print("\n\n")

    def main(self):
        '''
            Fontion principale.
        '''
        print("=====================================================================")
        print("===========================Calcul en cours===========================")
        print("=====================================================================")
        print("\n")
        actions = self.actions
        benefices = self.benefices
        meilleur_combinaison = self.meilleur_combinaison
        for i in tqdm(range(len(actions))):
            combinaisons = combi(actions, i + 1)
            for combinaison in combinaisons:
                calcul_prix_action = self.calcul_prix_actions(combinaison)
                if calcul_prix_action <= self.limite_achat:
                    calcul_benefice = self.calcul_benefices(combinaison)
                    if calcul_benefice > benefices:
                        benefices = calcul_benefice
                        meilleur_combinaison = combinaison
        self.resultats(meilleur_combinaison, benefices)

if __name__ == '__main__':
    sys("clear")
    brute = BruteForce()
    brute.main()
    