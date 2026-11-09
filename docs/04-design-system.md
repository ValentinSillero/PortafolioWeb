# 04 · Design system

Vista completa: [`img/design-system.png`](img/design-system.png) · Fuente: [`design/design-system.html`](design/design-system.html) (usa la misma hoja de estilos del sitio).
Tokens en código: `assets/css/styles.css` → bloque `:root`.

## Paleta

| Rol | Token | Claro | Oscuro | Contraste (claro) |
|---|---|---|---|---|
| Fondo | `--c-bg` | `#FAFAF7` | `#0B0C10` | — |
| Superficie | `--c-surface` / `--c-surface-2` | `#FFFFFF` / `#F3F3EE` | `#13151B` / `#101217` | — |
| Títulos | `--c-ink` | `#0D0E12` | `#F2F2EE` | 18.9:1 |
| Párrafos | `--c-ink-2` | `#3A3D45` | `#CDCFD6` | 10.4:1 |
| Secundario | `--c-muted` | `#5E616B` | `#A3A6B0` | 5.9:1 |
| Bordes | `--c-line` / `--c-line-strong` | `#E4E3DC` / `#CFCEC6` | `#262932` / `#353945` | decorativo |
| **Primario** | `--c-accent` | `#2E3BFF` | `#7C8AFF` | 6.3:1 · blanco sobre él 6.6:1 |
| Primario hover / active | `--c-accent-hover` / `--c-accent-active` | `#1E28D6` / `#161EA8` | `#98A3FF` / `#B3BBFF` | — |
| **Secundario** | `--c-violet` | `#6B4BFF` | `#A894FF` | 4.9:1 |
| Estado éxito | `--c-success` | `#0F7B4B` | `#3DDC97` | 5.1:1 |
| Estado error | `--c-danger` | `#B42318` | — | 6.6:1 sobre blanco |

## Escala tipográfica (Geist / Geist Mono)

| Token | Tamaño | Uso |
|---|---|---|
| `--fs-display` | clamp 48 → 120 px | Nombre en el hero |
| `--fs-3xl` | clamp 34 → 56 px | Títulos de sección (h2) |
| `--fs-2xl` | clamp 28 → 40 px | Títulos de proyecto (h3) |
| `--fs-xl` | 24 px | Lead, títulos de tarjeta |
| `--fs-lg` | 20 px | Subtítulos |
| `--fs-md` | 18 px | Párrafo destacado |
| `--fs-base` | 16 px | Texto base (interlineado 1.6) |
| `--fs-sm` | 14 px | Descripciones, tags |
| `--fs-xs` | 12 px | Etiquetas mono en mayúsculas |

## Espaciado y grilla

- Escala base **4 px**: 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 80 · 96.
- Padding vertical de sección fluido: 64 → 128 px.
- Grilla: **4 columnas** (375, gutter 16) · **8 columnas** (768) · **12 columnas** (1280, gutter 24, contenedor máx. 1200 px).
- Breakpoints: 640 · 768 · 1024 · 1280. Layout con **Flexbox y CSS Grid** únicamente.
- Radios: 6 · 12 · 20 · pill. Bordes de 1 px.

## Componentes

| Componente | Variantes / estados | Clase |
|---|---|---|
| Botón | primario · secundario · claro (sobre oscuro) · ghost · sm — **default / hover / focus-visible / active** + disabled | `.btn`, `.btn-primary`, `.btn-secondary`, `.btn-light`, `.btn-ghost-light` |
| Botón ícono | hover / focus / active | `.icon-btn` |
| Tag | default / hover | `.tag` |
| Pill de tipo | cliente (azul) · producto (violeta) · neutro | `.pill`, `.pill-accent`, `.pill-violet` |
| Badge de estado | con punto animado (se apaga con reduced motion) | `.badge`, `.status-dot` |
| Tarjeta de proyecto | estándar · destacada — hover: elevación + zoom de captura | `.project`, `.project-featured` |
| Ítem de timeline | marcador · período mono · rol · institución · 2 logros | `.timeline-item` |
| Tarjeta de skill / principio | hover con borde | `.skill-card`, `.principle` |
| Modal de detalle | `<dialog>` nativo, cierre con Esc / fondo / botón | `.dialog` |
| Input | **No aplica:** no hay formulario (es opcional y no quiero uno que simule enviar) | — |

## Microinteracciones

Hover en tarjetas (elevación + zoom), flecha que avanza en botones, indicador de sección activa, contador de métricas, copiar email con confirmación, menú hamburguesa que se transforma en cruz, entrada suave de secciones. Todas respetan `prefers-reduced-motion`.
