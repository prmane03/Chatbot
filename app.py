
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
from flask import Flask,render_template,request,url_for,jsonify
#import pickle

my_bot = ChatBot(name='chitty',read_only=True,logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                 'chatterbot.logic.BestMatch'])
                                            
training_data = open('training_data/data.txt').read().splitlines()
list_trainer = ListTrainer(my_bot)

list_trainer.train(training_data)
trainer_corpus = ChatterBotCorpusTrainer(my_bot)
#for i in range(9):
#	ip=input("You : ")
#	print("[•_•] :"+str(my_bot.get_response(ip)))

trainer_corpus.train('chatterbot.corpus.english')
trainer_corpus.train('chatterbot.corpus.marathi')

#list_trainer.export_for_training('./data.yml')

#f = open("bot.pkl","wb")
#pickle.dump(my_bot,f)
#f.close()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
 
 
@app.route("/bot")
def bot():
    return render_template("bot.html")
    

@app.route("/respond")
def respond():
	msg = request.args.get('msg')
	return jsonify(result=str(my_bot.get_response(msg)))
	
if __name__=="__main__":
	app.run(debug=True)