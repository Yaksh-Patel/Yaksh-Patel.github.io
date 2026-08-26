/* ============================================================
   main.js — theme, nav, reveal-on-scroll, blog search
   ============================================================ */

(function () {
  'use strict';

  var THEME_KEY = 'yaksh-theme';
  var root = document.documentElement;

  /* ---- Theme ----------------------------------------------------------
     The initial theme is set by an inline script in <head> to avoid a
     flash of the wrong palette. This only handles the toggle and keeps
     the icon in sync. */
  function syncIcon() {
    var use = document.querySelector('#themeIcon use');
    if (!use) return;
    var dark = root.getAttribute('data-theme') === 'dark';
    use.setAttribute('href', dark ? '#i-sun' : '#i-moon');
    var btn = document.getElementById('themeToggle');
    if (btn) btn.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
  }

  function initTheme() {
    syncIcon();
    var btn = document.getElementById('themeToggle');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem(THEME_KEY, next); } catch (e) {}
      syncIcon();
    });
  }

  /* ---- Mobile nav ---------------------------------------------------- */
  function initNav() {
    var burger = document.getElementById('hamburger');
    var nav = document.getElementById('mobileNav');
    if (!burger || !nav) return;

    burger.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', String(open));
    });

    document.addEventListener('click', function (e) {
      if (!burger.contains(e.target) && !nav.contains(e.target)) {
        nav.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        nav.classList.remove('open');
        burger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---- Header hairline appears once scrolled ------------------------- */
  function initHeader() {
    var header = document.getElementById('siteHeader');
    if (!header) return;
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- Reveal on scroll --------------------------------------------- */
  function initReveal() {
    var items = document.querySelectorAll('.reveal');
    if (!items.length) return;

    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduced || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-visible'); });
      return;
    }

    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    items.forEach(function (el) { obs.observe(el); });
  }

  /* ---- Blog search --------------------------------------------------- */
  function initSearch() {
    var input = document.getElementById('sidebarSearch');
    var empty = document.getElementById('blogSearchEmpty');
    if (!input) return;

    var cards = Array.prototype.slice.call(document.querySelectorAll('.post-card'))
      .filter(function (c) { return c.id !== 'blogSearchEmpty'; });

    function apply(q) {
      q = (q || '').trim().toLowerCase();
      var visible = 0;
      cards.forEach(function (card) {
        var match = !q || card.textContent.toLowerCase().indexOf(q) !== -1;
        card.style.display = match ? '' : 'none';
        if (match) visible++;
      });
      if (empty) empty.style.display = (q && visible === 0) ? 'block' : 'none';
    }

    /* Filter as you type — no page reload, no query-string round trip. */
    input.addEventListener('input', function () { apply(input.value); });

    var params = new URLSearchParams(window.location.search);
    var initial = params.get('search');
    if (initial) { input.value = initial; apply(initial); }
  }

  document.addEventListener('DOMContentLoaded', function () {
    initTheme();
    initNav();
    initHeader();
    initReveal();
    initSearch();
  });
})();
