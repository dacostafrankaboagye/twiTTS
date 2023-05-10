
from app import app
from flask import render_template, request, redirect, redirect, url_for,  send_file
from app.tts import syn
import io
import time


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/call_twiTTS", methods=["POST"])
def call_twiTTS():
    #global theUserInput

    text = request.form["text"]
    #print("This is the received text---", text)
    #print("synthesizing")
    #theUserInput = text

    # put the text in a file
    #print("inserting into file...")
    #with open("C:\\Users\\USER\\PycharmProjects\\capstoneProject\\TwiTTS\\app\\static\\userText.txt", 'w') as f:
    #    f.write( theUserInput)
    #print("inserted into file")

    # call the SCRIPT
    #print("running js...")
    #dummy_call()

    #print("...js executed")
    

    outputs = syn.tts(text)
    syn.save_wav(outputs, "/static/theAudio.wav")
    return render_template('forAudio.html')




    #outputs = syn.tts(text)
    # out = io.BytesIO()
    # syn.save_wav(outputs,out )
    #syn.save_wav(outputs, "C:\\Users\\USER\\PycharmProjects\\capstoneProject\\TwiTTS\\app\\static\\theAudio.wav")
    # print('saved Audio')
    # return send_file(out, mimetype="audio/wav")
    # return render_template('output.html')
    #return render_template('forAudio.html')
    #return render_template(url_for("/theScrapper/test.js"))



    #--return "wait for the audio"


#
#



'''
def dummy_call():
    counter = 0
    import os
    #os.system('cmd /k "node C:\\Users\\USER\\PycharmProjects\\capstoneProject\\TestingJSPY\\theScraper\\test.js"')

    os.system("start /B start cmd.exe @cmd /k node C:\\Users\\USER\\PycharmProjects\\capstoneProject\\TwiTTS\\app\\templates\\theScraper\\test.js")


    #os.system("start /wait cmd /c {node C:\\Users\\USER\\PycharmProjects\\capstoneProject\\TestingJSPY\\theScraper\\test.js}")

    while counter < 5:
        counter = counter + 1
        print(counter)

    print("...dummy executed")

    return "wait for audio"

'''

# @app.route("/call_js", methods=["POST"])
# def call_js():
#     # put the text in userText.txt
#
#
#     dummy_call()
#     return "wait for your audio"

'''
@app.route("/getAudio")
def getAudio():
    userTwiText = ""
    with open("C:\\Users\\USER\\PycharmProjects\\capstoneProject\\TwiTTS\\app\\static\\Output.txt", "r") as txt_file:
        userTwiText = txt_file.read()
    outputs = syn.tts(userTwiText)
    syn.save_wav(outputs, "C:\\Users\\USER\\PycharmProjects\\capstoneProject\\TwiTTS\\app\\static\\theAudio.wav")
    return render_template('forAudio.html')
'''


'''
f = open("demofile.txt", "r")

print(f.read())

'''