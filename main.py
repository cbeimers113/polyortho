# Christopher Beimers
# 191428350

import sys

from src.constants import POLY_DEG, TAMode
from src.data_analysis import create_detection_model
from src.language_detection import detect_language
from src.text_analysis import analyze_files
from src.text_cleaning import clean_files

"""
This program analyzes the European Parliament Proceedings Parallel Corpus 1996-2011.
The data were obtained from https://www.statmt.org/europarl/

The goal of this program is to train a model to take text as input and detect which
(if any) of the languages used in the European Parliament the text is written in.

The method used is an attempt to recognize a written language purely on an orthographical
basis. All text is first rendered into its equivalent Latin script form, then all variants
of each grapheme in the corpora are lemmatized into their base forms. These data are then 
analyzed for grapheme frequency and grapheme combination frequency, and the resulting 
observations are used to detect the source language of a given text.

The detection algorithm uses polynomial regression on the grapheme analysis and compares 
these functions to determine which language is present.

The user places a section of text in the target language in the input file (input.txt), and
the program will perform analysis on it as well as the EPPPC language data and determine
which language is most likely being presented. The more text in the target language given as
input, the more likely the program is to give an accurate detection.
"""


def __main__(mode):
    """Starting point of program."""
    print(
        f'Running Polyortho\nAnalysis Mode: {mode.name}\nPolynomial: n = {POLY_DEG}\n'
    )

    # Load the raw data and extract text as Latin script in each target language
    clean_files()
    print()

    # Analyze the cleaned data for grapheme and combination frequencies
    analyze_files(mode)
    print()

    # Create plots of language data and perform polynomial regression
    create_detection_model(POLY_DEG)
    print('\n')

    # Detect language
    results = detect_language()
    print(f'Detected: {results[0]}')


def print_help():
    """Print the usage help string."""
    print('Usage: python main.py <analysis mode>\n\tAnalysis modes:')

    for mode in TAMode:
        print(f'\t{mode.value} = {mode.name}')

    print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_help()

        # Use GRAPHEMES_ONLY after printing usage if no mode supplied
        __main__(TAMode.GRAPHEMES_ONLY)
    else:
        try:
            mode = int(sys.argv[1])

            if mode not in range(len(TAMode)):
                raise ValueError

            __main__(TAMode(mode))
        except ValueError:
            print_help()
