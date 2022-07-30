from utils.preprocessing.text.text_cleaner import TextCleaner
import pytest

# I have a list of texts for NLP tasks
texts = [
    "lorem ipsum dolor sit amet", " \t sed ut perspiciatis\n\n",
    "\n\tat vero   \t\t eos et \n \n \t accusamus lorem\r\r"
]

expected_cleaned_texts = [
    "lorem ipsum dolor sit amet", "sed ut perspiciatis", "at vero eos et accusamus lorem"
]

vocab = {
    "lorem": 1,
    "ipsum": 2,
    "dolor": 3,
    "sit": 4,
    "amet": 5,
    "sed": 6,
    "ut": 7,
    "vero": 8,
    "et": 9
}

OOV = '<OOVtoken>'

expected_sequences = [[1, 2, 3, 4, 5], [6, 7, OOV], [OOV, 8, OOV, 9, OOV, 1]]


def test_text_cleaner():
    # I have a list of text for NLP tasks
    # I impoort my utils and initilise the obj
    cln = TextCleaner()

    # suppose that I have my customised regex patterns
    # here is the same as the default patterns
    cln.regex_patterns = cln.default_regex_patterns

    # clean text for tokeniser
    cleaned_texts = [cln.clean(text) for text in texts]
    assert cleaned_texts == expected_cleaned_texts

    # then I pass the cleaned texts to a tokeniser
    tokenised_texts = [text.split(' ') for text in cleaned_texts]
    # I pick most used word in text 'vocab'
    # I set vocab attribute in my cleaner
    # I set OOV token for my cleaner
    cln.vocab = vocab
    cln.out_of_vocab_token = OOV

    # I covert my texts to sequences
    sequences = [cln.text_to_sequence(cleaned_text) for cleaned_text in tokenised_texts]
    assert sequences == expected_sequences

    # train NLP models