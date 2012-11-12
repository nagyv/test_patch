"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.conf import settings
settings.DEBUG = True

from tastypie.test import ResourceTestCase
import models

class MethodTest(ResourceTestCase):
    """Tests PUT, PATCH methods"""

    def test_put(self):
        res = self.api_client.put('/api/test/1/', format='json', data={'test': 'testelek'})
        self.assertHttpAccepted(res)        
        data = models.Test.objects.get(pk=1)
        self.assertEqual(data.test, 'testelek')
        self.assertEqual(data.nochange, 'we are set')

    def test_patch(self):
        res = self.api_client.patch('/api/test/1/', format='json', data={'test': 'jotest'})   
        self.assertHttpAccepted(res)
        data = models.Test.objects.get(pk=1)
        self.assertEqual(data.test, 'jotest')
        self.assertEqual(data.nochange, 'we are set')
