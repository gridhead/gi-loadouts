from io import BytesIO

from PIL import Image, ImageEnhance, ImageFilter
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


def modify_graphics_resource(path: str, radius: float = 2.5, shadow: float = 0.5) -> QPixmap:
    """
    Modify graphics resource using Python Image Library before it is displayed on the user interface

    :param shadow: Intensity of brightness effect to be applied on the image
    :param radius: Width of Gaussian Blur effect to be applied on the image
    :param path: Path to the imported image file in the resource
    :return: Pixmap created on transformation for user interface
    """
    resource = QResource(path)
    data = resource.data()
    iobt = BytesIO(data)
    proc = Image.open(iobt).convert("RGBA").filter(ImageFilter.GaussianBlur(radius=radius))
    proc = ImageEnhance.Brightness(proc).enhance(shadow)
    qimg = QImage(proc.tobytes(), proc.width, proc.height, QImage.Format_RGBA8888)
    rtrn = QPixmap.fromImage(qimg)
    return rtrn


def modify_datatype_to_transfer(text: str = ""):
    if text.strip() == "":
        rtrn = 0.0
    else:
        try:
            rtrn = float(text)
        except ValueError:
            rtrn = 0.0
    return rtrn
