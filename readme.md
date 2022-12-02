Projet disponible sur [github](https://github.com/AlanBlanchet/SantePubliqueFrance)

# Introduction

- Auteur                : Alan Blanchet
- Ecole                 : OpenClassrooms
- Mentor Ecole          : Chemseddine Nabti
- Tuteur entreprise     : Nicolas Grosjean

# Installation

Récupérer le fichier de données [ici](https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/parcours-data-scientist/P2/fr.openfoodfacts.org.products.csv.zip) et le mettre dans le `root` du projet

Lancer la commande (nécessite [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html))

```bash
conda install --file requirements.yml
```


# Execution

Utiliser les notebooks [`nettoyage.ipynb`](nettoyage.ipynb) et  [`analyse.ipynb`](analyse.ipynb) dans l'ordre.

# Présentation du projet

On le sait bien, chaque pays inscrit dans la globalisation possède des importations et des exportations de produit consommables.
La consommation d'un produit résultant d'une demande de la part des consommateur, il est donc possible d'analyser la consommation des citoyens d'un pays.

Le projet suivant consiste à effectuer plusieurs analyses de pays suivant son alimentation. On espère pouvoir proposer à un utilisateur de visiter un pays en fonction de son style d'alimentation

Une personne qui aime la bonne nourriture et être en bonne santée aimerais probablement voyager dans un pays qui propose de la nourriture avec un nutriscore correcte. Donc A ou B.

Ainsi l'application proposera à cet utilisateur des pays en fonction de son alimentation, ainsi que des recommendations sur les produits à consommer pendant son voyage.

# Présentation

[Lien Microsoft Office Live](https://1drv.ms/p/s!AmnxN1b1Hzwklukjr90-CRvepBB-Zw?e=PAVIiB)