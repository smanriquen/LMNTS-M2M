from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import Http404
from M2M.models import machine
from M2M.models import characteristics
from M2M.serializers import MachineSerializer
from M2M.serializers import CharacteristicsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MachineList(APIView):
	def get(self, request, format=None):
		machines = machine.objects.all()
		serializedMachines = MachineSerializer(machines, many = True)
		return Response(serializedMachines.data)

	def post(self, request, format=None):
		serializedMachines=MachineSerializer(data=request.data)
		if serializedMachines.is_valid():
			serializedMachines.save()
			return Response(serializedMachines.data, status = status.HTTP_201_CREATED)
		return Response(serializedMachines.errors, status = status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format = None):
		serial = request.data.get('serial')
		machineToDelete = machine.objects.get(serial=serial)
		machineToDelete.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class MachineDetails(APIView):

	def get_object(self, family, machineType, serial):

		try:
			foundMachine = machine.objects.all()
			if family:
				foundMachine = foundMachine.filter(family__iexact=family)
			if machineType:
				foundMachine = foundMachine.filter(machineType__iexact=machineType)
			if serial:
				foundMachine = foundMachine.filter(serial__exact=serial)
			return foundMachine
		except machine.DoesNotExist:
			raise Http404

	def get(self, request, family, machineType, serial, field, value, format = None):
		machine = self.get_object(family, machineType, serial)
		
		if field:
			machine = machine[:1].get()
			serializedMachine = MachineSerializer(machine)
			if not serializedMachine.data.get(field):
				return CharacteristicsDetails.as_view()(request,machine,field,value)
			else:
				return Response(serializedMachine.data.get(field))
		else:
			machines = MachineSerializer(machine, many=True)
			return Response(machines.data)

	def post(self, request, family, machineType, serial, field, value, format=None):
		machine = self.get_object(family, machineType, serial)
		machine = machine[:1].get()
		return CharacteristicsDetails.as_view()(request,machine,field,value) 	

	def put(self, request, family, machineType, serial, field, value, format=None):
		machine = self.get_object(family, machineType, serial)
		machine = machine[:1].get()
		if not field:
			serializedMachine = MachineSerializer(machine, data=request.data)
			if serializedMachine.is_valid():
				serializedMachine.save()
				return Response(serializedMachine.data)
			return Response(serializedMachine.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			return CharacteristicsDetails.as_view()(request,machine,field,value)
		

	def delete(self, request, family, machineType, serial, field, value, format=None):
		machine = self.get_object(family, machineType, serial)
		if not field:
			machine.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			machine = machine[:1].get()
			return CharacteristicsDetails.as_view()(request,machine,field,value)

class CharacteristicsDetails(APIView):

	def get(self, request, machine, field, value, format = None):
		 
		if field.lower()=='characteristics':
			characteristics = machine.characteristics.all()
			serializedCharacteristics = CharacteristicsSerializer(characteristics, many=True)
			return Response(serializedCharacteristics.data)
		else:	 
			characteristics = machine.characteristics.get(characteristicType__iexact=field)
			serializedCharacteristics = CharacteristicsSerializer(characteristics)
			if value:
				return Response(serializedCharacteristics.data.get(value))
			else:
				return Response(serializedCharacteristics.data)

	def post(self, request, machine, field, value, format=None):
		request.data['parent'] = machine.serial
		serializedCharacteristics=CharacteristicsSerializer(data=request.data)
		if serializedCharacteristics.is_valid():
			serializedCharacteristics.save()
			return Response(serializedCharacteristics.data, status = status.HTTP_201_CREATED)
		return Response(serializedCharacteristics.errors, status = status.HTTP_400_BAD_REQUEST)
		
	def put(self, request, machine, field, value, format=None):
		characteristics = machine.characteristics.get(characteristicType__iexact=field)
		if not value:		
			serializedCharacteristics = CharacteristicsSerializer(characteristics, data=request.data)
			if serializedCharacteristics.is_valid():
				serializedCharacteristics.save()		
		else:
			characteristics.value = request.data.get(value)
			characteristics.save()
			serializedCharacteristics = CharacteristicsSerializer(characteristics)
		return Response(serializedCharacteristics.data)
		return Response(serializedCharacteristics.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, machine, field, value, format=None):
		if field.lower()=='characteristics':
			characteristics = machine.characteristics.all()
		else:
			characteristics = machine.characteristics.get(characteristicType__iexact=field)
		characteristics.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	

# class CharacteristicsList(APIView):
# 	def get(self, request, format=None):
# 		characteristics = characteristics.objects.all()
# 		serializedCharacteristics = CharacteristicsSerializer(characteristics, many = True)
# 		return Response(serializedCharacteristics.data)

# 	def post(self, request, format=None):
# 		serializedCharacteristics=CharacteristicsSerializer(data=request.data)
# 		if serializedCharacteristics.is_valid():
# 			serializedCharacteristics.save()
# 			return Response(serializedCharacteristics.data, status = status.HTTP_201_CREATED)
# 		return Response(serializedCharacteristics.errors, status = status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, format = None):
# 		serial = request.data.get('serial')
# 		characteristicsToDelete = characteristics.objects.get(serial=serial)
# 		characteristicsToDelete.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)





