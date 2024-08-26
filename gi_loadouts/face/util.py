def truncate_text(text: str = "", qant: int = 30) -> str:
    """
    Truncate the provided text to the provided length limit if the length exceeds the length limit before returning it

    :param text:
    :param qant:
    :return:
    """
    if len(text) > qant:
        text = f"{text[0:qant-3]}..."
    return text
