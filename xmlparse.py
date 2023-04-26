from lxml import etree
import csv


article_features = ["title", "author", "year", "journal", "pages"]
inproceedings_features = ["title", "author", "year", "pages", "booktitle"]
proceedings_features = ["title", "editor", "year", "booktitle", "series", "publisher"]
book_features = ["title", "author", "publisher", "isbn", "year", "pages"]
incollection_features = ["title", "author", "booktitle", "ee", "crossref", "url", "year", "pages"]
phdthesis_features = ["title", "author", "publisher", "year", "series", "volume", "pages", "school", "isbn", "ee"]
mastersthesis_features = ["title", "author", "school", "year", "ee", "note"]


def create_csv_file():
    with open('article.csv', 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=article_features)
        writer.writeheader()

    with open('inproceedings.csv', 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=inproceedings_features)
        writer.writeheader()

    with open('proceedings.csv', 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=proceedings_features)
        writer.writeheader()

    with open('book.csv', 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=book_features)
        writer.writeheader()

    with open('incollection.csv', 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=incollection_features)
        writer.writeheader()

    with open('phdthesis.csv', 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=phdthesis_features)
        writer.writeheader()

    with open('mastersthesis.csv', 'a', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=mastersthesis_features)
        writer.writeheader()


def context_iter(dblp_path):
    return etree.iterparse(source=dblp_path, dtd_validation=True, load_dtd=True)


def clear_element(element):
    element.clear()
    while element.getprevious() is not None:
        del element.getparent()[0]


def parse_entity(elem, features):
    attribs = {}
    for feature in features:
        attribs[feature] = []

    for sub in elem.getchildren():
        if sub.tag in features:
            attribs[sub.tag].append(sub.text)

    return attribs


def parse_article(elem):
    return parse_entity(elem, article_features)


def parse_inproceedings(elem):
    return parse_entity(elem, inproceedings_features)


def parse_proceedings(elem):
    return parse_entity(elem, proceedings_features)


def parse_book(elem):
    return parse_entity(elem, book_features)


def parse_incollection(elem):
    return parse_entity(elem, incollection_features)


def parse_phdthesis(elem):
    return parse_entity(elem, phdthesis_features)


def parse_mastersthesis(elem):
    return parse_entity(elem, mastersthesis_features)


def parse_www(elem):
    pass


def parse_all(dblp_path):
    create_csv_file()

    for _, elem in context_iter(dblp_path):
        if elem.tag == 'article':
            attribs = parse_article(elem)
            with open('article.csv', 'a', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=article_features)
                writer.writerow(attribs)

        if elem.tag == 'inproceedings':
            attribs = parse_inproceedings(elem)
            with open('inproceedings.csv', 'a', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=inproceedings_features)
                writer.writerow(attribs)

        if elem.tag == 'proceedings':
            attribs = parse_proceedings(elem)
            with open('proceedings.csv', 'a', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=proceedings_features)
                writer.writerow(attribs)

        if elem.tag == 'book':
            attribs = parse_book(elem)
            with open('book.csv', 'a', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=book_features)
                writer.writerow(attribs)

        if elem.tag == 'incollection':
            attribs = parse_incollection(elem)
            with open('incollection.csv', 'a', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=incollection_features)
                writer.writerow(attribs)

        if elem.tag == 'phdthesis':
            attribs = parse_phdthesis(elem)
            with open('phdthesis.csv', 'a', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=phdthesis_features)
                writer.writerow(attribs)

        if elem.tag == 'mastersthesis':
            attribs = parse_mastersthesis(elem)
            with open('mastersthesis.csv', 'a', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=mastersthesis_features)
                writer.writerow(attribs)

        if elem.tag == 'www':
            parse_www(elem)

        clear_element(elem)


dblp_path = 'dblp.xml'

parse_all(dblp_path)
