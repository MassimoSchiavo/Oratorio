import telepot

bot = telepot.Bot('323732341:AAHeG_XRJNmwxRTNvDy7RmJFxNJXo7-hPFk')
bot.setWebhook()

with open('./id.txt', 'r') as idfile:
    chat_id = str(idfile.read())
idfile.close()
elencomembri = chat_id.split('\n')
for membro in elencomembri[0:len(elencomembri)-1]:
    bot.sendMessage(int(membro), "Questa è una prova per l'invio a tutti i contatti di un messaggio")
