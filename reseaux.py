"""
On considère un réseau à M couches

Vim = Sortie de la i-eme unité dans la m-eme couche
    i : indice d'unité
    m: indice de couche m = 1, 2, ... M
    
wij =poids connexion de Vm-1 j à Vmu
mu : yndice de prototype

s'il y'a p prototypes mu = 1...p
On fait untrer u prototype à la fois

"""




import math
import random

prototypes = [[1, 0, 1], [0, 1, 1], [1, 1, 0]]
sorties_desirees = [[1], [1], [0]]


architecture = [3, 2, 1]

M = len(architecture) - 1


V = []
h =[]
delta =[]
w= []

#sigmoide et dérivée
def g(x):
    return 1/ (1 + math.exp(-x))

def g_prime(x):
    return g(x)*(1- g(x))


# Step 1 : Initialiser les poids à de petites valeurs aléatoires

def initialiser_poids():
    
    # Pour chaque couche
    for taille_couche in architecture:
        V.append([0.0] * taille_couche)
        h.append([0.0]* taille_couche)
        delta.append([0.0]*taille_couche)
    
    # Pour directement passer à la première couche cacher
    w.append([])

    # On commence  pas aller sur première couche la couche cachée 
    for m in range(1, M +1 ):
        poids_couche = []
        
        # Ensuite on va sur chaque neurone de cette couche
        for i in range(0,  architecture[m]):
            poids_neurone = []
            
            # Ensuite on initialise ses poids vis à vis de la couche précédente et ainsi de suite 
            for j in range(0, architecture[m - 1]):
                poids_neurone.append(random.uniform(-0.5, 0.5))
            poids_couche.append(poids_neurone)
        w.append(poids_couche)
    print("OK")
                
# Step 2 : Choix du prototype


def choix_prototype(mu):
    for k in range(architecture[0]):
        V[0][k] =prototypes[mu][k]

# step 3 : propagation du signal vers l'avant 

def propagation_avant():
    for m in range(1, M +1):
        for i in range(architecture[m]):
            h[m][i] = 0.0 
            for j in range(architecture[m-1]):
                h[m][i] += w[m][i][j]*V[m-1][j]
            V[m][i] = g(h[m][i])

def delta_sortie(mu):
        for i in range(architecture[M]):
                delta[M][i] = g_prime(h[M][i])*(sorties_desirees[mu][i] - V[M][i])

initialiser_poids()