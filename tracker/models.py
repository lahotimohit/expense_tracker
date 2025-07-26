from django.db import models
import uuid


class BaseModel(models.Model):
    uuid=models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)

class Transaction(BaseModel):
    description=models.CharField(max_length=100)
    amount=models.FloatField()

    class Meta:
        ordering = ("description",)

    def is_negative(self):
        return self.amount < 0