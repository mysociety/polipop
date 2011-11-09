from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.gis.db import models

from django_date_extensions.fields import ApproximateDateField
from markitup.fields import MarkupField

from popit.models import ModelBase, DataKey, Data, date_help_text

class Organisation(ModelBase):
    name    = models.CharField(max_length=200)
    slug    = models.SlugField()
    summary = MarkupField(blank=True, default='')
    started = ApproximateDateField(blank=True, help_text=date_help_text)
    ended   = ApproximateDateField(blank=True, help_text=date_help_text)

    def __unicode__(self):
        return self.name

    #@models.permalink
    #def get_absolute_url(self):
    #    return ( 'organisation', [ self.slug ] )

    class Meta:
        ordering = [ "name" ]      
        app_label = 'popit'

class OrganisationDataKey(DataKey):
    class Meta:
        app_label = 'popit'

class OrganisationData(Data):
    organisation = models.ForeignKey(Organisation, related_name='data')
    key = models.ForeignKey(OrganisationDataKey, related_name='values')
    class Meta:
        app_label = 'popit'

class OrganisationCode(models.Model):
    organisation    = models.ForeignKey(Organisation, related_name='codes')
    type            = models.CharField(max_length=100)
    code            = models.CharField(max_length=100)

    class Meta:
        app_label = 'popit'

    def __unicode__(self):
        return u'%s (%s)' % (self.code, self.type)
