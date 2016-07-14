

def eslpod_update():
	header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
	url_dict = {}
	url_dict['cafe'] = 'https://www.eslpod.com/website/show_all.php?cat_id=-39570&low_rec=0'
	url_dict['life'] = 'https://www.eslpod.com/website/show_all.php?cat_id=10145&low_rec=0'
	url_dict['biz'] = 'https://www.eslpod.com/website/show_all.php?cat_id=-49513&low_rec=0'

	fail = ''
	index = 0

	for k,v in url_dict.items():
		try:
			resp = requests.get(v, headers=header)
		except Exception, e:
			fail = '%s%s' %(fail,k)
			log.error(e)
		else:
			pattern = r'<td align="left" valign="top"><span class="date-header">(.+?)</span>.+?class="podcast_title">(.+?)</a></strong>.*?<span class="pod_body ">.+?<img src="images/guide.gif".+?<a href="(.+?)" target="_blank">.+?Podcast</a>.+?</span>.*?<!-- SHOW PODCAST BLURB -->(.+?)<br>'
			# r = re.compile(r'<span class="pod_body ">.+?<img src="images/guide.gif".+?<a href="(.+?)" target="_blank">.+?Podcast</a>.+?</span>',re.DOTALL)
			r = re.compile(pattern,re.DOTALL)
			lines = r.findall(resp.content)
			# podcasts = []

			for line in lines:
				podcast = Podcast()
				podcast.timestamp = line[0].strip()
				podcast.name = line[1].strip()
				podcast.url = line[2].strip()
				podcast.intro = line[3].strip()
				podcast.category = k
				cast = Podcast.get_cast_by_name(podcast.name)
				if cast is None:
					podcast.save()
					index += 1
				# podcasts.append(podcast)
				# urls.append('<a href="%s" target="_blank">%s</a>' %(line,line))
	if fail != '':
		return fail
	else:
		return 'Sucessfully updated %d records' %index