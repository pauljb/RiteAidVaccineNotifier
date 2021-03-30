import requests,json,time,winsound,datetime

while True:
  #add a list of store numbers near your zip code as 
	stores=["###","####","####"]
  # number of times to beep if availability is found
	numBeeps=100
	enableOutput=True

	for store in stores:
		if enableOutput==True:
			ct = datetime.datetime.now()
			print(ct, "Checking store",store,". . . ",end='')
		url = "https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber="+store
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'Content-Type':'application/json'}
		result = requests.get(url, headers=headers)
		output = json.loads(result.content.decode())

		if output ['Status'] == 'SUCCESS':
			if output ['Data']['slots']['1'] == False:
				if enableOutput==True:
					print("No slots")
				time.sleep(3)
				continue
			else:
				print(store,' Has Shots!!!')
				for x in range(0, numBeeps):
					winsound.Beep(650, 250)
				continue
		else:
			if enableOutput==True:
				print("Error in response")
			continue
