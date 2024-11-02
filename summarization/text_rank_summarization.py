
# импортируем модуль sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


def sum_text(SENTENCES_COUNT: int, text_input: str) -> str:

    """

    :param SENTENCES_COUNT:
    :param text_input:
    :return: text

    Функция реализует сжатие текстом методом TextRank с помощью библиотеки sumy, которая предоставляет большой функционал для
    работы с суммаризацией текста. На вход падается SENTENCES_COUNT - количество предложений на выход, text_input -
    исходный текст для суммаризации. Возвращает text - сжатый текст
    """

    # задаем язык и количество предложений в резюме
    LANGUAGE = 'russian'

    # создаем парсер и суммаризатор
    parser = PlaintextParser.from_string(text_input, Tokenizer(LANGUAGE))

    stemmer = Stemmer(LANGUAGE)
    summarizer = TextRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)  # задаем стоп слова

    text = ''       # итоговый сжатый текст
    # выводим резюме
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        text += str(sentence)

    return text