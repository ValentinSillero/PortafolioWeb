# Genera los wireframes de baja fidelidad (mobile y desktop, página completa).
# Uso: python docs/design/wf.py  -> crea wireframe-mobile.html y wireframe-desktop.html
import pathlib

CSS = """
*{box-sizing:border-box}body{margin:0;background:#EDEDE8;font:12px/1.4 ui-monospace,Consolas,monospace;color:#222}
.page{width:%(w)spx;margin:24px auto;background:#fff;border:1.5px solid #222}
.sec{position:relative;border-bottom:1.5px dashed #999;padding:%(pad)spx}
.tag{position:absolute;top:6px;right:8px;font-size:10px;color:#C2410C;text-transform:uppercase;letter-spacing:.06em}
.row{display:flex;gap:%(gap)spx;align-items:center}.col{display:flex;flex-direction:column;gap:10px}
.grid{display:grid;gap:%(gap)spx}.b{border:1.5px solid #222;border-radius:6px;background:#fff}
.g{background:#D9D9D4}.l{height:9px;background:#C8C8C2;border-radius:3px}.lt{height:9px;background:#E3E3DE;border-radius:3px}
.x{position:relative;background:#E9E9E4;border:1.5px solid #222;border-radius:6px;overflow:hidden}
.x:before,.x:after{content:"";position:absolute;inset:0;background:linear-gradient(to top right,transparent calc(50%% - 1px),#999 50%%,transparent calc(50%% + 1px))}
.x:after{background:linear-gradient(to top left,transparent calc(50%% - 1px),#999 50%%,transparent calc(50%% + 1px))}
.btn{height:40px;border:1.5px solid #222;border-radius:20px;display:flex;align-items:center;justify-content:center;padding:0 18px;font-size:11px}
.btn.p{background:#222;color:#fff}.pill{height:26px;border:1.5px solid #222;border-radius:13px;width:170px;display:flex;align-items:center;padding:0 10px;font-size:10px}
.h1{height:%(h1)spx;background:#222;border-radius:4px}.h2{height:%(h2)spx;background:#555;border-radius:4px}
.chip{height:22px;width:64px;border:1.2px solid #777;border-radius:11px;display:inline-block;margin:0 6px 6px 0}
.dark{background:#333;color:#fff;border-radius:10px;padding:%(pad)spx}.dark .l{background:#777}.dark .lt{background:#555}
.note{font-size:10px;color:#C2410C}
"""

def lines(n, widths=(100, 92, 70)):
    return "".join(f'<div class="l" style="width:{widths[i % len(widths)]}%"></div>' for i in range(n))

def build(mobile):
    w = 375 if mobile else 1280
    pad = 20 if mobile else 56
    gap = 12 if mobile else 24
    css = CSS % {"w": w, "pad": pad, "gap": gap, "h1": 44 if mobile else 96, "h2": 24 if mobile else 34}
    cols = lambda d, m: (m if mobile else d)
    nav = '<div class="b" style="width:40px;height:40px;border-radius:20px"></div>' if mobile else \
        '<div class="row">' + "".join('<div class="lt" style="width:60px"></div>' for _ in range(6)) + '<div class="b" style="width:30px;height:30px;border-radius:15px"></div><div class="btn p">Contactarme</div></div>'
    hero_img = "" if mobile else '<div class="col" style="flex:1"><div class="x" style="height:300px"></div><div class="row" style="justify-content:space-between"><div class="lt" style="width:140px"></div><div class="l" style="width:90px"></div></div></div>'
    specs = "".join('<div class="col" style="flex:1;border-top:1.5px solid #222;padding-top:10px"><div class="lt" style="width:60px"></div><div class="l" style="width:80%"></div></div>' for _ in range(3))
    metrics = "".join('<div class="b col" style="padding:16px"><div class="h1" style="width:60%;height:' + ("34" if mobile else "48") + 'px"></div>' + lines(2) + '<div class="lt" style="width:70%"></div></div>' for _ in range(4))
    principles = "".join('<div class="b col" style="padding:14px"><div class="g" style="width:22px;height:22px;border-radius:4px"></div><div class="l" style="width:70%;background:#555"></div>' + lines(2) + "</div>" for _ in range(3))
    skills = "".join('<div class="b col" style="padding:18px"><div class="g" style="width:40px;height:40px;border-radius:8px"></div><div class="h2" style="width:50%;height:18px"></div>' + lines(2) + '<div>' + '<span class="chip"></span>' * 6 + "</div></div>" for _ in range(4))
    def project(feat=False):
        body = '<div class="col" style="padding:18px;flex:1"><div class="row"><div class="pill" style="width:90px">TIPO</div><div class="lt" style="width:40px"></div></div><div class="h2" style="width:80%"></div>' + lines(3) + '<div class="row" style="border-block:1.2px solid #999;padding:10px 0"><div class="col" style="flex:1"><div class="note">PROBLEMA</div>' + lines(2) + '</div><div class="col" style="flex:1"><div class="note">RESULTADO</div>' + lines(2) + '</div></div><div>' + '<span class="chip"></span>' * 6 + '</div><div class="row"><div class="btn p">Ver caso / detalles</div><div class="btn">Visitar sitio ↗</div></div></div>'
        img = f'<div class="x" style="{"flex:1.4;min-height:340px" if feat and not mobile else "height:" + ("190" if mobile else "260") + "px"}"></div>'
        direction = "row" if feat and not mobile else "col"
        return f'<div class="b {direction}" style="gap:0;overflow:hidden;{"grid-column:1/-1" if feat else ""}">{img}{body}</div>'
    timeline = "".join('<div class="row" style="align-items:flex-start"><div style="width:14px;height:14px;border:1.5px solid #222;border-radius:7px;margin-top:16px;flex:none"></div><div class="b col" style="padding:14px;flex:1"><div class="row"><div class="l" style="width:50px;background:#555"></div><div class="pill" style="width:70px;height:20px"></div></div><div class="h2" style="width:60%;height:16px"></div><div class="lt" style="width:50%"></div>' + lines(2) + "</div></div>" for _ in range(4))
    contact_rows = "".join('<div class="row" style="border-bottom:1px solid #777;padding:14px 0"><div class="g" style="width:20px;height:20px"></div><div class="col" style="flex:1"><div class="lt" style="width:50px"></div><div class="l" style="width:60%"></div></div><div>→</div></div>' for _ in range(3))
    footer_nav = "".join('<div class="lt" style="width:56px"></div>' for _ in range(6))

    html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Wireframe {'mobile 375' if mobile else 'desktop 1280'} — Valentín Sillero</title><style>{css}</style></head><body>
<div class="page">
 <div class="sec row" style="justify-content:space-between;padding-block:14px"><span class="tag">01 Header sticky</span><div class="row"><div class="g" style="width:36px;height:36px;border-radius:8px"></div><div class="l" style="width:110px;background:#555"></div></div>{nav}</div>
 <div class="sec col" style="gap:{gap}px"><span class="tag">02 Hero</span>
  <div class="row"><div class="lt" style="width:90px"></div><div class="lt" style="width:200px"></div></div>
  <div class="pill">● Consultá disponibilidad</div>
  <div class="h1" style="width:{'92' if mobile else '62'}%"></div><div class="h2" style="width:{'80' if mobile else '36'}%"></div>
  <div class="row" style="align-items:flex-start;gap:{gap * 2}px"><div class="col" style="flex:1;gap:{gap}px">{lines(3)}<div class="row"><div class="btn p">Ver proyectos →</div><div class="btn">Contactarme</div></div></div>{hero_img}</div>
  <div class="{'col' if mobile else 'row'}" style="gap:{gap}px">{specs}</div>
 </div>
 <div class="sec"><span class="tag">03 Métricas</span><div class="grid" style="grid-template-columns:repeat({cols(4, 2)},1fr)">{metrics}</div></div>
 <div class="sec col" style="gap:{gap}px"><span class="tag">07 Sobre mí</span><div class="lt" style="width:90px"></div><div class="h2" style="width:{'90' if mobile else '45'}%"></div>
  <div class="{'col' if mobile else 'row'}" style="align-items:flex-start;gap:{gap * 2}px"><div class="x" style="{'width:100%;height:300px' if mobile else 'width:380px;height:460px;flex:none'}"></div><div class="col" style="flex:1">{lines(5)}<div class="grid" style="grid-template-columns:repeat({cols(3, 1)},1fr);margin-top:12px">{principles}</div></div></div></div>
 <div class="sec col" style="gap:{gap}px;background:#F6F6F2"><span class="tag">04 Habilidades</span><div class="lt" style="width:90px"></div><div class="h2" style="width:{'90' if mobile else '45'}%"></div>{lines(1)}<div class="grid" style="grid-template-columns:repeat({cols(2, 1)},1fr)">{skills}</div></div>
 <div class="sec col" style="gap:{gap}px"><span class="tag">05 Proyectos</span><div class="lt" style="width:90px"></div><div class="h2" style="width:{'90' if mobile else '45'}%"></div><div class="grid" style="grid-template-columns:repeat({cols(2, 1)},1fr)">{project(True)}{project()}{project()}</div><div class="note">Destacado (cliente real) a todo el ancho · imagen = marco de navegador con captura real</div></div>
 <div class="sec" style="background:#F6F6F2"><span class="tag">06 Experiencia</span><div class="{'col' if mobile else 'row'}" style="align-items:flex-start;gap:{gap * 2}px"><div class="col" style="flex:5"><div class="lt" style="width:90px"></div><div class="h2" style="width:90%"></div><div class="h2" style="width:60%"></div></div><div class="col" style="flex:7;gap:14px;width:100%">{timeline}</div></div></div>
 <div class="sec"><span class="tag">08 Contacto</span><div class="dark {'col' if mobile else 'row'}" style="gap:{gap * 2}px;align-items:flex-end"><div class="col" style="flex:1.3;gap:14px"><div class="lt" style="width:80px"></div><div class="h1" style="width:80%;background:#eee"></div>{lines(2)}<div class="row"><div class="btn" style="background:#eee;color:#222">Escribirme un email</div><div class="btn" style="border-color:#aaa">Copiar email</div></div></div><div class="col" style="flex:1;width:100%">{contact_rows}</div></div></div>
 <div class="sec col" style="gap:16px;border-bottom:0"><span class="tag">09 Footer</span><div class="{'col' if mobile else 'row'}" style="justify-content:space-between;gap:16px"><div class="row"><div class="g" style="width:30px;height:30px;border-radius:6px"></div><div class="l" style="width:110px"></div></div><div class="row" style="flex-wrap:wrap">{footer_nav}</div><div class="row">{'<div class="b" style="width:34px;height:34px;border-radius:17px"></div>' * 3}</div></div><div class="lt" style="width:{'100' if mobile else '40'}%"></div></div>
</div></body></html>"""
    return html

here = pathlib.Path(__file__).parent
(here / "wireframe-mobile.html").write_text(build(True), encoding="utf-8")
(here / "wireframe-desktop.html").write_text(build(False), encoding="utf-8")
print("ok")
