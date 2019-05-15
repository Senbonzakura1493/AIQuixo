## Auteur ##
Ben Moussa Fatine 14354

## stratégie utilisée ##
 
Le meilleur coup à jouer est défini comme étant : 

- Soit le coup me permettant d'augmenter mes chances d'arriver à un 5.

- Soit le coup me permettant de bloquer la progression de l'ennemi. 
Celui ci ayant un nombre de cubes maximal lui appartenant sur une ligne , colonne ou diagonale supérieure au nombre maximal que je possède sur une ligne,</br>
colonne ou diagonale. 

Algotithme est le suivant : 

1. Faire la somme de cube m'appartennant
        </br> - sur chaque ligne.
        </br> - sur chaque colonne.
        </br> - sur chaque diagonale.
    </br>
2. Faire de même pour l'adversaire.</br>
3. Récupérer la valeur la plus élevée pour chaque joueur.( sont également récupérées , la position et la direction des valeurs)</br>
</br>
    - ex : Valeur est 4 ==> somme maximale trouvée pour le joueur.
     </br>Direction est 0 ==> direction est horyzontale.</br>
     Position est 1 ==> désigne la deuxième horizontale donc la deuxième ligne.

4. Comparer les deux valeurs.</br> 
    -Si la valeur du joueur est supérieure à celle de l'ennemie, on joue le coup qui augmente maximum existant. On verifie les freecubes qu'on a récupéré à partir de l'état du jeu, les cubes encore neutres et on joue le cube neutre satisfaisant notre condition.</br>
    -Si la valeur de l'ennemie est supérieure à celle du joueur , on joue le coup qui empèche l'ennemie d'augmenter cette valeur.On verifie les freecubes qu'on a récupéré à partir de l'état du jeu , les cubes encore neutres et on joue le cube neutre satisfaisant notre condition.

    -Ajout du mouvement dans moves et mise à jour de l'état du jeu

## reponse de la route move ##

La route move renvoie une réponse formatter comme demandée dans l'énoncé , le message indique si on effectue un mouvement bloquant l'ennemi ou maximisant notre valeur. 