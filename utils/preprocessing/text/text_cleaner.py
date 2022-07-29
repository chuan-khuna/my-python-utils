import re

DEFAULT_REGEX_PATTERNS = [(r'^\s*', ''), (r'\s*$', ''), (r"\s{2,}", " ")]


class TextCleaner:
    """A string preprocessor including:
        regular expression,
        stop word remover,
        n gram generator
    """

    def __init__(self, stop_words=None, delimiter='|'):
        self.stop_words = stop_words
        self.delimiter = delimiter
        self._regex_patterns = None
        self._default_regex_patterns = DEFAULT_REGEX_PATTERNS

    @property
    def default_regex_patterns(self):
        return self._default_regex_patterns

    @property
    def regex_patterns(self):
        return self._regex_patterns

    @regex_patterns.setter
    def regex_patterns(self, regex_patterns):
        print("Called regex patterns setters")
        self._regex_patterns = regex_patterns

    def _get_regex_patterns(self) -> list:
        if self.regex_patterns is None:
            return self._default_regex_patterns
        else:
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