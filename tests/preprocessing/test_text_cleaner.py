from bleach import clean
from utils.preprocessing.text.text_cleaner import TextCleaner
import pytest

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


def test_initialise_obj_without_problem():
    cleaner = TextCleaner()
    assert isinstance(cleaner, TextCleaner)


def test_default_instance_attributes():
    cleaner = TextCleaner()
    # None do not drop stop words
    assert cleaner.stop_words is None
    assert cleaner.delimiter == '|'
    # if regex_patterns is not set use default patterns
    assert cleaner.regex_patterns is None
    # add more patterns here
    assert cleaner.default_regex_patterns == DEFAULT_REGEX_PATTERNS
    assert cleaner.vocab is None
    assert cleaner.out_of_vocab_token == OOV_TOKEN


###
# test protected attributes
###
def test_default_regex_should_not_be_able_to_set():
    cleaner = TextCleaner()
    with pytest.raises(AttributeError):
        cleaner.default_regex_patterns = CUSTOMISED_PATTERN


# regex_patterns is protected
def test_customised_patterns_setter():
    cleaner = TextCleaner()
    cleaner.regex_patterns = CUSTOMISED_PATTERN


def test_inverse_vocab_should_not_be_able_to_set():
    cleaner = TextCleaner()
    with pytest.raises(AttributeError):
        cleaner.inverse_vocab = {1: 'inverse', 2: 'vocab'}


def test_inverse_vocab_should_be_matched_with_vocab():
    cleaner = TextCleaner()
    cleaner.vocab = {'this': 1, 'is': 2, 'vocab': 3}
    assert cleaner.inverse_vocab == {1: 'this', 2: 'is', 3: 'vocab'}


def test_regex_function_should_use_default_regex_if_patterns_is_none():
    cleaner = TextCleaner()
    assert cleaner._get_regex_patterns() == DEFAULT_REGEX_PATTERNS


def test_regex_function_should_use_customised_patterns_if_it_is_not_none():
    cleaner = TextCleaner()
    cleaner.regex_patterns = CUSTOMISED_PATTERN
    assert cleaner._get_regex_patterns() == CUSTOMISED_PATTERN


def test_cleaned_text_should_not_contain_leading_and_ending_spaces():
    cleaner = TextCleaner()
    expected = "text to clean"

    assert cleaner.clean(f"  {expected}  ") == expected
    assert cleaner.clean(f"\n{expected}\n") == expected
    assert cleaner.clean(f"\t{expected}\t") == expected
    assert cleaner.clean(f"\n\t{expected}\t\n") == expected


# TODO: Add more regex patterns test
def test_cleaned_text_should_not_contain_multiple_spaces_inside():
    cleaner = TextCleaner()
    assert cleaner.clean("text\t\nto  \r\nclean") == "text to clean"


def test_n_gram_function():
    words = ['a', 'b', 'c']
    n = 2
    cleaner = TextCleaner()
    n_grams = cleaner.generate_n_gram(words, n)
    assert n_grams == [('a', 'b'), ('b', 'c')]


def test_n_gram_function_if_n_is_equal_to_the_number_of_words():
    words = ['a', 'b', 'c']
    n = len(words)
    cleaner = TextCleaner()
    n_grams = cleaner.generate_n_gram(words, n)
    assert n_grams == [tuple(words)]


def test_invalid_n_n_is_less_than_one_in_n_gram_generator():
    with pytest.raises(ValueError):
        words = ['a', 'b', 'c']
        n = 0
        cleaner = TextCleaner()
        n_grams = cleaner.generate_n_gram(words, n)
        assert n_grams == [('a', 'b'), ('b', 'c')]


def test_invalid_n_n_is_larger_than_the_number_of_words():
    with pytest.raises(ValueError):
        words = ['a', 'b', 'c']
        n = 4
        cleaner = TextCleaner()
        n_grams = cleaner.generate_n_gram(words, n)


def test_remove_stop_words_should_do_nothing_if_stop_words_is_none():
    cleaner = TextCleaner()
    # default value of stop words is none
    # do nothing
    words = ['a', 'b', 'c']
    assert cleaner.remove_stop_words(words) == words


def test_remove_stop_words_should_work_properly():
    cleaner = TextCleaner()
    words = ['a', 'b', 'c', 'd']
    stop_words = ['a', 'c']
    cleaner.stop_words = stop_words
    assert cleaner.remove_stop_words(words) == ['b', 'd']


def test_join_words_with_delimiter():
    cleaner = TextCleaner()
    words = ['a', 'b', 'c', 'd']
    delimiter_splited_text = 'a|b|c|d|'
    return cleaner.join(words) == delimiter_splited_text


def test_if_vocab_is_none_raise_error():
    words = ['a', 'b', 'c', 'd']
    cleaner = TextCleaner()
    with pytest.raises(AttributeError):
        cleaner.text_to_sequence(words)


def test_convert_tokenised_text_to_sequence_of_indices():
    cleaner = TextCleaner()
    words = ['a', 'b', 'c', 'd']
    vocab = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    sequence = [1, 2, 3, 4]
    cleaner.vocab = vocab
    assert cleaner.text_to_sequence(words) == sequence


def test_convert_text_to_sequence_out_of_vocab_token():
    cleaner = TextCleaner()
    words = ['a', 'qwert', 'b', 'c', 'd', 'out of vocab']
    vocab = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    sequence = [1, OOV_TOKEN, 2, 3, 4, OOV_TOKEN]
    cleaner.vocab = vocab
    assert cleaner.text_to_sequence(words) == sequence


def test_convert_sequence_to_text():
    cleaner = TextCleaner()
    words = ['a', 'b', 'c', 'd']
    vocab = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    sequence = [1, 2, 3, 4]
    cleaner.vocab = vocab
    assert cleaner.sequence_to_text(sequence) == words


def test_convert_text_to_sequence_out_of_vocab_token():
    cleaner = TextCleaner()
    vocab = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    sequence = [1, OOV_TOKEN, 2, 3, 4, OOV_TOKEN]
    cleaner.vocab = vocab
    assert cleaner.sequence_to_text(sequence) == ['a', OOV_TOKEN, 'b', 'c', 'd', OOV_TOKEN]