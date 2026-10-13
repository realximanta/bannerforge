import random
import sys

from cfonts import render
from colorama import init

VALID_COLORS = {
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "gray",
    "boldblack", "boldred", "boldgreen", "boldyellow", "boldblue",
    "boldmagenta", "boldcyan", "boldwhite",
}

COLOR_COMBOS = [
    ("green", "yellow"), ("magenta", "red"), ("blue", "cyan"),
    ("white", "gray"), ("red", "magenta"), ("yellow", "green"),
    ("cyan", "green"), ("blue", "magenta"), ("yellow", "red"),
    ("cyan", "yellow"), ("green", "blue"), ("magenta", "yellow"),
    ("red", "blue"), ("white", "cyan"), ("gray", "magenta"),
    ("green", "red"), ("blue", "yellow"), ("cyan", "red"),
    ("white", "green"), ("magenta", "cyan"), ("red", "yellow"),
    ("green", "cyan"), ("blue", "green"),
]


class Banner:
    def __init__(self, text, subtitle=""):
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if not isinstance(subtitle, str):
            raise TypeError("subtitle must be a string")
        if not text.strip():
            raise ValueError("text cannot be empty")

        self.text = text
        self.subtitle = subtitle
        self.align = "right"
        self._custom_colors = None
        self._rendered = False

    def left(self):
        self.align = "left"
        return self

    def right(self):
        self.align = "right"
        return self

    def center(self):
        self.align = "center"
        return self

    centre = center

    def colors(self, main_color, sub_color):
        for color in (main_color, sub_color):
            if not isinstance(color, str):
                raise TypeError("color names must be strings")
            if color.lower() not in VALID_COLORS:
                raise ValueError(
                    f"invalid color '{color}'. "
                    f"supported: {', '.join(sorted(VALID_COLORS))}"
                )
        self._custom_colors = (main_color, sub_color)
        return self

    def to_string(self):
        if self._custom_colors:
            main_colors, sub_colors = self._custom_colors
        else:
            main_colors, sub_colors = random.sample(COLOR_COMBOS, 2)

        # cfonts iterates over strings, so wrap in list to avoid treating
        # "cyan" as ["c", "y", "a", "n"]
        if isinstance(main_colors, str):
            main_colors = [main_colors]
        if isinstance(sub_colors, str):
            sub_colors = [sub_colors]

        main = render(
            self.text,
            colors=main_colors,
            align="center",
            font="block",
            background="black",
        )
        if not main:
            raise ValueError(f"cfonts failed to render text: {self.text!r}")

        output = main

        if self.subtitle:
            sub = render(
                self.subtitle,
                colors=sub_colors,
                align=self.align,
                font="console",
                background="black",
            )
            if not sub:
                raise ValueError(f"cfonts failed to render subtitle: {self.subtitle!r}")
            output += sub

        return output

    def render(self):
        if self._rendered:
            return

        init(autoreset=True)

        output = self.to_string()

        print(output, end="")
        self._rendered = True

    def __del__(self):
        # check attr in case __init__ failed before setting _rendered
        if not getattr(self, '_rendered', True):
            try:
                self.render()
            except Exception:
                pass


def banner(text, subtitle=""):
    return Banner(text, subtitle)
