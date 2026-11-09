# 07 · Commits y despliegue

## Cómo se organizó el historial

El proyecto se desarrolló completo en una misma sesión de trabajo (9/11/2026) antes de inicializar Git. Para no inventar etapas, el historial **agrupa el trabajo terminado por áreas coherentes**: cada commit agrega una pieza real y completa (un documento del proceso, el design system, la estructura HTML, las interacciones, etc.). Las fechas de los commits son las reales y el orden sigue la dependencia lógica (proceso UX → design system → maquetación → contenido → despliegue → documentación), no una cronología reconstruida.

| # | Commit | Qué agrega |
|---|---|---|
| 1 | `docs(ux): investigación…` | Usuario, proto-persona, escenario y benchmark con capturas |
| 2 | `docs(ux): moodboard…` | Moodboard y concepto “Precisión digital” |
| 3 | `docs(ux): arquitectura…` | Sitemap, jerarquía y card sorting |
| 4 | `docs(ux): wireframes…` | Wireframes mobile y desktop + generador |
| 5 | `feat(ds): design system…` | Tokens CSS, tipografías, componentes y su documentación |
| 6 | `feat: estructura semántica…` | `index.html`, tema inicial, favicons y manifest |
| 7 | `feat(proyectos): capturas…` | Capturas reales en WebP |
| 8 | `feat(ui): interacciones…` | `main.js` |
| 9 | `feat(caso): caso de estudio…` | `caso-rebord.html` |
| 10 | `feat(seo): 404, robots…` | 404, robots, sitemap, imagen Open Graph |
| 11 | `chore(deploy): Vercel…` | `vercel.json`, `.vercelignore`, `.gitignore` |
| 12 | `docs: Figma, test…` | Figma, guion de test, este documento, pendientes |
| 13 | `docs: presentación…` | PDF del proceso, capturas, reportes Lighthouse |
| 14 | `docs: README…` | README completo |

Los cambios siguientes (URL publicada, email, LinkedIn, hallazgos del test de usabilidad) se suman como commits nuevos a medida que ocurren, por ejemplo `fix(ux): …` por cada hallazgo aplicado.

## Publicar en GitHub

```bash
gh repo create portfolio --public --source . --remote origin --description "Portfolio de Valentín Sillero — Desarrollador Web & Software"
git push -u origin main
```

(O crear el repo `portfolio` en github.com como **público** y seguir las instrucciones de “push an existing repository”.)

## Desplegar en Vercel (CI/CD desde GitHub)

1. Entrar a [vercel.com/new](https://vercel.com/new) con la cuenta de GitHub.
2. **Import Git Repository** → elegir `ValentinSillero/portfolio`.
3. **Framework Preset: Other**. Build Command: *vacío*. Output Directory: *vacío* (raíz). Install Command: *vacío*.
4. **Deploy**. Vercel publica en `https://<proyecto>.vercel.app` con HTTPS.
5. Desde ese momento, cada `git push` a `main` despliega a producción y cada pull request genera una URL de preview.
6. Reemplazar `SITE_URL` (en `index.html`, `caso-rebord.html`, `404.html`, `robots.txt`, `sitemap.xml`) por el dominio final, commitear y pushear.
7. Agregar la URL en el README y en la descripción del repo (**About → Website**).

`vercel.json` ya define headers de seguridad (CSP, HSTS, X-Frame-Options, nosniff, Referrer-Policy, Permissions-Policy) y caché por tipo de recurso. `.vercelignore` evita publicar `docs/`.
