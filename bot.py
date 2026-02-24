import telebot

TOKEN = "8539214283:AAEhFR-dK9KAV6RadULB72enCZ2z4vPeR04"

bot = telebot.TeleBot(TOKEN)

def calcular_value(cuota):
    prob_implicita = 1 / cuota
    prob_estimada = 0.60  # estimación base 60%
    
    if prob_estimada > prob_implicita:
        value = "✅ Sí hay value"
    else:
        value = "❌ No hay value"
    
    return prob_implicita, prob_estimada, value

@bot.message_handler(func=lambda message: True)
def analizar_apuesta(message):
    try:
        cuota = float(message.text)
        prob_implicita, prob_estimada, value = calcular_value(cuota)
        
        respuesta = f"""
📊 Análisis de Cuota

Cuota: {cuota}
Probabilidad implícita: {round(prob_implicita*100,2)}%
Probabilidad estimada: {round(prob_estimada*100,2)}%

Resultado:
{value}
"""
        bot.reply_to(message, respuesta)
    except:
        bot.reply_to(message, "Envíame solo la cuota. Ejemplo: 1.85")

bot.polling()
