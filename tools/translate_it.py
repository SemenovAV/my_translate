import requests
from tools.get_text import get_text
from tools.save_translate import save_translate
from tools.save_yd import save_yd

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_it(path_text_file, name_translate_file, from_lang, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param name_translate_file:
    :param path_text_file:
    :param from_lang:
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': get_text(path_text_file),
        'lang': from_lang.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    translate = ''.join(json_['text'])
    save_yd(name_translate_file, data=translate)
    save_translate(name_translate_file, translate, 'translates')
