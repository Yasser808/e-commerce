#produits par yasser mahzouli et said ait guaouzguit
import json


def lire_products():
    f = open("products.json", "r")
    data = json.load(f)
    f.close()
    return data


def save_products(data):
    f = open("products.json", "w")
    json.dump(data, f, indent=4)
    f.close()


def lire_cart():
    f = open("cart.json", "r")
    data = json.load(f)
    f.close()
    return data


def save_cart(data):
    f = open("cart.json", "w")
    json.dump(data, f, indent=4)
    f.close()


def show_products():
    produits = lire_products()

    print("\nPRODUITS ")

    for p in produits:
        print("ID:", p["id"], "| Nom:", p["nom"], "| Prix:", p["prix"], "DH")


def find_product_by_id(id_produit):
    produits = lire_products()

    for p in produits:
        if p["id"] == id_produit:
            return p

    return None


def show_product_by_id():
    try:
        id_produit = int(input("Entrer ID produit: "))

        produit = find_product_by_id(id_produit)

        if produit:
            print("\n===== PRODUIT =====")
            print("ID:", produit["id"])
            print("Nom:", produit["nom"])
            print("Prix:", produit["prix"], "DH")
        else:
            print("Produit introuvable")

    except:
        print("Erreur de saisie")


def add_product():
    produits = lire_products()

    try:
        nom = input("Nom du produit: ")
        prix = float(input("Prix: "))

        if len(produits) > 0:
            new_id = produits[-1]["id"] + 1
        else:
            new_id = 1

        produits.append({
            "id": new_id,
            "nom": nom,
            "prix": prix
        })

        save_products(produits)

    except:
        print("Erreur")


def add_to_cart():
    produits = lire_products()
    Panier = lire_cart()

    show_products()

    try:
        id_produit = int(input("ID produit: "))
        qte = int(input("Quantité: "))

        for p in produits:
            if p["id"] == id_produit:

                Panier.append({
                    "id": p["id"],
                    "nom": p["nom"],
                    "prix": p["prix"],
                    "qte": qte
                })

                save_cart(Panier)

                print("Ajouté au panier")
                return

        print("Produit introuvable")

    except:
        print("Erreur")


def show_cart():
    panier = lire_cart()

    print("\n PANIER ")

    if len(panier) == 0:
        print("Panier vide")
        return

    for i, p in enumerate(panier):
        print(i, "|", p["nom"], "| Prix:", p["prix"], "| Qté:", p["qte"])


def remove_from_cart():
    panier = lire_cart()

    show_cart()

    try:
        index = int(input("Index à supprimer: "))
        panier.pop(index)

        save_cart(panier)

        print("Supprimé")

    except:
        print("Erreur")


def checkout():
    panier = lire_cart()

    if len(panier) == 0:
        print("Panier vide")
        return

    total = sum(p["prix"] * p["qte"] for p in panier)

    print("\nTOTAL:", total, "DH")
    print("Commande validée")

    save_cart([])


while True:

    print("\n MENU ")
    print("1 - Produits")
    print("2 - Ajouter au panier")
    print("3 - Voir panier")
    print("4 - Retirer panier")
    print("5 - Checkout")
    print("6 - Ajouter produit")
    print("7 - Chercher produit par ID")
    print("0 - Quitter")

    choix = input("Choix: ")

    if choix == "1":
        show_products()

    elif choix == "2":
        add_to_cart()

    elif choix == "3":
        show_cart()

    elif choix == "4":
        remove_from_cart()

    elif choix == "5":
        checkout()

    elif choix == "6":
        add_product()

    elif choix == "7":
        show_product_by_id()

    elif choix == "0":
        print("Au revoir")
        break

    else:
        print("Choix invalide")