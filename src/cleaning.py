import pandas as pd
import re               #expressions régulières pour valider et nettoyer des chaînes de caractères


# Nettoyage des noms : suppression des espaces superflus + mise en majuscule 1ère lettre

def clean_name(name):
    if not name:                # Si le champ est vide ou None
        return None
    
    return " ".join(part.capitalize() for part in name.strip().split())      # On découpe le nom en mots, on met chaque mot en Capitalized, puis on les rejoint avec un espace


# Nettoyage des emails : suppression des espaces + conversion en minuscules + validation du format

def clean_email(email):
    if not email:                                                                      # Si le champ est vide ou None    
        return None
    
    email = email.strip().lower()                                                      # On enlève les espaces et on met en minuscules


# Vérifions que l'email a un format basique valide (texte@texte.domaine)

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format")                                         # Si le format n'est pas valide, on lève une exception
    return email

# Nettoyage des numéros de téléphone : suppression de tous les caractères non numériques + validation longueur

def clean_phone(phone):
    if not phone:
        return None
    
 # On supprime tout sauf les chiffres (ex: espaces, tirets, +33, etc.)

    digits = re.sub(r"\D", "", phone)                                                   # ne garder que les chiffres
    if len(digits) < 10:                                                                # On considère qu’un numéro valide contient au moins 10 chiffres
        raise ValueError("Invalid phone number")
    return digits


# Nettoyage de la date de naissance : conversion en format date standard, supporte jour/mois/année

def clean_birthdate(birthdate_str):
    try:
        return pd.to_datetime(birthdate_str, dayfirst=True).date()            # On convertit la chaîne en date, en considérant le format jour/mois/année    (format europeéen)
    except Exception:
        return None  # retourne None si le format est invalide



# Fonction principale : qui lit le fichier CSV brut, applique le nettoyage sur chaque ligne, et sauvegarde le fichier propre


def clean_customer_data(csv_input_path, csv_output_path):

    df = pd.read_csv(csv_input_path)                                         # lecture du fichier brut

    cleaned_rows = []                                                        # On prépare une liste pour stocker les lignes nettoyées

    for _, row in df.iterrows():                                             # On itère sur chaque ligne du DataFrame
        try:
            cleaned_rows.append({                                            # Nettoyage champ par champ pour chaque ligne
                'name': clean_name(row['name']),
                'email': clean_email(row['email']),
                'phone': clean_phone(row['phone']),
                'birthdate': clean_birthdate(row['birthdate'])
            })

        except Exception as e:
            # Log en cas d'erreur de nettoyage pour une ligne
            print(f"Erreur lors du nettoyage de la ligne : {row} → {e}")      # Si une erreur survient pendant le nettoyage, on affiche la ligne concernée et le message d'erreur

    cleaned_df = pd.DataFrame(cleaned_rows)                                   # recrée un DataFrame avec les données nettoyées

    cleaned_df.to_csv(csv_output_path, index=False)                           # sauvegarde dans un nouveau fichier CSV

    print(f"Données nettoyées sauvegardées dans : {csv_output_path}")         # Message de confirmation de la sauvegarde
