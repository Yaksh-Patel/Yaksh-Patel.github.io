/* ============================================================
   main.js — theme, nav, reveal-on-scroll, writing filters
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

  /* ---- Writing filters: search + topic + year -------------------------
     One pass over the cards for all three filters. Everything the filter
     needs is already on each card as a data- attribute (see
     _includes/post-card.html), so this never touches the DOM to read text,
     and the state round-trips through the query string so a filtered view
     can be linked or reloaded. */
  function initWritingFilters() {
    var bar = document.getElementById('writingFilters');
    var archive = document.getElementById('writingArchive');
    if (!bar || !archive) return;

    var input = document.getElementById('writingSearch');
    var count = document.getElementById('writingCount');
    var empty = document.getElementById('writingEmpty');
    var cards = Array.prototype.slice.call(archive.querySelectorAll('.post-card'));
    var yearGroups = Array.prototype.slice.call(archive.querySelectorAll('.archive-year'));
    var topicChips = Array.prototype.slice.call(bar.querySelectorAll('[data-topic]'));
    var yearChips = Array.prototype.slice.call(bar.querySelectorAll('[data-year]'));

    var state = { q: '', topic: '', year: '' };

    function matches(card) {
      if (state.topic) {
        /* Pad both sides so "ml" cannot match inside "ml-systems". */
        var topics = ' ' + (card.getAttribute('data-topics') || '') + ' ';
        if (topics.indexOf(' ' + state.topic + ' ') === -1) return false;
      }
      if (state.year && card.getAttribute('data-year') !== state.year) return false;
      if (state.q && (card.getAttribute('data-text') || '').indexOf(state.q) === -1) return false;
      return true;
    }

    function markChips(chips, key) {
      chips.forEach(function (chip) {
        var active = (chip.getAttribute('data-' + key) || '') === state[key];
        chip.classList.toggle('is-active', active);
        chip.setAttribute('aria-pressed', String(active));
      });
    }

    function syncUrl() {
      if (!window.history || !window.history.replaceState) return;
      var params = new URLSearchParams();
      if (state.topic) params.set('topic', state.topic);
      if (state.year) params.set('year', state.year);
      if (state.q) params.set('search', state.q);
      var query = params.toString();
      history.replaceState(null, '', window.location.pathname + (query ? '?' + query : '') + window.location.hash);
    }

    function apply() {
      var visible = 0;
      cards.forEach(function (card) {
        var ok = matches(card);
        card.hidden = !ok;
        if (ok) visible++;
      });

      /* A year heading with nothing left under it is just noise. */
      yearGroups.forEach(function (group) {
        group.hidden = !group.querySelector('.post-card:not([hidden])');
      });

      if (empty) empty.hidden = visible !== 0;
      if (count) {
        count.textContent = visible === cards.length
          ? cards.length + (cards.length === 1 ? ' note' : ' notes')
          : visible + ' of ' + cards.length + ' shown';
      }

      markChips(topicChips, 'topic');
      markChips(yearChips, 'year');
      syncUrl();
    }

    function pick(key, value) {
      /* Clicking the chip that is already on means "drop this filter". */
      state[key] = state[key] === value ? '' : value;
      apply();
    }

    topicChips.forEach(function (chip) {
      chip.addEventListener('click', function () { pick('topic', chip.getAttribute('data-topic')); });
    });
    yearChips.forEach(function (chip) {
      chip.addEventListener('click', function () { pick('year', chip.getAttribute('data-year')); });
    });

    if (input) {
      input.addEventListener('input', function () {
        state.q = input.value.trim().toLowerCase();
        apply();
      });
    }

    document.addEventListener('click', function (e) {
      var reset = e.target.closest && e.target.closest('[data-filter-reset]');
      if (!reset) return;
      state = { q: '', topic: '', year: '' };
      if (input) input.value = '';
      apply();
    });

    var params = new URLSearchParams(window.location.search);
    state.topic = params.get('topic') || '';
    state.year = params.get('year') || '';
    state.q = (params.get('search') || '').trim().toLowerCase();
    if (input && state.q) input.value = params.get('search');

    /* A topic or year in the URL that no chip offers would filter everything
       away with no way back, so drop it. */
    function offered(chips, key, value) {
      return !value || chips.some(function (c) { return c.getAttribute('data-' + key) === value; });
    }
    if (!offered(topicChips, 'topic', state.topic)) state.topic = '';
    if (!offered(yearChips, 'year', state.year)) state.year = '';

    apply();
  }

  document.addEventListener('DOMContentLoaded', function () {
    initTheme();
    initNav();
    initHeader();
    initReveal();
    initWritingFilters();
  });
})();
