/* =========================================================================
   Valentín Sillero — Portfolio · interacciones (JavaScript vanilla)
   Menú mobile · tema claro/oscuro · sección activa · header · animaciones
   de entrada · contador de métricas · reloj local · copiar email · modales
   ========================================================================= */
(function () {
  'use strict';

  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var desktop = window.matchMedia('(min-width: 1024px)');

  /* ---------- Menú mobile ---------- */
  var toggle = document.querySelector('[data-nav-toggle]');
  var panel = document.querySelector('[data-nav-panel]');
  var toggleLabel = document.querySelector('[data-nav-label]');

  function setMenu(open, restoreFocus) {
    if (!toggle || !panel) return;
    toggle.setAttribute('aria-expanded', String(open));
    if (toggleLabel) toggleLabel.textContent = open ? 'Cerrar menú' : 'Abrir menú';
    panel.classList.toggle('is-open', open);
    document.body.classList.toggle('nav-open', open);
    if (open) {
      var first = panel.querySelector('a, button');
      if (first) first.focus();
    } else if (restoreFocus) {
      toggle.focus();
    }
  }

  if (toggle && panel) {
    toggle.addEventListener('click', function () {
      setMenu(toggle.getAttribute('aria-expanded') !== 'true', false);
    });
    panel.addEventListener('click', function (e) {
      if (e.target.closest('a[href^="#"]') && !desktop.matches) setMenu(false, false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') setMenu(false, true);
    });
    // Mantener el foco dentro del menú abierto (Tab / Shift+Tab)
    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab' || toggle.getAttribute('aria-expanded') !== 'true') return;
      var items = [toggle].concat(Array.prototype.slice.call(panel.querySelectorAll('a, button')));
      var first = items[0];
      var last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    desktop.addEventListener('change', function (e) { if (e.matches) setMenu(false, false); });
  }

  /* ---------- Tema claro / oscuro ---------- */
  var themeBtn = document.querySelector('[data-theme-toggle]');
  var systemDark = window.matchMedia('(prefers-color-scheme: dark)');

  function currentTheme() {
    return root.getAttribute('data-theme') || (systemDark.matches ? 'dark' : 'light');
  }
  function syncThemeUI() {
    var dark = currentTheme() === 'dark';
    root.setAttribute('data-theme', dark ? 'dark' : 'light');
    if (themeBtn) themeBtn.setAttribute('aria-label', dark ? 'Cambiar a modo claro' : 'Cambiar a modo oscuro');
    var meta = document.querySelectorAll('meta[name="theme-color"]');
    for (var i = 0; i < meta.length; i++) meta[i].setAttribute('content', dark ? '#0B0C10' : '#FAFAF7');
  }
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = currentTheme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('vs-theme', next); } catch (e) { /* sin almacenamiento */ }
      syncThemeUI();
    });
  }
  syncThemeUI();

  /* ---------- Header con borde al hacer scroll ---------- */
  var header = document.querySelector('[data-header]');
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Indicador de sección activa ---------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.nav-link[href^="#"]'));
  if ('IntersectionObserver' in window && navLinks.length) {
    var byId = {};
    navLinks.forEach(function (link) { byId[link.getAttribute('href').slice(1)] = link; });
    var sections = Object.keys(byId).map(function (id) { return document.getElementById(id); }).filter(Boolean);
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navLinks.forEach(function (l) { l.removeAttribute('aria-current'); });
        var active = byId[entry.target.id];
        if (active) active.setAttribute('aria-current', 'true');
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ---------- Animaciones de entrada + contador ---------- */
  var reveals = document.querySelectorAll('.reveal');
  function countUp(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    if (!target || reduceMotion.matches) return;
    var start = null;
    var duration = 1100;
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = String(Math.round(target * eased));
      if (p < 1) window.requestAnimationFrame(step);
    }
    window.requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window && !reduceMotion.matches) {
    var revealObs = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        var counters = entry.target.querySelectorAll('[data-count]');
        for (var i = 0; i < counters.length; i++) countUp(counters[i]);
        obs.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    for (var r = 0; r < reveals.length; r++) revealObs.observe(reveals[r]);
  } else {
    for (var k = 0; k < reveals.length; k++) reveals[k].classList.add('is-visible');
  }

  /* ---------- Reloj local (Argentina, UTC−3) ---------- */
  var clock = document.querySelector('[data-clock]');
  if (clock && window.Intl) {
    var fmt = new Intl.DateTimeFormat('es-AR', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: 'America/Argentina/Buenos_Aires' });
    var tick = function () { clock.textContent = '· ' + fmt.format(new Date()); };
    tick();
    window.setInterval(tick, 30000);
  }

  /* ---------- Copiar email ---------- */
  var copyBtn = document.querySelector('[data-copy]');
  if (copyBtn) {
    var label = copyBtn.querySelector('[data-copy-label]');
    var icon = copyBtn.querySelector('[data-copy-icon] use');
    var status = document.querySelector('[data-copy-status]');
    copyBtn.addEventListener('click', function () {
      var text = copyBtn.getAttribute('data-copy');
      var done = function (ok) {
        if (label) label.textContent = ok ? 'Email copiado' : 'No se pudo copiar';
        if (status) status.textContent = ok ? 'Email copiado al portapapeles' : 'No se pudo copiar el email';
        if (icon && ok) icon.setAttribute('href', '#i-check');
        window.setTimeout(function () {
          if (label) label.textContent = 'Copiar email';
          if (icon) icon.setAttribute('href', '#i-copy');
          if (status) status.textContent = '';
        }, 2200);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(false); });
      } else {
        done(false);
      }
    });
  }

  /* ---------- Modales de detalle (<dialog>) ---------- */
  var lastTrigger = null;
  document.addEventListener('click', function (e) {
    var opener = e.target.closest('[data-dialog-open]');
    if (opener) {
      var dlg = document.getElementById(opener.getAttribute('data-dialog-open'));
      if (dlg && typeof dlg.showModal === 'function') {
        lastTrigger = opener.getAttribute('aria-hidden') === 'true'
          ? opener.closest('article').querySelector('.project-actions [data-dialog-open]')
          : opener;
        dlg.showModal();
        document.body.style.overflow = 'hidden';
      }
      return;
    }
    if (e.target.closest('[data-dialog-close]')) {
      var parent = e.target.closest('dialog');
      if (parent) parent.close();
      return;
    }
    // Clic en el fondo (backdrop) cierra el modal
    if (e.target.tagName === 'DIALOG' && e.target.open) e.target.close();
  });
  Array.prototype.forEach.call(document.querySelectorAll('dialog'), function (dlg) {
    dlg.addEventListener('close', function () {
      document.body.style.overflow = '';
      if (lastTrigger) lastTrigger.focus();
    });
  });

  /* ---------- Año actual en el footer ---------- */
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());
})();
