import pandas as pd

OOV_TOKEN = '<OOV>'
SPECIAL_TOKENS = [OOV_TOKEN]


class Vocabulary:

    def __init__(self, special_tokens: list[str] = SPECIAL_TOKENS):
        self._special_tokens = special_tokens

        # protected attributes
        self._vocab = {}
        self._inverse_vocab = {}
        self._words = None
        self._df = None

    @property
    def vocab(self):
        return self._vocab

    @property
    def inverse_vocab(self):
        return self._inverse_vocab

    @property
    def words(self):
        return self._words

    @property
    def df(self):
        return self._df

    @property
    def special_tokens(self):
        return self._special_tokens

    @special_tokens.setter
    def special_tokens(self, val: None | list[str]):
        if val is None:
            self._special_tokens = []
        elif isinstance(val, list):
            self._special_tokens = val
        else:
            raise TypeError("Special tokens should be a list of strings or None, [] empty list")

    def _reset_attributes(self):
        self._vocab = {}
        self._inverse_vocab = {}
        self._words = None
        self._df = None

    def from_list(self, words: list[str]):
        self._reset_attributes()
        for i, token in enumerate(self.special_tokens + words):
            self._vocab[token] = i + 1
            self._inverse_vocab[i + 1] = token
        self._words = self.special_tokens + words

    def from_df(self, df: pd.DataFrame, col: str):
        self._reset_attributes()
        self.from_list(df[col].tolist())
        self._df = df
