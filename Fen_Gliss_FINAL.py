# -*- coding: utf-8 -*-

def calcul_GC(document, pas: int, fen: int) -> list:
    """
    Si la sequence est valide,
    Renvoie le taux de GC du parametre sequence_ADN,
    (Via fenêtre glissante), 
    Avec pour pas et la taille de la fenêtre,
    Les paramètres de la fonction: pas et fen.
    Sinon renvoie un message d'erreur.
    """
    # Pour utiliser la fenêtre glissante, on va regrouper l'ensemble du fichier en une ligne.
    # Cette ligne sera alors sectionnée en plusieurs parties via la fenêtre glissante.

    liste_resultat = ["Taux GC (%)\t Position\n"] 
    # Liste vide pour y stocker les résultats de chaque fenêtre  
    file = open(document,"r")
    # Ouverture du document donné en paramètre de la fonction
    lignes = file.readlines()
    # Renvoie une liste de toutes les lignes du document
    seq_totale = ""
    # Str vide qu'on concatènera avec chaque élément dans lignes.
    # Le tout formera une seule ligne, afin de la séparer en plusieurs fenêtres
    A, C, T, G, N = 0,0,0,0,0
    # Compteur pour chaque type de nucléotide (N désigne un nucléotide non séquencé)


    for indice_ligne in range (1, len(lignes)): 
        # On explore chaque ligne dans lignes sauf la première
        seq_maj = lignes[indice_ligne].upper()
        # Chaque ligne comporte désormais que des caractères en majuscule
        seq_normale = seq_maj.replace("\n","")
        # On enlève \n dans chaque ligne en le remplaçant par un Str vide
        seq_totale += seq_normale
        # Concaténation en une seule ligne de tous éléments dans le document

    for bond in range(0, len(seq_totale), pas):
        # bond va de 0 au dernier indice de seq_totale de pas en pas
        last_fen = bond+fen 
        # Définition de notre fenêtre glissante
        if last_fen > len(seq_totale):
            # Si il y a effet de bord
            last_fen = bond + (len(seq_totale)-bond)
            # Alors on réduit la taille de notre fenêtre glissante

        for ind_nuc in range(bond,last_fen):
                if not seq_totale[ind_nuc] in "ATGCNRYMKWS":
                    # Si l'élément ne figure pas parmi ATGCN
                    message = "Erreur dans la séquence !"
                    return message
                    # Alors on renvoie un message d'erreur
                else:
                    # Sinon, si l'élément correspond à un des nucléotides,
                    # On incrémente son compteur respectif
                    if seq_totale[ind_nuc]=="A":
                        A+=1
                    elif seq_totale[ind_nuc]=="C":
                        C+=1
                    elif seq_totale[ind_nuc]=="T":
                        T+=1
                    elif seq_totale[ind_nuc]=="G":
                        G+=1
                    elif seq_totale[ind_nuc]=="N":
                        N+=1
        
        nb_gc = G+C # Somme de G et de C
        nb_total= A+T+G+C+N # Somme totale des compteurs de nucléotides
        txgc = (nb_gc/nb_total)*100 # Calcul du taux de GC
        A,T,G,C,N = 0,0,0,0,0 # Réinitialisation des compteurs
        resultat = str(txgc)+"\t"+str(last_fen)+"\n"
        # On réunit le taux de GC, le nombre total et de GC dans une variable
        liste_resultat.append(resultat)
        # Le résultat donnée par la fenêtre est enregistrée dans une liste

        if bond+fen > len(seq_totale):
            break # Si il y a effet de bord, on sort de la boucle

    file.close()    # Fermeture du fichier 
    return liste_resultat # On renvoie la liste de résultats de chaque fenêtre


# On teste avec n'importe quel fichier
doc = input("Entrez le chemin d'accès du fichier à ANALYSER: ")
doc+="." # Aucun besoin de mettre le point dans le chemin d'accès désormais
doc2 = input("Entrez le chemin d'accès du fichier sur lequel ENREGISTRER les résultats: ")
doc2+="." # Aucun besoin de mettre le point dans le chemin d'accès désormais

p = int(input("Entrez le PAS de la fenêtre: "))
f = int(input("Entrez la TAILLE de la fenêtre: "))
file_donnee = open(doc2, "w")
analyse = calcul_GC(doc,p,f)

for element in analyse:
    file_donnee.write(element) # On met nos résultats dans un fichier txt
print(analyse)

file_donnee.close()