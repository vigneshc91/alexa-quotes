from flask import Flask, render_template
from flask_ask import Ask, statement, question
import logging
from quotes import Quotes
from constants import AppConstants

app = Flask(__name__)
app.config['ASK_APPLICATION_ID'] = AppConstants.ALEXA_SKILL_ID

ask = Ask(app, '/')
quoteObj = Quotes()

@app.route('/')
def index():
    return 'welcome to Qutes for the day'

@ask.launch
def launched():
    info = quoteObj.info()
    text = render_template('quote_not_found')

    if not isinstance(info, dict):
        return statement(text)
    text = info['quote']

    return statement(text).simple_card(
        title=info['author'],
        content=info['quote']
    )

@ask.intent('AMAZON.HelpIntent')
def help():
    text = render_template('help')
    return question(text)

@ask.intent('AMAZON.CancelIntent')
@ask.intent('AMAZON.StopIntent')
def stop():
    text = render_template('cancel')
    return statement(text)
    
if __name__ == '__main__':
    app.run(debug=True)
