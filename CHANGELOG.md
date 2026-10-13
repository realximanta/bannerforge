# changelog

all notable changes to bannerforge are documented here.
format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [0.2.1] — 2026-10-13

### fixed
- `__version__` in `bannerforge/__init__.py` now matches `pyproject.toml`
- LICENSE link in README now uses an absolute GitHub URL so it resolves
  correctly on the PyPI project page

### added
- `Issues` URL in `[project.urls]`

## [0.2.0] — 2026-10-13

### added
- `.render()` for explicit, deterministic output
- `.colors(main, sub)` to override random color picking
- input validation (empty string, type checks)
- render-failure detection via cfonts return value

### changed
- `__del__` now delegates to `.render()` and tracks a `_rendered` flag
  so the banner never prints twice
- errors now print to stderr and re-raise instead of being swallowed

## [0.1.0] — 2026-10-13

### added
- initial release
- `banner(text, subtitle)` with random color picking
- auto-render on `__del__`
- `.left()`, `.right()`, `.center()` subtitle alignment
