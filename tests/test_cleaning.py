# Importation de pytest pour écrire et exécuter les tests unitaires
import pytest

# Importation des fonctions à tester depuis le module src.cleaning
from src.cleaning import clean_name, clean_email, clean_phone, clean_birthdate, clean_customer_data      

# Autres packages nécessaires                    
import pandas as pd
import os
import datetime


# 1.    Test de la fonction clean_name :

#  Vérifions que la fonction clean_name corrige les majuscules et les espaces superflus

def test_clean_name():
    assert clean_name("  john DOE ") == "John Doe"               # "  john DOE " devient "John Doe". Ce test s’assure que la fonction met la bonne casse 
                                                                 # (majuscule en début de mot) et supprime les espaces avant/après.


# 2.    Test de la fonction clean_email: 

# a.    cas d'un email bien formé mais avec des majuscules et des espaces :
def test_clean_email_valid():
    assert clean_email("  MARIE.CURIE@science.org  ") == "marie.curie@science.org"                   # "  MARIE.CURIE@science.org  " devient "marie.curie@science.org"


# b.    email mal formé (pas de "@"), on s’attend à une erreur
def test_clean_email_invalid():
    with pytest.raises(ValueError):
        clean_email("jane_smith@gmail")                # pas de ".com", donc invalide . Ce test vérifie que la fonction détecte un email invalide et lève une exception propre 
                                                       # (ValueError), plutôt que de planter silencieusement.


# 3.    Test de la fonction clean_phone avec:
# a.     un numéro valide :

def test_clean_phone_valid():
    assert clean_phone("06 12 34 56 78") == "0612345678"        # Ce test montre que la fonction supprime tous les caractères non numériques et retourne un numéro nettoyé et utilisable.


# b.    Numéro trop court:
def test_clean_phone_invalid():
    with pytest.raises(ValueError):
        clean_phone("123")                       # moins de 10 chiffres

# Ce test vérifie que la fonction ne laisse pas passer un numéro invalide et protège les données en levant une erreur si besoin.

# 4.    Test de clean_birthdate():
# a.    Test d'une date de naissance bien formatée:

def test_clean_birthdate_valid():
    
    assert clean_birthdate("25/12/1985") == datetime.date(1985, 12, 25)             # "25/12/1985" converti en objet date (datetime.date)


# b.    Test d'une date mal formée:

def test_clean_birthdate_invalid():
    
    assert clean_birthdate("invalid-date") is None                                  # "invalid-date" doit retourner None


# 5.    Test de la fonction clean_customer_data():

# Test d'intégration de la fonction qui lit, nettoie et sauvegarde le fichier complet:

def test_clean_customer_data(tmp_path):

    # 1. Créer un petit CSV brut
    input_file = tmp_path / "test_input.csv"
    output_file = tmp_path / "test_output.csv"

    # 2. Contenu simulé avec erreurs à nettoyer
    input_file.write_text(
        "name,email,phone,birthdate\n"
        "  john DOE , JOHN@MAIL.COM , 06 12 34 56 78 , 01/01/1990\n"
        "alice smith, alice[at]example.com , 123 , 99/99/9999\n"
    )

    # 3. Appel de la fonction de nettoyage
    clean_customer_data(str(input_file), str(output_file))

    # 4. Vérification du fichier de sortie
    df = pd.read_csv(output_file, dtype=str)

    # 1 seule ligne correcte (la deuxième est invalide)
    assert len(df) == 1
    assert df.iloc[0]["name"] == "John Doe"
    assert df.iloc[0]["email"] == "john@mail.com"
    assert df.iloc[0]["phone"] == "0612345678"
    assert df.iloc[0]["birthdate"] == "1990-01-01"


# Ce test vérifie:
    # Qu’on peut lire un vrai fichier CSV brut 
    # Que la fonction nettoie chaque ligne
    # Que les lignes invalides sont ignorées
    # Que la sortie est propre, prête pour l’analyse ou chargemen