import os
from tools.logger import MyLogger
from translate_it import translate_it

if __name__ == '__main__':
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
                os.path.join(result_directories, result_name),
                from_lng,
                name
            )
