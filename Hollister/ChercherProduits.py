import requests
import urllib3
import time
import random
from Db import Visualisation


# Désactivation des messages d'avertissement
urllib3.disable_warnings()


def ChercherProduits(product_dict, id_category, list_ref, list_sizes):
    # Configuration du header
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "fr-fr",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
        "Connection": "keep-alive",
    }

    # Requètes de Recherche par taille
    phase = 0
    for x in list_sizes:
        # Avancement
        print("Recherche des produits : %s/%s" % (phase, len(list_sizes)))

        # Liste des id à rechercher
        id_list = []
        for product in list_ref:
            if product[0] == x:
                id_list.append([product[1], product[2]])

        # Paramètres de l'url
        x = x.split("-")
        if len(x) == 2:
            payload = {
                "catalogId": "11558",
                "facet": [
                    'ads_f43002_ntk_cs:("%s")' % x[0],
                    'ads_f43003_ntk_cs:("%s")' % x[1],
                ],
                "requestType": "category",
                "rows": "240",
                "start": "0",
                "storeId": "19158",
            }
        else:
            payload = {
                "catalogId": "11558",
                "facet": 'ads_f43002_ntk_cs:("%s")' % x[0],
                "requestType": "category",
                "rows": "240",
                "start": "0",
                "storeId": "19158",
            }

        # Accès à la page
        url_produit = (
            "https://www.hollisterco.com/api/search/h-eu-fr/search/category/%s"
            % id_category
        )
        r = requests.get(url_produit, headers=header, params=payload)

        # Récupération des dictionnaires
        rep_dict = r.json()

        # Listes produit disponibles dans la taille recherchée
        products_list = rep_dict["products"]

        # Recherche des produits
        for product in products_list:
            for id in id_list:
                if product["productSeoToken"] == "p/%s" % id[1]:
                    try:
                        product_dict[id[0]][product["swatchName"]][x[0]] = product[
                            "lowPrice"
                        ]
                    except:
                        product_dict[id[0]][product["swatchName"]] = {}
                        product_dict[id[0]][product["swatchName"]][x[0]] = product[
                            "lowPrice"
                        ]

                for y in product["swatchList"]:
                    if y["productId"] == id[0]:
                        try:
                            product_dict[id[0]][product["swatchName"]][x[0]] = product[
                                "lowPrice"
                            ]
                        except:
                            product_dict[id[0]][product["swatchName"]] = {}
                            product_dict[id[0]][product["swatchName"]][x[0]] = product[
                                "lowPrice"
                            ]

        # Avancement
        phase += 1
        print("Recherche des produits : %s/%s" % (phase, len(list_sizes)))

        # Fin de tâche
        if id_category == "85265" and phase == len(list_sizes):
            return product_dict

        # Ralentissement du processus (sécurités anti-bot)
        else:
            print("Début Pause")
            list_time = [
                30,
                33.5,
                43,
                32.2,
                40,
                32.1,
                36.1,
                33.1,
                30.8,
                37.1,
                41.2,
                32.33,
                32.3133,
                30.322,
                37.324,
                31.322,
                37.032,
                38.900,
                30.32213,
                33.0,
            ]
            time_sleep = random.choice(list_time)
            time.sleep(time_sleep)
            print("Pause - Terminée")

    return product_dict


def HollisterScraper():
    # Homme
    category_homme = "85264"
    list_sizes_h = []
    list_products_h = []

    # Femme
    category_femme = "85265"
    list_sizes_f = []
    list_products_f = []

    # Connexion à la base de données et récupération des informations
    db = Visualisation()

    # Produits et tailles à rechercher
    for x in db:
        if x[0] == "M":
            if x[1] not in list_sizes_h:
                list_sizes_h.append(x[1])
            list_products_h.append([x[1], x[2], x[3]])
        else:
            if x[1] not in list_sizes_f:
                list_sizes_f.append(x[1])
            list_products_f.append([x[1], x[2], x[3]])

    # Dictionnaire avec les données recherchées
    product_dict = {}
    for x in list_products_h:
        product_dict[x[1]] = {}
    for x in list_products_f:
        product_dict[x[1]] = {}


    # Recherche des produits hommes
    print("Début Phase 1")
    product_dict = ChercherProduits(
        product_dict, category_homme, list_products_h, list_sizes_h
    )
    print("Phase 1 - Terminée")

    # Recherche des produits femmes
    print("Début Phase 2")
    product_dict = ChercherProduits(
        product_dict, category_femme, list_products_f, list_sizes_f
    )
    print("Phase 2 - Terminée")
    print("\n")
    print(product_dict)

    return product_dict


while True:
    products_dict = HollisterScraper()
    time.sleep(300)
