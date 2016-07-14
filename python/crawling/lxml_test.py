# encoding: utf-8
'''
Created on 2016年7月13日
'''

import urllib2, urlparse
from lxml import etree


# Set Max Craw Page Here
max_craw_page = 10
# Set Max Craw Page Here

root_url = 'http://www.bttiantang.com/'
urls = set()
urls_old = set()
urls.add(root_url)
count = 0
movielist = []


def craw(url):
    '''craw function'''
    global count, movielist
    count += 1
    print '%d: crawing: %s' % (count, url)
    try:
        response = urllib2.urlopen(url)
        content = response.read()
        
        tree = etree.HTML(content)
        links = tree.xpath("//a[contains(@href, '/?PageNo=')]")
        for link in links:
            ulink = urlparse.urljoin(root_url, link.attrib['href'])
            if ulink not in urls_old:
                urls.add(ulink)
    
        titles = tree.xpath("//div[@class='title']")
        for r in titles:
            title_node = r.xpath('.//p/a')[0]
            score_node = r.xpath('.//p[@class="rt"]/descendant::text()')
            oldlink = title_node.attrib['href']
            newlink = urlparse.urljoin(url, title_node.attrib['href'])
            title = etree.tostring(title_node, encoding='utf-8', method='html')
            title = title.replace(str(oldlink), str(newlink))
            score = ''.join(score_node)
            movielist.append({'title':title,'score':score})

    except:
        print 'craw failed!'
    
def get_urls():
    '''get urls function'''
    if len(urls) != 0:
        url = urls.pop()
    urls_old.add(url)
    return url

if __name__ == "__main__":
    while len(urls) != 0:
        craw(get_urls())
        if count > max_craw_page:
            break
    strScript = '''
    <script type="text/javascript">
    $(function(){
        $("#filtername").keyup(function(){
            var filtername = $(this).val();
            if( filtername != ""){
            $('table tbody tr').hide().filter(":contains('"+filtername+"')").show();
            }else{
            $('table tbody tr').show();
            }
        })
    })
    </script>
    '''
    with open('movielist.html', 'w') as f:
        f.write('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>Movie List</title>')
        f.write('<script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>')
        f.write(strScript)
        f.write('<style>table{border:solid #0069c0; border-width:1px 0px 0px 1px;}th,td{border:solid #0069c0;border-width:0px 1px 1px 0px;}</style></head><body><table>')
        f.write('<span>Filter:&nbsp;&nbsp;</span><input type="text" id="filtername"/>')
        f.write('<tr><th>ID</th><th>TITLE</th><th>SCORE</th></tr>')
        id = 0
        for movie in movielist:
            id += 1
            f.write('<tr><td>%d</td><td>%s</td><td>%s</td></tr>' % (id, movie['title'], movie['score'].encode('utf-8')))
        f.write('</table></body></html>')
        print "It's done!"
        raw_input('Please open movelist.html to check the results!')
    

