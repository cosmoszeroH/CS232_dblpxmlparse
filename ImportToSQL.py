import pandas as pd
import pyodbc


def import_article():
    data = pd.read_csv(r'article.csv')
    df = pd.DataFrame(data)

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-KNVR3PT;'
                          'Database=DBLP;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute('''
                    CREATE TABLE article(
                        title VARCHAR(MAX),
                        author VARCHAR(MAX),
                        year VARCHAR(MAX),
                        journal VARCHAR(MAX),
                        pages VARCHAR(MAX)
                    )
                    ''')

    for index, row in df.iterrows():
        cursor.execute('''
                        INSERT INTO article (title, author, year, journal, pages)
                        VALUES (?, ?, ?, ?, ?)
                        ''',
                       row.title,
                       row.author,
                       row.year,
                       row.journal,
                       row.pages
                       )

    conn.commit()
    cursor.close()


def import_book():
    data = pd.read_csv(r'book.csv')
    df = pd.DataFrame(data)

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-KNVR3PT;'
                          'Database=DBLP;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute('''
                        CREATE TABLE book(
                            title VARCHAR(MAX),
                            author VARCHAR(MAX),
                            publisher VARCHAR(MAX),
                            isbn VARCHAR(MAX),
                            year VARCHAR(MAX),
                            pages VARCHAR(MAX)
                        )
                        ''')

    for index, row in df.iterrows():
        cursor.execute('''
                            INSERT INTO book (title, author, publisher, isbn, year, pages)
                            VALUES (?, ?, ?, ?, ?, ?)
                            ''',
                       row.title,
                       row.author,
                       row.publisher,
                       row.isbn,
                       row.year,
                       row.pages
                       )


def import_incollection():
    data = pd.read_csv(r'incollection.csv')
    df = pd.DataFrame(data)

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-KNVR3PT;'
                          'Database=DBLP;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute('''
                        CREATE TABLE incollection(
                            title VARCHAR(MAX),
                            author VARCHAR(MAX),
                            booktitle VARCHAR(MAX),
                            ee VARCHAR(MAX),
                            crossref VARCHAR(MAX),
                            url VARCHAR(MAX),
                            year VARCHAR(MAX),
                            pages VARCHAR(MAX)
                        )
                        ''')

    for index, row in df.iterrows():
        cursor.execute('''
                            INSERT INTO incollection (title, author, booktitle, ee, crossref, url, year, pages)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                            ''',
                       row.title,
                       row.author,
                       row.booktitle,
                       row.ee,
                       row.crossref,
                       row.url,
                       row.year,
                       row.pages
                       )


def import_inproceedings():
    data = pd.read_csv(r'inproceedings.csv')
    df = pd.DataFrame(data)

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-KNVR3PT;'
                          'Database=DBLP;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute('''
                        CREATE TABLE inproceedings(
                            title VARCHAR(MAX),
                            author VARCHAR(MAX),
                            year VARCHAR(MAX),
                            pages VARCHAR(MAX),
                            booktitle VARCHAR(MAX)
                        )
                        ''')

    for index, row in df.iterrows():
        cursor.execute('''
                            INSERT INTO inproceedings (title, author, year, pages, booktitle)
                            VALUES (?, ?, ?, ?, ?)
                            ''',
                       row.title,
                       row.author,
                       row.year,
                       row.pages,
                       row.booktitle
                       )


def import_mastersthesis():
    data = pd.read_csv(r'mastersthesis.csv')
    df = pd.DataFrame(data)

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-KNVR3PT;'
                          'Database=DBLP;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute('''
                        CREATE TABLE mastersthesis(
                            title VARCHAR(MAX),
                            author VARCHAR(MAX),
                            school VARCHAR(MAX),
                            year VARCHAR(MAX),
                            ee VARCHAR(MAX),
                            note VARCHAR(MAX)
                        )
                        ''')

    for index, row in df.iterrows():
        cursor.execute('''
                            INSERT INTO masterthesis (title, author, school, year, ee, note)
                            VALUES (?, ?, ?, ?, ?, ?)
                            ''',
                       row.title,
                       row.author,
                       row.school,
                       row.year,
                       row.ee,
                       row.note
                       )


def import_phdthesis():
    data = pd.read_csv(r'phdthesis.csv')
    df = pd.DataFrame(data)

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-KNVR3PT;'
                          'Database=DBLP;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute('''
                        CREATE TABLE phdthesis(
                            title VARCHAR(MAX),
                            author VARCHAR(MAX),
                            publisher VARCHAR(MAX),
                            year VARCHAR(MAX),
                            series VARCHAR(MAX),
                            volume VARCHAR(MAX),
                            pages VARCHAR(MAX),
                            school VARCHAR(MAX),
                            isbn VARCHAR(MAX),
                            ee VARCHAR(MAX)
                        )
                        ''')

    for index, row in df.iterrows():
        cursor.execute('''
                            INSERT INTO phdthesis (title, author, publisher, year, series, volume, pages, school, isbn, ee)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            ''',
                       row.title,
                       row.author,
                       row.publisher,
                       row.year,
                       row.series,
                       row.volume,
                       row.pages,
                       row.school,
                       row.isbn,
                       row.ee
                       )


def import_proceedings():
    data = pd.read_csv(r'proceedings.csv')
    df = pd.DataFrame(data)

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-KNVR3PT;'
                          'Database=DBLP;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute('''
                        CREATE TABLE proceedings(
                            title VARCHAR(MAX),
                            editor VARCHAR(MAX),
                            year VARCHAR(MAX),
                            booktitle VARCHAR(MAX),
                            series VARCHAR(MAX),
                            publisher VARCHAR(MAX),
                        )
                        ''')

    for index, row in df.iterrows():
        cursor.execute('''
                            INSERT INTO proceedings (title, editor, year, booktitle, series, publisher)
                            VALUES (?, ?, ?, ?, ?, ?)
                            ''',
                       row.title,
                       row.editor,
                       row.year,
                       row.booktitle,
                       row.series,
                       row.publisher,
                       )


import_article()
import_book()
import_incollection()
import_inproceedings()
import_mastersthesis()
import_phdthesis()
import_proceedings()