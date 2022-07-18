# Christopher Beimers
# 191428350

"""This module is responsible for loading and cleaning the text data."""

import os

from src.constants import DEAD_CHARS, DIGRAPHS, LEMMAS, TRANSLIT


def transliterate(text):
    """Transliterate non-Latin text into the equivalent Latin script."""
    transliterated = ''

    # Separate digraphs
    for digraph, monographs in DIGRAPHS.items():
        text = text.replace(digraph, monographs)

    for grph in text:
        next_grph = grph

        if grph in TRANSLIT.keys():
            next_grph = TRANSLIT[grph]

        transliterated += LEMMAS[next_grph] if next_grph in LEMMAS else next_grph

    return transliterated


def clean_text(text):
    """Clean some text."""
    cleaned = ''

    for grph in text.lower():
        if grph in DEAD_CHARS or grph.isnumeric():
            continue
        cleaned += grph

    return cleaned.strip()


def clean_files():
    """Iterate through language folders and extract the necessary data."""
    print('Cleaning', end='', flush=True)
    languages = {}

    for lang in os.listdir('data/txt'):
        languages[lang] = set()  # Avoid storing duplicate text

    for dirname, _, files in os.walk('data/txt'):
        if not len(files):
            continue

        lang = os.path.basename(dirname)
        print('.', end='', flush=True)

        # Find and extract words in the target language
        for langfile in files:
            with open(os.path.join(dirname, langfile), 'r', encoding='utf-8') as f:
                f.readline()

                # The second line of each file contains text in that language
                text = clean_text(f.readline().strip())

                # Some lines contain this extra tag, so ignore it
                if 'speaker id language name' in text:
                    continue

                languages[lang].add(transliterate(text))

        # Save collected clean data
        with open(os.path.join('data/clean', f'{lang}.txt'), 'w', encoding='utf-8') as f:
            for line in languages[lang]:
                if not line:
                    continue
                f.write(f'{line}\n')
