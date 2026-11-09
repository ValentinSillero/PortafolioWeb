# 01 · Investigación

> Trabajo Final UX/UI 2026 · Valentín Sillero
> Estado: **completo** (salvo el portfolio de referencia del docente, ver nota en Benchmark).

## 1. Usuario objetivo

¿Quién visita este portfolio y qué necesita encontrar en **menos de 30 segundos**?

| Perfil | Qué busca | Qué tiene que encontrar en < 30 s |
|---|---|---|
| **Cliente potencial** (comercio, profesional o pyme de la región) — *primario* | Alguien que le haga un sitio o sistema y que sea confiable | Qué hago, un proyecto real parecido a lo que necesita, cómo contactarme |
| **Reclutador / líder técnico** — *secundario* | Un perfil junior/semi-senior con experiencia práctica | Stack, proyectos publicados, GitHub, formación |
| **Docente / evaluador** — *contexto académico* | Cumplimiento de la consigna y proceso UX | Las 9 secciones, caso de estudio, accesibilidad |

**Decisión:** priorizo al **cliente potencial**. Es quien más se beneficia de ver proyectos reales en producción (Rebord es exactamente su caso) y a quien la marca personal le tiene que generar confianza. El reclutador queda bien servido con las mismas piezas (métricas verificables, stack, GitHub).

## 2. Proto-persona

> Una proto-persona se construye con supuestos del equipo, **no con entrevistas**. Hay que validarla con el test de usabilidad (ver `06-test-usabilidad.md`).

**Martín, 42 — dueño de una inmobiliaria / comercio en Entre Ríos**

- **Contexto:** tiene un negocio con trayectoria local; hoy publica en redes sociales y portales, pero quiere un sitio propio.
- **Dispositivo:** llega desde el **celular**, por un link que le pasaron por WhatsApp o desde Instagram.
- **Objetivos:** entender rápido si esta persona puede resolver lo que necesita; ver algo terminado y funcionando; contactar sin vueltas.
- **Frustraciones:** sitios de “desarrolladores” llenos de jerga técnica; portfolios con proyectos de práctica que no se parecen a un negocio real; no encontrar un medio de contacto claro.
- **Frase:** *“No necesito saber qué es Next.js. Necesito ver que ya lo hiciste para alguien como yo.”*

## 3. Escenario de uso

1. Martín recibe por WhatsApp el link al portfolio mientras está en el local.
2. Lo abre en el celular. En el **hero** lee “Desarrollador Web & Software” y la propuesta de valor; ve el botón “Ver proyectos”.
3. Toca “Ver proyectos” y lo primero que aparece es **Rebord Negocios Inmobiliarios — Cliente real**, una inmobiliaria de la zona.
4. Toca “Visitar sitio”, recorre el catálogo publicado y vuelve.
5. Entra al **caso de estudio** para entender cómo se pensó el proyecto.
6. Baja a **Contacto** (o usa el menú) y toca “Escribirme un email”.

**Tiempo objetivo:** de la llegada al primer proyecto real, menos de 30 segundos y 1–2 toques.

## 4. Benchmark (3 portfolios de referencia)

Capturas de las versiones publicadas (noviembre de 2026) en [`img/`](img/).

| | **Brittany Chiang** — [brittanychiang.com](https://brittanychiang.com) | **Lee Robinson** — [leerob.com](https://leerob.com) | **Rauno Freiberg** — [rauno.me](https://rauno.me) |
|---|---|---|---|
| Perfil | Frontend engineer | Ingeniero y escritor (ex-Vercel) | Diseñador de interacción |
| Estructura | One-page: About, Experience, Projects; columna izquierda fija con nav | Bio en prosa + listas de notas y blogs | Página experimental con tarjetas horizontales y manifiesto |
| **Qué funciona** | Nav por anclas con indicador de sección activa; experiencia con período + rol + tags; link “saltar al contenido”; capturas en proyectos | Velocidad y legibilidad extremas; jerarquía tipográfica clara; contacto con `mailto:` directo | Identidad muy fuerte con pocos recursos; microinteracciones (copiar email al portapapeles); tipografía como protagonista |
| **Qué no funciona** (para mi usuario) | Paleta oscura muy reconocible y muy copiada; mucho texto antes de ver un proyecto; pensado para reclutadores, no para clientes | Casi no muestra proyectos ni imágenes: un cliente no ve “qué hizo”; poco escaneable | La navegación experimental exige explorar; no comunica servicios ni contacto rápido; poco claro para alguien no técnico |
| **Qué tomo** | Indicador de sección activa, timeline con período + tags, skip link | Tipografía sans sobria, aire, mailto visible | Copiar email, detalle tipográfico, un único color de acento |

**Nota:** la consigna permite incluir el portfolio de referencia del docente. Como no tengo su URL a mano, el benchmark usa tres referentes públicos e identificables. *Pendiente opcional:* agregar el del docente como cuarta columna antes de la entrega.

## 5. Moodboard y concepto visual

Ver [`design/moodboard.html`](design/moodboard.html) (exportado en `img/moodboard.png`).

**Concepto: “Precisión digital”** — el lenguaje de un plano técnico (grillas finas, medidas, índices numerados, tipografía monoespaciada para datos) aplicado a un portfolio claro y editorial.

### Tres palabras clave

| Palabra | Cómo se traduce en color | En tipografía | En imágenes y recursos |
|---|---|---|---|
| **Innovación** | Un único acento **azul eléctrico** `#2E3BFF` sobre neutros | Geist: sans geométrica contemporánea, diseñada para interfaces | Capturas reales de productos digitales dentro de marcos de navegador |
| **Precisión** | Neutros cálidos y líneas de 1 px `#E4E3DC`; contraste AA en todo | **Geist Mono** para etiquetas, índices (`01`, `02`), períodos y fuentes de datos | Grilla de plano de fondo, marcas de esquina, métricas con su fuente |
| **Simplicidad** | Fondo blanco cálido `#FAFAF7`, sin gradientes llamativos | Escala corta (8 tamaños), pesos 400–600 | Mucho espacio en blanco, íconos de línea, cero emojis |

### Justificación de colores

- **Blanco cálido `#FAFAF7`** en vez de blanco puro: menos fatiga visual y una sensación más “editorial” que un fondo `#FFF` de plantilla.
- **Tinta `#0D0E12`** casi negra para títulos; **`#3A3D45`** para párrafos (10.4:1) y **`#5E616B`** para texto secundario (5.9:1). Todo supera AA.
- **Azul eléctrico `#2E3BFF`** (6.3:1 sobre el fondo; texto blanco sobre azul 6.6:1): transmite tecnología y confianza; se usa solo para acciones y detalles, así guía la mirada.
- **Violeta `#6B4BFF`** (4.9:1) como secundario, reservado para diferenciar “Producto propio”.
- **Verde `#0F7B4B`** solo para el estado del badge.
- **Modo oscuro** con los mismos roles (acento `#7C8AFF`, 6.5:1 sobre `#0B0C10`).
- Me diferencio de la referencia típica (paleta oscura navy + verde menta) con una base **clara y cálida**.

### Justificación tipográfica (máx. 2 familias)

- **Geist** (títulos y texto): sans neo-grotesca de Vercel, muy legible en pantalla, con buen rendimiento en tamaños display (120 px) y en cuerpo (16 px). Variable: un solo archivo de 57 KB cubre todos los pesos.
- **Geist Mono** (datos y etiquetas): refuerza “precisión” y lo técnico sin recargar.
- Licencia **SIL Open Font License**; auto-hospedadas con `font-display: swap` (sin dependencias externas ni bloqueo de render).
