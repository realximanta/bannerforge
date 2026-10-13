import sys
import pytest
from bannerforge import banner, __version__
from bannerforge.logo import VALID_COLORS


def test_version_exists():
    assert __version__ == "0.3.0"


def test_basic_render():
    b = banner("HELLO", "World")
    output = b.to_string()
    assert "HELLO" in output
    assert "World" in output


def test_no_subtitle():
    b = banner("HELLO")
    output = b.to_string()
    assert "HELLO" in output


def test_empty_text_raises():
    with pytest.raises(ValueError):
        banner("")


def test_whitespace_text_raises():
    with pytest.raises(ValueError):
        banner("   ")


def test_non_string_text_raises():
    with pytest.raises(TypeError):
        banner(123)


def test_non_string_subtitle_raises():
    with pytest.raises(TypeError):
        banner("HELLO", 123)


def test_custom_colors_valid():
    b = banner("HELLO", "World").colors("cyan", "yellow")
    output = b.to_string()
    assert "HELLO" in output


def test_custom_colors_invalid():
    with pytest.raises(ValueError):
        banner("HELLO").colors("notacolor", "yellow")


def test_custom_colors_non_string():
    with pytest.raises(TypeError):
        banner("HELLO").colors(123, "yellow")


def test_idempotent_render(capsys):
    b = banner("HELLO", "World")
    b.render()
    b.render()  # second call should do nothing
    captured = capsys.readouterr()
    assert captured.out.count("HELLO") == 1


def test_alignment_methods():
    b = banner("HELLO", "World")
    assert b.left().align == "left"
    assert b.right().align == "right"
    assert b.center().align == "center"
    assert b.centre().align == "center"
