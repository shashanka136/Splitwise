from django.db import models
from django.contrib.auth.models import User
from sgroups.models import Groups

# Create your models here.

class activity(models.Model):
    def __str__(self):
        if not(self.exp) :
            return self.friend1.username+ " added " + self.friend2.username + " in " + self.group.name
        if self.expense >= 0:
            return self.friend1.username + " paid " + str(self.expense) + " to " + self.friend2.username + " in " + self.group.name
        else:
            return self.friend2.username + " paid " + str(-self.expense) + " to " + self.friend1.username + " in " + self.group.name

    friend1 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='fri1')
    friend2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='fri2')
	# friend1 gives money to friend2
    exp = models.BooleanField(default=False)
    group = models.ForeignKey(Groups,on_delete=models.CASCADE,related_name='grp')
    expense = models.FloatField(default=0.0)
