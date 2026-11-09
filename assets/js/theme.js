/* Aplica el tema guardado antes de pintar la página (evita el parpadeo claro/oscuro). */
(function () {
  var root = document.documentElement;
  root.classList.add('js');
  try {
    var saved = localStorage.getItem('vs-theme');
    if (saved === 'light' || saved === 'dark') root.setAttribute('data-theme', saved);
  } catch (e) { /* almacenamiento no disponible: se usa la preferencia del sistema */ }
})();
