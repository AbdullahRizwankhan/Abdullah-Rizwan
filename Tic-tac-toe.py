import random


#pour la grille 3*3
grille=[" "]*3*3
#fabrication de tableau
points="............."
def fabric_tableau():
    print("|",grille[0],"|",grille[1],"|",grille[2],"|")
    print(points)
    print("|",grille[3],"|",grille[4],"|",grille[5],"|")
    print(points)
    print("|",grille[6],"|",grille[7],"|",grille[8],"|")
    print(points)
fabric_tableau()




#La fonction de vérification du gagnant consiste à vérifier le gagnant. Dans cette fonction, je donne trois conditions de victoire, une horizontalement, une verticalement et une en diagonale. Cette fonction fera donc correspondre les trois symboles consécutifs du joueur ou de la machine dans chaque direction pour décider du gagnant. Si personne entre le joueur et la machine ne peut répondre à ces conditions, le match sera nul qui je écrit dans la fonction de la machine.
def verification_du_gagnant(symbole):
    #pour horizonatale ligne
    for i in range(0,9,3):
        if grille[i]==grille[i+1]==grille[i+2]==symbole:
            return True
    #pour verticale ligne

    for i in range(3):
        if grille[i]==grille[i+3]==grille[i+6]==symbole:
            return True
    #pour diagonale ligne
    if grille[0]==grille[4]==grille[8]==symbole or grille[2]==grille[4]==grille[6]==symbole:
        return True
    return False
#la fonction joueur est destinée au joueur qui a le choix entre 0 et 8 pour décider dans quelle ligne de jeu il veut ajouter son symbole
#J'ai utilisé la boucle while avec true dans le but que le jeu ne s'arrête pas si quelqu'un entre une mauvaise commande
def joueur():
    while True:
        try:
            position_j=(int(input("veuillez entrer un nombre entier pour mouvement entre 0 et 8:")))
            if position_j< 0 or position_j >8:
                print("invalide nombre, veuillez entrer un nombre pour mouvement entre 0 et 8:")
            elif grille[position_j]!=" ":
                print("cette case est deja occupée,veuillez choisir un autre case")
            else:
                grille[position_j] = joueur_h
                fabric_tableau()
                if verification_du_gagnant(joueur_h):
                    print("félicitation, vous avez gagné")
                    return True
                break
        except ValueError:
            print("invalide command","veuillez entrer un nombre entier entre 0-8")
             

#La fonction tour de machine est destinée à la machine qui peut choisir son nombre au hasard grace à la fonction builtin random.choice .
def tour_de_machine():
    disponible_mouvement=[i for i in range(9) if grille[i]==" "]
    if len(disponible_mouvement) > 0:
        position_m=random.choice(disponible_mouvement)
        grille[position_m]= joueur_m
        fabric_tableau()
        if verification_du_gagnant(joueur_m):
            print("désolé vous avez perdu")
            return True
    else:
        print("le match est nul")
        return True
    return False
   


  
  

def main():
    print("Tic toe Toe")
    fabric_tableau()
    while True:
        if joueur():
            break
        if tour_de_machine():
            break
joueur_h="x"
joueur_m="o"

main()









