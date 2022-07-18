# Christopher Beimers
# 191428350

"""This module uses the model to determine the likelihood that the input is in each language."""

from src.constants import LANG_FULL_NAME, MODEL_FILE


def detect_language():
    """Detect which language the input is written in, and rank all languages."""
    ranks = []
    results = []

    with open(MODEL_FILE, 'r', encoding='utf-8') as f:
        line = f.readline()

        while line:
            data = line.split(',')
            lang = data[0]
            score = float(data[1])
            ranks.append((score, lang))
            line = f.readline()

    for rank in sorted(ranks):
        results.append(LANG_FULL_NAME[rank[1]])

    return results
