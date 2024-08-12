def truncate_text(text: str = "", qant: int = 36):
    if len(text) > qant:
        text = f"{text[0:qant-3]}..."
    return text

