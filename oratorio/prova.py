import telepot
import time
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
bot = telepot.Bot('323732341:AAHeG_XRJNmwxRTNvDy7RmJFxNJXo7-hPFk')
bot.setWebhook()
iscritti = []
maglietteordinate = []
piazzaduomo = []
mandatoanimatori = []


def on_callback_query(msg):

    user = msg['from']
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    if query_data == 'Piazza Duomo' and user['id'] not in piazzaduomo:
        with open('./piazzaduomo.txt', 'a') as f:
            f.write(str(user['last_name']) + ' ' + user['first_name'] + '\n')
        piazzaduomo.append(user['id'])
        bot.sendMessage(user['id'], user['first_name'] + ' ti sei correttamente iscritto alla proposta Piazza Duomo',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[[KeyboardButton(text="Piazza duomo")], [KeyboardButton(text="mandato animatori")]
                                      ]))
    elif query_data == 'XXL' and user['id'] not in maglietteordinate:
        with open('./magliette.txt', 'a') as f:
            f.write(str(user['last_name']) + ' ' + user['first_name'] + ' ' + query_data + '\n')
        maglietteordinate.append(user['id'])
        bot.sendMessage(user['id'], user['first_name'] + ' hai ordinato una maglietta animatori taglia XXL',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[[KeyboardButton(text="Piazza duomo")], [KeyboardButton(text="mandato animatori")]
                                      ]))
        bot.answerCallbackQuery(query_id, text='XXL')
    elif query_data == 'XL' and user['id'] not in maglietteordinate:
        with open('./magliette.txt', 'a') as f:
            f.write(str(user['last_name']) + ' ' + user['first_name'] + ' ' + query_data + '\n')
        maglietteordinate.append(user['id'])
        bot.sendMessage(user['id'], user['first_name'] + ' hai ordinato una maglietta animatori taglia XL',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[[KeyboardButton(text="Piazza duomo")], [KeyboardButton(text="mandato animatori")]
                                      ]))
        bot.answerCallbackQuery(query_id, text='XL')
    elif query_data == 'L' and user['id'] not in maglietteordinate:
        with open('./magliette.txt', 'a') as f:
            f.write(str(user['last_name']) + ' ' + user['first_name'] + ' ' + query_data + '\n')
        maglietteordinate.append(user['id'])
        bot.sendMessage(user['id'], user['first_name'] + ' hai ordinato una maglietta animatori taglia L',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[[KeyboardButton(text="Piazza duomo")], [KeyboardButton(text="mandato animatori")]
                                      ]))
        bot.answerCallbackQuery(query_id, text='L')
    elif query_data == 'M' and user['id'] not in maglietteordinate:
        with open('./magliette.txt', 'a') as f:
            f.write(str(user['last_name']) + ' ' + user['first_name'] + ' ' + query_data + '\n')
        maglietteordinate.append(user['id'])
        bot.sendMessage(user['id'], user['first_name'] + ' hai ordinato una maglietta animatori taglia M',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[[KeyboardButton(text="Piazza duomo")], [KeyboardButton(text="mandato animatori")]
                                      ]))
        bot.answerCallbackQuery(query_id, text='M')
    elif query_data == 'S' and user['id'] not in maglietteordinate:
        with open('./magliette.txt', 'a') as f:
            f.write(str(user['last_name']) + ' ' + user['first_name'] + ' ' + query_data + '\n')
        maglietteordinate.append(user['id'])
        bot.sendMessage(user['id'], user['first_name'] + ' hai ordinato una maglietta animatori taglia S',
                        reply_markup=ReplyKeyboardMarkup(
                            keyboard=[[KeyboardButton(text="Piazza duomo")], [KeyboardButton(text="mandato animatori")]
                                      ]))
        bot.answerCallbackQuery(query_id, text='S')
    elif (query_data == 'XXL' or query_data == 'XL' or query_data == 'L' or query_data == 'M' or query_data == 'S') \
            and user['id'] in maglietteordinate:
        bot.sendMessage(user['id'], user['first_name'] + ' hai già ordinato una maglietta!')


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, msg)
    user = msg['from']

    # NOTA BENE, DA MODIFICARE AGGIUNGENDO COMANDI QUALORA SI PARTISSE CON PIU' COMANDI
    if content_type == 'text' and 'reply_to_message' not in msg:
        if msg['text'] == '/start':
            if 'last_name' not in user or 'username' not in user:
                bot.sendMessage(chat_id, 'Prima di procedere controlla nelle impostazioni di telegram '
                                         'di aver correttamente inserito il Congnome e lo Username. '
                                         'Una volta fatto, premi "Ho fatto"',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="Ho fatto")]
                                    ]
                                ))
            else:
                bot.sendMessage(chat_id, 'Seleziona tra i comandi disponibili',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="Prenota maglietta")],
                                        [KeyboardButton(text="Piazza duomo")],
                                        [KeyboardButton(text="Mandato animatori")]
                                    ]))
                iscritti.append(user['id'])
            with open('./id.txt', 'a') as f:
                f.write(str(msg['chat']['id']) + '\n')

        # RICONTROLLO SUL COGNOME E SULLO USERNAME,
        # QUANDO SI AVRA' DAVVERO FATTO ALLORA VERRANNO VISUALIZZATI I COMANDI BASE.
        elif msg['text'] == 'Ho fatto':
            if 'last_name' not in user or 'username' not in user:
                bot.sendMessage(chat_id, 'Prima di procedere controlla nelle impostazioni di telegram'
                                         ' di aver correttamente inserito il Congnome e lo Username. '
                                         'Una volta fatto, premi "Ho fatto"',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="Ho fatto")]
                                    ]
                                ))
            else:
                bot.sendMessage(chat_id, 'Seleziona tra i comandi disponibili',
                                reply_markup=ReplyKeyboardMarkup(
                                    keyboard=[
                                        [KeyboardButton(text="Prenota maglietta")],
                                        [KeyboardButton(text="Piazza duomo")],
                                        [KeyboardButton(text="mandato animatori")]
                                    ]))
                iscritti.append(user['id'])
            with open('./id.txt', 'a') as f:
                f.write(str(msg['chat']['id']) + '\n')

        # COMANDO PER PIAZZA DUOMO
        elif msg['text'] == 'Piazza duomo' and user['id'] not in piazzaduomo:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Partecipo', callback_data='Piazza Duomo')]
            ])
            bot.sendMessage(chat_id, 'Ciao, utilizza questo comando per iscriverti alla proposta Piazza Duomo. '
                                     'VENERDÌ 19 MAGGIO5€ PER IL PULLMANCENA AL SACCORientro previsto per le 00.00',
                            reply_markup=keyboard)

        elif msg['text'] == 'Piazza duomo' and user['id'] in piazzaduomo:
            bot.sendMessage(chat_id, user['first_name'] + ' hai già effetuato l'' iscrizione per Piazza Duomo')

        elif msg['text'] == 'Prenota maglietta' and user['id'] not in maglietteordinate:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='XXL', callback_data='XXL')],
                                                             [InlineKeyboardButton(text='XL', callback_data='XL')],
                                                             [InlineKeyboardButton(text='L', callback_data='L')],
                                                             [InlineKeyboardButton(text='M', callback_data='M')],
                                                             [InlineKeyboardButton(text='S', callback_data='S')]
                                                             ])
            bot.sendMessage(chat_id, 'Ciao, utilizza questo comando per prenotare la tua maglietta animatori',
                            reply_markup=keyboard)

        elif msg['text'] == 'Prenota maglietta' and user['id'] in maglietteordinate:
            bot.sendMessage(chat_id, user['first_name'] + ' hai già prenotato la tua maglietta')


        elif msg['text'] == 'admin' and user['username'] in ['MassimoSchiavo', 'LucaRedaschi']:
            bot.sendMessage(chat_id, 'Scrivi qui il testo che vuoi inviare a tutti gli utenti',
                            reply_markup=ForceReply())

        elif 'reply_to_message' in msg and user['username'] in ['MassimoSchiavo', 'LucaRedaschi']:
            sendMessaggio(msg['text'])

        else:
            print(msg)
            bot.sendMessage(chat_id, user['first_name'] + ' puoi effettuare'
                                                          ' solamente le operazioni consentite dal menù sottostante.',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[[KeyboardButton(text="Piazza duomo")],
                                          [KeyboardButton(text="mandato animatori")]
                                          ]))
    if 'reply_to_message' in msg:
        if content_type == 'text':
            sendMessaggio(msg['text'])
        elif content_type == 'sticker':
            sendSticker(msg['sticker'])
        elif content_type == 'document':
            sendDocument(msg['document'])
        elif content_type == 'photo':
            sendPhoto(msg['photo'])

def sendPhoto(sms):
    with open('./id.txt', 'r') as idfile:
        chat_id = str(idfile.read())
    idfile.close()
    elencomembri = chat_id.split('\n')
    for membro in elencomembri[0:len(elencomembri) - 1]:
        bot.sendPhoto(int(membro), sms[1]['file_id'])


def sendDocument(sms):
    with open('./id.txt', 'r') as idfile:
        chat_id = str(idfile.read())
    idfile.close()
    elencomembri = chat_id.split('\n')
    for membro in elencomembri[0:len(elencomembri) - 1]:
        bot.sendDocument(int(membro), sms['file_id'])

def sendMessaggio(sms):
    with open('./id.txt', 'r') as idfile:
        chat_id = str(idfile.read())
    idfile.close()
    elencomembri = chat_id.split('\n')
    for membro in elencomembri[0:len(elencomembri) - 1]:
        bot.sendMessage(int(membro), sms)


def sendSticker(sms):
    with open('./id.txt', 'r') as idfile:
        chat_id = str(idfile.read())
    idfile.close()
    elencomembri = chat_id.split('\n')
    for membro in elencomembri[0:len(elencomembri) - 1]:
        bot.sendSticker(int(membro), sms['file_id'])


MessageLoop(bot, {'chat': handle, 'callback_query': on_callback_query}).run_as_thread()

print('Listening...')
while 1:
    time.sleep(1)
    if time.strftime("%H:%M:%S") == '18:22:00':
        elencomagliette = open('./magliette.txt')
        bot.sendDocument(126318224, elencomagliette)