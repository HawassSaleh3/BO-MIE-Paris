/* BO&MIE Paris — site behaviour: i18n, nav, reveal, hours, form */
(function () {
  "use strict";

  var DICT = window.I18N || {};
  var SUPPORTED = ["en", "fr"];
  var STORE_KEY = "bomie-lang";

  /* ---------------- language ---------------- */
  function detectLang() {
    var q = new URLSearchParams(location.search).get("lang");
    if (q && SUPPORTED.indexOf(q) > -1) return q;
    try {
      var s = localStorage.getItem(STORE_KEY);
      if (s && SUPPORTED.indexOf(s) > -1) return s;
    } catch (e) {}
    var nav = (navigator.language || "en").slice(0, 2).toLowerCase();
    return SUPPORTED.indexOf(nav) > -1 ? nav : "en";
  }

  function t(key, lang) {
    var d = DICT[lang] || DICT.en || {};
    return Object.prototype.hasOwnProperty.call(d, key) ? d[key] : (DICT.en && DICT.en[key]) || "";
  }

  function applyLang(lang) {
    document.documentElement.setAttribute("lang", lang);

    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var v = t(el.getAttribute("data-i18n"), lang);
      if (v) el.textContent = v;
    });

    // data-i18n-attr="attr:key;attr:key"
    document.querySelectorAll("[data-i18n-attr]").forEach(function (el) {
      el.getAttribute("data-i18n-attr").split(";").forEach(function (pair) {
        var bits = pair.split(":");
        if (bits.length !== 2) return;
        var v = t(bits[1].trim(), lang);
        if (v) el.setAttribute(bits[0].trim(), v);
      });
    });

    // <title> + meta description
    var tk = document.body.getAttribute("data-title-key");
    if (tk) document.title = t(tk, lang);
    var dk = document.body.getAttribute("data-desc-key");
    var md = document.querySelector('meta[name="description"]');
    if (dk && md) md.setAttribute("content", t(dk, lang));

    document.querySelectorAll(".lang button").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.lang === lang));
    });

    try { localStorage.setItem(STORE_KEY, lang); } catch (e) {}
    document.dispatchEvent(new CustomEvent("langchange", { detail: { lang: lang } }));
  }

  var currentLang = detectLang();
  applyLang(currentLang);

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".lang button");
    if (!btn) return;
    currentLang = btn.dataset.lang;
    applyLang(currentLang);
  });

  /* ---------------- mobile nav ---------------- */
  var burger = document.querySelector(".burger");
  var nav = document.getElementById("primary-nav");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", String(open));
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("is-open");
        burger.setAttribute("aria-expanded", "false");
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        burger.setAttribute("aria-expanded", "false");
        burger.focus();
      }
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 960) {
        nav.classList.remove("is-open");
        burger.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ---------------- sticky header shadow ---------------- */
  var header = document.querySelector(".header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-stuck", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------------- reveal on scroll ---------------- */
  var revealables = document.querySelectorAll(".reveal");
  if (revealables.length) {
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
      revealables.forEach(function (el, i) {
        el.style.transitionDelay = (i % 4) * 70 + "ms";
        io.observe(el);
      });
    } else {
      revealables.forEach(function (el) { el.classList.add("is-in"); });
    }
  }

  /* ---------------- opening hours ---------------- */
  // Paris time, Mon–Sat 7:30–20:00, Sun 8:00–20:00
  var OPEN = [480, 450, 450, 450, 450, 450, 450]; // index 0 = Sunday
  var CLOSE = 1200;

  function parisNow() {
    var s = new Date().toLocaleString("en-US", { timeZone: "Europe/Paris" });
    return new Date(s);
  }

  function refreshHours() {
    var now = parisNow();
    var dow = now.getDay();
    var mins = now.getHours() * 60 + now.getMinutes();
    var isOpen = mins >= OPEN[dow] && mins < CLOSE;

    document.querySelectorAll("[data-hours-status]").forEach(function (el) {
      el.textContent = t(isOpen ? "info.status.open" : "info.status.closed", currentLang);
    });
    document.querySelectorAll("[data-hours-dot]").forEach(function (el) {
      el.classList.toggle("dot--closed", !isOpen);
    });
    // highlight today's row (rows carry data-dow 0..6)
    document.querySelectorAll(".hours tr[data-dow]").forEach(function (tr) {
      tr.classList.toggle("is-today", Number(tr.dataset.dow) === dow);
    });
  }
  refreshHours();
  setInterval(refreshHours, 60000);
  document.addEventListener("langchange", refreshHours);

  /* ---------------- current year ---------------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---------------- contact form ---------------- */
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var status = document.getElementById("form-status");
      if (status) {
        status.textContent = t("co.f.ok", currentLang);
        status.classList.add("is-visible");
        status.setAttribute("role", "status");
      }
      form.reset();
      if (status) status.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  }
})();
