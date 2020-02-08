#!flask/bin/python
from flask import Flask
import dystyfinance as dystf
from flask import request


app = Flask(__name__)
@app.route('/')
def index():
    return "Working!!"

@app.route('/get_dividends/<string:ticker>',methods=['GET'])
def get_dividends(ticker):
	start_date = request.args.get('start-date')
	end_date = request.args.get('end-date')
	return dystf \
		.get_dividends(ticker,start_date,end_date) \
		.to_json(date_format="iso")

@app.route('/get_close_price/<string:ticker>',methods=['GET'])
def get_close_price(ticker):
	start_date = request.args.get('start-date')
	end_date = request.args.get('end-date')
	return dystf \
		.get_close_price(ticker,start_date,end_date) \
		.to_json(date_format="iso")

@app.route('/get_recomendations/<string:ticker>',methods=['GET'])
def get_recomendations(ticker):
	start_date = request.args.get('start-date')
	end_date = request.args.get('end-date')
	return dystf \
		.get_recomendations(ticker,start_date,end_date) \
		.to_json(date_format="iso")

if __name__ == '__main__':
    app.run(debug=True)
