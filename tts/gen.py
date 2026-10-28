import asyncio, json, os, edge_tts
SEGS = [
"¡Espera! Si tu negocio todavía depende de cuadernos y Excel… este video es para ti.",
"Inventarios que no cuadran. Reportes que te roban la tarde. Clientes esperando una respuesta.",
"¿Y si todo eso funcionara solo?",
"Soy ingeniero de sistemas, y convierto tus ideas en software que trabaja por ti, para que tú te enfoques en hacer crecer tu negocio.",
"¿Necesitas una app? La desarrollo. ¿Un sistema web? Lo construyo. ¿Algo único para tu empresa? Lo creamos a tu medida.",
"Ventas, inventario, caja y facturación electrónica con SUNAT… todo en un solo lugar, y desde tu celular.",
"Reportes automáticos. Alertas al instante. Decisiones con datos reales, no con suposiciones.",
"¿Y si algo falla? No estás solo: soporte técnico, redes y seguridad para proteger tu información.",
"Y esto no es una promesa. Ya he creado más de diez aplicaciones reales: para salud, Toolkit SISMED, Inmunia y EasyPharma. Para finanzas, Serviqo, Yupana y Pagadia. Para negocios, AgroAcopio, Comprobante OK, Tenlo y sistemas para restaurantes… y hasta un bingo virtual en línea.",
"Me encargo de todo: entiendo tu proceso, diseño la solución, la desarrollo, la lanzo… y te acompaño después.",
"¿Tienes una idea? Escríbeme hoy al 956 606 972. ¡Tu negocio puede ser el próximo!",
]
async def one(voice, i, text):
    c = edge_tts.Communicate(text, voice, rate="+10%", boundary="WordBoundary")
    words = []
    with open(f"out/{voice}_{i}.mp3", "wb") as f:
        async for ch in c.stream():
            if ch["type"] == "audio":
                f.write(ch["data"])
            elif ch["type"] == "WordBoundary":
                words.append([ch["offset"] / 1e7, ch["duration"] / 1e7, ch["text"]])
    json.dump(words, open(f"out/{voice}_{i}.json", "w"), ensure_ascii=False)
async def main():
    os.makedirs("out", exist_ok=True)
    for i, s in enumerate(SEGS):
        for k in range(5):
            try:
                await one("es-PE-AlexNeural", i, s); break
            except Exception as e:
                print("retry", i, e); await asyncio.sleep(3)
asyncio.run(main())
