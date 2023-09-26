from config import CONN, CURSOR
import sqlite3


class Song:
    def __init__(self, name, album, id=None):
        self.id = id
        self.name = name
        self.album = album
        
    def save(self):
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO songs (name, album) VALUES (?, ?)', (self.name, self.album))
            self.id = cursor.lastrowid 
        else:
            cursor.execute('UPDATE songs SET name=?, album=? WHERE id=?', (self.name, self.album, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('music.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                album TEXT
            )
        ''')
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song