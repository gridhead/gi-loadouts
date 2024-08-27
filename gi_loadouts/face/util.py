from io import BytesIO

from PIL import Image, ImageEnhance, ImageFilter, UnidentifiedImageError
from PySide6.QtCore import QResource
from PySide6.QtGui import QImage, QPixmap


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


def modify_graphics_resource(path) -> QPixmap:
    """
    Modify graphics resource using Python Image Library before it is displayed on the user interface

    :param path: Path to the imported image file in the resource
    :return: Pixmap created on transformation for user interface
    """
    try:
        resource = QResource(path)
        data = resource.data()
        iobt = BytesIO(data)
        proc = Image.open(iobt).convert("RGBA").filter(ImageFilter.GaussianBlur(radius=2.5))
        proc = ImageEnhance.Brightness(proc).enhance(0.5)
        qimg = QImage(proc.tobytes(), proc.width, proc.height, QImage.Format_RGBA8888)
        rtrn = QPixmap.fromImage(qimg)
    except UnidentifiedImageError:
        rtrn = QPixmap(path)
    return rtrn
