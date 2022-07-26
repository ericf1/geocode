import sqlite3


def generate_highways(cur):
    cur.execute('''
                CREATE TABLE Highways (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                highway_type TEXT NOT NULL
                );
                ''')


def generate_nodes(cur):
    cur.execute('''
                CREATE TABLE Nodes (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  highway_id INTEGER,
                  name TEXT NOT NULL,
                  lon INTEGER,
                  lat INTEGER,
                  FOREIGN KEY (highway_id) REFERENCES Highways(id)
                );
                ''')


def drop_highways(cur):
    cur.execute('''
                DROP TABLE Highways
                ''')


def drop_nodes(cur):
    cur.execute('''
                DROP TABLE Nodes
                ''')


def show_tables(cur):
    cur.execute(".tables")


def recreate_tables(cur):
    drop_highways(cur)
    drop_nodes(cur)
    generate_highways(cur)
    generate_nodes(cur)


def create_tables(cur):
    generate_highways(cur)
    generate_nodes(cur)


def drop_tables(cur):
    drop_highways(cur)
    drop_nodes(cur)


if __name__ == "__main__":
    con = sqlite3.connect('highways.db')
    cur = con.cursor()
    recreate_tables(cur)
