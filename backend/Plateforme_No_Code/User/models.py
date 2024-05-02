import bcrypt
from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)
    password =  models.CharField(max_length=100)
    date_creation = models.DateField()
    date_update = models.DateField()
    def save(self, *args, **kwargs):
        # Hasher le mot de passe en utilisant bcrypt
        if self.password:
            self.password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode()
        super().save(*args, **kwargs)