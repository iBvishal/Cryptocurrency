import requests 
import json
import calendar
def getMonth(date):
	x=int(date[5])*10+int(date[6])
	return calendar.month_name[x]
	#return calendar.month_name(int(date[5])*10+int(date[6]))

def getExchangeRates():
	try:
		#My API Key fixer.io to get updated exchange rates
		url="http://data.fixer.io/api/latest?access_key=c47aa2253f59a0e4c58b1202ba6ff451"
		request=requests.get(url)
		data=request.json()
		return data
		# date=data['date']
		# rates=data['rates']
	except:
		return False

data=getExchangeRates()
if data!=False:
	date=data['date']
	rates=data['rates']
	today=getMonth(date)+" "+date[8]+date[9]+","+date[0]+date[1]+date[2]+date[3]
	#since the price of Cryptocurrencies is initially given in Dollors
	inr=rates['INR']
	usd=rates['USD']
	#all exchange rates are given in relation to Euro
	factor=inr/usd
	factor=float("{0:.4f}".format(factor))
	print("Dated : "+today)
	print("Exchange Rate today is : 1 USD = "+str(factor)+" INR")

else:
	print("Can't Reach the Destination ...")

