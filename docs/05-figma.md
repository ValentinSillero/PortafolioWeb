# 05 · Figma: design system y prototipo

**Archivo:** [Portfolio Valentín Sillero — UX/UI 2026](https://www.figma.com/design/3AxCDCuNJOfTUIWiVaQyt2)
Creado el 9/11/2026 desde la integración de Figma de Claude Code, en tus **Drafts** (plan Starter).

> **Acción pendiente:** en Figma → **Share** → “Anyone with the link” → **can view**. Sin eso el docente no puede abrirlo. Opcional: moverlo de Drafts a un proyecto.

## Contenido (3 páginas: el máximo del plan Starter)

### 01 Proceso UX
Secciones: **1 · Investigación** (usuario, proto-persona, escenario) · **2 · Benchmark** (3 capturas + análisis) · **3 · Moodboard** + 3 palabras clave · **4 · Arquitectura** (sitemap + card sorting) · **5 · Wireframes** mobile 375 y desktop 1280 (página completa).

### 02 Design System
- **Variables** (con code syntax `var(--…)` igual al CSS):
  - `Primitives` (31 colores, ocultos de los selectores).
  - `Color · Light` y `Color · Dark` (16 tokens semánticos cada una, alias a primitivos, scopes específicos).
  - `Spacing & Radius` (12 espaciados base 4 + 4 radios).
  - *Limitación del plan Starter:* 1 modo por colección, por eso Light y Dark son **dos colecciones** con los mismos nombres de token en vez de dos modos.
- **Estilos de texto** (9): Display, H2 Sección, H3 Tarjeta, Lead, Body Large, Body, Small, Button, Label Mono — Geist / Geist Mono.
- **Componentes** (todos con fills, bordes y radios ligados a variables):
  - `Button` — Style (Primary, Secondary) × State (Default, Hover, Focus, Active, Disabled) = 10 variantes.
  - `Tag` — Default / Hover.
  - `Pill` — Cliente / Producto / Académico.
  - `Timeline item` — marcador + tarjeta con período, rol, institución y 2 logros.
  - `Project card` — captura en marco de navegador, meta, título, descripción, problema/aprendizaje, tags y acciones (usa instancias de Button, Tag y Pill).
- **Foundations · Light**: paleta, escala tipográfica y escala de espaciado.

### 03 Prototipo (alta fidelidad, navegable)
Flujos de inicio: **Desktop** y **Mobile** (Present ▶).

| Frame | Interacciones |
|---|---|
| Desktop · Home (1440, scroll vertical, header fijo) | Links del menú → *scroll to* cada sección · “Ver proyectos” → Proyectos · “Contactarme” → Contacto · “Ver caso de estudio” → frame del caso |
| Desktop · Caso de estudio Rebord | Logo / “Volver a proyectos” → Back |
| Mobile · Home (375, scroll, header fijo) | Hamburguesa → abre overlay del menú · CTAs → *scroll to* · “Ver caso de estudio” → caso |
| Mobile · Menú abierto (overlay) | ✕ y links → cierran el menú |

**Cómo se hizo (declaración honesta):** el diseño de alta fidelidad se trabajó *code-first* sobre el design system; las pantallas del prototipo son **capturas reales del sitio implementado** (no capas vectoriales editables), con zonas interactivas encima. Los componentes y tokens del design system sí son nativos y editables.

**Limitaciones del plan Starter encontradas:** máximo 3 páginas, 1 modo por colección de variables y una sola acción por interacción (por eso los links del menú mobile cierran el overlay pero no hacen además el scroll a la sección).

## Pendientes en Figma

- [ ] Compartir con permiso de visualización y pegar el link en la entrega.
- [x] Capturas del prototipo (Desktop · Home y Mobile · Home) actualizadas a la versión actual del sitio, con foto y badge “Disponible” (revisado por Valentín en Figma).
- [ ] Comparación lado a lado Figma / sitio de 2 secciones (sugerencia del docente para la presentación).
- [ ] Si el test de usabilidad se hace sobre el prototipo, registrar en `06-test-usabilidad.md` que se usó este archivo.
