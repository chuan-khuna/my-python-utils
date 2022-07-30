from utils.preprocessing.text.text_cleaner import TextCleaner
from utils.preprocessing.text.vocabulary import Vocabulary
import pytest
from unittest.mock import patch, MagicMock, Mock

################################
# regex note
################################
# \n, \r \t -> white space
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
CUSTOMISED_PATTERN = [(r'\s', 'new pattern')]


def generate_mock_vocab(special_tokens=[]):
    words = ['a', 'b', 'c', 'd']
    if special_tokens:
        words = special_tokens + words
    vocab = {k: i + 1 for i, k in enumerate(words)}
    inverse_vocab = {i + 1: k for i, k in enumerate(words)}
    return words, vocab, inverse_vocab


@pytest.fixture
def cleaner():
    cleaner = TextCleaner()
    yield cleaner
    del cleaner


def test_initialise_obj_without_any_problems(cleaner):
    assert isinstance(cleaner, TextCleaner)


def test_default_attributes(cleaner):
    # if stop words is None then do nothing(= return the input)
    # if regex patterns is None then use the default one, the default one is protected
    assert cleaner.stop_words is None
    assert cleaner.delimiter == '|'
    assert cleaner.regex_patterns is None
    assert cleaner.default_regex_patterns == DEFAULT_REGEX_PATTERNS
    assert cleaner.vocab is None
    assert cleaner.out_of_vocab_token == OOV_TOKEN


################################
# test protected attributes
################################
def test_default_regex_should_be_protected(cleaner):
    with pytest.raises(AttributeError):
        # try to overide default patterns
        # default patterns are used as reference
        cleaner.default_regex_patterns = []


def test_customised_patterns_setter(cleaner):
    # this attribute has the setter method
    cleaner.regex_patterns = CUSTOMISED_PATTERN


def test_regex_function_should_use_default_regex_if_patterns_is_none(cleaner):
    assert cleaner._get_regex_patterns() == cleaner.default_regex_patterns


def test_regex_function_should_use_customised_patterns_if_it_is_not_none(cleaner):
    cleaner.regex_patterns = CUSTOMISED_PATTERN
    assert cleaner._get_regex_patterns() == cleaner.regex_patterns


def test_cleaned_text_should_not_contain_leading_and_ending_spaces(cleaner):
    expected = "text to clean"
    assert cleaner.clean(f"  {expected}  ") == expected
    assert cleaner.clean(f"\n{expected}\n") == expected
    assert cleaner.clean(f"\t{expected}\t") == expected
    assert cleaner.clean(f"\n\t{expected}\t\n") == expected


# TODO: Add more regex patterns test
def test_cleaned_text_should_not_contain_multiple_spaces_inside(cleaner):
    assert cleaner.clean("text\t\nto \t \r\nclean") == "text to clean"


def test_n_gram_function(cleaner):
    words = ['a', 'b', 'c']
    n = 2
    n_grams = cleaner.generate_n_gram(words, n)
    assert n_grams == [('a', 'b'), ('b', 'c')]


def test_n_gram_function_if_n_is_equal_to_the_number_of_words(cleaner):
    words = ['a', 'b', 'c']
    n = len(words)
    n_grams = cleaner.generate_n_gram(words, n)
    assert n_grams == [tuple(words)]


def test_invalid_n_n_is_less_than_one_in_n_gram_generator(cleaner):
    with pytest.raises(ValueError):
        words = ['a', 'b', 'c']
        n = 0
        cleaner.generate_n_gram(words, n)


def test_invalid_n_n_is_larger_than_the_number_of_words(cleaner):
    with pytest.raises(ValueError):
        words = ['a', 'b', 'c']
        n = 4
        cleaner.generate_n_gram(words, n)


def test_remove_stop_words_should_do_nothing_if_stop_words_is_none(cleaner):
    # default value of stop words is none
    # do nothing
    words = ['a', 'b', 'c']
    assert cleaner.remove_stop_words(words) == words


def test_remove_stop_words_should_work_properly(cleaner):
    words = ['a', 'b', 'c', 'd']
    stop_words = ['a', 'c']
    cleaner.stop_words = stop_words
    assert cleaner.remove_stop_words(words) == ['b', 'd']


def test_join_words_with_delimiter(cleaner):
    words = ['a', 'b', 'c', 'd']
    delimiter_splited_text = 'a|b|c|d'
    assert cleaner.join(words) == delimiter_splited_text


def test_text_to_sequence_will_raise_error_if_vocab_is_none(cleaner):
    # the default value of vocab is None
    words = ['a', 'b', 'c', 'd']
    with pytest.raises(AttributeError):
        cleaner.text_to_sequence(words)


def test_sequence_to_text_will_raise_error_if_inverse_vocab_is_none(cleaner):
    sequence = [1, 2, 3, 4]
    with pytest.raises(AttributeError):
        cleaner.sequence_to_text(sequence)


def test_convert_tokenised_text_to_sequence_of_indices(cleaner):
    # assume that we tokenise text into words
    # then we have already created vocab obj.

    # this test start with OOV is not included in vocabulary
    # and all words are in vocabulary
    words, vocab, inverse_vocab = generate_mock_vocab()
    # Mocking Vocabulary class
    vocab_mock = Mock(vocab=vocab, inverse_vocab=inverse_vocab)

    expected_sequence = [1, 2, 3, 4]
    cleaner.vocab = vocab_mock.vocab
    assert cleaner.text_to_sequence(words) == expected_sequence


def test_convert_text_to_sequence_with_OOV_token(cleaner):

    # What if a text contains words that are not in dictionary?
    # and OOV token is also not in dictionary
    words, vocab, inverse_vocab = generate_mock_vocab()
    text = ['a', 'qwert', 'b', 'c', 'd', 'out of vocab']
    vocab_mock = Mock(vocab=vocab, inverse_vocab=inverse_vocab)
    cleaner.vocab = vocab_mock.vocab
    expected_sequence = [1, OOV_TOKEN, 2, 3, 4, OOV_TOKEN]
    assert cleaner.text_to_sequence(text) == expected_sequence

    # Tensorflow's OOV token is set to index 1 ref: preprocessing.text.Tokenizer
    # OOV token is in vocabulary
    words, vocab, inverse_vocab = generate_mock_vocab([OOV_TOKEN])
    vocab_mock = Mock(vocab=vocab, inverse_vocab=inverse_vocab)
    cleaner.vocab = vocab_mock.vocab
    assert cleaner.text_to_sequence(text) == [2, 1, 3, 4, 5, 1]


def test_convert_sequence_to_text(cleaner):
    # all words are in vocabulary and OOV is not in vocabulary
    words, vocab, inverse_vocab = generate_mock_vocab()
    vocab_mock = Mock(vocab=vocab, inverse_vocab=inverse_vocab)
    sequence = [1, 2, 3, 4]
    expected_words = words
    cleaner.vocab = vocab_mock.vocab
    assert cleaner.sequence_to_text(sequence) == expected_words


def test_convert_sequence_to_text_with_out_of_vocab_token(cleaner):

    # OOV is not in vocabulary
    words, vocab, inverse_vocab = generate_mock_vocab()
    vocab_mock = Mock(vocab=vocab, inverse_vocab=inverse_vocab)
    sequence = [1, OOV_TOKEN, 2, 3, 4, OOV_TOKEN]
    cleaner.vocab = vocab_mock.vocab
    assert cleaner.sequence_to_text(sequence) == ['a', OOV_TOKEN, 'b', 'c', 'd', OOV_TOKEN]

    # OOV is in vocabulary
    words, vocab, inverse_vocab = generate_mock_vocab([OOV_TOKEN])
    vocab_mock = Mock(vocab=vocab, inverse_vocab=inverse_vocab)
    cleaner.vocab = vocab_mock.vocab
    assert cleaner.sequence_to_text([2, 1, 3]) == ['a', OOV_TOKEN, 'b']