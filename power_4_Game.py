"""
__author__ = Fayssal Ben Hammou

__matricule__ = 000479863

__date__ = 4 Novembre 2018

BUT_Du_Programme = d’implémenter un "puissance 4" ainsi qu’une
intelligence artificielle permettant à un joueur d’affronter l’ordinateur. Celle-ci est relativement
basique et développée par niveaux. Dans le premier, l’intelligence artificielle (IA) se contente de
placer son jeton au hasard parmi les colonnes possibles. Dans le second niveau, l’IA joue au hasard
sauf si l’adversaire possède un alignement de 3 jetons dans une fenêtre de 4 et qu’un choix permet
de briser cet alignement. Dans le troisième niveau, en plus de ce qui est décrit ci-avant, si un choix
permet à l’IA d’obtenir un alignement de 3 jetons dans une fenêtre de 4, elle opère ce choix. Il vous
est également demandé de développer un quatrième niveau de votre choix dont vous détaillerez le
fonctionnement dans un docstring au sein de votre programme.

Entrée : un choix de colonne pour l'utilisateur

Sortie : un choix de jeu selon le niveau choisi pour l'IA ( plus le niveau augmente plus la difficulté augmente


"""


from random import randint, seed
import numpy as np                                  #module PACKAGE pour analyser en diagonale la matrice

ligne1 = "|       |"
ligne2 = "|       |"
ligne3 = "|       |"
ligne4 = "|       |"
ligne5 = "|       |"
ligne6 = "|       |"
#MATRICE
grille = [list(ligne1), list(ligne2), list(ligne3), list(ligne4), list(ligne5), list(ligne6), list("-1234567-")]
#grille = [ligne1, ligne2, ligne3, ligne4, ligne5, ligne6, '-1234567-']
compteur = 5                        # Car il y à 6 lignes
step = 0
select_player = 0
print("Bienvenue au Puissance 4")

def print_mat(grille):              #affichage du jeu
    for lignes in grille:
        for colonne in lignes:
            print(colonne, end='')        #c = caractère ou colonne de la Matrice
        print()
    return grille

def colonne_plein():                       #Pour IA
    list_col_free = []
    compteur_1 = 0
    for i in ligne1:
        if ligne1[compteur_1] == ' ':                 #ajoute toute les cases(colonne) lible de la ligne1 dans une liste
            list_col_free.append(compteur_1)
        compteur_1 += 1

    #print("Les colonnes libres sont : "+str(list_col_free))

    choice_index_IA = randint(0 , len(list_col_free)-1)     #choisis une case(colonne) vide aléatoire
    choix_col_IA = list_col_free[choice_index_IA]

    #print("L'IA a choisi au hasard la colonne : " + str(choix_col_IA))

    li = compteur
    out = 0

    while grille[li][choix_col_IA] != ' ' and out == 0:                     #imprime à la première ligne disponible dans
        if li == 0:                                                         # dans la colonne selectionné
           out = 1
        else:
            li -= 1

    if grille[li][choix_col_IA] == ' ':
        grille[li][choix_col_IA] = 'O'              #print("L'IA a bien joué à la colonne : " + str(choix_col_IA))




    # ATTENTION table = grille
def puissance4(table):                              #Analyse pour chaque manière de faire Puissance 4
    if analyse_partie_nulle(table) == 1:            # la Fonction renvoie 1 si elle est activé
        return 1
    if analyse_horizontal(table) == 1:
        return 1
    if analyse_vertical(table) == 1:
        return 1
    if analyse_diagonal(table) == 1:
        return 1
    return 0                                        # return 0 si il se passe rien




def analyse_partie_nulle(table):                    # si la ligne1 est pleine , la partie est nulle
    compteur_2 = 0
    for i in table[0]:
        if i != ' ':
            compteur_2 += 1
    if compteur_2 == len(table[0]):

        print("Partie nulle")


        return 1
    else:
        return 0



def analyse_horizontal(table):          #analyse horizontale
    compteur = 0
    str_horizontal = ""                                             #initie un string pour y ajouter tous les
    #print("")                                                       # caractères de chaque lignes
    for i in table:
        if compteur != len(table)-1:
            str_horizontal = str(table[compteur][1])+str(table[compteur][2])+str(table[compteur][3])+str(
                table[compteur][4]) + str(table[compteur][5]) + str(table[compteur][6]) + str(table[compteur][7])
            if (str_horizontal.find("XXXX") != -1) :

                #print("Félicitations, vous avez gagné la partie !")

                return 1                            #return 1 si victoire de l'utilisateur

            if (str_horizontal.find("OOOO") != -1) :

                #print("L'intelligence artificielle vous a battu !")

                return 1                            #return 1 si victoire de l'IA
        compteur += 1
    return 0                        #return 0 si il se passe rien



def analyse_vertical(table):            #ANALYSE verticale
    compteur = 0
    str_vertical = ""                                                   #initie un string pour y ajouter tous les
    #print("")                                                           # caractères de chaque lignes
    for i in table[0] :
        if compteur != len(table[0])-1 and compteur != 0 :
            str_vertical = str(table[0][compteur])+str(table[1][compteur])+str(table[2][compteur])+str(
                table[3][compteur]) + str(table[4][compteur]) + str(table[5][compteur])

            if (str_vertical.find("XXXX") != -1) :                          #cherche XXXX dans str

                #print(" Félicitations, vous avez gagné la partie ! ")

                return 1                                        #return 1 si victoire de l'utilisateur

            if (str_vertical.find("OOOO") != -1) :                          #cherche OOOO dans str

                #print(" L'intelligence artificielle vous a battu ! ")

                return 1                                        #return 1 si victoire de l'IA
        compteur += 1
    return 0                           #return 0 si il se passe rien




def analyse_diagonal(table):                #ANALYSE diagonale
    # transpose les colonnes de droite à gauche et inversement
    table = np.array(table)
    table_normal = [table[:,1] , table[:,2] , table[:,3] , table[:,4] , table[:,5] , table[:,6] , table[:,7]]
    table_normal = np.transpose(table_normal) #transpose toute mes diagonales droite
    table_mirror = [table[:,7] , table[:,6] , table[:,5] , table[:,4] , table[:,3] , table[:,2] , table[:,1]]
    table_mirror = np.transpose(table_mirror) #transpose toute mes diagonales gauche

    # Diagonales dans le sens vers la droite ( normal )
    compteur_droite = -3                                    #position ligne 4
    for i in table_normal:
        diag_droite = np.diag(table_normal , k=compteur_droite)
        str_diag_droite = ""
        for i in diag_droite :                                      #même principe que horizontale et verticale
            str_diag_droite = str_diag_droite+str(i)

        if (str_diag_droite.find("XXXX") != -1):
            #print(" Félicitations, vous avez gagné la partie ! ")
            return 1                                                #return 1 si victoire de l'utilisateur

        if (str_diag_droite.find("OOOO") != -1):
            #print(" L'intelligence artificielle vous a battu ! ")
            return 1                                                #return 1 si victoire de l'IA

        #print("Diagonal droite = "+str_diag_droite)
        compteur_droite += 1

    # Diagonales dans le sens vers la gauche
    compteur_gauche = -3                                        #position ligne4
    for i in table_mirror :
        diag_gauche = np.diag(table_mirror, k=compteur_gauche)  #même principe que horizontale et verticale
        str_diag_gauche = ""
        for i in diag_gauche :
            str_diag_gauche = str_diag_gauche+str(i)

        if (str_diag_gauche.find("XXXX") != -1):

            #print("Félicitations, vous avez gagné la partie !")
            return 1
        if (str_diag_gauche.find("OOOO") != -1):
            #print("L'intelligence artificielle vous a battu !")
            return 1
        #print("Diagonal gauche = "+str_diag_gauche)
        compteur_gauche += 1

    return 0                #return 0 si il se passe rien




def IA_brise_horizontal(table):                 #ANALYSE brise la possibilitée de faire 4 en HORIZONTALE
    compteur = 0
    out = 1
    res = False
    str_horizontal = ""  # initie un string pour cote_gauche ajouter tous les caractères de chaque lignes
    # print("")
    for i in table:
        if compteur != len(table) - 1:
            str_horizontal = str(table[compteur][1]) + str(table[compteur][2]) + str(table[compteur][3]) + str(
                table[compteur][4]) + str(table[compteur][5]) + str(table[compteur][6]) + str(table[compteur][7])
                                                                            #imprime la matrice

            if str_horizontal.find("X XX") != -1:                            #analyse pour chaque ligne (compteur += 1)
                #print(str_horizontal)
                y = str_horizontal.index("X XX")                             #si il trouve "X XX" ou "XX X" ou "XXX"
                                                                             # ensuit cherche l'indice position du find
                if grille[compteur + 1][y + 2] != ' ' and out != 2:          # et analyse les possibilitées
                    res = True                                               # ensuite imprime si c'est possible
                    out = 2
                    grille[compteur][y + 2] = 'O'

            if str_horizontal.find("XX X") != -1:
                # print(str_horizontal)
                w = str_horizontal.index("XX X")

                if grille[compteur + 1][w + 3] != ' ' and out != 2:
                    out = 2
                    res = True
                    grille[compteur][w + 3] = 'O'


            if str_horizontal.find("XXX") != -1:
                #print(str_horizontal)
                x = str_horizontal.index("XXX")
                cote_gauche = x
                cote_droite = x+4
                #print(compteur)
                #print(x)

                if grille[compteur + 1][x] != ' ' and grille[compteur + 1][x+4] != ' ' and \
                    grille[compteur][cote_gauche] == ' ' and grille[compteur][cote_droite] == ' ' and out != 2:
                    #print("2 CHOIX")
                    choice = randint(1, 2)
                    out = 2
                    res = True

                    if choice == 1:
                        grille[compteur][cote_gauche] = 'O'
                    else:
                        grille[compteur][cote_droite] = 'O'

                elif grille[compteur + 1][cote_gauche] != ' ' and grille[compteur][cote_gauche] == ' ' and out != 2:
                    #print("1 CHOIX GAUCHE")
                    out = 2
                    res = True
                    grille[compteur][cote_gauche] = 'O'

                elif grille[compteur + 1][cote_droite] != ' ' and grille[compteur][cote_droite] == ' ' and out != 2:
                    #print("1 CHOIX DROITE")
                    out = 2
                    res = True
                    grille[compteur][cote_droite] = 'O'


        compteur += 1

    return res                  #return TRUE ou FALSE


def IA_brise_vertical(table):                           #ANALYSE brise la possibilitée de faire 4 en VERTICALE
    compteur_verti = 0
    out = 1
    res = False
    str_vertical = ""
    for i in table[0]:                                               #Meme principe que horizontale
        if compteur_verti != len(table[0])-1 and compteur_verti != 0:
            str_vertical = str(table[0][compteur_verti])+str(table[1][compteur_verti])+str(table[2][compteur_verti])+str(
                table[3][compteur_verti]) + str(table[4][compteur_verti]) + str(table[5][compteur_verti])
            #print(str_vertical)
                                                                      #sauf qu'ici on cherche "XXX"
            if str_vertical.find("XXX") != -1 and out ==1:            #analyse pour chaque ligne (compteur += 1)
                x = str_vertical.index("XXX")
                ligne = x - 1
                colonne = compteur_verti

                                                           #ligne

                if grille[ligne][colonne] == ' ' and out == 1:
                    #print("case libre", x, colonne)
                    res = True
                    out = 2
                    grille[ligne][colonne] = 'O'


        compteur_verti += 1
    return res                                      #return TRUE ou FALSE


def IA_brise_diagonal(table):                       #ANALYSE brise la possibilitée de faire 4 en DIAGONALE
    out = 1
    res = False
    table = np.array(table)
    table_normal = [table[:, 1], table[:, 2], table[:, 3], table[:, 4], table[:, 5], table[:, 6], table[:, 7]]
    table_normal = np.transpose(table_normal)   # Diagonales dans le sens vers la gauche ( normal )
    table_mirror = [table[:, 7], table[:, 6], table[:, 5], table[:, 4], table[:, 3], table[:, 2], table[:, 1]]
    table_mirror = np.transpose(table_mirror)   # Diagonales dans le sens vers la droite ( normal )
    compteur_droite = -3
    compteur_gauche = -3
    compteur_diag_gauche = 1
    compteur_diag_droite = 1

    for i in table_normal :
        diag_droite = np.diag(table_normal, k=compteur_droite)
        str_diag_droite = ""
        for i in diag_droite:  # même principe que horizontale et verticale
            str_diag_droite = str_diag_droite + str(i)

        #print("Diagonale gauche :"+str_diag_droite)

        if (str_diag_droite.find("XXX") != -1):
            x = str_diag_droite.index("XXX")
            #print("diag gauche", x, compteur_diag_gauche)

            if x == 1 and compteur_diag_gauche == 4:
                if grille[1][1] != ' ' and grille[0][1] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][1] = 'O'
            if x == 1 and compteur_diag_gauche == 3:
                if grille[2][1] != ' 'and grille[1][1] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][1] = 'O'
            if x == 1 and compteur_diag_gauche == 2:
                if grille[3][1] != ' ' and grille[2][1] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][1] = 'O'
            if x == 1 and compteur_diag_gauche == 5:
                if grille[1][2] != ' ' and grille[0][2] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][2] = 'O'
            if x == 1 and compteur_diag_gauche == 6:
                if grille[1][3] != ' ' and grille[0][3] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][3] = 'O'
            if x == 1 and compteur_diag_gauche == 7:
                if grille[1][4] != ' ' and grille[0][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][4] = 'O'
            if x == 2 and compteur_diag_gauche == 4:
                if grille[2][2] != ' ' and grille[1][2] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][2] = 'O'
            if x == 2 and compteur_diag_gauche == 5:
                if grille[2][3] != ' ' and grille[1][3] == ' ' and out == 1:
                    res = True
                    out = 1
                    grille[1][3] = 'O'
            if x == 2 and compteur_diag_gauche == 6:
                if grille[2][4] != ' ' and grille[1][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][4] = 'O'
            if x == 3 and compteur_diag_gauche == 3:
                if grille[3][2] != ' ' and grille[2][2] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][2] = 'O'
            if x == 3 and compteur_diag_gauche == 4:
                if grille[3][3] != ' ' and grille[2][3] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][3] = 'O'
            if x == 2 and compteur_diag_gauche == 5:
                if grille[3][4] != ' ' and grille[2][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][4] = 'O'

        compteur_droite += 1
        compteur_diag_gauche += 1


    for i in table_mirror:
        diag_gauche = np.diag(table_mirror, k=compteur_gauche)  # même principe que horizontale et verticale
        str_diag_droite = ""
        for i in diag_gauche:
            str_diag_droite = str_diag_droite + str(i)

        #print("Diagonales droites :"+str_diag_droite)              ANALYSE toute les positions possible de l'indicateur
                                                                    #position de y et x dans les deux types de diagonales
        if (str_diag_droite.find("XXX") != -1):                     #imprime si c'est possible
            y = str_diag_droite.index("XXX")
            #print("diag droite", y, compteur_diag_droite)

            if y == 1 and compteur_diag_droite == 4:
                if grille[1][7] != ' ' and grille[0][7] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][7] = 'O'
            if y == 1 and compteur_diag_droite == 5:
                if grille[1][6] != ' ' and grille[0][6] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][6] = 'O'
            if y == 1 and compteur_diag_droite == 6:
                if grille[1][5] != ' ' and grille[0][5] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][5] = 'O'
            if y == 1 and compteur_diag_droite == 7:
                if grille[1][4] != ' ' and grille[0][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][4] = 'O'
            if y == 1 and compteur_diag_droite == 3:
                if grille[2][7] != ' ' and grille[1][7] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][7] = 'O'
            if y == 2 and compteur_diag_droite == 4:
                if grille[2][6] != ' ' and grille[1][6] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][6] = 'O'
            if y == 2 and compteur_diag_droite == 5:
                if grille[2][5] != ' ' and grille[1][5] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][5] = 'O'
            if y == 2 and compteur_diag_droite == 6:
                if grille[2][4] != ' ' and grille[1][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][4] = 'O'
            if y == 1 and compteur_diag_droite == 2:
                if grille[3][7] != ' ' and grille[2][7] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][7] = 'O'
            if y == 2 and compteur_diag_droite == 3:
                if grille[3][6] != ' ' and grille[2][6] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][6] = 'O'
            if y == 3 and compteur_diag_droite == 4:
                if grille[3][5] != ' ' and grille[2][5] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][5] = 'O'
            if y == 3 and compteur_diag_droite == 5:
                if grille[3][4] != ' ' and grille[2][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][4] = 'O'


        compteur_gauche += 1
        compteur_diag_droite += 1

    return res                                      #return TRUE ou FALSE



def IA_gagnant_horizontal(table):           #ANALYSE gagne si possibilitée de faire 4 en HORIZONTALE
    compteur = 0                            #Même chose que les fonctions Brise sauf qu'ici on cherche à gagner
    out = 1
    res = False
    str_horizontal = ""  # initie un string pour cote_gauche ajouter tous les caractères de chaque lignes
    # print("")
    for i in table:
        if compteur != len(table) - 1:
            str_horizontal = str(table[compteur][1]) + str(table[compteur][2]) + str(table[compteur][3]) + str(
                table[compteur][4]) + str(table[compteur][5]) + str(table[compteur][6]) + str(table[compteur][7])
                                                                            #imprime la matrice


            if str_horizontal.find("O OO") != -1:                            #analyse pour chaque ligne (compteur += 1)
                #print(str_horizontal)
                y = str_horizontal.index("O OO")

                if grille[compteur + 1][y + 2] != ' ' and out != 2:
                    res = True
                    out = 2
                    grille[compteur][y + 2] = 'O'

            if str_horizontal.find("OO O") != -1:
                # print(str_horizontal)
                y = str_horizontal.index("OO O")

                if grille[compteur + 1][y + 3] != ' ' and out != 2:
                    out = 2
                    res = True
                    grille[compteur][y + 3] = 'O'


            if str_horizontal.find("OOO") != -1:
                #print(str_horizontal)
                x = str_horizontal.index("OOO")
                cote_gauche = x
                cote_droite = x+4
                #print(compteur)
                #print(x)

                if grille[compteur + 1][x] != ' ' and grille[compteur + 1][x+4] != ' ' and \
                    grille[compteur][cote_gauche] == ' ' and grille[compteur][cote_droite] == ' ' and out != 2:
                    #print("2 CHOIX")
                    choice = randint(1, 2)
                    out = 2
                    res = True

                    if choice == 1:
                        grille[compteur][cote_gauche] = 'O'
                    else:
                        grille[compteur][cote_droite] = 'O'

                elif grille[compteur + 1][cote_gauche] != ' ' and grille[compteur][cote_gauche] == ' ' and out != 2:
                    #print("1 CHOIX GAUCHE")
                    out = 2
                    res = True
                    grille[compteur][cote_gauche] = 'O'

                elif grille[compteur + 1][cote_droite]  != ' ' and grille[compteur][cote_droite] == ' ' and out != 2:
                    #print("1 CHOIX DROITE")
                    out = 2
                    res = True
                    grille[compteur][cote_droite] = 'O'

        compteur += 1

    return res                      #return TRUE ou FALSE



def IA_gagnant_vertical(table):                     #ANALYSE gagne si possibilitée de faire 4 en VERTICALE
    compteur_verti = 0
    out = 1
    res = False
    str_vertical = ""
    for i in table[0]:
        if compteur_verti != len(table[0])-1 and compteur_verti != 0:
            str_vertical = str(table[0][compteur_verti])+str(table[1][compteur_verti])+str(table[2][compteur_verti])+str(
                table[3][compteur_verti]) + str(table[4][compteur_verti]) + str(table[5][compteur_verti])
            #print(str_vertical)

            if str_vertical.find("OOO") != -1 and out ==1:
                x = str_vertical.index("OOO")
                ligne = x - 1
                colonne = compteur_verti



                if grille[ligne][colonne] == ' ' and out == 1:
                    #print("case libre", x, colonne)
                    res = True
                    out = 2
                    grille[ligne][colonne] = 'O'


        compteur_verti += 1
    return res                          #return TRUE ou FALSE



def IA_gagnant_diagonal(table):             #ANALYSE gagne si possibilitée de faire 4 en DIAGONALE
    out = 1
    res = False
    table = np.array(table)
    table_normal = [table[:, 1], table[:, 2], table[:, 3], table[:, 4], table[:, 5], table[:, 6], table[:, 7]]
    table_normal = np.transpose(table_normal)   # Diagonales dans le sens vers la droite ( normal )
    table_mirror = [table[:, 7], table[:, 6], table[:, 5], table[:, 4], table[:, 3], table[:, 2], table[:, 1]]
    table_mirror = np.transpose(table_mirror)   # Diagonales dans le sens vers la gauche ( normal )
    compteur_droite = -3         # position ligne 4
    compteur_gauche = -3
    compteur_diag_gauche = 1
    compteur_diag_droite = 1

    for i in table_normal :
        diag_droite = np.diag(table_normal, k=compteur_droite)
        str_diag_gauche = ""
        for i in diag_droite:  # même principe que horizontale et verticale
            str_diag_gauche = str_diag_gauche + str(i)

        #print("Diagonale gauche :"+str_diag_droite)

        if (str_diag_gauche.find("OOO") != -1):
            x = str_diag_gauche.index("OOO")
            #print("diag gauche", x, compteur_diag_gauche)

            if x == 1 and compteur_diag_gauche == 4:
                if grille[1][1] != ' ' and grille[0][1] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][1] = 'O'
            if x == 1 and compteur_diag_gauche == 3:
                if grille[2][1] != ' 'and grille[1][1] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][1] = 'O'
            if x == 1 and compteur_diag_gauche == 2:
                if grille[3][1] != ' ' and grille[2][1] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][1] = 'O'
            if x == 1 and compteur_diag_gauche == 5:
                if grille[1][2] != ' ' and grille[0][2] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][2] = 'O'
            if x == 1 and compteur_diag_gauche == 6:
                if grille[1][3] != ' ' and grille[0][3] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][3] = 'O'
            if x == 1 and compteur_diag_gauche == 7:
                if grille[1][4] != ' ' and grille[0][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][4] = 'O'
            if x == 2 and compteur_diag_gauche == 4:
                if grille[2][2] != ' ' and grille[1][2] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][2] = 'O'
            if x == 2 and compteur_diag_gauche == 5:
                if grille[2][3] != ' ' and grille[1][3] == ' ' and out == 1:
                    res = True
                    out = 1
                    grille[1][3] = 'O'
            if x == 2 and compteur_diag_gauche == 6:
                if grille[2][4] != ' ' and grille[1][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][4] = 'O'
            if x == 3 and compteur_diag_gauche == 3:
                if grille[3][2] != ' ' and grille[2][2] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][2] = 'O'
            if x == 3 and compteur_diag_gauche == 4:
                if grille[3][3] != ' ' and grille[2][3] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][3] = 'O'
            if x == 2 and compteur_diag_gauche == 5:
                if grille[3][4] != ' ' and grille[2][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][4] = 'O'

        compteur_droite += 1
        compteur_diag_gauche += 1


    for i in table_mirror:
        diag_gauche = np.diag(table_mirror, k=compteur_gauche)  # même principe que horizontale et verticale
        str_diag_droite = ""
        for i in diag_gauche:
            str_diag_droite = str_diag_droite + str(i)

        #print("Diagonales droites :"+str_diag_droite)

        if (str_diag_droite.find("OOO") != -1):
            y = str_diag_droite.index("OOO")
            #print("diag droite", y, compteur_diag_droite)

            if y == 1 and compteur_diag_droite == 4:
                if grille[1][7] != ' ' and grille[0][7] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][7] = 'O'
            if y == 1 and compteur_diag_droite == 5:
                if grille[1][6] != ' ' and grille[0][6] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][6] = 'O'
            if y == 1 and compteur_diag_droite == 6:
                if grille[1][5] != ' ' and grille[0][5] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][5] = 'O'
            if y == 1 and compteur_diag_droite == 7:
                if grille[1][4] != ' ' and grille[0][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[0][4] = 'O'
            if y == 1 and compteur_diag_droite == 3:
                if grille[2][7] != ' ' and grille[1][7] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][7] = 'O'
            if y == 2 and compteur_diag_droite == 4:
                if grille[2][6] != ' ' and grille[1][6] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][6] = 'O'
            if y == 2 and compteur_diag_droite == 5:
                if grille[2][5] != ' ' and grille[1][5] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][5] = 'O'
            if y == 2 and compteur_diag_droite == 6:
                if grille[2][4] != ' ' and grille[1][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[1][4] = 'O'
            if y == 1 and compteur_diag_droite == 2:
                if grille[3][7] != ' ' and grille[2][7] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][7] = 'O'
            if y == 2 and compteur_diag_droite == 3:
                if grille[3][6] != ' ' and grille[2][6] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][6] = 'O'
            if y == 3 and compteur_diag_droite == 4:
                if grille[3][5] != ' ' and grille[2][5] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][5] = 'O'
            if y == 3 and compteur_diag_droite == 5:
                if grille[3][4] != ' ' and grille[2][4] == ' ' and out == 1:
                    res = True
                    out = 2
                    grille[2][4] = 'O'


        compteur_gauche += 1
        compteur_diag_droite += 1

    return res                  #return TRUE ou FALSE





def niv4_brise_horizontal(table):                 #ANALYSE brise la possibilitée de faire 3 en HORIZONTALE
    compteur = 0
    out = 1
    res = False
    str_horizontal = ""  # initie un string pour cote_gauche ajouter tous les caractères de chaque lignes
    # print("")
    for i in table:
        if compteur != len(table) - 1:
            str_horizontal = str(table[compteur][1]) + str(table[compteur][2]) + str(table[compteur][3]) + str(
                table[compteur][4]) + str(table[compteur][5]) + str(table[compteur][6]) + str(table[compteur][7])
                                                                            #imprime la matrice

            if str_horizontal.find("X X") != -1:                            #analyse pour chaque ligne (compteur += 1)
                #print(str_horizontal)
                y = str_horizontal.index("X X")                             #si il trouve "X XX" ou "XX X" ou "XXX"
                                                                             # ensuit cherche l'indice position du find
                if grille[compteur + 1][y + 2] != ' ' and out != 2:          # et analyse les possibilitées
                    res = True                                               # ensuite imprime si c'est possible
                    out = 2
                    grille[compteur][y + 2] = 'O'


            if str_horizontal.find("XX") != -1:
                #print(str_horizontal)
                x = str_horizontal.index("XX")
                cote_gauche = x
                cote_droite = x+3
                #print(compteur)
                #print(x)

                if grille[compteur + 1][x] != ' ' and grille[compteur + 1][x+3] != ' ' and \
                    grille[compteur][cote_gauche] == ' ' and grille[compteur][cote_droite] == ' ' and out != 2:
                    #print("2 CHOIX")
                    choice = randint(1, 2)
                    out = 2
                    res = True

                    if choice == 1:
                        grille[compteur][cote_gauche] = 'O'
                    else:
                        grille[compteur][cote_droite] = 'O'

                elif grille[compteur + 1][cote_gauche] != ' ' and grille[compteur][cote_gauche] == ' ' and out != 2:
                    #print("1 CHOIX GAUCHE")
                    out = 2
                    res = True
                    grille[compteur][cote_gauche] = 'O'

                elif grille[compteur + 1][cote_droite] != ' ' and grille[compteur][cote_droite] == ' ' and out != 2:
                    #print("1 CHOIX DROITE")
                    out = 2
                    res = True
                    grille[compteur][cote_droite] = 'O'


        compteur += 1

    return res                  #return TRUE ou FALSE


def niv4_brise_vertical(table):                           #ANALYSE brise la possibilitée de faire 3 en VERTICALE
    compteur_verti = 0
    out = 1
    res = False
    str_vertical = ""
    for i in table[0]:                                               #Meme principe que horizontale
        if compteur_verti != len(table[0])-1 and compteur_verti != 0:
            str_vertical = str(table[0][compteur_verti])+str(table[1][compteur_verti])+str(table[2][compteur_verti])+str(
                table[3][compteur_verti]) + str(table[4][compteur_verti]) + str(table[5][compteur_verti])
            #print(str_vertical)
                                                                      #sauf qu'ici on cherche "XXX"
            if str_vertical.find("XX") != -1 and out ==1:            #analyse pour chaque ligne (compteur += 1)
                x = str_vertical.index("XX")
                ligne = x - 1
                colonne = compteur_verti

                                                           #ligne

                if grille[ligne][colonne] == ' ' and out == 1:
                    #print("case libre", x, colonne)
                    res = True
                    out = 2
                    grille[ligne][colonne] = 'O'


        compteur_verti += 1
    return res                                      #return TRUE ou FALSE




# __________________________________________________________________________________

#Débute de Partie

while step == 0:
    niveau = int(input("Veuillez choisir le niveau de l'IA (1-4) : "))
    select_player = 1
    graine = int(input("Veuillez entrer votre graine : "))
    print_mat(grille)

    if niveau == 1:                                 #l'UTILISATEUR choisi son niveau
            step = 1
    elif niveau == 2:
            step = 2
    elif niveau == 3:
            step = 3
    elif niveau == 4:
            step = 4
    else:
        print("Pas possible, recommencez : ")
        step = 0


while step == 1:                                        # boucle pour niveau 1
    if select_player == 1:                              # tour de l'utilisateur
        print("Dans quelle colonne souhaitez-vous jouer ?")
        c = int(input())                                # utilisateur choisi une colonne
        li = compteur                                   # tu inities li = 5 parce que c'est ma dernière ligne de
                                                        #  ma grille ( ligne6 )


        if grille[li][c] == ' ':                        # si la case ( ligne, colonne ) est libre print 'X'
            grille[li][c] = 'X'
        else:
            while grille[li][c] != ' ':             # si elle est pas libre , monte de une ligne et refait le même test
                li -= 1
            if grille[li][c] == ' ':
                grille[li][c] = 'X'
        select_player = 2 # select player = 2 pour passer la main à l'IA

        if puissance4(grille) == 1 :                    # Analyse si puissance 4
            print_mat(grille)
            if analyse_partie_nulle(grille) == 1:
                print("Partie nulle")
            else:
                print(" Félicitations, vous avez gagné la partie ! ")
                step = "end"
            select_player = 0


    if select_player == 2:                              # IA
        nbre_alea = randint(1, 7)  # meme chose que au dessus sauf qu'il y a un
                                   # randint pour choisir la colonne au hasard entre 1 et 7
        li = compteur
        out = 0
        decision = 0

        if grille[li][nbre_alea] == ' ':
            grille[li][nbre_alea] = 'O'
        else:
            while grille[li][nbre_alea] != ' ' and out==0:          #si la case de la ligne1 est libre imprime
                if li == 0:
                    if grille[0][nbre_alea] == ' ':
                        out=1
                        decision = 0  # l'IA remplit la colonne
                    else :                                          #sinon
                        out=1
                        decision = 1  # l'IA va rechercher d'autres colonnes libres
                else:
                    li -= 1

            if li == 0:                                     #analys si la ligne1 est pleine
                #print("Decision : "+str(decision))
                if decision == 0 :
                    grille[li][nbre_alea] = 'O'
                    #print("COLONNE MAINTENANT PLEIN")
                else :                                      #si oui applique la fonction colonne_pleine()
                    #print("RECHERCHE D'AUTRES COLONNES VIDES")
                    colonne_plein()
            else :
                if grille[li][nbre_alea] == ' ':
                    grille[li][nbre_alea] = 'O'

        select_player = 1
        print_mat(grille)
        if puissance4(grille) == 1:
            if analyse_partie_nulle(grille) == 1:
                print("Partie nulle")
            else:
                print("L'intelligence artificielle vous a battu !")
                step = "end"
            select_player = 0



while step == 2:                                        #NIVEAU 2 --> casser quand select player 1 possède 3 pions alignés
    if select_player == 1:                              #l'UTILISATEUR joue
        print("Dans quelle colonne souhaitez-vous jouer ?")
        c = int(input())
        li = compteur


        if grille[li][c] == ' ':
            grille[li][c] = 'X'
        else:
            while grille[li][c] != ' ':
                li -= 1
            if grille[li][c] == ' ':
                grille[li][c] = 'X'
        select_player = 2
        if puissance4(grille) == 1 :
            print_mat(grille)
            if analyse_partie_nulle(grille) == 1:
                print("Partie nulle")
            else:
                print(" Félicitations, vous avez gagné la partie ! ")
                step = "end"
            select_player = 0

    if select_player == 2:
        nbre_alea = randint(1, 7)
        li = compteur                           # si il est possible de briser une possibilité de faire 4
        out = 0                                 # active la fonction et si celle ci ne fait rien renvoie FALSE
        decision = 0

        if IA_brise_horizontal(grille) == False and IA_brise_vertical(grille) == False and \
            IA_brise_diagonal(grille) == False:

            if grille[li][nbre_alea] == ' ':                #si la case de la ligne6 est libre imprime 'O'
                grille[li][nbre_alea] = 'O'

            else:
                while grille[li][nbre_alea] != ' ' and out == 0:        # sinon remonte de ligne
                    if li == 0:                                         # si la li = ligne1
                        if grille[0][nbre_alea]==' ':
                            out = 1
                            decision = 0  # l'IA remplit la colonne
                        else :
                            out = 1
                            decision = 1  # l'IA va rechercher d'autres colonnes libres
                    else:
                        li -= 1

                if li == 0:
                    #print("Decision : "+str(decision))
                    if decision == 0 :
                        grille[li][nbre_alea] = 'O'
                        #print("COLONNE MAINTENANT PLEIN")
                    else :
                        #print("RECHERCHE D'AUTRES COLONNES VIDES")
                        colonne_plein()
                else:
                    if grille[li][nbre_alea] == ' ':
                        grille[li][nbre_alea] = 'O'

        select_player = 1
        print_mat(grille)
        if puissance4(grille) == 1:
            if analyse_partie_nulle(grille) == 1:
                print("Partie nulle")
            else:
                print(" L'intelligence artificielle vous a battu ! ")
                step = "end"
            select_player = 0






while step == 3:                                #NIVEAU 3 L'IA doit bloquer l'autre joueur et gagner quand c'est possible
    if select_player == 1:                      #l'UTILISATEUR joue
        print("Dans quelle colonne souhaitez-vous jouer ?")
        c = int(input())
        li = compteur
        # faire une fonction casse
        #
        if grille[li][c] == ' ':
            grille[li][c] = 'X'  #
        else:  #
            while grille[li][c] != ' ':
                li -= 1
            if grille[li][c] == ' ':
                grille[li][c] = 'X'
        select_player = 2
        if puissance4(grille) == 1 :
            print_mat(grille)
            if analyse_partie_nulle(grille) == 1:
                print("Partie nulle")
            else:
                print(" Félicitations, vous avez gagné la partie ! ")
                step = "end"
            select_player = 0



    if select_player == 2:
        nbre_alea = randint(1, 7)
        li = compteur
        out = 0
        decision = 0                                 #ANALYSE toute les fonction et regarde leurs sorties

        if IA_brise_horizontal(grille) == False and IA_brise_vertical(grille) == False and \
            IA_brise_horizontal(grille) == False and IA_brise_vertical(grille) == False and \
            IA_brise_diagonal(grille) == False and IA_gagnant_horizontal(grille) == False \
            and IA_gagnant_vertical(grille) == False and IA_gagnant_diagonal(grille) == False:
            if grille[li][nbre_alea] == ' ':
                grille[li][nbre_alea] = 'O'

            else:
                while grille[li][nbre_alea] != ' ' and out == 0:                        #même procéder qu'auparavant
                    if li == 0:
                        if grille[0][nbre_alea] == ' ':
                            out = 1
                            decision = 0  # l'IA remplit la colonne
                        else:
                            out = 1
                            decision = 1  # l'IA va rechercher d'autres colonnes libres
                    else:
                        li -= 1

                if li == 0:
                    # print("Decision : "+str(decision))
                    if decision == 0:
                        grille[li][nbre_alea] = 'O'
                        # print("COLONNE MAINTENANT PLEIN")
                    else:
                        # print("RECHERCHE D'AUTRES COLONNES VIDES")
                        colonne_plein()
                else:
                    if grille[li][nbre_alea] == ' ':
                        grille[li][nbre_alea] = 'O'

        select_player = 1
        print_mat(grille)
        if puissance4(grille) == 1 :
            if analyse_partie_nulle(grille) == 1:
                print("Partie nulle")
            else:
                print("L'intelligence artificielle vous a battu !")
                step = "end"
            select_player = 0


                                                #DOCSTRING:
while step == 4:                            #NIVEAU 4 casse quand l'utilisateur aligne "XX" en horizontale et verticale
    if select_player == 1:                      # + niveau 2 et niveau 3
        print("Dans quelle colonne souhaitez-vous jouer ?")
        c = int(input())
        li = compteur
        # faire une fonction casse
        #
        if grille[li][c] == ' ':
            grille[li][c] = 'X'  #
        else:  #
            while grille[li][c] != ' ':
                li -= 1
            if grille[li][c] == ' ':
                grille[li][c] = 'X'
        select_player = 2
        if puissance4(grille) == 1 :
            print_mat(grille)
            if analyse_partie_nulle(grille) == 1:
                print("Partie nulle")
            else:
                print(" Félicitations, vous avez gagné la partie ! ")
                step = "end"
            select_player = 0



    if select_player == 2:
        nbre_alea = randint(1, 7)
        li = compteur
        out = 0
        decision = 0                                 #ANALYSE toute les fonction et regarde leurs sorties

        if IA_brise_horizontal(grille) == False and IA_brise_vertical(grille) == False and \
            IA_brise_horizontal(grille) == False and IA_brise_vertical(grille) == False and \
            IA_brise_diagonal(grille) == False and IA_gagnant_horizontal(grille) == False and \
            IA_gagnant_vertical(grille) == False and IA_gagnant_diagonal(grille) == False and \
            niv4_brise_horizontal(grille) == False and niv4_brise_vertical(grille) == False:
            if grille[li][nbre_alea] == ' ':
                grille[li][nbre_alea] = 'O'

            else:
                while grille[li][nbre_alea] != ' ' and out == 0:                        #même procéder qu'auparavant
                    if li == 0:
                        if grille[0][nbre_alea] == ' ':
                            out = 1
                            decision = 0  # l'IA remplit la colonne
                        else:
                            out = 1
                            decision = 1  # l'IA va rechercher d'autres colonnes libres
                    else:
                        li -= 1

                if li == 0:
                    # print("Decision : "+str(decision))
                    if decision == 0:
                        grille[li][nbre_alea] = 'O'
                        # print("COLONNE MAINTENANT PLEIN")
                    else:
                        # print("RECHERCHE D'AUTRES COLONNES VIDES")
                        colonne_plein()
                else:
                    if grille[li][nbre_alea] == ' ':
                        grille[li][nbre_alea] = 'O'

        select_player = 1
        print_mat(grille)
        if puissance4(grille) == 1 :
            if analyse_partie_nulle(grille) == 1:
                print("Partie nulle")
            else:
                print("L'intelligence artificielle vous a battu !")
                step = "end"
            select_player = 0

