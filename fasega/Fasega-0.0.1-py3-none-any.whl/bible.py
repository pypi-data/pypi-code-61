"""
Bible application
"""
import random
import datetime

import requests

old_testament_books = [
    "Genesis",
    "Exodus",
    "Leviticus",
    "Numbers",
    "Deuteronomy",
    "Joshua",
    "Judges",
    "Ruth",
    "1 Samuel",
    "2 Samuel",
    "1 Kings",
    "2 Kings",
    "1 Chronicles",
    "2 Chronicles",
    "Ezra",
    "Nehemiah",
    "Esther",
    "Job",
    "Psalms",
    "Proverbs",
    "Ecclesiastes",
    "Song of Solomon",
    "Isaiah",
    "Jeremiah",
    "Lamentations",
    "Ezekiel",
    "Daniel",
    "Hosea",
    "Joel",
    "Amos",
    "Obadiah",
    "Jonah",
    "Micah",
    "Nahum",
    "Habakkuk",
    "Zephaniah",
    "Haggai",
    "Zechariah",
    "Malachi"
]

new_testament_books = [
    "Matthew",
    "Mark",
    "Luke",
    "John",
    "Acts",
    "Romans",
    "1 Corinthians",
    "2 Corinthians",
    "Galatians",
    "Ephesians",
    "Philippians",
    "Colossians",
    "1 Thessalonians",
    "2 Thessalonian",
    "1 Timothy",
    "2 Timothy",
    "Titus",
    "Philemon",
    "Hebrews",
    "James",
    "1 Peter",
    "2 Peter",
    "1 John",
    "2 John",
    "3 John",
    "Jude",
    "Revelation"
]

all_books = new_testament_books + old_testament_books
max_chapter = 150
max_verse = 100


def get_verse(book: dict):
    """

    :param book:
    :return:
    """
    book_name = book.get("book_name")
    chapter = 'unknown'
    verse_number = 'unknown'
    verse = 'unknown'
    for key, value in book.get("chapter").items():
        chapter = key
        verse_number = value.get('verse_nr')
        verse = value.get('verse')

    verse_info = {
        "book_name": book_name,
        "chapter": chapter,
        "verse_number": verse_number,
        "verse": verse
    }
    return verse_info


class BibleVerse(object):
    """
    Bible book object
    """
    book: str = None
    chapter: int = None
    verse_number: int = None
    verse: dict = {}


def get_random_verse() -> (str, int, int, str):
    """

    :return: (book, chapter, verse, texture)
    """
    versions = ["kjv", "hsab", "arabicsv"]
    book = random.choice(all_books)
    chapter = str(random.randint(1, max_chapter))
    verse = str(random.randint(1, max_verse))
    results = {"book": book, "chapter": chapter, "verse": verse, "versions": {}}
    for version in versions:
        try:
            response = requests.get(f'https://getbible.net/json?scripture={book}{chapter}:{verse}&version={version}')
            result: dict = eval(response.text[:-1])
            if result.get("type") == "verse":
                verse_dict = get_verse(result.get("book")[0])
                results["versions"][version] = verse_dict["verse"]
        except NameError:
            return get_random_verse()

    return results


def get_bible_verse(book: str = None, chapter: int = None, verse_no: int = None, versions: list = None,
                    retry: int = 5) -> BibleVerse:
    """
    Get a bible verse
    :param retry:
    :param versions:
    :param book:
    :param chapter:
    :param verse_no:
    :return:
    """

    bible_verse = BibleVerse()
    bible_verse.versions = versions if versions is not None else ["kjv", "hsab", "arabicsv"]
    bible_verse.book = book if book is not None else random.choice(all_books)
    bible_verse.chapter = str(chapter) if chapter is not None else str(random.randint(1, max_chapter))
    bible_verse.verse_number = str(verse_no) if verse_no is not None else str(random.randint(1, max_verse))

    for version in bible_verse.versions:
        try:
            response = requests.get(f'https://getbible.net/json?scripture={bible_verse.book}{bible_verse.chapter}:'
                                    f'{bible_verse.verse_number}&version={version}')
            result: dict = eval(response.text[:-1])
            if result.get("type") == "verse":
                verse_dict = get_verse(result.get("book")[0])
                bible_verse.verse[version] = verse_dict["verse"]
        except NameError:
            retry = retry - 1
            if retry <= 0:
                today = datetime.datetime.today()
                return get_bible_verse(book, today.month, today.day, versions, 5)
            else:
                return get_bible_verse(book=book, versions=versions, retry=retry)
    return bible_verse
