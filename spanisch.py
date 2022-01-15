import psycopg2

class Vokabeltrainer:
    # Konstanten
    DB_HOST = "localhost"
    DB_NAME = "spanischdb"
    DB_User = "postgres"
    DB_PASS = "root"

    # Variablen
    connector_db = None
    cursor_db = None

    def __init__(self):
        self.connector_db = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_User, password=self.DB_PASS, host=self.DB_HOST)
        self.cursor_db = self.connector_db.cursor()

    def select_data(self):
            #with self.cursor_db as cursor:
            self.cursor_db.execute("SELECT * FROM wort")
            for row in self.cursor_db:
                print(row)

    def insert_data(self, esp_input, de_input):
        self.cursor_db.execute("INSERT INTO wort (spanisch, deutsch) VALUES(%s, %s)", (esp_input, de_input))
        #self.connector_db.commit()

    def update_data(self, esp_input, de_input):
        db_query = self.cursor_db.execute("SELECT * FROM wort WHERE spanisch='" + esp_input + "';")
        row = self.cursor_db.fetchone()
        if row:
            print("Datensatz gefunden.")
            self.cursor_db.execute("UPDATE wort SET deutsch ='" + de_input + "' WHERE spanisch='" + esp_input + "';")
        else:
            print("Nichts gefunden")
            db_query = self.cursor_db.execute("SELECT * FROM wort WHERE deutsch=" + de_input + ";")
            row = self.cursor_db.fetchone()
            if row:
                print("Doch etwas gefunden.")
                self.cursor_db.execute("UPDATE wort SET spanisch =" + esp_input + " WHERE deutsch=" + de_input + ";")


    def delete_data(self, esp_input, de_input):
        db_query = self.cursor_db.execute("SELECT * FROM wort WHERE spanisch='" + esp_input + "';")
        row = self.cursor_db.fetchone()
        if row:
            print("Datensatz gefunden.")
            self.cursor_db.execute("DELETE FROM wort WHERE spanisch='" + esp_input + "';")
        else:
            print("Nichts gefunden")
            db_query = self.cursor_db.execute("SELECT * FROM wort WHERE deutsch='" + de_input + "';")
            row = self.cursor_db.fetchone()
            if row:
                print("Doch etwas gefunden.")
                self.cursor_db.execute("DELETE FROM wort WHERE deutsch='" + de_input + "';")

    def final_commit(self):
        self.connector_db.commit()
        self.cursor_db.close()
        self.connector_db.close()

