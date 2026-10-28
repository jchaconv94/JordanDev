import asyncio, json, os, edge_tts
SEGS = [
"¡Espera! Si tu negocio todavía depende de cuadernos y Excel… este video es para ti.",
"Inventarios que no cuadran. Reportes que te roban la tarde. Clientes esperando.",
"¿Y si todo eso funcionara solo?",
"Soy ingeniero de sistemas, y convierto tus ideas en software que trabaja por ti.",
"¿Necesitas una app? La desarrollo. ¿Un sistema web? Lo construyo. ¿Algo a tu medida? Lo creamos.",
"Ventas, inventario y facturación electrónica con SUNAT, todo en un solo lugar, y desde tu celular.",
"Reportes automáticos, alertas al instante, y decisiones con datos reales.",
"¿Y si algo falla? No estás solo: soporte técnico, redes y seguridad.",
"Y no es una promesa: ya he creado más de diez aplicaciones reales, para salud, finanzas y negocios… ¡y hasta un bingo virtual!",
"Me encargo de todo: analizo, diseño, desarrollo, lanzo… y te acompaño.",
"¿Tienes una idea? Escríbeme hoy al 956 606 972. ¡Tu negocio puede ser el próximo!",
]
async def one(voice, i, text):
    c = edge_tts.Communicate(text, voice, rate="+12%", boundary="WordBoundary")
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
