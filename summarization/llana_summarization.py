# импорт библиотеки llana_cpp
from llama_cpp import Llama
def llana_model(file_path: str,
                count_sentences: int,
                model_path = 'C:/Users/User/.cache/lm-studio/models/IlyaGusev/saiga_mistral_7b_gguf/model-q4_K.gguf'
                ) -> str:
    """

    :param text:
    :param count_sentences:
    :return: res["choices"][0]["text"]

    Данная функция реализует суммаризацию текста с помощью модели Llana, модели которой являются open-source. На вход
    функции передаются text - текст для сжатия, и count_sentences - количество предложений, которые будут в итогов
    сжатом тексте, а возвращается str, которая является сжатым текстом. Модель является довольно производительной,
    поэтому для запуска рекомендуется использовать мощный сервер.
    """




    # указываем путь до модели llana, которая умеет работать с русским текстом

    # Инициализируем модель
    llm = Llama(
        model_path=model_path,   # путь до модели
        n_ctx=16000,  # Длина контекста
        n_threads=20,            # Количество потоков CPU, которые может использовать модель
        n_gpu_layers=0        # количество слоев, которые будут выгружаться на GPU (-1 - все слои)
    )

    # Генерация kwargs для передачи модели
    generation_kwargs = {
        "max_tokens": 20000,    # количество токенов
        "stop": ["</s>"],      # остановка модели (Ctrl + S)
        "echo": False,    # Выводить prompt обратно
        "top_k": 1    # Параметр жадного декодирования. Если > 1, то будет происходить выборочное декодирование
    }

    string_text = ''
    with open(file_path, 'r')as file:
        for i in file:
            string_text += i

    # Создание prompt
    prompt = f"Суммаризируй данный текст до {count_sentences} предложений, мне очень сильно это надо\n" + string_text
    res = llm(prompt, **generation_kwargs)  # Результат - словарь

    # Получение параметра текста и его возврат
    return res["choices"][0]["text"]