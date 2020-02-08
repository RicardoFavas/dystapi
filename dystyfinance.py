import yfinance as yf
import json

def get_dividends(ticker,start_date,end_date):
	yfticker = yf.Ticker(ticker)
	pd = yfticker.dividends.loc[start_date:end_date]
	return pd

def get_close_price(ticker,start_date,end_date):
	yfticker = yf.Ticker(ticker)
	pd = yfticker.history(interval='1d', start=start_date,end = end_date).Close
	return pd

def get_recomendations(ticker,start_date,end_date):
	recmap = {
		'Buy':1, 
		'Strong Buy':1.5,
		'Sell':-1,
		'Strong Sell':-1.5,
		'Positive':1,
		'Negative':-1
	}
	yfticker = yf.Ticker(ticker)
	pd = yfticker \
		.recommendations['To Grade'] \
		.loc[start_date:end_date] \
		.apply(lambda v: recmap.get(v,0))
	pd = pd.loc[~pd.index.duplicated(keep='first')]
	return pd

print('running')