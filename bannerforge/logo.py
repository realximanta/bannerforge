import random

from cfonts import render
from colorama import init

init(autoreset=True)

# (main, subtitle) color pairs. random.sample picks two per call.
COLOR_COMBOS = [
    ("green", "yellow"),
    ("magenta", "red"),
    ("blue", "cyan"),
    ("white", "gray"),
    ("red", "magenta"),
    ("yellow", "green"),
    ("cyan", "green"),
    ("blue", "magenta"),
    ("yellow", "red"),
    ("cyan", "yellow"),
    ("green", "blue"),
    ("magenta", "yellow"),
    ("red", "blue"),
    ("white", "cyan"),
    ("gray", "magenta"),
    ("green", "red"),
    ("blue", "yellow"),
    ("cyan", "red"),
    ("white", "green"),
    ("magenta", "cyan"),
    ("red", "yellow"),
    ("green", "cyan"),
    ("blue", "green"),
]


class Banner:
    def __init__(self, text, subtitle=""):
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if not isinstance(subtitle, str):
            raise TypeError("subtitle must be a string")

        self.text = text
        self.subtitle = subtitle
        self.align = "right"

    def left(self):
        self.align = "left"
        return self

    def right(self):
        self.align = "right"
        return self

    def center(self):
        self.align = "center"
        return self

    # brits keep typing it wrong, so
    centre = center

    def _render(self):
        main_colors, sub_colors = random.sample(COLOR_COMBOS, 2)

        main = render(
            self.text,
            colors=list(main_colors),
            align="center",
            font="block",
            background="black",
        )
        print(main, end="")

        if self.subtitle:
            sub = render(
                self.subtitle,
                colors=list(sub_colors),
                align=self.align,
                font="console",
                background="black",
            )
            print(sub, end="")

    def __del__(self):
        # __del__ fires when the object is GC'd. since the user usually
        # doesn't bind the return value, this prints immediately and
        # saves them from wrapping everything in print().
        # wrapped in try/except because __del__ during interpreter
        # shutdown can blow up if stdout is already closed.
        try:
            self._render()
        except Exception:
            pass


def banner(text, subtitle=""):
    return Banner(text, subtitle)
