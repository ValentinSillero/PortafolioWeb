# 03 · Wireframes de baja fidelidad

Página completa, mobile (375 px) y desktop (1280 px), con las 9 secciones en el orden final.

| Mobile 375 | Desktop 1280 |
|---|---|
| [`img/wireframe-mobile.png`](img/wireframe-mobile.png) | [`img/wireframe-desktop.png`](img/wireframe-desktop.png) |

**Fuente editable:** `design/wireframe-mobile.html` y `design/wireframe-desktop.html`, generados con `design/wf.py` desde una única estructura (así mobile y desktop siempre tienen el mismo contenido). Para regenerarlos: `python docs/design/wf.py`.

## Convenciones

- Rectángulo con cruz = imagen. Barra negra = título; barra gris = texto.
- Etiqueta naranja arriba a la derecha = número de sección de la consigna.
- Pastilla negra = botón primario; pastilla con borde = secundario.

## Decisiones que se fijaron en el wireframe

1. **Hero:** el nombre ocupa todo el ancho; debajo, texto + CTAs a la izquierda y vista previa del último proyecto a la derecha (en mobile la vista previa se omite para no empujar los CTAs).
2. **Métricas:** 4 tarjetas en fila (2×2 en mobile), cada una con su fuente.
3. **Proyectos:** el destacado (cliente real) a todo el ancho con imagen a la izquierda; los otros dos en dos columnas. En mobile, todo apilado y botones a ancho completo.
4. **Experiencia:** título fijo a la izquierda + timeline a la derecha en desktop.
5. **Contacto:** bloque oscuro de alto contraste para marcar el cierre.

## Pendiente de Figma

Pasar estos wireframes a una página “Wireframes” del archivo de Figma (ver `05-figma.md`).
