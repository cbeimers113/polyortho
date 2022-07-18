# Christopher Beimers
# 191428350

"""
This module is responsible for creating observations from the language data.

Observations are the frequency of each grapheme and the likelihood each grapheme
will be followed by any grapheme or is word-final for a language.
"""

import os

from src.text_cleaning import clean_text, transliterate
from src.constants import DATA_FILE, INPUT_FILE, GRAPHEMES, TAMode


def init_header(mode):
    """Initialize the headers for the observations csv file."""
    header = 'lang,'

    # Grapheme frequency header
    if mode in (
        TAMode.GRAPHEMES_ONLY,
        TAMode.GRAPHEMES_AND_COMBOS,
        TAMode.GRAPHEMES_AND_WORD_FINAL,
        TAMode.ALL
    ):
        for grapheme in GRAPHEMES:
            header += f'frq_{grapheme},'

    # Grapheme combinations header
    if mode in (
        TAMode.COMBOS_ONLY,
        TAMode.GRAPHEMES_AND_COMBOS,
        TAMode.COMBOS_AND_WORD_FINAL,
        TAMode.ALL
    ):
        for g1 in GRAPHEMES:
            for g2 in GRAPHEMES:
                header += f'f_{g1}_{g2},'

    # Word final graphemes header
    if mode in (
        TAMode.WORD_FINAL_ONLY,
        TAMode.COMBOS_AND_WORD_FINAL,
        TAMode.GRAPHEMES_AND_WORD_FINAL,
        TAMode.ALL
    ):
        for i, grph in enumerate(GRAPHEMES):
            header += f'end_{grph}'

            if i < len(GRAPHEMES) - 1:
                header += ','

    return header


def analyze_text(lang, text, mode):
    """Perform analysis on the given text."""
    counts = [0 for _ in GRAPHEMES]
    combos = []
    finals = [0 for _ in GRAPHEMES]
    num_graphemes = 0
    num_combos = 0
    num_finals = 0
    freq_data = f'{lang},'

    # Count total number of graphemes in corpus along with each individual grapheme
    if mode in (
        TAMode.GRAPHEMES_ONLY,
        TAMode.GRAPHEMES_AND_COMBOS,
        TAMode.GRAPHEMES_AND_WORD_FINAL,
        TAMode.ALL
    ):
        for grph in text:
            if grph.isspace():
                continue
            counts[GRAPHEMES.index(grph)] += 1
            num_graphemes += 1

    # Count grapheme combinations
    if mode in (
        TAMode.COMBOS_ONLY,
        TAMode.GRAPHEMES_AND_COMBOS,
        TAMode.COMBOS_AND_WORD_FINAL,
        TAMode.ALL
    ):
        for g1 in GRAPHEMES:
            for g2 in GRAPHEMES:
                combo = f'{g1}{g2}'
                combo_count = text.count(combo)
                combos.append(combo_count)
                num_combos += combo_count

    # Count word-final graphemes
    if mode in (
        TAMode.WORD_FINAL_ONLY,
        TAMode.COMBOS_AND_WORD_FINAL,
        TAMode.GRAPHEMES_AND_WORD_FINAL,
        TAMode.ALL
    ):
        for i, grph in enumerate(GRAPHEMES):
            for word in text.split():
                if word.endswith(grph):
                    finals[i] += 1
                    num_finals += 1

    # Collect count data
    if mode in (
        TAMode.GRAPHEMES_ONLY,
        TAMode.GRAPHEMES_AND_COMBOS,
        TAMode.GRAPHEMES_AND_WORD_FINAL,
        TAMode.ALL
    ):
        for count in counts:
            # Store frequencies as percentages
            freq_data += f'{round(100 * count / num_graphemes, 2)},'

    # Collect combinations data
    if mode in (
        TAMode.COMBOS_ONLY,
        TAMode.GRAPHEMES_AND_COMBOS,
        TAMode.COMBOS_AND_WORD_FINAL,
        TAMode.ALL
    ):
        for combo in combos:
            # Store combinations as a percentage of all combinations
            freq_data += f'{round(100 * combo / num_combos, 2)},'

    # Collect word-final grapheme data
    if mode in (
        TAMode.WORD_FINAL_ONLY,
        TAMode.COMBOS_AND_WORD_FINAL,
        TAMode.GRAPHEMES_AND_WORD_FINAL,
        TAMode.ALL
    ):
        for final in finals:
            # Store value as frequency of all word-final graphemes
            freq_data += f'{round(100 * final / num_finals, 2)},'

    # Remove final comma
    freq_data = freq_data[:-1]

    return freq_data


def analyze_files(mode):
    """Create observations for each of the languages."""
    print('Analyzing', end='', flush=True)

    # Initialize observation list
    observations = [init_header(mode)]

    # Create observations for the input file
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        analysis = analyze_text(
            'input', transliterate(clean_text(f.read())), mode
        )
        observations.append(analysis)

    # Create observations for languages
    for filename in os.listdir('data/clean'):
        lang = filename.replace('.txt', '')
        print('.', end='', flush=True)

        with open(os.path.join('data/clean', filename), 'r', encoding='utf-8') as f:
            analysis = analyze_text(lang, f.read(), mode)
            observations.append(analysis)

    # Save observations as a csv file
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        for obs in clean_data(observations):
            f.write(obs + '\n')


def clean_data(data):
    """Remove columns from the data set that don't have any data."""
    zeroes = set()

    # Check each column for all zeroes
    for col in range(1, len(data)):
        zero = True

        # Skip header
        for line in data[1:]:
            if float(line.split(',')[col]) != 0:
                zero = False
                break

        if zero:
            zeroes.add(col)

    # Rebuild data set without zeroes
    for i, line in enumerate(data):
        clean_line = ''

        for col, datum in enumerate(line.split(',')):
            if col not in zeroes:
                clean_line += f'{datum},'

        data[i] = clean_line[:-1]

    return data
