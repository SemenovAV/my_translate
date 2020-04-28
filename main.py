import json
import os
from tools.logger import MyLogger
from tools.translate_it import translate_it

with open('app.config.json',encoding='utf8') as f:
    config = json.load(f)
disk_token = config.get('yandex_disk_api_token')
translate_key = config.get('yandex_translate_api_key')

if __name__ == '__main__':
    if disk_token and translate_key:
        directories = 'data'
        result_directories = 'translates'
        from_lng = 'ru'
        log_file = os.path.join(result_directories, 'translate.log')
        for file in os.listdir(directories):
            name = file.split('.')[0]
            result_name = f'{name}-translate-{from_lng}.txt'
            with MyLogger(log_file):
                translate_it(
                    os.path.join(directories, file),
                    result_name,
                    from_lng,
                    name,
                    translate_key,
                    disk_token
                )
