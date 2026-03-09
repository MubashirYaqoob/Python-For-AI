# --  Ai Chat Bot Frame 
class ChatBot :
    def __init__(self,name,response_rules):
        self.name = name 
        self.response_rules = response_rules
        conversion_history = []
        sentiment_tracker = {"Positive" : 0,"Negative" : 0}

    def respond(self,user_input) :
        user_input= user_input.lower()

        for i ,response in self.response_rules.items() : # - why items reason item return pair key with value 
            if i in user_input :
                bot_replay = response
                break
            else :
                bot_replay = "Sorry I don't Understand "
        self.conversation_history.append("user",user_input)
        self.conversation_histoyr.append(self.name,bot_replay)
        return bot_replay


