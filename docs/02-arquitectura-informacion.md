# 02 · Arquitectura de información

## Sitemap

```
valentinsillero (one-page)                      Páginas internas
│
├── #inicio        Hero                         ├── /caso-rebord.html  Caso de estudio
├── #metricas      Métricas / highlights        │     01 Contexto · 02 Problema · 03 Objetivo
├── #sobre-mi      Sobre mí                     │     04 Proceso · 05 Solución · 06 Resultados
├── #habilidades   Skills (4 categorías)        │     → Siguiente proyecto
├── #proyectos     Proyectos (3)                ├── /404.html  Página no encontrada
│     ├── Rebord  → caso de estudio + sitio     │
│     ├── DEETA   → modal de detalle + sitio    Externos
│     └── Cubrí   → modal de detalle + sitio    ├── github.com/ValentinSillero
├── #experiencia   Experiencia / formación      ├── LinkedIn (pendiente)
├── #contacto      Contacto (CTA)               └── Sitios publicados de los 3 proyectos
└── footer         Footer
```

Header fijo presente en todas las páginas, con anclas a: Inicio · Sobre mí · Habilidades · Proyectos · Experiencia · Contacto + GitHub + CTA “Contactarme”.

## Orden y jerarquía de secciones

| # | Sección | Ancla | Por qué está ahí |
|---|---|---|---|
| 1 | Header | — | Siempre visible: orientación y contacto a un toque |
| 2 | Hero | `#inicio` | Responde “quién es y qué hace” en 5 segundos |
| 3 | Métricas | `#metricas` | Prueba rápida y **verificable** (cada cifra tiene su fuente) |
| 4 | **Sobre mí** | `#sobre-mi` | *Cambio de orden justificado:* para un cliente, la confianza personal va antes del detalle técnico. Además coincide con el orden pedido para la navegación |
| 5 | Habilidades | `#habilidades` | Contexto técnico antes de ver los proyectos |
| 6 | Proyectos | `#proyectos` | El contenido más importante; el destacado (cliente real) va primero y a todo el ancho |
| 7 | Experiencia | `#experiencia` | Respalda los proyectos con un recorrido en el tiempo |
| 8 | Contacto | `#contacto` | Cierre con CTA potente |
| 9 | Footer | — | Navegación repetida, redes y créditos |

La consigna permite cambiar el orden “si se justifica”: las 9 secciones están presentes; solo **Sobre mí** sube antes de Habilidades.

## Justificación de la navegación

- **One-page con anclas**: el contenido es corto y lineal; cada sección es un paso del escenario de uso (conocer → confiar → ver trabajo → contactar).
- **Header sticky** con CTA “Contactarme” siempre visible: el objetivo principal (contacto) nunca queda a más de un toque.
- **Indicador de sección activa** (`aria-current`) para orientarse durante el scroll.
- **Mobile:** menú hamburguesa a pantalla completa, con `aria-expanded`/`aria-controls`, cierre con `Esc` y foco contenido dentro del menú.
- **Proyectos:** dos acciones explícitas por tarjeta (“Ver caso / detalles” y “Visitar sitio”). No hago toda la tarjeta clickeable porque tiene dos destinos; la imagen sí abre el detalle (con el mouse) para quien hace clic ahí por instinto.
- **Caso de estudio en página interna** (no modal): se puede compartir por link, indexar y leer con calma; tiene “Volver a proyectos” y “Siguiente proyecto”.
- `scroll-behavior: smooth` + `scroll-margin-top` para que el header fijo no tape los títulos.

## Card sorting simple

**Método:** card sorting **cerrado**, realizado por el autor con 24 tarjetas del contenido propio y las 9 categorías de la consigna. *Pendiente opcional:* repetirlo con 2–3 personas (abierto) para contrastar.

| Categoría | Tarjetas asignadas |
|---|---|
| Header | Logo VS · Links de sección · GitHub · CTA Contactarme · Cambio de tema |
| Hero | Nombre · Rol · Propuesta de valor · Badge disponibilidad · Ubicación + zona horaria · CTA Ver proyectos · CTA Contactarme |
| Métricas | 3 proyectos publicados · 400 propiedades en Rebord · 18 tecnologías · 25 repositorios |
| Sobre mí | Presentación · Retrato · 3 principios de trabajo |
| Habilidades | Frontend · Backend y BD · Herramientas y despliegue · Diseño UX/UI |
| Proyectos | Rebord · DEETA · Cubrí Seguros |
| Experiencia | Rebord (cliente) · DEETA (producto) · Licenciatura UADER · Cursos 2023–2024 |
| Contacto | Email · LinkedIn · GitHub · Copiar email |
| Footer | Copyright · Nav repetida · Redes · Crédito de tecnología |

**Tarjetas dudosas y decisión:**

- *“Cubrí Seguros”* encajaba en Proyectos y en Formación → va a **Proyectos** (es un producto navegable) y se **menciona** como logro en Formación.
- *“DEETA”* en Proyectos y Experiencia → aparece en ambos con **enfoques distintos**: en Proyectos el producto, en Experiencia mi rol.
- *“Cantidad de tecnologías”* en Métricas o Habilidades → **Métricas** (con la fuente “Detalle en Habilidades”).
