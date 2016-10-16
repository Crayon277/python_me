from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField()

    def __unicode__(self):
        infomsg = self.name + ' ' +self.website
        return infomsg

    class Meta:
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField(blank = True, verbose_name = 'cy_e_mail')
    def __unicode__(self):
        return u'%s %s' %(self.first_name,self.last_name)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)
    #publisher = models.ForeighKey(Publisher)
    publication_date = models.DateField(blank = True)
    publisher = models.ForeignKey(Publisher)
    def __unicode__(self):
        return self.title
'''
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60) 
    state_province = models.CharField(max_length=30) 
    country = models.CharField(max_length=50) 
    website = models.URLField()

class Author(models.Model):
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=40)     
    email = models.EmailField()
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author) 
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
# Create your models here.
'''