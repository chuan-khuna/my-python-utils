import re

################################
# regex note
################################
# \n and \t -> white space
# urls
# https://regex101.com/r/hG9t0Q/1
# https://regexr.com/3e6m0
# https://regexr.com/37i6s

DEFAULT_REGEX_PATTERNS = [
    (r"[\n|\r|\t]", " "), (r'^\s*', ''), (r'\s*$', ''), (r"(?:\s)(\s+)", " "),
    (r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
     '')
]
OOV_TOKEN = '<OOV>'


class TextCleaner:
    """A string preprocessor including:
        regular expression,
        stop word remover,
        n gram generator
    """

    def __init__(self, stop_words: list = None, delimiter: str = '|'):
        self.stop_words = stop_words
        self.delimiter = delimiter
        self._regex_patterns = None
        self._default_regex_patterns = DEFAULT_REGEX_PATTERNS
        self._vocab = None
        self._inverse_vocab = None
        self.out_of_vocab_token = OOV_TOKEN

    @property
    def default_regex_patterns(self):
        return self._default_regex_patterns

    @property
    def regex_patterns(self):
        return self._regex_patterns

    @regex_patterns.setter
    def regex_patterns(self, regex_patterns: list[tuple[str, str]]):
        self._regex_patterns = regex_patterns

    @property
    def vocab(self):
        return self._vocab

    @vocab.setter
    def vocab(self, vocab: dict[str, int]):
        self._vocab = vocab
        self._inverse_vocab: dict[int, str] = {}
        for k, v in vocab.items():
            self._inverse_vocab[v] = k

    @property
    def inverse_vocab(self):
        return self._inverse_vocab

    def _get_regex_patterns(self) -> list:
        if self.regex_patterns is None:
            return self._default_regex_patterns
        return self.regex_patterns

    def clean(self, text: str) -> str:
        for pattern, replace in self._get_regex_patterns():
            pattern = re.compile(pattern)
            text = re.sub(pattern, replace, text)

        return text

    def generate_n_gram(self, words: list[str], n: int) -> list[tuple[str]]:
        if n > len(words) or n <= 0:
            raise ValueError("Invalid number: n should be in range 1..len(words) (including)")

        n_grams = []
        for current_index in range(0, len(words) - n + 1):
            n_gram_tuple = [words[current_index + n_gram_index] for n_gram_index in range(n)]
            n_grams.append(tuple(n_gram_tuple))
        return n_grams

    def remove_stop_words(self, words: list[str]) -> list[str]:
        if self.stop_words is not None:
            return [word for word in words if word not in self.stop_words]
        else:
            return words

    def join(self, words: list[str]) -> str:
        return self.delimiter.join(words)

    def _map_key_to_value(self, sequence: list[str | int], dict_):
        new_sequence = []
        for k in sequence:
            if k in dict_.keys():
                new_sequence.append(dict_[k])
            else:
                new_sequence.append(self.out_of_vocab_token)
        return new_sequence

    def text_to_sequence(self, text: list[str]) -> list[int]:
        if self.vocab is None:
            raise AttributeError(
                "Vocabulary is None. Please set vocabulary before converting text to sequence")
        sequence = self._map_key_to_value(text, self.vocab)
        return sequence

    def sequence_to_text(self, sequence: list[int]) -> list[str]:
        if self.vocab is None:
            raise AttributeError(
                "Vocabulary is None. Please set vocabulary before converting text to sequence")
        sequence = self._map_key_to_value(sequence, self.inverse_vocab)
        return sequence