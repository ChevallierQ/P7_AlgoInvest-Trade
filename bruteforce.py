from csv import reader as read
from os import system as sys, times
from sys import argv
from time import time


class BruteForce:
    '''
        Classe principale de l'algorithme brute force.
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
                                liste_action.append([i[0], float(i[1]), float(i[2])*float(i[1])/100])            
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
        benefices = "{:.2f}".format(arg[0][0])
        actions = []
        prix = []
        i = 0
        while arg:
            try:
                actions.append(arg[0][1][i][0])
                prix.append(arg[0][1][i][1])
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
        print(f"\nCalcul réalisé en {arg[1]} sec.")

def recu(limite_achat, actions, elements_selection = []):
    if actions:
        val1, lstVal1 = recu(limite_achat, actions[1:], elements_selection)
        val = actions[0]
        if val[1] <= limite_achat:
            val2, lstVal2 = recu(limite_achat - val[1], actions[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    else:
        return sum([i[2] for i in elements_selection]), elements_selection


if __name__ == '__main__':
    sys("clear")
    brute = BruteForce()
    print("=====================================================================")
    print("===========================Calcul en cours===========================")
    print("=====================================================================")
    print("\n")
    print(f"Algorithme utilisé: {argv[0]}")
    print(f"Valeur du portefeuille: {brute.limite_achat}€")
    print(f"Data analysé: {argv[1]}")
    print(f"Nombre d'actions: {brute.nb_action}")
    print(f"Nombre d'actions valble: {len(brute.actions)}")
    print("\n")
    start = time()
    print("0 sec ...")
    calcul = recu(brute.limite_achat, brute.actions)
    tmpstot = "{:.2f}".format(time() - start)
    print(tmpstot, " sec")
    brute.resultats(calcul, tmpstot)
    