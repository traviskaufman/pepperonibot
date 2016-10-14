import random

from pepperonibot import get_model


def run():
    num_sentences = random.randint(1, 3)
    model = get_model()
    for _ in range(num_sentences):
        print model.make_short_sentence(300)


if __name__ == '__main__':
    run()
