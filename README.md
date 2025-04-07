# Customer Data Cleaning Pipeline

Un projet complet de Data Engineering pour nettoyer, valider et fiabiliser des données CRM. Construit avec Python, pytest et GitHub Actions, il démontre une approche rigoureuse et automatisée du traitement de données.


![CI](https://github.com/JulWebana/customer-data-cleaning/actions/workflows/ci.yml/badge.svg)


---

## Objectifs du projet

- Nettoyer un fichier CSV de clients avec des données malformées
- Écrire un pipeline modulaire, robuste et testable
- Appliquer les bonnes pratiques de qualité logicielle (tests unitaires, couverture, CI)
- Préparer les données pour une ingestion future dans un entrepôt (ex : Snowflake, BigQuery)

---

## Structure du projet

```
customer-data-cleaning/
├── src/                                        # Module de nettoyage
│   └── cleaning.py
├── tests/                                      # Tests unitaires avec pytest 
│   └── test_cleaning.py
├── data/                                       # Données brutes et nettoyées 
│   ├── raw_customers.csv
│   └── cleaned_customers.csv
├── run_cleaning.py                             # Script principal de traitement 
├── requirements.txt                            # Dépendances du projet 
├── .gitignore
└── .github/
    └── workflows/                              # Workflow GitHub Actions CI 
        └── ci.yml
```
       
---

## Commençons par lancer le projet localement

1. **Cloner le projet**

```bash
git clone https://github.com/ton-utilisateur/customer-data-cleaning.git
cd customer-data-cleaning

```
2. **Installer les dépendances**

```bash
pip install -r requirements.txt

```
---

3. **Lancer le nettoyage des données**

```bash
python run_cleaning.py                  # Un fichier cleaned_customers.csv sera généré dans le dossier data/.

```
---

4. **Exécution des tests**

```bash
python -m pytest --cov=src tests/

```
---

5.  **Exemple de données**

***Entrée (raw_customers.csv)***

```csv
name,email,phone,birthdate
  JOHN DOE , JOHN@MAIL.COM , 06 12 34 56 78 , 01/01/1990
Alice Smith, alice[at]example.com , 123 , 99/99/9999

```

***Sortie (cleaned_customers.csv)***

```csv
name,email,phone,birthdate
John Doe,john@mail.com,0612345678,1990-01-01

```

---

## Intégration Continue

Les tests sont automatiquement exécutés à chaque push grâce à GitHub Actions. 
Voir l’onglet Actions du dépôt.

---

**Auteur**

Projet réalisé par Julien T.W AGA dans le cadre de ma montée en compétence en Data Engineering & Data Analytics.

LinkedIn : https://www.linkedin.com/in/julien-t-webana-aga-408256143

