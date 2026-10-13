# bannerforge

<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/bannerforge.png?style=flat-square&color=0A66C2&labelColor=0A66C2&logo=pypi&logoColor=white&cacheSeconds=300&v=0.2.1)](https://pypi.org/project/bannerforge/)
[![License](https://img.shields.io/badge/license-Attribution-2ea44f.png?style=flat-square&color=2ea44f&labelColor=2ea44f&logo=opensourceinitiative&logoColor=white)](./LICENSE)

</div>

**Colorful terminal banners. One line, one print, done.**

```
██╗  ██╗███████╗██╗     ██╗      ██████╗
██║  ██║██╔════╝██║     ██║     ██╔═══██╗
███████║█████╗  ██║     ██║     ██║   ██║
██╔══██║██╔══╝  ██║     ██║     ██║   ██║
██║  ██║███████╗███████╗███████╗╚██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝
                                      World
```

## install

```bash
pip install bannerforge
```

## usage

```python
from bannerforge import banner

banner("HELLO", "World")
```

That's it. No `print()`, no assignment, no ceremony. The banner renders on
its own.

### explicit rendering

If you need deterministic timing — tests, CI, precise control — call
`.render()` explicitly:

```python
banner("HELLO", "World").render()
```

This bypasses the `__del__` magic and prints immediately. Once rendered,
the object won't render again.

### rendering to a string

If you need the banner as a string instead of printed output:

```python
output = banner("HELLO", "World").to_string()
print(output)
```

### alignment

```python
banner("HELLO", "World").left()
banner("HELLO", "World").right()
banner("HELLO", "World").center()
```

Only the subtitle moves. The main text is always centered.

### custom colors

By default a random color pair is picked each call. To pin them:

```python
banner("HELLO", "World").colors("cyan", "yellow").render()
```

Valid colors are the same ones `cfonts` accepts: `black`, `red`, `green`,
`yellow`, `blue`, `magenta`, `cyan`, `white`, `gray`, and their `bold*`
variants (e.g. `boldred`).

### no subtitle

```python
banner("HELLO")
```

### error handling

If rendering fails, `bannerforge` raises an exception and prints a clear
message to stderr. You can catch it if you want:

```python
try:
    banner("").render()
except ValueError as e:
    print(f"caught: {e}")
```

The `__del__` fallback swallows errors silently (to avoid interpreter
shutdown crashes), so for reliable error reporting always use `.render()`.

## how it works

The banner object normally renders itself in `__del__`. When you don't
bind the return value, Python drops the reference immediately and the
banner prints. If you *do* bind it, the banner waits until the variable
goes out of scope.

```python
# prints immediately
banner("HELLO", "World")

# prints when x goes out of scope / program ends
x = banner("HELLO", "World")
```

For predictable behavior, prefer `.render()`. It makes the output timing
explicit and surfaces any rendering errors.

## license

Custom Attribution License — see [LICENSE](https://github.com/realximanta/bannerforge/blob/main/LICENSE).

You can use, modify, and redistribute this code freely. If you do, you
must credit **Himanta Bhuyan** and link back to this repository.

## author

Himanta Bhuyan — [@realximanta](https://github.com/realximanta)
