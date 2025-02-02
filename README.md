# bibleGPT

This project showcases a simple markov model for text generation. This model has learned on the whole bible as dataset.

## Usage

To generate a new text from a current word use the command: ```python main.py <word>```

The model will predict and generate text based on learned probabilities from the dataset.

## Markov Model Principle

Based on the last token, predict the next next using a learned distribution $p(x_i | x_{i_1})$. To learn this probability distribution, we compute the frequency of occurrences of each token following a given token in the dataset. This allows us to generate text by repeatedly sampling the next word based on the learned distribution.

## Tokenizer

The tokenizer used in this project follows a simple word-based tokenization approach, where each unique word is treated as a token. The implementation can be found in [tokenizer](tokenizer.py)


## Limitations

- Since it is a first-order Markov model, it only considers one word at a time, limiting the coherence of generated text.
- The model does not understand grammar or semantics beyond statistical word co-occurrence.

## Future Improvements

- Implementing higher-order Markov chains to consider multiple previous tokens for better coherence. Need a larger dataset to capture longer dependencies.
- Exploring n-gram smoothing techniques to improve text generation for rare words.
- Extending the model to use neural networks (e.g., LSTMs or Transformers) for more sophisticated text generation.

## License

This project is open-source and distributed under the MIT License.

This version provides better structure, clarifies the methodology, and suggests improvements for future development. Let me know if you want any modifications! 🚀

