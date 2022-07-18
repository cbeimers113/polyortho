
#  Polyortho

###  A lightweight language detection algorithm

  

Polyortho (POLYnomial regression + ORTHOgraphy) is a lightweight language detection algorithm that applies concepts from natural language processing, statistical analysis, regression analysis and integral calculus to detect which of 21 languages an input text is written in.

  

The supported languages are Bulgarian, Czech, Danish, German, Greek, English, Spanish, Estonian, Finnish, French, Hungarian, Italian, Lithuanian, Latvian, Dutch, Polish, Portuguese, Romanian, Slovak, Slovene, and Swedish.

  

The data used to train and test the model are from the [European Parliament Proceedings Parallel Corpus 1996-2011](https://www.statmt.org/europarl/).

  

The program has three analysis modes: grapheme frequency, grapheme combination frequency, and word-final grapheme frequency. Due to the central limit theorem, Polyortho works best when at least 10 KB of sample text are used.

  

### Here's how to use Polyortho:

Clone the repository:

`git clone git@github.com:cbeimers113/polyortho.git`

  

Download the [Europarl corpus](https://www.statmt.org/europarl/v7/europarl.tgz) (1.5 GB) and extract the 'txt' folder to the data/ directory of the project.

  

Place text to be analyzed in input.txt (at least 10 KB of text)

  

Run main.py with Python 3 (3.8 or higher recommended):

`python main.py` <br>

or <br>

`python3 main.py` <br>

  

The output should look something like this:

```Cleaning.....................

Analyzing.....................

Modelling......................

Integrating.....................

Detected: <target language>
```

If the input language is not supported by Polyortho, it should detect the supported language with the closest similarity of the chosen feature analysis mode.