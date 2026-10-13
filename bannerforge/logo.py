import random
import sys

from cfonts import render
from colorama import init

init(autoreset=True)

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
        """
        Override random colors.
        Pass valid cfonts color names like 'green', 'cyan', 'boldred'.
        """
        self._custom_colors = (main_color, sub_color)
        return self

    def render(self):
        """
        Explicitly render the banner.
        Call this instead of relying on __del__ if you need deterministic
        output, reproducible tests, or precise timing.
        """
        if self._rendered:
            return

        try:
            if self._custom_colors:
                main_colors, sub_colors = self._custom_colors
            else:
                main_colors, sub_colors = random.sample(COLOR_COMBOS, 2)

            main = render(
                self.text,
                colors=list(main_colors),
                align="center",
                font="block",
                background="black",
            )
            
            if not main:
                raise ValueError(
                    f"cfonts failed to render text: {self.text!r}"
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
                if not sub:
                    raise ValueError(
                        f"cfonts failed to render subtitle: {self.subtitle!r}"
                    )
                print(sub, end="")

            self._rendered = True

        except Exception as e:
            # Print to stderr instead of silently swallowing.
            # Use a plain message so it's readable in CI logs.
            print(f"bannerforge: render failed: {e}", file=sys.stderr)
            raise

    def __del__(self):
        # Fallback magic: if the user didn't call .render() explicitly,
        # try to print on destruction. Swallow errors here because
        # __del__ during interpreter shutdown can crash.
        if not self._rendered:
            try:
                self.render()
            except Exception:
                pass


def banner(text, subtitle=""):
    return Banner(text, subtitle)
