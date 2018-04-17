#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import tkinter as tk
import requests as req
from pprint import pprint

subscription_key = os.environ.get("subscription_key")

root = tk.Tk()
analizedText=tk.StringVar()
analizedText.set("")

field1=tk.Label(text='Input text:')
field2=tk.Label(text='Analized text:')
inText=tk.Text()
outText=tk.Text()

def textAnalitics():
    global analizedText
    global inText
    textdata=inText.get("1.0",tk.END)

    headers={
        "Ocp-Apim-Subscription-Key": subscription_key
    }
    documents = { 'documents': [
        { 'id': '1', 'text': textdata,'language': 'ja'}
    ]}
    response = req.post("https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases",headers=headers,json=documents);
    response = response.json()
    
    outText.delete("1.0",tk.END)
    outText.insert("1.0",response);

root.title("MS Text Analitics")
root.geometry("640x800")

submit=tk.Button(root,text="submit",command=textAnalitics)

field1.grid()
inText.grid()
submit.grid()
field2.grid()
outText.grid()

root.mainloop();

