from vecteur import vecteur
from distance import distance
from vecteur import vecteur
from verificateur_type import verificatueur

while(True):

    try:
        # distance
        print("Calcule Distance")
        recuperateur_des_valeurs_pour_distance = verificatueur()
        xA = recuperateur_des_valeurs_pour_distance[0]
        yA = recuperateur_des_valeurs_pour_distance[1]
        xB = recuperateur_des_valeurs_pour_distance[2]
        yB = recuperateur_des_valeurs_pour_distance[3]
        responses = distance(xA , yA ,xB ,yB)
        print(responses[0])
        print(responses[1])


        # vecteur 
        print("Calcule vecteur")
        recup_vecteur = verificatueur()
        xA = recup_vecteur[0]
        yA = recup_vecteur[1]
        xB = recup_vecteur [2]
        yB = recup_vecteur[3]
        reponse_vecteur = vecteur(xA , xB ,yA , yB)
        print("vecteur",reponse_vecteur)

    except ValueError:
        print("La valeur qui vous avez entré n'est pas une valeur entière ou décimale")