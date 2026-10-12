# bannerforge

Colorful terminal banners. One line, one print, done.

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

### alignment

```python
banner("HELLO", "World").left()
banner("HELLO", "World").right()
banner("HELLO", "World").center()
```

Only the subtitle moves. The main text is always centered.

### no subtitle

```python
banner("HELLO")
```

## how it works

The banner object renders itself in `__del__`. When you don't bind the
return value, Python drops the reference immediately and the banner
prints. If you *do* bind it, the banner waits until the variable goes
out of scope.

```python
# prints immediately
banner("HELLO", "World")

# prints when x goes out of scope / program ends
x = banner("HELLO", "World")
```

## license

Custom Attribution License — see [LICENSE](./LICENSE).

You can use, modify, and redistribute this code freely. If you do, you
must credit **Himanta Bhuyan** and link back to this repository.

## author

Himanta Bhuyan — [@realximanta](https://github.com/realximanta)
