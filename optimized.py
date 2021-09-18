from csv import reader as read
from tqdm import tqdm
from os import system as syst
from sys import argv

from cvxpy import Variable,Problem,Maximize,GLPK_MI as Vari,Probl,Maxim,GLP


class Optimized:
    '''
        Classe principale de l'algorithme optimisé.
    '''

    def __init__(self):
        '''
            Initialisation de la classe et de ses variables, 
            test, ouverture et lecture du fichier csv.
        '''
        if len(argv) == 1:
                print("Vous n'avez pas communqué de base de données.")
                exit()
        else:
            try:
                with open(argv[1], newline='') as data_csv:
                    data_action = read(data_csv, delimiter=',', quotechar='|')
                    liste_action = []
                    for i in data_action:
                        if float(i[1]) <= 0:
                            pass
                        else:
                            liste_action.append([i[0], ])###############################
            except FileNotFoundError:
                print("La base de données csv n'a pas été trouvée.")
        self.actions = liste_action
        self.limite_achat = 500

    def resultats(self, *arg):
        '''
            Fonction affichant le resultat final en forme.
            arguments -> list, list
        '''
        prix = self.calcul_prix_actions(arg[0])
        benefices = "{:.2f}".format(arg[1])
        combinaison = arg[2]
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

        #self.resultats()

if __name__ == '__main__':
    syst("clear")
    optimise = Optimized()
    optimise.main()
