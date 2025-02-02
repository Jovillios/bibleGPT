import numpy as np
from tokenizer import encode


def generate(input, p, tokenizer, max_len=100):
    encoded_input = encode(input, tokenizer)
    res = [encoded_input[-1]]
    for i in range(max_len):
        curr = res[-1]
        p_curr = p[curr]
        eps = np.random.rand()
        cumul = 0
        for next in p[curr]:
            cumul += p[curr][next]
            if cumul >= eps:
                break
        res.append(next)
    return res
