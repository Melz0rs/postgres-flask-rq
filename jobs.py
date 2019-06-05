import psycopg2
import json
from psycopg2.extras import RealDictCursor
from logger import get_logger

logger = get_logger()


def add_person_to_db(person):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="example", host="postgres")
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    query = f"INSERT INTO Persons (first_name, age) VALUES (%s, %s) RETURNING *"

    cursor.execute(query, (person['name'], person['age']))

    result = cursor.fetchone()

    logger.info(f"result: {result}")

    conn.commit()

    conn.close()
    cursor.close()

    return json.dumps(result)

