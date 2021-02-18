def FormateurUrl(url):
    # Nom brut du produit
    decomposition_1 = url.split("/")
    index_ref = decomposition_1.index("p") + 1
    decomposition_2 = decomposition_1[index_ref].split("?")
    product_name_brut = decomposition_2[0]
    # Nom et ID du produit
    decomposition_2_bis = product_name_brut.split("-")
    taille_liste = len(decomposition_2_bis)
    product_name = ""
    if len(decomposition_2_bis[taille_liste - 1]) == 1:
        id_product = decomposition_2_bis[taille_liste - 2]
        for x in range(0, taille_liste - 2):
            if x == taille_liste - 3:
                product_name += decomposition_2_bis[x]
            else:
                product_name += decomposition_2_bis[x] + "-"
    else:
        id_product = decomposition_2_bis[taille_liste - 1]
        for x in range(0, taille_liste - 1):
            if x == taille_liste - 2:
                product_name += decomposition_2_bis[x]
            else:
                product_name += decomposition_2_bis[x] + "-"

    # ID de la catégorie du produit
    decomposition_3 = decomposition_2[1].split("=")
    index_categoryid = decomposition_3.index("categoryId") + 1
    category_id_brut = decomposition_3[index_categoryid]
    decomposition_3_bis = category_id_brut.split("&")
    id_category = decomposition_3_bis[0]

    return [product_name_brut, product_name, id_product, id_category]


# Tests Unitaires
'''
url = "https://www.hollisterco.com/shop/eu-fr/p/sweat-à-capuche-zippé-tie-dye-oversize-44492320?categoryId=85265&seq=02&faceout=model1"
test = FormateurUrl(url)
print(test)
'''