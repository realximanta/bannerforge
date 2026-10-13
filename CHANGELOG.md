# changelog

all notable changes to bannerforge are documented here.
format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [0.3.0] — 2026-10-13

### added
- `to_string()` returns the rendered banner without printing
- runtime validation for `.colors()` — invalid names raise `ValueError`
- `tests/` directory with a unit test suite
- CI test gate across Python 3.9, 3.12, 3.13
- tag-to-version validation in the publish workflow

### changed
- `colorama.init()` is now called lazily in `.render()`, not at import
- `.render()` builds the full string before printing so failures
  never produce partial output
- `__del__` is now a fallback only, not the recommended rendering path

### fixed
- duplicate `HELLO` output when subtitle rendering failed after the
  main banner already printed
- version duplication between `pyproject.toml` and `__init__.py` —
  now sourced dynamically from `bannerforge.__version__`

## [0.2.1] — 2026-10-13

### fixed
- `__version__` in `bannerforge/__init__.py` now matches `pyproject.toml`
- LICENSE link in README now uses an absolute GitHub URL

### added
- `Issues` URL in `[project.urls]`

## [0.2.0] — 2026-10-13

### added
- `.render()` for explicit, deterministic output
- `.colors(main, sub)` to override random color picking
- input validation (empty string, type checks)
- render-failure detection via cfonts return value

## [0.1.0] — 2026-10-13

### added
- initial release
- `banner(text, subtitle)` with random color picking
- auto-render on `__del__`
- `.left()`, `.right()`, `.center()` subtitle alignment
