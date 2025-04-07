# Ce script est utilisé pour exécuter le processus de nettoyage des données sur les données des clients.

from src.cleaning import clean_customer_data


input_file = "data/raw_customers.csv"
output_file = "data/cleaned_customers.csv"

clean_customer_data(input_file, output_file)
