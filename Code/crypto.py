import requests 
import json
import calendar
from prettytable import PrettyTable as pt

def getMonth(date):
	x=int(date[5])*10+int(date[6])
	today=calendar.month_name[x]+" "+date[8]+date[9]+","+date[0]+date[1]+date[2]+date[3]
	return today

def getExchangeRates():
	try:
		#My API Key fixer.io to get updated exchange rates
		url="http://data.fixer.io/api/latest?access_key=c47aa2253f59a0e4c58b1202ba6ff451"
		request=requests.get(url)
		data=request.json()
		if data!=False:
			date=data['date']
			rates=data['rates']
			today=getMonth(date)
			#since the price of Cryptocurrencies is initially given in Dollors
			inr=rates['INR']
			usd=rates['USD']
			#all exchange rates are given in relation to Euro
			factor=inr/usd
			factor=float("{0:.4f}".format(factor))
			print("Dated : "+today)
			print("Exchange Rate today is : 1 USD = "+str(factor)+" INR")
	except:
		print("Can't Reach the Destination ...")

def ChooseTimeForChecking():
	print("Choose Suitable option: \n1. Check Previous 1 hour\n2. Check Previous 24 hours\n3. Check Previous 7 days\n")
	time=int(input())


def getCoinMarketCapAll():
	#globalURL = "https://api.coinmarketcap.com/v1/global/"
	tickerURL = "https://api.coinmarketcap.com/v1/ticker/"
	#Pretty Table to format Output
	table = pt()
	table.field_names = ["Name (Symbols)", "Price (in USD)", "Percentage Change (1hr)", "Percentage Change (24hr)","Percentage Change (7days)"]
	request = requests.get(tickerURL)
	data = request.json()
	for x in data:
		CurrencyName=x['name']+" ("+x['symbol']+")"
		#print(CurrencyName)
		price_usd=x['price_usd']
		price_usd=float("{0:.4f}".format(float(price_usd)))
		#print(price_usd)
		percent_change_1h = x['percent_change_1h'] 
		#print(percent_change_1h)
		percent_change_24h = x['percent_change_24h']
		#print(percent_change_24h)
		percent_change_7d = x['percent_change_7d']
		#print(percent_change_7d)
		table.add_row([CurrencyName,price_usd,percent_change_1h,percent_change_24h,percent_change_7d])
	return table

def getCoinCapSingle():
	table=pt()
	table.field_names = ["Name (Symbols)", "Price (in USD)", "Change (1hr)", "Change (24hr)","Change (7days)"]
	tickerURL = "https://api.coinmarketcap.com/v1/ticker/"
	choice=input("Enter Name of cryptocurrency: ")
	tickerURL += '/'+choice+'/'
	request = requests.get(tickerURL)
	data = request.json()
	CurrencyName = data[0]['symbol']
	price_usd = data[0]['price_usd']
	percent_change_1h = data[0]['percent_change_1h']
	percent_change_24h = data[0]['percent_change_24h']
	percent_change_7d = data[0]['percent_change_7d']
	# print(ticker + ":\t\t$" + price+ ":\t\t$" + percent_change_1h+ ":\t\t$" + percent_change_24h++ ":\t\t$" + percent_change_7d)
	table.add_row([CurrencyName,price_usd,percent_change_1h,percent_change_24h,percent_change_7d])
	return table

def DriverMenu():
	driver="yes"
	while(driver=="yes"):
		print("Choose Suitable Option : \n1. Get Status of Single Cryptocurrency\n2. Fetch top 100 Cryptocurrencies\n3. Find Best Investment")
		choice=int(input())
		if choice==1:
			table=getCoinCapSingle()
			print(table)
		elif choice==2:
			table=getCoinMarketCapAll()
			print(table)
		elif choice==3:
			ChooseTimeForChecking()
		else:
			print("Enter a Valid Input ...")
		driver=input("Enter 'yes' to continue... ")	

def main():
	getExchangeRates()
	# if data!=False:
	# 	date=data['date']
	# 	rates=data['rates']
	# 	today=getMonth(date)
	# 	#since the price of Cryptocurrencies is initially given in Dollors
	# 	inr=rates['INR']
	# 	usd=rates['USD']
	# 	#all exchange rates are given in relation to Euro
	# 	factor=inr/usd
	# 	factor=float("{0:.4f}".format(factor))
	# 	print("Dated : "+today)
	# 	print("Exchange Rate today is : 1 USD = "+str(factor)+" INR")
	# 	coinCap = getCoinMarketCap()
	#	bestInvestment = getBestInvestment(coinCap)
	DriverMenu()

if __name__ == '__main__':
	main()
