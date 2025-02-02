import pickle
from tokenizer import encode, load_tokenizer


def get_markov_distribution(encoded_text):
    res = {}
    n = len(encoded_text)
    for i in range(n - 1):
        if encoded_text[i] not in res:
            res[encoded_text[i]] = {}
        if encoded_text[i + 1] in res[encoded_text[i]]:
            res[encoded_text[i]][encoded_text[i + 1]] += 1
        else:
            res[encoded_text[i]][encoded_text[i + 1]] = 1

    for prev in res:
        n = 0
        for curr in res[prev]:
            n += res[prev][curr]
        for curr in res[prev]:
            res[prev][curr] /= n
    return res


def save_markov(markov, path="models/markov.pickle"):
    with open(path, "wb") as f:
        pickle.dump(markov, f)


def load_markov(path="models/markov.pickle"):
    with open(path, "rb") as f:
        markov = pickle.load(f)
    return markov


if __name__ == "__main__":
    with open("bible.txt", "r") as f:
        bible = f.read()
    encoded_text = encode(bible, load_tokenizer())
    markov = get_markov_distribution(encoded_text)
    save_markov(markov)
