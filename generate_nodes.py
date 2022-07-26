import sqlite3

con = sqlite3.connect('nodes.db')
cur = con.cursor()


def create_table():
    cur.execute('''
    CREATE TABLE Nodes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        house_number TEXT NOT NULL,
        street_name TEXT NOT NULL,
        lon TEXT NOT NULL,
        lat TEXT NOT NULL
    );
    ''')
    create_unique_index()


def drop_table():
    cur.execute("DROP TABLE Nodes")


def insert_table(house_number, street_name, lon, lat):
    cur.execute(
        f'INSERT INTO Nodes (house_number, street_name, lon, lat) values ("{house_number}", "{street_name}", "{lon}", "{lat}")')
    con.commit()


def read_table():
    cur.execute(
        "SELECT * FROM Nodes"
    )
    return cur.fetchall()


def create_unique_index():
    cur.execute(''' 
    CREATE UNIQUE INDEX house_numberstreet_name
    ON Nodes (house_number, street_name);
    ''')


def regenerate_table():
    drop_table()
    create_table()


if __name__ == "__main__":
    # insert_table("house number", "street name", "lon", "lat")
    print(read_table())
