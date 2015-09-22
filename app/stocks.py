import requests
from app import app
from flask import request

@app.route('/stock', methods=['GET', 'POST'])
def get_stock():
    print request.args
    ticker = request.args.get('text')
    channel = request.args.get('channel_name')
    r = requests.get("http://finance.yahoo.com/d/quotes.csv?s="+ticker+"&f=csl1d1t1c1ohgv&e=.csv")
    stock_info = r.content.split(",")
    ret_string = "\nSymbol: " + stock_info[1][1:-1]
    ret_string += "\nCurrent price: " + stock_info[2]
    ret_string += "\nPrice retrieved at: " + stock_info[4][1:-1]
    ret_string += "\nToday's open: " + stock_info[6]
    ret_string += "\nToday's high: " + stock_info[7]
    ret_string += "\nToday's low: " + stock_info[8]
    ret_string += "\nVolume: " + stock_info[9]
    ret_string += "\nhttp://chart.finance.yahoo.com/z?s="+stock_info[1][1:-1]+"&t=1d&q=l&l=on&z=s&p=m50,m200"
    r = requests.post('https://algorerhythms.slack.com/services/hooks/slackbot?token=cORCNdAEH7fhNaWndKUDu9Mw&channel=%23'+channel, ret_string)
    return ''
