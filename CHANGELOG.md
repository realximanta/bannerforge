# changelog

all notable changes to bannerforge are documented here.
format loosely follows [Keep a Changelog](https://keepachangelog.com/).

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

## [0.1.0 as v1.0.0 in releases] — 2026-10-12

### added
- initial release
- `banner(text, subtitle)` with random color picking
- auto-render on `__del__`
- `.left()`, `.right()`, `.center()` subtitle alignment
