# Christopher Beimers
# 191428350

"""This module is used for testing purposes."""

import os

from src.constants import TAMode, INPUT_FILE, LANG_FULL_NAME
from src.data_analysis import create_detection_model
from src.language_detection import detect_language
from src.text_analysis import analyze_files
from src.text_cleaning import clean_files


def generate_test_files():
    """Create the testing files from the cleaned data."""
    for tfile in os.listdir('data/clean'):
        with open(os.path.join('data/clean', tfile), 'r', encoding='utf-8') as ifile:
            for _ in range(50):
                with open(os.path.join('data/testing/', tfile), 'a', encoding='utf-8') as ofile:
                    ofile.write(ifile.readline())


def test_parameters():
    """
    Determine the minimum polynomial for each analysis mode to find which is most efficient.

    Warning: Very long computation time
    """
    degrees = {}

    for mode in TAMode.GRAPHEMES_ONLY, TAMode.COMBOS_ONLY, TAMode.WORD_FINAL_ONLY:
        degrees[mode.name] = test_polynomial(mode)

    return degrees


def test_polynomial(mode):
    """Determine the minimum polynomial degree that detects all test languages."""
    n = 1

    while not test_files(mode, n) and n < 10:
        n += 1

    return n


def test_files(mode, n):
    """Test the algorithm on all files with a given polynomial degree. Return True if 100% accurate."""
    num_correct = 0
    num_tests = 0

    clean_files()
    print('\n')

    for test_file in os.listdir('data/testing'):
        lang = test_file.replace('.txt', '')

        # Copy contents of test file to input file
        with open(os.path.join('data/testing', test_file), 'r', encoding='utf-8') as in_f:
            with open(INPUT_FILE, 'w', encoding='utf-8') as out_f:
                out_f.write(in_f.read())

        print(f'Testing against {LANG_FULL_NAME[lang]}')
        analyze_files(mode)
        print()
        create_detection_model(n)

        results = detect_language()
        print(f'\nDetected: {results[0]}\n')

        success = LANG_FULL_NAME[lang] == results[0]
        num_tests += 1
        num_correct += 1 if success else 0

        if not success:
            return False

    return True


print(test_files(TAMode.GRAPHEMES_ONLY, 7))
