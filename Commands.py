from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
import requests
import re


"""
*We used TVMAZE's API in our code. 
*We created a class because if we want add another api to our code we can simply create another class so there is no confusion.
*Every function is defined according to content of the TVMAZE API.
"""
class tvmaze_data:
    def __init__(self):
        self.api_url = "https://api.tvmaze.com"


    def show_id(self,movie_name):
        data = requests.get(f"{self.api_url}/singlesearch/shows?q={movie_name}").json()
        if movie_name.lower() == data['name'].lower():
            return data['id']
        else:
            return ""
    

    def show_search(self,movie_name):
        data = requests.get(f"{self.api_url}/singlesearch/shows?q={movie_name}").json()

        if(data == None):
            quit()

        
        name = data['name']
        language = data['language']
        rating = data['rating']['average']
        premiered = data['premiered'][0:4] # start
        if data['status'] == "Ended":
            ended = data['ended'][0:4]
        else:
            ended = "now"
        
        genres = ""
        for x in data['genres']:
            genres += x + " "

        summary = data['summary']
        summary = re.sub('<[^<]+?>', '', summary)

        message = f"{name} ({premiered}-{ended})\n\nIMDB: {rating}  /  Language: {language}\n\nSummary: {summary}"
        
        return message



    def show_episode_list(self,id):
        
        data = requests.get(f"{self.api_url}/shows/{id}/episodes").json()

        if(data == None):
            quit()
        
        seasons = {x+1 : [] for x in range(data[-1]['season'])}

        for x in range(len(data)):
            message = f"S{data[x]['season']}E{data[x]['number']} - {data[x]['name']} ({data[x]['rating']['average']})"
            seasons[int(data[x]['season'])].append(message)

        result = ""
        for x in range(len(seasons)):
            result += "\n".join(seasons[x+1])
            result += "\n\n"
        
        
        return result
    

    def show_crew(self,id):
        data = requests.get(f"{self.api_url}/shows/{id}/crew").json()
        for x in range(len(data)):    
            if data[x]['type'] == 'Creator':
                return data[x]['person']['name']
        return 'None'
        


    def show_cast(self,id):
        data = requests.get(f"{self.api_url}/shows/{id}/cast").json()
        result = ""
        for x in range(len(data)):
            result += data[x]['character']['name'] + " - " + data[x]['person']['name'] + "\n"
        
        return result
        



#creating instance
tvm_data  = tvmaze_data()

def single_search(update: Update, context: CallbackContext):
    texted_message = update.message.text
    
    """We can see the sent message."""
    print(texted_message)
    id = tvm_data.show_id(texted_message)
    

    if type(id) == str:
        update.message.reply_text("Please be sure entered serie name is correct.")
    else:
        content1 = tvm_data.show_search(texted_message)
        update.message.reply_text(content1)

        content2 =""
        content2 += "Creator: " + tvm_data.show_crew(id) + "\n\n"
        content2 += tvm_data.show_cast(id)
        update.message.reply_text(content2)

        content3 = tvm_data.show_episode_list(id)



        """Telegram character limit"""
        if len(content3) > 4096:
            temp_data = requests.get(f"https://api.tvmaze.com/shows/{id}/episodes").json()
            
            temp_list = []
            for x in range(temp_data[-1]['season']):
                season_checking = "S" + str(x+1)
                temp_str = ""
                
                if(content3.find(season_checking) > 3000 ):
                    temp_str += content3[:content3.find("S"+str(x))]
                    temp_list.append(temp_str)
                    content3 = content3[content3.find("S"+str(x)):]
                    
                    if(len(content3) < 4096):
                        temp_list.append(content3)
                        break

            for x in range(len(temp_list)):
                update.message.reply_text(temp_list[x])
        else:
            update.message.reply_text(content3)
