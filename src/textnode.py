from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text: str, text_type: enumerate, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target: object) -> bool:
        if self.text == target.text and self.text_type == target.text_type and self.url == target.url:
            return True
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"