import requests 
import json
import calendar
def getMonth(date):
	x=int(date[5])*10+int(date[6])
	print("MOnth is :"+ str(x))
	print(calendar.month_name[x])
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
	print(date)
	month=getMonth(date)
	print(month)
	print(rates)
else:
	print("Can't Reach the Destination ...")
	pass
