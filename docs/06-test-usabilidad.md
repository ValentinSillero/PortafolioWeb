# 06 · Test de usabilidad

> **Estado: realizado el 9/11/2026 con 3 personas** sobre el sitio publicado. Resultados, hallazgos y cambios aplicados al final del documento.

## Objetivo

Verificar que una persona que llega por primera vez puede, sin ayuda, **encontrar cómo contactarme, abrir mis proyectos y entender qué hago** en poco tiempo.

## Formato

- **Participantes:** mínimo 3 (idealmente: 1 perfil “cliente” no técnico, 1 perfil técnico, 1 compañero/a de la materia).
- **Material:** prototipo de Figma o, si no está listo, el sitio publicado. Anotar cuál se usó.
- **Dispositivo:** al menos 1 prueba en celular y 1 en computadora.
- **Duración:** 10–15 minutos por persona.
- **Método:** pensar en voz alta. Quien modera no ayuda ni señala; solo repite la tarea si hace falta.
- **Registro:** tiempo por tarea, éxito (sí / con ayuda / no), comentarios textuales.

## Guion

**Introducción (leer):**
> “Gracias por ayudarme. Vamos a probar mi portfolio, no a vos: si algo cuesta, es un problema del diseño. Te voy a pedir algunas tareas; por favor decí en voz alta lo que pensás mientras lo hacés. Podés dejar cuando quieras.”

**Pregunta de 5 segundos:** mostrar el inicio 5 segundos y ocultarlo.
> “¿Qué recordás? ¿Quién es esta persona y a qué se dedica?”

| # | Tarea (leer textual) | Éxito si… |
|---|---|---|
| T1 | “Querés escribirle a Valentín. Encontrá su email.” | Llega al email o al botón “Escribirme un email” / “Copiar email” |
| T2 | “Abrí el sistema de gestión DEETA.” | Abre deetaia.vercel.app o el detalle de DEETA |
| T3 | “Buscá un proyecto relacionado con inmobiliarias y contame qué problema resolvía.” | Encuentra Rebord y menciona el problema (búsqueda/organización/contacto) |
| T4 | “¿Qué tecnologías usa Valentín para el frontend?” | Nombra al menos 3 del bloque Frontend |
| T5 | “Abrí el proyecto más reciente y su caso de estudio.” | Abre `caso-rebord.html` |
| T6 (mobile) | “Usá el menú para ir a Experiencia.” | Abre el menú hamburguesa y navega |

**Cierre:**
1. Del 1 al 5, ¿qué tan fácil fue encontrar lo que buscabas?
2. ¿Qué fue lo más confuso?
3. ¿Le escribirías para un proyecto? ¿Por qué?

## Plantilla de registro (una por participante)

```
Participante: P_   Perfil: ____________   Fecha: __/__/2026
Material: [ ] Prototipo Figma  [ ] Sitio publicado    Dispositivo: [ ] Mobile  [ ] Desktop

5 segundos — qué recordó: ___________________________________________

| Tarea | Éxito (Sí / Ayuda / No) | Tiempo | Observaciones / citas textuales |
|-------|-------------------------|--------|---------------------------------|
| T1    |                         |        |                                 |
| T2    |                         |        |                                 |
| T3    |                         |        |                                 |
| T4    |                         |        |                                 |
| T5    |                         |        |                                 |
| T6    |                         |        |                                 |

Facilidad (1–5): __   Lo más confuso: ____________________________
¿Le escribiría? ___________________________________________________
```

## Resultados del test (9/11/2026)

- **Material:** sitio publicado (https://portafolioweb-taupe-chi.vercel.app), versión previa a los cambios de este test.
- **Participantes:** 3 personas, con 2 pruebas en celular y 1 en computadora.
- **Registro:** cada participante hizo una tarea principal. Se anotaron observaciones y propuestas de mejora; **no se registraron tiempos ni la escala de facilidad**, por eso no figuran.

| Participante | Perfil | Dispositivo | Tarea | Observación | Mejora propuesta |
|---|---|---|---|---|---|
| P1 | Compañero de la facultad | Computadora | Encontrar los proyectos y acceder a Rebord | La navegación es clara y los proyectos están bien organizados | Destacar más el botón de contacto |
| P2 | Familiar | Celular | Abrir el menú y encontrar DEETA | El menú resulta intuitivo, aunque algunas descripciones son extensas | Acortar los textos de las tarjetas en mobile |
| P3 | Amigo (perfil potencial cliente) | Celular | Consultar los trabajos realizados y encontrar un medio de contacto | Los proyectos transmiten experiencia, pero “Visitar sitio” y “Ver caso de estudio” podrían distinguirse mejor | Diferenciar visualmente ambos botones |

**Lo que funcionó:** la navegación y la organización de los proyectos (P1), el menú mobile (P2) y la percepción de experiencia que transmiten los proyectos (P3).

> Nota de registro: estas observaciones primero quedaron documentadas como “evaluación simulada” (commits `7c72308` y `7da195a`) porque el texto original estaba redactado así. Valentín confirmó después que provienen de las tres personas indicadas, y este documento se corrigió en consecuencia.

## Síntesis de hallazgos

| # | Hallazgo | Participante | Cambio aplicado | Estado |
|---|---|---|---|---|
| H1 | El contacto no es lo bastante visible | P1 | En mobile y tablet el botón de contacto solo existía dentro del menú hamburguesa. Ahora hay un botón **“Contacto”** siempre visible en el header, junto al menú (en desktop ya estaba en la barra). | Aplicado · `7c72308` |
| H2 | Las descripciones de las tarjetas son extensas en mobile | P2 | Se acortaron la descripción, el problema y el resultado/aprendizaje de las 3 tarjetas (entre un 29 % y un 36 % menos de caracteres por tarjeta), sin quitar los campos que pide la consigna. | Aplicado · `7c72308` |
| H3 | “Visitar sitio” y “Ver caso de estudio” no se distinguen lo suficiente | P3 | La acción principal sigue como botón relleno (“Ver caso de estudio” / “Ver detalles”) y “Visitar sitio ↗” pasó a ser un **enlace subrayado** con ícono externo: dos niveles visuales para dos destinos distintos. | Aplicado · `7c72308` |

## Próximos pasos

- Repetir una ronda corta con las tareas que no se cubrieron (T1 encontrar el email, T4 tecnologías, T6 menú → Experiencia) y medir tiempos.
- Verificar con P1–P3 o con nuevas personas que los tres cambios resolvieron los hallazgos.
