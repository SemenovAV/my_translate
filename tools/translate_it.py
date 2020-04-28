import requests, json
from tools.get_text import get_text
from tools.save_translate import save_translate
from tools.save_yd import save_yd


def translate_it(path_text_file, name_translate_file, from_lang, to_lang, translate_api_key, disk_api_token):
    """
     Функция переводит текст с помощью он-лайн переводчика яндека и с сохранением переведеного на яндекс диск.

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param path_text_file: str Имя файла который требуется перевести
    :param name_translate_file: str Как назвать файл с переводом
    :param from_lang: str С которого языка переводить
    :param to_lang: str На который.
    :param disk_api_token: str OAuth-токен апи яндекс диска.
    :param translate_api_key: str API-key переводчика яндекса.
    :return:
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': translate_api_key,
        'text': get_text(path_text_file),
        'lang': from_lang.format(to_lang),
    }
    try:
        response = requests.get(url, params=params)
    except requests.exceptions.BaseHTTPError as e:
        raise Exception(f'Translate-it:{e}')
    json_ = response.json()
    translate = ''.join(json_['text'])
    save_yd(name_translate_file, disk_api_token, data=translate)
    save_translate(name_translate_file, translate, 'translates')
