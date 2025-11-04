from django.db import models

from core.models import BaseModel

class Upload(BaseModel):
  uploaded_at = models.DateTimeField(auto_now_add=True)
  file = models.FileField()
