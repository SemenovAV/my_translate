def get_text(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    return text
