import asyncio, json, os, edge_tts
TXT = "¡Espera! Si tu negocio todavía depende de cuadernos y Excel… ¡este video es para ti! ¿Necesitas una app? ¡La desarrollo! ¿Un sistema web? ¡Lo construyo!"
VOICES = [
 ("1_peru_alex", "es-PE-AlexNeural", "+18%", "+12Hz"),
 ("2_mexico_jorge", "es-MX-JorgeNeural", "+15%", "+6Hz"),
 ("3_colombia_gonzalo", "es-CO-GonzaloNeural", "+15%", "+6Hz"),
 ("4_latino_alonso", "es-US-AlonsoNeural", "+15%", "+6Hz"),
 ("5_argentina_tomas", "es-AR-TomasNeural", "+12%", "+4Hz"),
 ("6_andrew_multilingue", "en-US-AndrewMultilingualNeural", "+12%", "+4Hz"),
 ("7_brian_multilingue", "en-US-BrianMultilingualNeural", "+12%", "+4Hz"),
]
async def main():
    os.makedirs("out", exist_ok=True)
    for name, v, r, p in VOICES:
        for k in range(4):
            try:
                await edge_tts.Communicate(TXT, v, rate=r, pitch=p).save(f"out/{name}.mp3"); break
            except Exception as e:
                print("retry", name, e); await asyncio.sleep(3)
asyncio.run(main())
