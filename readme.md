# Installation

Récupérer le fichier de données [ici](https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/parcours-data-scientist/P2/fr.openfoodfacts.org.products.csv.zip) et le mettre dans le `root` du projet

Lancer la commande (nécessite [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html))

```bash
conda install --file requirements.yml
```

# Execution

Utiliser les notebooks `nettoyage.ipynb` et `analyse.ipynb` dans l'ordre.

# Présentation du projet

On le sait bien, chaque pays inscrit dans la globalisation possède des importations et des exportations de produit consommables.
La consommation d'un produit résultant d'une demande de la part des consommateur, il est donc possible d'analyser la consommation des citoyens d'un pays.

Le projet suivant consiste donc à effectuer plusieurs analyses de pays suivant son alimentation.
On pourra par exemple classer les pays en fonction de leur impacte sur la santé grâce au nutriscore.