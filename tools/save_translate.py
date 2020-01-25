def save_translate(path, translate):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(translate)