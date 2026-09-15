# BO&MIE Paris — Hôtel de Ville

Bilingual (EN / FR) static website for the BO&MIE creative bakery at
48 rue de Rivoli, 75004 Paris.

## Stack

Plain HTML, CSS and vanilla JavaScript — no framework, no build step required
to deploy. Works on any static host (Netlify, Vercel, GitHub Pages, Apache,
Nginx, or a plain shared hosting folder).

## Structure

```
index.html        Home
creations.html    Our creations / product range
about.html        Our story
visit.html        Address, hours, map, how to get here
contact.html      Contact form + direct lines
assets/css/       style.css  — full design system
assets/js/        i18n.js    — EN/FR dictionary (all site copy)
                  main.js    — language switch, nav, hours, reveal, form
assets/img/       photography + favicon
build.py          optional generator that assembles the pages
```

## Editing content

All visible text lives in `assets/js/i18n.js`, keyed by `data-i18n`
attributes in the HTML. Change a string there and it updates in both
places it appears. Keep the `en` and `fr` objects in sync.

## Rebuilding the pages

The HTML files are committed and can be edited directly. If you prefer to
change the shared header/footer in one place, edit `build.py` and run:

```bash
python3 build.py
```

## Local preview

```bash
python3 -m http.server 3000
# http://localhost:3000
```

## Features

- Full EN / FR switch, remembered in `localStorage`, auto-detects browser language
- Responsive from 320px to ultrawide; mobile drawer navigation
- Live "open now / closed" status computed in Europe/Paris time
- Today's row highlighted in the opening-hours table
- Accessible: skip link, focus rings, ARIA states, reduced-motion support
- SEO: per-language `<title>` and meta description, canonical, Open Graph,
  and `Bakery` JSON-LD with address, hours and rating
- OpenStreetMap embed (no API key, no tracking cookies)
