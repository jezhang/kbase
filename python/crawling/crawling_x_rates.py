def update_currency_rate_by_now(currency='CNY',amount='100'):
	print('call function update_currency_rate_by_now')
	rate_url = 'http://www.x-rates.com/table/?from=%s&amount=%s' %(currency,amount)
	print('Ready to requests.get(%s)' % rate_url)
	header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
	try:
		resp = requests.get(rate_url, headers=header)
	except Exception, e:
		InterfaceMessage.add_message('01','sya.views.update_currency_rate_by_now(%s,%s)' %(currency,amount),False,"requests.get('%s')\n%s" %(rate_url,str(e)))
		log.error(e)
		return -1
	else:
		log.info('Return code : %d' %resp.status_code)
		r = re.compile(r"<tr>.*?rtRates.*?rtRates.*?href=.*?from=(.*?)&.+?to=CNY'>(.*?)</a></td>",re.DOTALL)
		lines = r.findall(resp.content)
		rates = dict()
		getcontext().prec = 5
		new_rates = CurrencyRate()
		new_rates.datetime_created = datetime.datetime.now()
		for line in lines:
			rates[line[0]] = line[1]
			if 'USD' == line[0]:
				new_rates.USD = str(Decimal(line[1]) * 100)
			if 'EUR' == line[0]:
				new_rates.EUR = str(Decimal(line[1]) * 100)
			if 'GBP' == line[0]:
				new_rates.GBP = str(Decimal(line[1]) * 100)
			if 'INR' == line[0]:
				new_rates.INR = str(Decimal(line[1]) * 100)
			if 'AUD' == line[0]:
				new_rates.AUD = str(Decimal(line[1]) * 100)
			if 'CAD' == line[0]:
				new_rates.CAD = str(Decimal(line[1]) * 100)
			if 'SGD' == line[0]:
				new_rates.SGD = str(Decimal(line[1]) * 100)
			if 'CHF' == line[0]:
				new_rates.CHF = str(Decimal(line[1]) * 100)
			if 'MYR' == line[0]:
				new_rates.MYR = str(Decimal(line[1]) * 100)
			if 'JPY' == line[0]:
				new_rates.JPY = str(Decimal(line[1]) * 100)
			if 'ARS' == line[0]:
				new_rates.ARS = str(Decimal(line[1]) * 100)
			if 'BHD' == line[0]:
				new_rates.BHD = str(Decimal(line[1]) * 100)
			if 'BWP' == line[0]:
				new_rates.BWP = str(Decimal(line[1]) * 100)
			if 'BRL' == line[0]:
				new_rates.BRL = str(Decimal(line[1]) * 100)
			if 'BND' == line[0]:
				new_rates.BND = str(Decimal(line[1]) * 100)
			if 'BGN' == line[0]:
				new_rates.BGN = str(Decimal(line[1]) * 100)
			if 'CLP' == line[0]:
				new_rates.CLP = str(Decimal(line[1]) * 100)
			if 'COP' == line[0]:
				new_rates.COP = str(Decimal(line[1]) * 100)
			if 'HRK' == line[0]:
				new_rates.HRK = str(Decimal(line[1]) * 100)
			if 'CZK' == line[0]:
				new_rates.CZK = str(Decimal(line[1]) * 100)
			if 'DKK' == line[0]:
				new_rates.DKK = str(Decimal(line[1]) * 100)
			if 'HKD' == line[0]:
				new_rates.HKD = str(Decimal(line[1]) * 100)
			if 'HUF' == line[0]:
				new_rates.HUF = str(Decimal(line[1]) * 100)
			if 'ISK' == line[0]:
				new_rates.ISK = str(Decimal(line[1]) * 100)
			if 'IDR' == line[0]:
				new_rates.IDR = str(Decimal(line[1]) * 100)
			if 'IRR' == line[0]:
				new_rates.IRR = str(Decimal(line[1]) * 100)
			if 'ILS' == line[0]:
				new_rates.ILS = str(Decimal(line[1]) * 100)
			if 'KZT' == line[0]:
				new_rates.KZT = str(Decimal(line[1]) * 100)
			if 'KRW' == line[0]:
				new_rates.KRW = str(Decimal(line[1]) * 100)
			if 'KWD' == line[0]:
				new_rates.KWD = str(Decimal(line[1]) * 100)
			if 'LYD' == line[0]:
				new_rates.LYD = str(Decimal(line[1]) * 100)
			if 'MUR' == line[0]:
				new_rates.MUR = str(Decimal(line[1]) * 100)
			if 'MXN' == line[0]:
				new_rates.MXN = str(Decimal(line[1]) * 100)
			if 'NPR' == line[0]:
				new_rates.NPR = str(Decimal(line[1]) * 100)
			if 'NZD' == line[0]:
				new_rates.NZD = str(Decimal(line[1]) * 100)
			if 'NOK' == line[0]:
				new_rates.NOK = str(Decimal(line[1]) * 100)
			if 'OMR' == line[0]:
				new_rates.OMR = str(Decimal(line[1]) * 100)
			if 'PKR' == line[0]:
				new_rates.PKR = str(Decimal(line[1]) * 100)
			if 'PHP' == line[0]:
				new_rates.PHP = str(Decimal(line[1]) * 100)
			if 'PLN' == line[0]:
				new_rates.PLN = str(Decimal(line[1]) * 100)
			if 'QAR' == line[0]:
				new_rates.QAR = str(Decimal(line[1]) * 100)
			if 'RON' == line[0]:
				new_rates.RON = str(Decimal(line[1]) * 100)
			if 'RUB' == line[0]:
				new_rates.RUB = str(Decimal(line[1]) * 100)
			if 'SAR' == line[0]:
				new_rates.SAR = str(Decimal(line[1]) * 100)
			if 'SGD' == line[0]:
				new_rates.SGD = str(Decimal(line[1]) * 100)
			if 'ZAR' == line[0]:
				new_rates.ZAR = str(Decimal(line[1]) * 100)
			if 'LKR' == line[0]:
				new_rates.LKR = str(Decimal(line[1]) * 100)
			if 'SEK' == line[0]:
				new_rates.SEK = str(Decimal(line[1]) * 100)
			if 'TWD' == line[0]:
				new_rates.TWD = str(Decimal(line[1]) * 100)
			if 'THB' == line[0]:
				new_rates.THB = str(Decimal(line[1]) * 100)
			if 'TTD' == line[0]:
				new_rates.TTD = str(Decimal(line[1]) * 100)
			if 'TRY' == line[0]:
				new_rates.TRY = str(Decimal(line[1]) * 100)
			if 'AED' == line[0]:
				new_rates.AED = str(Decimal(line[1]) * 100)
			if 'VEF' == line[0]:
				new_rates.VEF = str(Decimal(line[1]) * 100)
			if 'LVL' == line[0]:
				new_rates.LVL = str(Decimal(line[1]) * 100)
			if 'LTL' == line[0]:
				new_rates.LTL = str(Decimal(line[1]) * 100)
		new_rates.save()
		mc.delete("rates_today")
		mc.set("rates_today",new_rates)
		return new_rates