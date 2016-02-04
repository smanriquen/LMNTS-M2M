from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from M2M.models import machine
from M2M.models import characteristics

class CreateMachineTests(APITestCase):

	def setUp(self):

		self.url = reverse('machines_list')
		self.data = ({'machineType': 'Humidity',
			    'family': 'Actuator',
				    #'serial': '2016-000010',
				'MAC': '00:00:00:00:00:10',
				'services': '',
				'characteristics': [{
								        'characteristicType': 'Humidity',
								        'value': '80%',
								        'timer': '10:00'
								        
								      }]})

	def test_can_create_machine(self):
		"""
		Ensure we can create a new account object.
		"""
		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(machine.objects.count(), 1)
		#self.assertEqual(machine.objects.get().serial, '2016-000010')
		self.assertIsNotNull(response.data['serial'])