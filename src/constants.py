# Christopher Beimers
# 191428350

"""This module stores constants used throughout the program."""

import enum
import string

# This file will store the user's input
INPUT_FILE = 'input.txt'

# This file will store text analysis observations
DATA_FILE = 'data/data.csv'

# This file will store regression analysis data
MODEL_FILE = 'data/model.csv'

# These characters should be filtered out during the cleaning process
DEAD_CHARS = string.punctuation + '«»“”°ºª№·΄¿ˇ˛­'

# The degree of polynomial to use in regression
POLY_DEG = 7


class TAMode(enum.Enum):
    """Text analysis modes."""
    GRAPHEMES_ONLY = 0
    COMBOS_ONLY = 1
    WORD_FINAL_ONLY = 2
    GRAPHEMES_AND_COMBOS = 3
    GRAPHEMES_AND_WORD_FINAL = 4
    COMBOS_AND_WORD_FINAL = 5
    ALL = 6


# Map the language code to its full name
LANG_FULL_NAME = {
    'bg': 'Bulgarian',
    'cs': 'Czech',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'es': 'Spanish',
    'et': 'Estonian',
    'fi': 'Finnish',
    'fr': 'French',
    'hu': 'Hungarian',
    'it': 'Italian',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'nl': 'Dutch',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'sk': 'Slovak',
    'sl': 'Slovene',
    'sv': 'Swedish'
}

# Transliteration mappings
TRANSLIT = {
    # Bulgarian
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'f',
    'е': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'і': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'sht',
    'ъ': 'a',
    'ь': 'u',
    'ю': 'yu',
    'я': 'ya',

    # Greek
    'α': 'a',
    'ά': 'á',
    'β': 'v',
    'γ': 'g',
    'δ': 'd',
    'ε': 'e',
    'έ': 'é',
    'ζ': 'z',
    'η': 'ī',
    'ή': 'î',
    'θ': 'th',
    'ι': 'i',
    'ί': 'í',
    'ϊ': 'ï',
    'ΐ': 'ḯ',
    'κ': 'k',
    'λ': 'l',
    'μ': 'm',
    'ν': 'n',
    'ξ': 'ks',
    'ο': 'o',
    'ό': 'ó',
    'π': 'p',
    'ρ': 'r',
    'σ': 's',
    'ς': 's',
    'τ': 't',
    'υ': 'u',
    'ύ': 'ú',
    'ϋ': 'ü',
    'ΰ': 'ǘ',
    'φ': 'ph',
    'χ': 'ch',
    'ψ': 'ps',
    'ω': 'ō',
    'ώ': 'ṓ',

    # Miscellaneous
    'ĳ': 'ij',
    'œ': 'oe',
    'æ': 'ae'
}

# Digraph-monograph mappings
DIGRAPHS = {
    'γγ': 'ng',
    'μπ': 'b'
}

# The frequencies of these graphemes will be analyzed
GRAPHEMES = (
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
)

# Map various forms of graphemes to their base forms
LEMMAS = {
    'à': 'a',
    'á': 'a',
    'â': 'a',
    'ã': 'a',
    'ä': 'a',
    'å': 'a',
    'ā': 'a',
    'ă': 'a',
    'ą': 'a',
    'ç': 'c',
    'ć': 'c',
    'č': 'c',
    'ď': 'd',
    'è': 'e',
    'é': 'e',
    'ê': 'e',
    'ë': 'e',
    'ē': 'e',
    'ė': 'e',
    'ę': 'e',
    'ě': 'e',
    'ģ': 'g',
    'ì': 'i',
    'í': 'i',
    'î': 'i',
    'ï': 'i',
    'ī': 'i',
    'į': 'i',
    'ḯ': 'i',
    'ķ': 'k',
    'ĺ': 'l',
    'ļ': 'l',
    'ľ': 'l',
    'ł': 'w',
    'ñ': 'n',
    'ń': 'n',
    'ņ': 'n',
    'ň': 'n',
    'ō': 'o',
    'ő': 'o',
    'ò': 'o',
    'ó': 'o',
    'ô': 'o',
    'õ': 'o',
    'ö': 'o',
    'ø': 'o',
    'ṓ': 'o',
    'ŕ': 'r',
    'ŗ': 'r',
    'ř': 'r',
    'ß': 's',
    'ś': 's',
    'ş': 's',
    'š': 's',
    'ș': 's',
    'ţ': 't',
    'ť': 't',
    'ț': 't',
    'ù': 'u',
    'ú': 'u',
    'û': 'u',
    'ü': 'u',
    'ū': 'u',
    'ů': 'u',
    'ű': 'u',
    'ų': 'u',
    'ý': 'y',
    'ź': 'z',
    'ż': 'z',
    'ž': 'z'
}
