# -*- coding: utf-8 -*-

def calcul_taux(donnee: str) -> str:
  """
  Si la sequence est valide,
  Renvoie le taux de GC du parametre sequence_ADN,
  Sinon renvoie un message d'erreur.
  """
  compteur_A, compteur_T, compteur_G, compteur_C, compteur_N = 0,0,0,0,0
  taux_GC = 0

  for sequence_ADN in donnee:
    sequence_ADN1 = sequence_ADN.upper() # Met tout en majuscule
    sequence_ADN2 = sequence_ADN1 # Cas normal

    if not sequence_ADN1[-1] in "ATGCNRYMKWS":
      sequence_ADN2 = sequence_ADN1[:-1]  # Enleve un eventuel /n
    
    if len(sequence_ADN2) == 1: # Si ligne vide
        compteur_A += 0
        compteur_C += 0
        compteur_G += 0
        compteur_T += 0

    for nucleotide in sequence_ADN2:
      if not nucleotide in "ATGCNRYMKWS":
        # Si caractère différent d'un nucléotide
        message = "Sequence non valide, veuillez reessayer."
        return message

      else:
        if nucleotide == "C":
          compteur_C += 1
        elif nucleotide == "G":
          compteur_G += 1
        elif nucleotide == "A":
          compteur_A += 1
        elif nucleotide == "T":
          compteur_T += 1
        elif nucleotide == "N":
          compteur_N += 1
    nb_GC = compteur_C + compteur_G
    nb_total =  compteur_C + compteur_G + compteur_A + compteur_T + compteur_N
    taux_GC = (nb_GC / nb_total) * 100
  
  
  resultat = ""
  resultat += str(nb_total) + "\t" + str(taux_GC) +"\n"

  return resultat
  # Renvoie un str contenant la longueur du chromosome et le taux de GC


# On teste avec n'importe quel fichier
doc = input("Entrez le chemin d'accès du fichier à ANALYSER: ")
doc+="." # Aucun besoin de mettre le point dans le chemin d'accès désormais
doc2 = input("Entrez le chemin d'accès du fichier sur lequel ENREGISTRER les résultats: ")
doc2+="." # Aucun besoin de mettre le point dans le chemin d'accès désormais
file_seq = open(doc,"r")
file_donnee = open(doc2, "a")

analyse = file_seq.readlines()
result = calcul_taux(analyse[1:]) # On exclue la première ligne du fichier FASTA

file_donnee.write(result) 
print(result)


file_donnee.close()
file_seq.close()