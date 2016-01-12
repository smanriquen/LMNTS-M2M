from django.db import models

# Create your models here.

class machine(models.Model):
	machineType = models.CharField(max_length=140)
	family = models.CharField(max_length=140)
	serial = models.CharField(max_length=100, primary_key=True)
	MAC = models.CharField(max_length=20)
	services = models.TextField(null=True, blank=True)

	

class characteristics(models.Model):
	characteristicType = models.CharField(max_length=140)
	parent = models.ForeignKey(machine, related_name='characteristics', on_delete=models.CASCADE)
	value = models.CharField(max_length=140)
	timer = models.CharField(max_length=140)
	lastRead = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return '%s: %s' % (self.characteristicType, self.value)



