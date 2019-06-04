import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="example", host="postgres")
cursor = conn.cursor()


def add_person_to_db(person):
    cursor.execute("INSERT INTO Persons(name, age) VALUES (%s, %s)", (person.name, person.age))
