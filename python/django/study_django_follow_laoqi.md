跟老齐学Django
==============

### 知识点梳理

#### 使用时区时间

```python
from django.utils import timezone
# ...
publish = models.DateTimeField(default=timezone.now)
```

> 注：使用timezone需要安装模块pytz，用它来提供时区数值

```sh
pip install pytz
```

#### raw_id_fields 的用法

默认情况下，多对多字段在管理界面中是以多选列表框的形式出现的，这样编辑起来不是很方便，用filter_horizontal则可大大提高易用性，特 别是在记录数大于10的情况下。

至于外键字段，默认是用下拉框来编辑的，这在外键数据量很大的时候会造成响应速度很慢，解决办法就是用raw_id_fields直接输入rawid，点击字段边上的放大镜可以查找相应的外键记录。 

[参考例子]<https://ask.helplib.com/django/post_5056003>


### 用户登录

#### URL配置
```python
# global urls.py
urlpatterns = [
	...,
	url(r'^account/', include('account.urls', namespace='account', app_name='account')),
]

# account/urls.py
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
	url(r'^login/$', views.user_login, name='user_login'),
]


```

#### 表单类
```python
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
```

#### 登录的视图函数
```python
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
	if request.method == 'POST':
	login_form = LoginForm(request.POST)
	if login_form.is_valid():
		cd = login_form.cleaned_data
		user = authenticate(username=cd['username'], password=cd['password'])

		if user:
			login(request, user)
			return HttpResponse("Welcome You. You have been authenticated successfully")
		else:
			return HttpResponse("Sorry, Your username or password is not right.")
	else:
		return HttpResponse("Invalid login")
	if request.method == "GET":
		login_form = LoginForm()
		return render(request, "account/login.html", {"form": login_form})

```

#### 前端界面
```html
{% extends 'base.html' %}
{% block title %}Login{% endblock %}
{% block content %}
<div class="row text-center vertical-middle-sm">
	<h1>Login</h1>
	<p>Input your username and password</p>
	<form class="form-horizontal" action="." method="post">
		{% csrf_token %}
		{{ form.as_p }}
		<input type="submit" value="Login">
	</form>
</div>
{% endblock %}
```

#### 用户注册扩展知识

第三方注册的库 **django-registration**

<http://django-registration.readthedocs.io/en/2.0.4/install.html)

**Django Social Auth** 是一个专门用于社交媒体账户登录django项目第三方应用

<https://github.com/omab/django-social-auth

用django-social-auth做中国社交网站三方登录，
<http://blog.csdn.net/asd131531/article/details/42457389?locationNum=10&fps=1>

### 文章管理

#### 文章发布slug名称

```python
class ArticlePost(models.Model):
	author = models.ForeignKey(User, related_name="article")
	title  = models.CharField(max_length=200)
	slug   = models.SlugField(max_length=500)

	class Meta:
		ordering = ('title',)
		index_together = (('id', 'slug'),) # 组合索引

	def __str__(self):
		return self.title

	def save(self, *args, **kargs):
		self.slug = slugify(self.title)
		super(ArticlePost, self).save(*args, **kargs)

	def get_absolute_url(self):
		return reverse("article:article_detail", args=[self.id, self.slug])

>>> from django.utils.text import slugify
>>> slugify("Learn Python in itdiffer.com")
>>> 'learn-python-in-itdiffercom'
```

如果是中文标题，需要安装一个第三方库

```python
$ pip install awesome-slugify
>>> from slugify import slugify
>>> slugify("跟老齐学")
'Gen-Lao-Qi-Xue'
>>> slugify("Learn Python in itdiffer.com")
'Learn-Python-in-itdiffer-com'
```

#### 最热文章

通过redis提供的相关函数来实现

- zincrby(name, value, amount)根据amount所设定的步长值增加有序集合(name)中的value的数值。本例中实现了article_ranking中的article.id以步长1自增，即文章被访问一次，article_ranking就将该文章id的值增加1
- zrange(name, start, end, desc=False, withscores=False, score_cast_func=float)也是redis数据库连接对象的一个方法。本例中得到article_ranking中排序前10名的对象。



```python
def article_detail(request, id, slug):
	article = get_object_or_404(ArticlePost, id=id, slug=slug)
	total_views = redis_instance.incr("article:{}:views".format(article.id))
	redis_instance.zincrby('article_ranking', article.id, 1)

	article_ranking = r.zrange('article_ranking', 0, -1, desc=True)[:10]
	article_ranking_ids = (int(id) for id in article_ranking)
	most_viewed = list(ArticlePost.objects.filter(id__in=article_ranking_ids))
	most_viewed.sort(key=lambda x: article_ranking_ids.index(x.id))
	return render(request, 'article/list/article_detail.html', {'article':article,
'total_views':total_views, 'most_viewed': most_viewed})
```
