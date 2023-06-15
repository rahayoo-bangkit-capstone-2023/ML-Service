# libraries
import random
import numpy as np
import pickle
import json
from flask import Flask, render_template, request
import requests
import time
import spacy
#from keras.models import load_model
import tensorflow
import os

# chat initialization
#model = load_model("mymodel.h5")
model = tensorflow.keras.models.load_model("mymodel.h5", compile=False)
intents = json.loads(open("intents.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

app = Flask(__name__)

# @app.route("/")
# def home():

#     return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    if msg.startswith('my name is'):
        name = msg[11:]
        ints = predict_class(msg, model)
        res1 = getResponse(ints, intents)
        res = res1.replace("{n}", name)
    elif msg.startswith('hi my name is'):
        name = msg[14:]
        ints = predict_class(msg, model)
        res1 = getResponse(ints, intents)
        res = res1.replace("{n}", name)
    else:
        ints = predict_class(msg, model)
        res = getResponse(ints, intents)
    return res

# chat functionalities
def clean_up(sentence):
    # sentence_words=nltk.word_tokenize(sentence)
    sentence = sentence.lower()
    sentence_words = nlp(sentence)
    sentence_words = [word.lemma_ for word in sentence_words]
    return sentence_words

def create_bow(sentence,words):
    sentence_words=clean_up(sentence)
    bag=list(np.zeros(len(words)))

    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence,model):
    p=create_bow(sentence,words)
    res=model.predict(np.array([p]))[0]
    threshold=0.8
    results=[[i,r] for i,r in enumerate(res) if r>threshold]
    results.sort(key=lambda x: x[1],reverse=True)
    return_list=[]

    for result in results:
        return_list.append({'intent':classes[result[0]],'prob':str(result[1])})
    return return_list

def getResponse(return_list,intents):

    if len(return_list)==0:
        tag='noanswer'
    else:
        tag=return_list[0]['intent']
    if tag=='datetime':
        print(time.strftime("%A"))
        print (time.strftime("%d %B %Y"))
        print (time.strftime("%H:%M:%S"))
        
    list_of_intents= intents['intents']
    for i in list_of_intents:
        if tag==i['tag'] :
            result= random.choice(i['responses'])
    return result


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))
