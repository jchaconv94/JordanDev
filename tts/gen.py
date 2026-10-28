import asyncio, json, os, edge_tts
SEGS = [
"Y no es una promesa: ya he creado más de diez aplicaciones reales. Para salud: Toolkit SISMED, Inmunia y EasyPharma. Para finanzas: Serviqo, Yupana y Pagadia. Y para negocios: AgroAcopio, Comprobante OK, Tenlo y sistemas para restaurantes.",
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
                await one("es-PE-AlexNeural", 8, s); break
            except Exception as e:
                print("retry", i, e); await asyncio.sleep(3)
asyncio.run(main())
