from csv import reader as read
from tqdm import tqdm
from math import ceil
from os import system as syst
from sys import argv
from time import time


class Optimized:
    '''
        Classe principale de l'algorithme optimisé.
    '''

    def __init__(self):
        '''
            Initialisation de la classe et de ses variables, 
            test, ouverture et lecture du fichier csv.
        '''
        if len(argv) == 0:
                print("Vous n'avez pas communqué de base de données.")
                exit()
        else:
            try:
                with open(argv[1], newline='') as data_csv:
                    data_action = read(data_csv, delimiter=',', quotechar='|')
                    liste_action = []
                    a = 0
                    for i in data_action:
                        a+=1
                        if i[1] == "price":
                            a-=1
                            pass
                        else:
                            if float(i[1]) <= 0:
                                pass
                            else:
                                liste_action.append([i[0], int(ceil(float(i[1]))), float(i[2])*float(i[1])/100])            
            except FileNotFoundError:
                print("La base de données csv n'a pas été trouvée.")
        self.nb_action = a
        self.actions = liste_action
        self.limite_achat = 500

    def resultats(self, *arg):
        '''
            Fonction affichant le resultat final en forme.
            arguments -> list, list
        '''
        print("\n")
        print("=====================================================================")
        print("=======================La meilleur combinaison=======================")
        print("=====================================================================")
        print("\n")
        benefices = "{:.2f}".format(arg[0])
        actions = []
        prix = []
        i = 0
        while arg:
            try:
                actions.append(arg[1][i][0])
                prix.append(arg[1][i][1])
                i+=1
            except IndexError:
                break
        tot = sum(prix)
        print(f"Pour {tot}€, vous pouvez gagner au bout de 2 ans {benefices}€")
        print("avec la combinaison d'actions suivante :\n")
        i = 0
        for x in actions:
            print(f"Action n°{x}, coût {prix[i]}€.")
            i+=1
        print(f"\nCalcul réalisé en {arg[-1]} sec.")

    def main(self):
        '''
            Fontion principale.
        '''
        print("=====================================================================")
        print("===========================Calcul en cours===========================")
        print("=====================================================================")
        print("\n")
        print(f"Algorithme utilisé: {argv[0]}")
        print(f"Valeur du portefeuille: {self.limite_achat}€")
        print(f"Data analysé: {argv[1]}")
        print(f"Nombre d'actions: {self.nb_action}")
        print(f"Nombre d'actions valble: {len(self.actions)}")
        print("\n")
        limite_achat = self.limite_achat
        actions = self.actions
        matrice = [[0 for x in range(limite_achat + 1)] for x in range(len(actions) + 1)]

        for i in tqdm(range(1, len(actions) + 1)):
            for w in range(1, limite_achat + 1):
                if actions[i-1][1] <= w:
                    matrice[i][w] = max(actions[i-1][2] + matrice[i-1][w-actions[i-1][1]], matrice[i-1][w])
                else:
                    matrice[i][w] = matrice[i-1][w]

        w = limite_achat
        n = len(actions)
        elements_selection = []
        while w >= 0 and n >= 0:
            e = actions[n-1]
            if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
                elements_selection.append(e)
                w -= e[1]
            n -= 1

        tmpstot = "{:.2f}".format(time() - start)
        self.resultats(matrice[-1][-1], elements_selection, tmpstot)

if __name__ == '__main__':
    syst("clear")
    optimise = Optimized()
    start = time()
    optimise.main()
