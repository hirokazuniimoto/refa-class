from typing import Final

COLOR_DICT: Final = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "end": "\033[0m",
}


class ColorText:
    def __init__(self, text: str):
        self.text = text

    def coloring(self, color: str):
        if color not in COLOR_DICT:
            raise ValueError("color is not defined")
        return COLOR_DICT[color] + self.text + COLOR_DICT["end"]
