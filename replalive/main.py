from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    resres = 'Your project is alive! now go <a href="https://repl.it/talk/learn/Hosting-discordpy-bots-with-replit/11008">here</a> and go to the 4th step, do the rest of it.'
    return resres
    
def run():
    app.run(host="0.0.0.0", port=8080)
    
def keep_alive():
    server = Thread(target=run)
    server.start()
