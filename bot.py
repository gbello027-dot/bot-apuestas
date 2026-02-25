
import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("8539214283:AAEhFR-dK9KAV6RadULB72enCZ2z4vPeR04")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Bot de Apuestas Activo 🔥\n\n"
        "Envíame un partido así:\n"
        "Barcelona vs Real Madrid"
    )

def generar_analisis():
    over25 = random.randint(55, 75)
    ambos_marcan = random.randint(50, 70)
    
    if over25 > ambos_marcan:
        pick = "Over 2.5 goles"
        cuota_minima = "1.70"
    else:
        pick = "Ambos equipos marcan"
        cuota_minima = "1.65"

    return over25, ambos_marcan, pick, cuota_minima

async def analizar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    
    if "vs" not in texto.lower():
        await update.message.reply_text("Escríbeme el partido así:\nEquipo1 vs Equipo2")
        return
    
    over25, ambos, pick, cuota = generar_analisis()
    
    respuesta = (
        f"📊 Análisis del partido:\n\n"
        f"⚽ Over 2.5: {over25}%\n"
        f"⚽ Ambos marcan: {ambos}%\n\n"
        f"🔥 Pick recomendado: {pick}\n"
        f"💰 Cuota mínima de valor: {cuota}+"
    )
    
    await update.message.reply_text(respuesta)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analizar))

app.run_polling()
