def fetch_chinaforex_com(request):
	log.info('call function fetch_chinaforex_com.')
	url_chinaforex = 'http://www.chinaforex.com.cn/index.php'
	header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
	r = re.compile(r'<div class="content.*?<h4><a href="(.+?)" target="_blank">(.+?)</a></h4>.*?p class="date">(.+?)</p>.*?<p>(.+?)</p>.*?</div>',re.DOTALL)
	try:
		resp = requests.get(url_chinaforex, headers=header)
	except Exception, e:		
		log.error(e)
		return -1
	else:
		log.info('Return code : %d' %resp.status_code)
		if resp.encoding.lower() == 'gbk' or resp.encoding.lower() == 'gb2312':
			utf8_content = resp.content.decode('gbk').encode('utf-8')
		if resp.encoding.lower() == 'iso-8859-1':
			utf8_content = resp.content.decode('iso-8859-1').encode('utf-8')
		lines = r.findall(utf8_content)
		for line in lines:
			print line[0]
			anews = News()
			# anews.author = u'中国外汇网'
			anews.article_url = line[0]
			anews.title = line[1]
			anews.summary = line[3]
			anews.category = 'info'
			anews.article_from = '1'
			anews.status = '0'
			if not anews.is_duplicated():
				anews.save()
	news_list = News.objects.filter(category='info',status='0',article_from='1')
	for anews in news_list:
		print 'ready to fetch content for %s' %anews.title
		try:
			resp = requests.get(anews.article_url, headers=header)
		except Exception, e:
			log.error(e)
		else:
			if resp.encoding.lower() == 'gbk' or resp.encoding.lower() == 'gb2312':
				html = resp.content.decode('gbk').encode('utf-8')
				vs = ''
				if html.find('<div class="img">') >= 0: # 发现头图
					r = re.compile(r'<div class="img">.*?img src="(.+?)".*?</div>.*?<div class="gap"></div>',re.DOTALL)
					imgs = r.findall(html)
					if len(imgs) > 0:
						anews.article_pic = imgs[0]
						vs = '<img src="%s" alt="%s" />' % (anews.article_pic,anews.title)
				html_article_body = ''
				html_part_arr = html.split('<div class="info">')
				if len(html_part_arr) == 3:
					html_info = html_part_arr[1]
					html_part_arr = html_info.split('<div class="gap"></div>')
					if len(html_part_arr) > 1:
						html_article_body = html_part_arr[1]
				anews.content = '%s\n%s' %(vs, html_article_body)
				anews.status = '1'
				anews.save()
	return HttpResponse('Successfully fetched (%d) news from chinaforex.com' %len(news_list))