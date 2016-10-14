"""
I'm a gigantic asshole.
"""

from glob import glob
from os import path
import markovify

DATA_DIR = path.abspath(
    path.join(path.dirname(path.realpath(__file__)), '..', 'dat'))
print DATA_DIR
DATA_FILE = path.join(DATA_DIR, 'model.json')


def train():
    training_data = glob(path.join(DATA_DIR, '*.data'))
    models = []
    print "Training over {} data sets".format(len(training_data))
    for corpus in training_data:
        print "Training on {}".format(path.relpath(corpus, DATA_DIR))
        with open(corpus, mode='r') as f:
            models.append(markovify.Text(f.read(), state_size=2))
    final_model = markovify.combine(models)
    print "Serializing model to {}".format(DATA_FILE)
    with open(DATA_FILE, mode='w') as data_file:
        data_file.write(final_model.chain.to_json())
    return final_model


def get_model():
    if path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            model = markovify.Text.from_chain(f.read())
    else:
        model = train()

    return model
