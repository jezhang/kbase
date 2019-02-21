Link in django admin to foreign key object
==========================================

### Description

I have a model A with a ForeignKey to a model B. In Django admin, how can I add a link in the admin page of model A next to the ForeignKey field which open the admin page of the model B ?

### Solution

You can do the following:

models.py (example):

```py
model B(models.Model):
    name = models.CharField(max_length=20)

model A(models.Model):
    field1 = models.CharField(max_length=20)
    Bkey = models.ForeignKey(B)
```

admin.py

```py
from django.core import urlresolvers

class AAdmin(admin.ModelAdmin):
    list_display = ["field1","link_to_B"]
    def link_to_B(self, obj):
        link=urlresolvers.reverse("admin:yourapp_b_change", args=[obj.B.id]) #model name has to be lowercase
        return u'<a href="%s">%s</a>' % (link,obj.B.name)
    link_to_B.allow_tags=True
```
