from generate import generate
from markov import load_markov
from tokenizer import decode, load_tokenizer
import sys

if __name__ == "__main__":
    markov = load_markov()
    tokenizer = load_tokenizer()
    input = sys.argv[1]
    output = generate(input, markov, tokenizer)
    print(decode(output, tokenizer))
