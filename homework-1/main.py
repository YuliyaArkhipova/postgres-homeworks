"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="123456"
) as connection:

    with connection.cursor() as cursor:
        with open (f'north_data/employees_data.csv') as csv_file:
            header = next(csv_file)
            reader = csv.reader(csv_file)
            for row in reader:
                cursor.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
        with open (f'north_data/customers_data.csv') as csv_file:
            header = next(csv_file)
            reader = csv.reader(csv_file)
            for row in reader:
                cursor.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
        with open (f'north_data/orders_data.csv') as csv_file:
            header = next(csv_file)
            reader = csv.reader(csv_file)
            for row in reader:
                cursor.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)

connection.close()



