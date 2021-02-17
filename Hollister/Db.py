import mysql.connector


# Connexion à la base de données Fastocks
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Dubai007::", database="fastocks"
)

# Préparation d'une tâche
mycursor = mydb.cursor()

# Insertion de valeurs dans la table hollister
def Insertion(val):
    sql = "INSERT INTO hollister (gender, size, id_product, name_product) VALUES (%s, %s, %s, %s)"

    mycursor.executemany(sql, val)

    mydb.commit()


# Visualisation des valeurs de la table hollister
def Visualisation():
    mycursor.execute("SELECT gender, size, id_product, name_product FROM hollister")

    myresult = mycursor.fetchall()

    return myresult


# Test unitaire fonction insertion
"""
val = [
        ("F", 'L', 41328322, 'doudoune-effet-col-montant-41328322')
    ]
Insertion(val)
"""

# Test unitaire fonction visualisation
"""
test = Visualisation()
print(test)
"""
