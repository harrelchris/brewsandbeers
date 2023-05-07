from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
