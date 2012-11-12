from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
import models

class TestResource(ModelResource):
    class Meta:
        queryset = models.Test.objects.all()
        authorization = Authorization()
        authentication = Authentication()