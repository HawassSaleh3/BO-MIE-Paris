#!/usr/bin/env python3
"""Tiny static-site builder for BO&MIE Paris.
Assembles shared header/footer around per-page content into plain HTML files.
Run:  python3 build.py
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://www.boetmie.com"
ORDER = "https://commande.boetmie.com/brand/boetmie"
MAPS = ("https://www.google.com/maps/search/?api=1&query=BO%26MIE%20H%C3%B4tel%20de%20Ville"
        "%2C%2048%20rue%20de%20Rivoli%2C%2075004%20Paris&query_place_id=ChIJd_vVDW5v5kcRFEWfGnHyacI")
TEL = "+33142509112"
TEL_H = "+33 1 42 50 91 12"

PAGES = [
    ("index.html", "home", "nav.home"),
    ("creations.html", "creations", "nav.creations"),
    ("about.html", "about", "nav.about"),
    ("visit.html", "visit", "nav.visit"),
    ("contact.html", "contact", "nav.contact"),
]

NAV = [("index.html", "nav.home"), ("creations.html", "nav.creations"),
       ("about.html", "nav.about"), ("visit.html", "nav.visit"),
       ("contact.html", "nav.contact")]


def head(page, title_key, desc_key, canonical):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>BO&amp;MIE H&ocirc;tel de Ville — Boulangerie créative, Paris 4e</title>
<meta name="description" content="Creative French bakery and pâtisserie at 48 rue de Rivoli, facing the Hôtel de Ville, Paris 4e.">
<meta name="theme-color" content="#FBF7F0">
<link rel="canonical" href="{SITE}/{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BO&amp;MIE Hôtel de Ville">
<meta property="og:title" content="BO&amp;MIE Hôtel de Ville — Creative bakery, Paris 4e">
<meta property="og:description" content="Breads, viennoiseries, pastries and coffee, baked fresh every day at 48 rue de Rivoli.">
<meta property="og:image" content="{SITE}/assets/img/hero.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body data-page="{page}" data-title-key="{title_key}" data-desc-key="{desc_key}">
<a class="skip" href="#main" data-i18n="a11y.skip">Skip to content</a>
"""


def header(active):
    cur = ' aria-current="page"'
    labels = {"nav.home": "Home", "nav.creations": "Our creations", "nav.about": "Our story",
              "nav.visit": "Visit us", "nav.contact": "Contact"}
    links = "\n".join(
        '      <a href="%s"%s data-i18n="%s">%s</a>' % (href, cur if href == active else "", key, labels[key])
        for href, key in NAV)
    return f"""<header class="header">
  <div class="container header__inner">
    <a class="brand" href="index.html" aria-label="BO&amp;MIE Hôtel de Ville — home">
      <span class="brand__name">BO&amp;MIE</span>
      <span class="brand__sub" data-i18n="brand.sub">Creative bakery · Paris</span>
    </a>
    <nav class="nav" id="primary-nav" aria-label="Main">
{links}
      <a class="btn btn--accent btn--sm" href="{ORDER}" target="_blank" rel="noopener" data-i18n="nav.order">Order online</a>
    </nav>
    <div class="header__actions">
      <div class="lang" role="group" aria-label="Language" data-i18n-attr="aria-label:a11y.lang">
        <button type="button" data-lang="en" aria-pressed="false">EN</button>
        <button type="button" data-lang="fr" aria-pressed="false">FR</button>
      </div>
      <a class="btn btn--primary btn--sm btn--order" href="{ORDER}" target="_blank" rel="noopener" data-i18n="nav.order">Order online</a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Menu" data-i18n-attr="aria-label:nav.menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
"""


FOOTER = f"""<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <span class="brand__name" style="font-size:1.5rem">BO&amp;MIE</span>
        <p style="margin-top:14px;max-width:34ch;font-size:.93rem" data-i18n="ft.tag">Creative bakery and pâtisserie.</p>
        <div class="social">
          <a href="https://www.instagram.com/boetmie/" target="_blank" rel="noopener" aria-label="Instagram">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.9.07 1.2.06 1.8.25 2.2.42.6.22 1 .48 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c0 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2 0-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c0-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2Zm0 1.8c-3.1 0-3.5 0-4.7.07-1.1.05-1.7.24-2.1.4-.5.2-.9.44-1.2.77-.3.3-.6.7-.8 1.2-.2.4-.3 1-.4 2.1C2.7 9.7 2.7 10.1 2.7 12s0 2.3.1 3.5c0 1.1.2 1.7.4 2.1.2.5.4.9.8 1.2.3.3.7.6 1.2.8.4.2 1 .3 2.1.4 1.2.05 1.6.07 4.7.07s3.5 0 4.7-.07c1.1 0 1.7-.2 2.1-.4.5-.2.9-.4 1.2-.8.3-.3.6-.7.8-1.2.2-.4.3-1 .4-2.1.05-1.2.07-1.6.07-3.5s0-2.3-.07-3.5c0-1.1-.2-1.7-.4-2.1-.2-.5-.4-.9-.8-1.2-.3-.3-.7-.6-1.2-.8-.4-.2-1-.3-2.1-.4C15.5 4 15.1 4 12 4Zm0 3.1a4.9 4.9 0 1 1 0 9.8 4.9 4.9 0 0 1 0-9.8Zm0 8.1a3.2 3.2 0 1 0 0-6.4 3.2 3.2 0 0 0 0 6.4Zm6.3-8.3a1.15 1.15 0 1 1-2.3 0 1.15 1.15 0 0 1 2.3 0Z"/></svg>
          </a>
          <a href="https://www.facebook.com/boetmie/" target="_blank" rel="noopener" aria-label="Facebook">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 22v-8h2.7l.4-3.1h-3.1V8.9c0-.9.25-1.5 1.55-1.5h1.65V4.6c-.3 0-1.3-.1-2.45-.1-2.4 0-4.05 1.5-4.05 4.2v2.2H7.5V14h2.7v8h3.3Z"/></svg>
          </a>
          <a href="https://www.linkedin.com/company/boetmie/" target="_blank" rel="noopener" aria-label="LinkedIn">
            <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.94 5a1.94 1.94 0 1 1-3.88 0 1.94 1.94 0 0 1 3.88 0ZM3.2 8.4h3.5V21H3.2V8.4Zm5.7 0h3.35v1.72h.05c.47-.85 1.6-1.75 3.3-1.75 3.53 0 4.18 2.2 4.18 5.07V21h-3.5v-6.05c0-1.45-.03-3.3-2.05-3.3-2.05 0-2.36 1.57-2.36 3.2V21H8.9V8.4Z"/></svg>
          </a>
        </div>
      </div>
      <div>
        <h4 data-i18n="ft.explore">Explore</h4>
        <ul>
          <li><a href="index.html" data-i18n="nav.home">Home</a></li>
          <li><a href="creations.html" data-i18n="nav.creations">Our creations</a></li>
          <li><a href="about.html" data-i18n="nav.about">Our story</a></li>
          <li><a href="visit.html" data-i18n="nav.visit">Visit us</a></li>
          <li><a href="contact.html" data-i18n="nav.contact">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4 data-i18n="ft.visit">Visit</h4>
        <ul>
          <li><a href="{MAPS}" target="_blank" rel="noopener">48 rue de Rivoli<br>75004 Paris</a></li>
          <li><a href="tel:{TEL}">{TEL_H}</a></li>
          <li data-i18n="ft.hours">Mon–Sat 7:30 – 20:00</li>
          <li data-i18n="ft.hours2">Sunday 8:00 – 20:00</li>
        </ul>
      </div>
      <div>
        <h4 data-i18n="ft.legal">Legal</h4>
        <ul>
          <li><a href="#" data-i18n="ft.l1">Legal notice</a></li>
          <li><a href="#" data-i18n="ft.l2">Privacy policy</a></li>
          <li><a href="#" data-i18n="ft.l3">Cookies</a></li>
          <li><a href="#" data-i18n="ft.l4">Accessibility</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> BO&amp;MIE. <span data-i18n="ft.rights">All rights reserved.</span></span>
      <span data-i18n="ft.made">48 rue de Rivoli, 75004 Paris</span>
    </div>
  </div>
</footer>
<script src="assets/js/i18n.js"></script>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""

LD_JSON = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Bakery",
  "name": "BO&MIE H\\u00f4tel de Ville",
  "image": "%s/assets/img/shop.jpg",
  "url": "%s/",
  "telephone": "%s",
  "priceRange": "€€",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "48 rue de Rivoli",
    "addressLocality": "Paris",
    "postalCode": "75004",
    "addressCountry": "FR"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 48.857, "longitude": 2.3515 },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.4", "reviewCount": "1102" },
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "07:30", "closes": "20:00" },
    { "@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "08:00", "closes": "20:00" }
  ]
}
</script>""" % (SITE, SITE, TEL_H)


def hours_table():
    rows = [("mon", 1, "7:30 – 20:00"), ("tue", 2, "7:30 – 20:00"), ("wed", 3, "7:30 – 20:00"),
            ("thu", 4, "7:30 – 20:00"), ("fri", 5, "7:30 – 20:00"), ("sat", 6, "7:30 – 20:00"),
            ("sun", 0, "8:00 – 20:00")]
    trs = "\n".join(
        f'    <tr data-dow="{dow}"><td data-i18n="day.{d}">{d}</td><td>{h}</td></tr>'
        for d, dow, h in rows)
    return f'<table class="hours">\n  <tbody>\n{trs}\n  </tbody>\n</table>'


MARQUEE = """<div class="marquee" aria-hidden="true">
  <div class="marquee__track">
""" + "".join(
    f'    <span data-i18n="mq.{i}">·</span>\n' for i in list(range(1, 7)) * 2
) + """  </div>
</div>
"""

CTA_BAND = f"""<section class="section section--ink">
  <div class="container center">
    <h2 data-i18n="band.h2">Hungry already?</h2>
    <p class="lead" data-i18n="band.p">Order online, or push the door at 48 rue de Rivoli.</p>
    <div class="btn-row" style="margin-top:26px">
      <a class="btn btn--light" href="{ORDER}" target="_blank" rel="noopener" data-i18n="band.cta1">Order online</a>
      <a class="btn btn--ghost" href="visit.html" data-i18n="band.cta2">Plan your visit</a>
    </div>
  </div>
</section>
"""


def info_block():
    return f"""<div class="panel reveal">
  <span class="eyebrow" data-i18n="info.eyebrow">Hôtel de Ville · Marais · Rivoli</span>
  <h2 data-i18n="info.h2">Your bakery in Paris 4e</h2>
  <div class="dl">
    <div class="dl__row"><span class="dl__k" data-i18n="info.address">Address</span>
      <span class="dl__v"><a class="link-arrow" href="{MAPS}" target="_blank" rel="noopener">48 rue de Rivoli, 75004 Paris</a></span></div>
    <div class="dl__row"><span class="dl__k" data-i18n="info.metro">Metro</span>
      <span class="dl__v">Hôtel de Ville · <span class="muted">1 &amp; 11</span></span></div>
    <div class="dl__row"><span class="dl__k" data-i18n="info.phone">Phone</span>
      <span class="dl__v"><a href="tel:{TEL}">{TEL_H}</a></span></div>
  </div>
  <p style="display:flex;align-items:center;gap:10px;font-weight:600">
    <span class="dot" data-hours-dot></span><span data-hours-status>Open now</span>
  </p>
  {hours_table()}
  <ul class="chips">
    <li data-i18n="info.f1">Eat in</li><li data-i18n="info.f2">Terrace</li><li data-i18n="info.f3">Wi-Fi</li>
    <li data-i18n="info.f4">Sockets</li><li data-i18n="info.f5">Restrooms</li><li data-i18n="info.f6">Wheelchair access</li>
  </ul>
  <div class="btn-row" style="margin-top:26px">
    <a class="btn btn--primary" href="{MAPS}" target="_blank" rel="noopener" data-i18n="info.dir">Get directions</a>
    <a class="btn btn--ghost" href="tel:{TEL}" data-i18n="info.call">Call the shop</a>
  </div>
</div>"""


MAP_EMBED = """<div class="map-wrap reveal">
  <iframe title="Map" data-i18n-attr="title:map.title" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"
    src="https://www.openstreetmap.org/export/embed.html?bbox=2.3435%2C48.8535%2C2.3595%2C48.8605&amp;layer=mapnik&amp;marker=48.8570%2C2.3515"></iframe>
</div>"""


def pagehead(crumb_key, h1_key, lead_key):
    return f"""<section class="pagehead">
  <div class="container">
    <p class="crumbs"><a href="index.html" data-i18n="nav.home">Home</a> / <span data-i18n="{crumb_key}"></span></p>
    <h1 data-i18n="{h1_key}"></h1>
    <p class="lead" data-i18n="{lead_key}"></p>
  </div>
</section>"""


# ------------------------------------------------------------------ pages
def page_home():
    cats = [
        (1, "viennoiserie.jpg"), (2, "patisserie.jpg"), (3, "bread.jpg"),
        (4, "savoury.jpg"), (5, "coffee.jpg"), (6, "coffee.jpg"),
    ]
    cards = "\n".join(f"""      <article class="card reveal">
        <div class="card__media"><img src="assets/img/{img}" alt="" loading="lazy" width="800" height="600"></div>
        <div class="card__body">
          <span class="card__tag" data-i18n="cat.{i}.tag"></span>
          <h3 data-i18n="cat.{i}.t"></h3>
          <p data-i18n="cat.{i}.d"></p>
        </div>
      </article>""" for i, img in cats)

    values = "\n".join(f"""      <div class="value reveal">
        <div class="value__num">0{i}</div>
        <h3 data-i18n="val.{i}.t"></h3>
        <p data-i18n="val.{i}.d"></p>
      </div>""" for i in range(1, 5))

    sig_imgs = ["patisserie.jpg", "viennoiserie.jpg", "coffee.jpg", "hero.jpg", "bread.jpg"]
    sigs = "\n".join(f"""      <li>
        <span class="sig__n">0{i}</span>
        <img class="sig__img" src="assets/img/{sig_imgs[i-1]}" alt="" loading="lazy" width="64" height="64">
        <span><span class="sig__t" data-i18n="sig.{i}.t"></span><br><span class="sig__d" data-i18n="sig.{i}.d"></span></span>
      </li>""" for i in range(1, 6))

    reviews = "\n".join(f"""      <blockquote class="quote reveal">
        <div class="stars" aria-hidden="true">★★★★★</div>
        <p data-i18n="rev.{i}"></p>
        <footer data-i18n="rev.{i}.a"></footer>
      </blockquote>""" for i in range(1, 4))

    faqs = "\n".join(f"""    <details{" open" if i == 1 else ""}>
      <summary data-i18n="faq.q{i}"></summary>
      <p data-i18n="faq.a{i}"></p>
    </details>""" for i in range(1, 7))

    return f"""<main id="main">

<section class="hero">
  <div class="container hero__grid">
    <div class="hero__copy">
      <span class="hero__kicker" data-i18n="hero.kicker"></span>
      <h1><span data-i18n="hero.h1a"></span><br><em data-i18n="hero.h1b"></em></h1>
      <p class="lead" data-i18n="hero.lead"></p>
      <div class="btn-row" style="margin-top:28px">
        <a class="btn btn--primary" href="creations.html" data-i18n="hero.cta1"></a>
        <a class="btn btn--ghost" href="{MAPS}" target="_blank" rel="noopener" data-i18n="hero.cta2"></a>
      </div>
    </div>
    <figure class="hero__media" style="margin:0">
      <img src="assets/img/hero.jpg" alt="" data-i18n-attr="alt:hero.alt" width="900" height="1125" fetchpriority="high">
      <figcaption class="hero__badge"><span class="dot" data-hours-dot></span><span data-i18n="hero.badge"></span></figcaption>
    </figure>
  </div>
</section>

{MARQUEE}

<section class="section" id="creations">
  <div class="container">
    <div class="center" style="margin-bottom:46px">
      <span class="eyebrow" data-i18n="cat.eyebrow"></span>
      <h2 data-i18n="cat.h2"></h2>
      <p class="lead" data-i18n="cat.lead"></p>
    </div>
    <div class="grid grid--3">
{cards}
    </div>
    <div class="center" style="margin-top:44px">
      <a class="link-arrow" href="creations.html"><span data-i18n="cat.cta"></span><span class="ar">→</span></a>
    </div>
  </div>
</section>

<section class="section section--cream2">
  <div class="container">
    <div class="center" style="margin-bottom:44px">
      <span class="eyebrow" data-i18n="val.eyebrow"></span>
      <h2 data-i18n="val.h2"></h2>
    </div>
    <div class="grid grid--4">
{values}
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="container split">
    <div>
      <span class="eyebrow" data-i18n="sig.eyebrow"></span>
      <h2 data-i18n="sig.h2"></h2>
      <p class="lead" data-i18n="sig.lead"></p>
    </div>
    <ul class="sig">
{sigs}
    </ul>
  </div>
</section>

<section class="section">
  <div class="container split split--rev">
    <figure class="split__media reveal" style="margin:0">
      <img src="assets/img/shop.jpg" alt="" loading="lazy" width="1000" height="800">
    </figure>
    <div class="reveal">
      <span class="eyebrow" data-i18n="story.eyebrow"></span>
      <h2 data-i18n="story.h2"></h2>
      <p data-i18n="story.p1"></p>
      <p data-i18n="story.p2"></p>
      <div class="grid grid--2" style="gap:14px;margin:26px 0">
        <div><strong style="font-family:var(--ff-display);font-size:1.5rem">2024</strong><br><span class="muted" style="font-size:.85rem" data-i18n="story.s1"></span></div>
        <div><strong style="font-family:var(--ff-display);font-size:1.5rem" data-i18n="story.s2"></strong><br><span class="muted" style="font-size:.85rem" data-i18n="story.s2v"></span></div>
        <div><strong style="font-family:var(--ff-display);font-size:1.5rem">110 m²</strong><br><span class="muted" style="font-size:.85rem" data-i18n="story.s3"></span></div>
        <div><strong style="font-family:var(--ff-display);font-size:1.5rem" data-i18n="story.s4v"></strong><br><span class="muted" style="font-size:.85rem" data-i18n="story.s4"></span></div>
      </div>
      <a class="link-arrow" href="about.html"><span data-i18n="story.cta"></span><span class="ar">→</span></a>
    </div>
  </div>
</section>

<section class="section section--cream2" id="visit">
  <div class="container info-grid">
    {info_block()}
    {MAP_EMBED}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:10px">
      <span class="eyebrow" data-i18n="rev.eyebrow"></span>
      <h2 data-i18n="rev.h2"></h2>
    </div>
    <div class="rating">
      <span class="rating__score">4,4</span>
      <span><span class="stars" aria-hidden="true">★★★★☆</span><br><span class="muted" style="font-size:.88rem" data-i18n="rev.count"></span></span>
    </div>
    <div class="grid grid--3">
{reviews}
    </div>
    <div class="center" style="margin-top:36px">
      <a class="link-arrow" href="{MAPS}" target="_blank" rel="noopener"><span data-i18n="rev.cta"></span><span class="ar">→</span></a>
    </div>
  </div>
</section>

<section class="section section--cream2">
  <div class="container">
    <div class="center" style="margin-bottom:36px">
      <span class="eyebrow" data-i18n="faq.eyebrow"></span>
      <h2 data-i18n="faq.h2"></h2>
    </div>
    <div class="faq">
{faqs}
    </div>
  </div>
</section>

{CTA_BAND}
</main>
{LD_JSON}
"""


def page_creations():
    cats = [(1, "viennoiserie.jpg"), (2, "patisserie.jpg"), (3, "bread.jpg"),
            (4, "savoury.jpg"), (5, "hero.jpg"), (6, "coffee.jpg")]
    cards = "\n".join(f"""      <article class="card reveal">
        <div class="card__media"><img src="assets/img/{img}" alt="" loading="lazy" width="800" height="600"></div>
        <div class="card__body">
          <span class="card__tag" data-i18n="cat.{i}.tag"></span>
          <h3 data-i18n="cat.{i}.t"></h3>
          <p data-i18n="cat.{i}.d"></p>
        </div>
      </article>""" for i, img in cats)

    seasons = "\n".join(f"""      <div class="value reveal">
        <h3 data-i18n="cr.s{i}.t"></h3>
        <p data-i18n="cr.s{i}.d"></p>
      </div>""" for i in range(1, 6))

    steps = "\n".join(f"""      <div class="value reveal">
        <div class="value__num">0{i}</div>
        <h3 data-i18n="cr.p{i}.t"></h3>
        <p data-i18n="cr.p{i}.d"></p>
      </div>""" for i in range(1, 5))

    return f"""<main id="main">
{pagehead("cr.crumb", "cr.h1", "cr.lead")}

<section class="section">
  <div class="container">
    <div class="grid grid--3">
{cards}
    </div>
    <p class="muted center" style="margin-top:40px;font-size:.9rem" data-i18n="cr.note"></p>
  </div>
</section>

<section class="section section--cream2">
  <div class="container">
    <div class="center" style="margin-bottom:44px">
      <span class="eyebrow" data-i18n="cr.season.eyebrow"></span>
      <h2 data-i18n="cr.season.h2"></h2>
      <p class="lead" data-i18n="cr.season.lead"></p>
    </div>
    <div class="grid grid--3">
{seasons}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:44px">
      <span class="eyebrow" data-i18n="cr.proc.eyebrow"></span>
      <h2 data-i18n="cr.proc.h2"></h2>
    </div>
    <div class="grid grid--4">
{steps}
    </div>
  </div>
</section>

{CTA_BAND}
</main>
{LD_JSON}
"""


def page_about():
    stats = [("25+", "ab.st1"), ("5", "ab.st2"), ("300+", "ab.st3"), ("2017", "ab.st4")]
    st = "\n".join(f"""      <div class="stat"><div class="stat__v">{v}</div><div class="stat__l" data-i18n="{k}"></div></div>"""
                   for v, k in stats)
    return f"""<main id="main">
{pagehead("ab.crumb", "ab.h1", "ab.lead")}

<section class="section">
  <div class="container split">
    <figure class="split__media reveal" style="margin:0"><img src="assets/img/facade.jpg" alt="" loading="lazy" width="1000" height="800"></figure>
    <div class="reveal">
      <span class="eyebrow" data-i18n="story.eyebrow"></span>
      <h2 data-i18n="story.h2"></h2>
      <p data-i18n="story.p1"></p>
      <p data-i18n="story.p2"></p>
    </div>
  </div>
</section>

<section class="section section--cream2">
  <div class="container split split--rev">
    <figure class="split__media reveal" style="margin:0"><img src="assets/img/shop.jpg" alt="" loading="lazy" width="1000" height="800"></figure>
    <div class="reveal">
      <h2 data-i18n="ab.h2a"></h2>
      <p data-i18n="ab.p1"></p>
      <p data-i18n="ab.p2"></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <figure class="split__media reveal" style="margin:0"><img src="assets/img/patisserie.jpg" alt="" loading="lazy" width="1000" height="800"></figure>
    <div class="reveal">
      <h2 data-i18n="ab.h2b"></h2>
      <p data-i18n="ab.p3"></p>
      <p data-i18n="ab.p4"></p>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="container">
    <div class="center" style="margin-bottom:40px">
      <span class="eyebrow" data-i18n="ab.tl.eyebrow"></span>
      <h2 data-i18n="ab.tl.h2"></h2>
    </div>
    <div class="stats">
{st}
    </div>
  </div>
</section>

{CTA_BAND}
</main>
{LD_JSON}
"""


def page_visit():
    transit = "\n".join(f'      <li data-i18n="vi.t{i}"></li>' for i in range(1, 6))
    faqs = "\n".join(f"""    <details{" open" if i == 1 else ""}>
      <summary data-i18n="faq.q{i}"></summary>
      <p data-i18n="faq.a{i}"></p>
    </details>""" for i in range(1, 7))
    return f"""<main id="main">
{pagehead("vi.crumb", "vi.h1", "vi.lead")}

<section class="section">
  <div class="container info-grid">
    {info_block()}
    {MAP_EMBED}
  </div>
</section>

<section class="section section--cream2">
  <div class="container split">
    <figure class="split__media reveal" style="margin:0"><img src="assets/img/shop.jpg" alt="" loading="lazy" width="1000" height="800"></figure>
    <div class="reveal">
      <h2 data-i18n="vi.around.h2"></h2>
      <p data-i18n="vi.around.p"></p>
      <h2 style="margin-top:36px" data-i18n="vi.near.h2"></h2>
      <p data-i18n="vi.near.p"></p>
      <h3 style="margin-top:28px" data-i18n="vi.transit.h3"></h3>
      <ul class="chips" style="flex-direction:column;align-items:flex-start">
{transit}
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:36px">
      <span class="eyebrow" data-i18n="faq.eyebrow"></span>
      <h2 data-i18n="faq.h2"></h2>
    </div>
    <div class="faq">
{faqs}
    </div>
  </div>
</section>

{CTA_BAND}
</main>
{LD_JSON}
"""


def page_contact():
    subs = "\n".join(f'            <option data-i18n="co.f.s{i}"></option>' for i in range(1, 7))
    return f"""<main id="main">
{pagehead("co.crumb", "co.h1", "co.lead")}

<section class="section">
  <div class="container info-grid">
    <div class="panel reveal">
      <h2 data-i18n="co.form.h2"></h2>
      <div class="form__status" id="form-status"></div>
      <form class="form" id="contact-form" novalidate>
        <div class="form__row">
          <div class="field">
            <label for="f-name" data-i18n="co.f.name"></label>
            <input id="f-name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="f-email" data-i18n="co.f.email"></label>
            <input id="f-email" name="email" type="email" autocomplete="email" required>
          </div>
        </div>
        <div class="form__row">
          <div class="field">
            <label for="f-phone" data-i18n="co.f.phone"></label>
            <input id="f-phone" name="phone" type="tel" autocomplete="tel">
          </div>
          <div class="field">
            <label for="f-subject" data-i18n="co.f.subject"></label>
            <select id="f-subject" name="subject">
{subs}
            </select>
          </div>
        </div>
        <div class="field">
          <label for="f-msg" data-i18n="co.f.msg"></label>
          <textarea id="f-msg" name="message" required></textarea>
        </div>
        <button class="btn btn--primary" type="submit" data-i18n="co.f.send"></button>
        <p class="form__note" data-i18n="co.f.note"></p>
      </form>
    </div>

    <div class="reveal">
      <div class="panel" style="margin-bottom:24px">
        <h3 data-i18n="co.side.h3"></h3>
        <div class="dl">
          <div class="dl__row"><span class="dl__k" data-i18n="co.side.shop"></span><span class="dl__v"><a href="tel:{TEL}">{TEL_H}</a></span></div>
          <div class="dl__row"><span class="dl__k" data-i18n="co.side.email"></span><span class="dl__v"><a href="mailto:hoteldeville@boetmie.com">hoteldeville@boetmie.com</a></span></div>
          <div class="dl__row"><span class="dl__k" data-i18n="co.side.press"></span><span class="dl__v"><a href="mailto:presse@boetmie.com">presse@boetmie.com</a></span></div>
          <div class="dl__row"><span class="dl__k" data-i18n="co.side.jobs"></span><span class="dl__v"><a href="mailto:recrutement@boetmie.com">recrutement@boetmie.com</a><br><span class="muted" style="font-size:.86rem" data-i18n="co.side.jobsv"></span></span></div>
          <div class="dl__row"><span class="dl__k" data-i18n="co.side.hq"></span><span class="dl__v" data-i18n="co.side.hqv"></span></div>
        </div>
        <p style="display:flex;align-items:center;gap:10px;font-weight:600;margin:0">
          <span class="dot" data-hours-dot></span><span data-hours-status></span>
        </p>
        {hours_table()}
      </div>
      {MAP_EMBED}
    </div>
  </div>
</section>

{CTA_BAND}
</main>
{LD_JSON}
"""


BUILDERS = {
    "home": (page_home, "meta.home.title", "meta.home.desc"),
    "creations": (page_creations, "meta.creations.title", "meta.creations.desc"),
    "about": (page_about, "meta.about.title", "meta.about.desc"),
    "visit": (page_visit, "meta.visit.title", "meta.visit.desc"),
    "contact": (page_contact, "meta.contact.title", "meta.contact.desc"),
}


def main():
    for filename, page, _ in PAGES:
        fn, tk, dk = BUILDERS[page]
        canonical = "" if filename == "index.html" else filename
        html = head(page, tk, dk, canonical) + header(filename) + fn() + FOOTER
        (ROOT / filename).write_text(html, encoding="utf-8")
        print("built", filename)


if __name__ == "__main__":
    main()
