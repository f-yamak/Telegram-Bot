from telegram import ParseMode
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update


"""Response when bot is called for the first time and /start is commanded"""
def start_command(update: Update, context: CallbackContext):
    message = "You can search all series by typing the serie name. Please make sure the serie name is correct. You can see the details of the search results by typing <b>/help</b>"
    update.message.reply_text(message,parse_mode = ParseMode.HTML)
    

"""Responds to the /help command"""
def help(update: Update, context: CallbackContext):
    update.message.reply_text("I am botonom. My purpose is to show deatail of series." +
                              "\nYou can search for the serie you want by typing its name." + 
                              "\nSerie details are shown as below" +
                              "\n\n[Name] (date)" +
                              "\n[IMDB] / [Language]" +
                              "\n[Summary]"+
                              "\n[Creator and Series Cast]" +
                              "\n[Episodes] (Rating)")



"""Responds to the Incorrect command"""
def unknown_command(update: Update, context: CallbackContext):
    # hatalı komut girilince döndürülecek mesaj
    update.message.reply_text("Unknown command!")