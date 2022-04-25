import sqlite3


def db_connect(query):
    connection = sqlite3.connect('netflix.db')
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    return result


def get_actors(name1='Rose McIver', name2='Ben Lamb'):
    query = f"""
            SELECT
                "cast"
            FROM netflix
            WHERE "cast" LIKE '%{name1}%'
                AND "cast" LIKE '%{name2}%'
        """
    response = db_connect(query)
    actors = []
    for cast in response:
        actors.extend(cast[0].split(', '))
    result = []
    for a in actors:
        if a not in [name1, name2]:
            if actors.count(a) > 2:
                result.append(a)

    result = set(result)
    print(result)


get_actors()
