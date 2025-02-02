# read the bible and write it to a file
import pickle

with open("bible.txt") as f:
    bible = f.read()


# create a tokenizer
def build_tokenizer(text):
    tokens = {}
    for word in text.split(" "):
        current_token = word
        if current_token in tokens:
            tokens[current_token] += 1
        else:
            tokens[current_token] = 1
    tokens = list(tokens.keys())
    tokens = {token: i for i, token in enumerate(tokens)}
    return tokens


def save_tokenizer(tokenizer, path="tokenizer.pickle"):
    with open(path, "wb") as f:
        pickle.dump(tokenizer, f)


def load_tokenizer(path="tokenizer.pickle"):
    with open(path, "rb") as f:
        tokenizer = pickle.load(f)
    return tokenizer


def encode(text, tokenizer):
    res = []
    for word in text.split(" "):
        res.append(tokenizer[word])
    return res


def decode(encoded_text, tokenizer):
    decode_tokens = {i: token for token, i in tokenizer.items()}
    res = []
    for token_id in encoded_text:
        res.append(decode_tokens[token_id])
    return " ".join(res)


if __name__ == "__main__":
    tokenizer = build_tokenizer(bible)
    save_tokenizer(tokenizer)
