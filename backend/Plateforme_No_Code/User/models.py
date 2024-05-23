import bcrypt
from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    google_id_client =models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=200,blank=True, null=True)
    password =models.CharField(max_length=200,blank=True, null=True)
    date_creation = models.DateField(auto_now=True)
    date_update = models.DateField(auto_now=True)
    """  def save(self, *args, **kwargs):
        # Hasher le mot de passe en utilisant bcrypt
        if self.password:
            self.password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode()
        super().save(*args, **kwargs) """