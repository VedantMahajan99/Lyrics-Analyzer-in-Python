import nltk

#----------------------------------------------------- Uncomment to download libraries/packages-----------------------------------------------------
# import nltk
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()
#-----------------------------------------------------------------------------------------------------------------------------------------------------

from nltk.tokenize import PunktSentenceTokenizer, word_tokenize


def word_sentence_tokenize(text):
    # create a PunktSentenceTokenizer
    sentence_tokenizer = PunktSentenceTokenizer(text)

    # sentence tokenize text
    sentence_tokenized = sentence_tokenizer.tokenize(text)

    # create a list to hold word tokenized sentences
    word_tokenized = list()

    # for-loop through each tokenized sentence in sentence_tokenized
    for tokenized_sentence in sentence_tokenized:
        # word tokenize each sentence and append to word_tokenized (lists o lists containing tokenized sentences)
        word_tokenized.append(word_tokenize(tokenized_sentence))

    return word_tokenized