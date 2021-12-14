
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

chatbot = ChatBot(
    'ibrahim',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        
    ],
    database_uri='sqlite:///database.sqlite3'
)


trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train("chatterbot.corpus.english")

trainer.train("data/icorpus/bengali/")
trainer.train("data/icorpus/manual/")

@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(chatbot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()

print("\nHello I am Chatter\n")
while True:
    try:
        bot_input = input()

        if bot_input.strip()=='Stop':
            print('Chatter: Bye')
            break

        bot_response = chatbot.get_response(bot_input)
        print(bot_response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break