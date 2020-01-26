import requests


def save_yd(filename, **kwargs):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    TOKEN = 'AgAAAAAcYqxYAADLWwWpsXAbJ0eYp9noiVDT8To'
    data = ''
    if kwargs.get('data', False):
        data = kwargs['data'].encode('utf-8')
    elif kwargs.get('path', False):
        with open(kwargs['path'], 'rb', encoding='utf=8') as f:
            data = f.read()
    else:
        return

    headers = {
        'Authorization': f'OAuth {TOKEN}'
    }
    params = {
        'path': filename,
        'overwrite': 'true'
    }
    response = requests.get(URL, headers=headers, params=params)
    json_ = response.json()
    requests.put(json_['href'], data=data)


