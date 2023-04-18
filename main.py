# Version 12.0.0b1 
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import Commands as cmd
import GeneralCommands as gc

# Created by BotFather
TOKEN = "YOUR_TOKEN"

def main():
    """Updater: This will contain the API key to specify in which bot we are adding functionalities to using our python code."""
    updater = Updater(TOKEN, use_context=True)    


    """Dispatcher: It is a class whose responsibility it is to do something with the updates."""
    ud = updater.dispatcher

    """CommandHandler: This Handler class is used to handle any command sent by the user to the bot, a command always starts with “/” i.e “/start”,”/help” etc."""
    ud.add_handler(CommandHandler("start", gc.start_command))
    ud.add_handler(CommandHandler("help", gc.help))

    """MessageHandler: This Handler class is used to handle any normal message sent by the user to the bot."""
    ud.add_handler(MessageHandler(Filters.text, cmd.single_search)) #for the text 
    ud.add_handler(MessageHandler(Filters.command, gc.unknown_command)) #wrong comment
    
    
    updater.start_polling()  #Starts the bot
    updater.idle()  #Keeps the bot running


if __name__ == "__main__":
    main()