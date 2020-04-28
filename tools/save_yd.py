import requests


def save_yd(filename, token, data='', path=False):
    """
    Функция сохраняет переданный файл или текстовые данные на яндекс диск
    :param filename: str Имя файла
    :param token: str OAuth-токен яндекс диска.
    :param path: str Путь к файлу.
    :param data: str Текст
    :return:
    """
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    if data:
        data = data.encode('utf-8')
    elif path:
        with open(path, 'rb', encoding='utf=8') as f:
            data = f.read()
    else:
        return

    headers = {
        'Authorization': f'OAuth {token}'
    }
    params = {
        'path': filename,
        'overwrite': True
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        json_ = response.json()
        requests.put(json_['href'], data=data)
        return True
    except requests.exceptions.BaseHTTPError as e:
        return False
