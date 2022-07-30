from utils.preprocessing.text.vocabulary import Vocabulary
import pytest
import pandas as pd

OOV_TOKEN = '<OOV>'
SPECIAL_TOKENS = [OOV_TOKEN]


@pytest.fixture
def vocab():
    return Vocabulary()


def test_initialise_vocab_obj_without_error():
    vocab = Vocabulary()


def test_vocab_default_attributes(vocab):
    assert vocab.special_tokens == SPECIAL_TOKENS

    # these attributes should be protected
    # it will only be updated by special methods, eg from_list and from_data_frame
    assert vocab.vocab == {}
    assert vocab.inverse_vocab == {}
    # return a list of words, input dataframe
    assert vocab.words == None
    assert vocab.df == None


def test_if_there_is_no_special_token_words_should_start_at_index_one(vocab):
    vocab.special_tokens = None
    words = ['a', 'b']
    expected_vocab = {'a': 1, 'b': 2}
    vocab.from_list(words)
    assert vocab.vocab == expected_vocab
    # the vocabulary function should handle special_tokens as list
    # in order to be able to concat with another list
    assert vocab.special_tokens == []
    assert vocab.inverse_vocab == {1: 'a', 2: 'b'}


def test_special_tokens_should_come_first_then_words(vocab):
    words = ['a', 'b']
    expected_vocab = {OOV_TOKEN: 1, 'a': 2, 'b': 3}
    vocab.from_list(words)
    assert vocab.vocab == expected_vocab
    assert vocab.words == [OOV_TOKEN] + words
    # if vocabulary is not create from df, df should be None
    assert vocab.df is None
    assert vocab.inverse_vocab == {1: OOV_TOKEN, 2: 'a', 3: 'b'}


def test_there_are_more_than_one_special_tokens(vocab):
    words = ['a', 'b']
    special_tokens = ['<oov>', '<punct>']
    vocab.special_tokens = special_tokens
    vocab.from_list(words)
    assert vocab.vocab == {'<oov>': 1, '<punct>': 2, 'a': 3, 'b': 4}


def test_import_vocabulary_from_dataframe(vocab):
    # clas private methods
    df = pd.DataFrame({'word': ['a', 'b'], 'freq': [10, 9]})
    vocab.from_df(df, col='word')
    assert vocab.vocab == {OOV_TOKEN: 1, 'a': 2, 'b': 3}
    assert vocab.words == [OOV_TOKEN] + df['word'].tolist()
    assert (vocab.df == df).all