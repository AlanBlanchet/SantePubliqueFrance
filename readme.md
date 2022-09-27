# Installation

Récupérer le fichier de données [ici](https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/parcours-data-scientist/P2/fr.openfoodfacts.org.products.csv.zip) et le mettre dans le `root` du projet

Lancer la commande (nécessite [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html))

```bash
conda install --file requirements.txt
```

# Execution

Utiliser le notebook `main.ipynb`

# Présentation du projet

On le sait bien, chaque pays inscrit dans la globalisation possède des importations et des exportations de produit consommables.
La consommation d'un produit résultant d'une demande de la part des consommateur, il est donc possible d'analyser la consommation des citoyens d'un pays.

Le projet suivant consiste donc à effectuer plusieurs classements de pays suivant l'alimentation ses citoyens.
On pourra par exemple classer les citoyens d'un pays en fonction de son impacte sur la santé grâce au nutriscore, l'écologie ,
