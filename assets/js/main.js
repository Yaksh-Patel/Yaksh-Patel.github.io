/* ============================================================
   main.js — Theme toggle, mobile nav, sidebar search
   ============================================================ */

/* ---- Theme Toggle ---- */
const THEME_KEY = 'yaksh-theme';

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  const icon  = document.getElementById('themeIcon');
  const label = document.getElementById('themeLabel');
  if (!icon || !label) return;
  if (theme === 'dark') {
    icon.textContent  = '☀️';
    label.textContent = 'Light';
  } else {
    icon.textContent  = '🌙';
    label.textContent = 'Dark';
  }
}

function initTheme() {
  const saved  = localStorage.getItem(THEME_KEY);
  const system = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  applyTheme(saved || system);
}

document.addEventListener('DOMContentLoaded', () => {
  initTheme();

  /* Theme toggle button */
  const btn = document.getElementById('themeToggle');
  if (btn) {
    btn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next    = current === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      localStorage.setItem(THEME_KEY, next);
    });
  }

  /* ---- Mobile hamburger ---- */
  const hamburger  = document.getElementById('hamburger');
  const mobileNav  = document.getElementById('mobileNav');
  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      mobileNav.classList.toggle('open');
      const isOpen = mobileNav.classList.contains('open');
      hamburger.setAttribute('aria-expanded', isOpen);
    });

    /* Close on outside click */
    document.addEventListener('click', (e) => {
      if (!hamburger.contains(e.target) && !mobileNav.contains(e.target)) {
        mobileNav.classList.remove('open');
      }
    });
  }

  /* ---- Sidebar search ---- */
  const searchInput = document.getElementById('sidebarSearch');
  if (searchInput) {
    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const q = searchInput.value.trim();
        if (q) {
          window.location.href = `/blog/?search=${encodeURIComponent(q)}`;
        }
      }
    });
  }

  /* ---- Skill bars animate on scroll ---- */
  const fills = document.querySelectorAll('.skill-fill');
  if (fills.length > 0 && 'IntersectionObserver' in window) {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.width = entry.target.getAttribute('data-width') || entry.target.style.width;
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });

    fills.forEach(fill => {
      const w = fill.style.width;
      fill.setAttribute('data-width', w);
      fill.style.width = '0';
      setTimeout(() => obs.observe(fill), 100);
    });
  }

  /* ---- Active nav link highlight ---- */
  const currentPath = window.location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('.site-nav a').forEach(link => {
    const href = link.getAttribute('href').replace(/\/$/, '') || '/';
    if (href !== '/' && currentPath.startsWith(href)) {
      link.classList.add('active');
    } else if (href === '/' && currentPath === '') {
      link.classList.add('active');
    }
  });
});
