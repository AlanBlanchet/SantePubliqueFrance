import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import utils.countriesMap as cm
import re

data = pd.read_csv("fr.openfoodfacts.org.products.csv", sep="\t")

# Conservation des données utiles
data = data.filter(
    [
        "url",
        "product_name",
        "generic_name",
        "quantity",
        "packaging",
        "packaging_tags",
        "countries_tags",
        "image_url",
        "image_small_url",
        "nutrition-score-fr_100g",
    ],
    axis=1,
)

# -------------
# generic_name

# On conserve les non null
generic_exists = data["generic_name"].notna()
# On conserve les lignes qui ne contiennent pas uniquement des espaces
generic_no_space = data["generic_name"].ne(" ")
# On conserve les noms en dessous de 50 caractères
generic_not_long = data["generic_name"].str.len() < 50
# Test booléen
generic = generic_exists & generic_no_space & generic_not_long
# Table qui contient les éléments qui respectent les critères précédents
generic_match = data.loc[generic, ["generic_name"]]

# -------------
# product_name

# Retirer les nulls
product_exists = data["product_name"].notna()
# Table qui contient les éléments qui respectent les critères précédents
product_match = data.loc[product_exists, ["product_name"]]

# Colonnes qui ne contiennent pas de product_name mais contiennent un generic_name
no_product_with_generic = (~product_exists) & generic

# Remplacer les product_name non valide par son generic_name valide dans data
data.loc[no_product_with_generic, ["product_name"]] = data.loc[
    no_product_with_generic, ["generic_name"]
]

# On peut désormait retirer generic_name qui n'est plus d'aucune utilité
data.drop(["generic_name"], axis=1, inplace=True)


# Nettoyage des Pays
countries_tags_count = data["countries_tags"].value_counts()

# On récupère toutes les valeurs possibles de tags et on en garde 1 seul exemplaire
all_countries = (
    pd.DataFrame(countries_tags_count.index.str.split(",")).explode(0).drop_duplicates()
)
# Il y a des pays qui ne contiennent pas le string ":". Ce ne sont donc pas des pays
all_countries = all_countries.loc[all_countries[0].str.contains(":")]
# On retire les préfixes
all_countries[0].replace("^.*:", "", regex=True, inplace=True)
# Cela peut entrainé des doublons, par exemple fr:france et en:france => france et france
all_countries.drop_duplicates(inplace=True)


def map_country(c_list):
    c_list = list(map(lambda y: re.sub("^.*:", "", y), c_list))
    try:
        # On map le nom de pays dans la langue inconnue à son pays en français
        c_list = list(map(lambda y: cm.countries[y], c_list))
    except:
        return np.NaN
    return ",".join(c_list)


# Tous les pays définis
defined_countries = ~data["countries_tags"].isna()
# On créer une colonne "countries" dans laquelle on met le mapping de leur tag "countries_tags"
data.loc[defined_countries, "countries"] = (
    data.loc[defined_countries, "countries_tags"].str.split(",").apply(map_country)
)

# Maintenant que le traitement est effectué, on peut supprimer "countries_tags"
data.drop("countries_tags", axis=1, inplace=True)
# Retirer les lignes qui n'ont pas de pays
defined_countries = ~data["countries"].isna()
data = data.loc[defined_countries]
