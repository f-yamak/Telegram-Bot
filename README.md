# Telegram-Bot

### GOAL
This bot show series detail.  
Name / Date / IMDB / Language / Summary / Creator / Cast / Episodes

### HOW TO USE
You can use it by searching **@tsdif_bot** on telegram
 
### INSTALLATION
```bash
$pip install python-telegram-bot==12.0.0b1 --upgrade
```

### HOW TO CREATE YOUR BOT
> Create your bot on Telegram
> * Search for **'BotFather'**.
> * Open 'BotFather' and type **/newbot**.
> * Give a unique name to your bot.
> * Decide the username ending with **'bot'**. For example my_bot.
> * After these you will see the **TOKEN**.
> * You will use this token on code in 'main'

Copy the token paste it into the variable named TOKEN in the 'main' method.

Run the main method.

Search your new bot and try.
 
### HOW CODE WORKS
Receives incoming messages from the sent, if it is correct it gives the details of the series, otherwise it gives a warning.

There are 2 functional command /start and /help.

- /start explain breifly the aim of bot.
 
 - /help tells to user what it does and how to use it.
