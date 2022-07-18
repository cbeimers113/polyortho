# Christopher Beimers
# 191428350

"""This module creates scatterplots for the data and performs polynomial regression."""

import matplotlib.pyplot as plt
import numpy as np

from src.constants import DATA_FILE, LANG_FULL_NAME, MODEL_FILE


# Store the polynomial of the input text to render it on other language graphs
INPUT_POLY = None


def create_plot(data, n):
    """Create a scatterplot and perform n-degree polynomial regression on a line of data."""
    lang = 'Input Data'

    if data[0] in LANG_FULL_NAME:
        lang = LANG_FULL_NAME[data[0]]

    x_axis = [i for i in range(len(data) - 1)]
    y_axis = [float(d) for d in data[1:]]

    # Scale the plot up so the axes are readable
    plt.figure(figsize=(8, 6))

    # Plot data
    plt.title(f'Grapheme Analysis for {lang}')
    plt.xlabel('Grapheme Feature')
    plt.ylabel('Frequency (%)')
    plt.scatter(x_axis, y_axis)

    # Plot polynomial regression line
    model = np.poly1d(np.polyfit(x_axis, y_axis, n))
    line = np.linspace(0, len(x_axis))
    plt.plot(line, model(line), color='red')

    # Show the difference from the input polynomial
    global INPUT_POLY

    if lang == 'Input Data' and INPUT_POLY is None:
        INPUT_POLY = model
    else:
        diff_model = np.polysub(model, INPUT_POLY)
        plt.plot(line, diff_model(line), color='green')

    # Save data
    plt.legend(('Grapheme Features', 'Polynomial Regression',
               'Difference Polynomial'))
    plt.savefig(f'data/plots/{lang}.png')

    # Clear previous plots
    plt.clf()
    plt.close()

    return data[0], model


def integrate(model, x_lim, num_points=1000):
    """Manually estimate the definite integral, treating each negative area as positive."""
    area = 0

    for x in range(x_lim * num_points):
        area += abs(model(x / num_points))

    return area / num_points


def create_detection_model(n):
    """Create plots and a detection model from the data file."""
    models = {}
    x_lim = 0  # Domain of difference polynomial to integrate over
    print('Modelling', end='', flush=True)

    # Create plots and collect regression polynomials
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        line = f.readline()
        line = f.readline()  # Skip the header line

        while line:
            data = line.split(',')
            x_lim = len(data) - 1
            lang, model = create_plot(data, n)
            models[lang] = model
            line = f.readline()
            print('.', end='', flush=True)

    print('\nIntegrating', end='', flush=True)

    # Save the model as the integral of the difference between the input and each lang polynomial
    with open(MODEL_FILE, 'w', encoding='utf-8') as f:
        for lang, model in models.items():
            if lang == 'input':
                continue

            print('.', end='', flush=True)
            delta = integrate(np.polysub(model, models['input']), x_lim)
            f.write(f'{lang},{delta}\n')
