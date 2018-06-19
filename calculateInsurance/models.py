from django.db import models
import uuid
# from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User
# from calculateInsurance import views

# Create your models here.
class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    make_of_vehicle = models.CharField(max_length = 50)
    type_of_risk = models.CharField(max_length = 50)
    cubic_capacity = models.PositiveIntegerField(blank=True,null=True)
    registration_number = models.CharField(max_length = 50)
    chassis = models.CharField(max_length = 50, blank = True, null=True)
    engine_number = models.CharField(max_length=50, blank = True, null=True)
    year = models.CharField(max_length = 4, blank=True, null=True)
    number_of_seats = models.IntegerField()
    license_issued_year = models.CharField(max_length=4)
    insurance_type = models.CharField(max_length=50)
    insurance_payment_due = models.IntegerField(editable=False, default=333, null=True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField(null=True)

    def __str__(self):
        return "Id: {} Make: {} Risk: {} Insurance Type: {} Insurance Payment: {}".format(self.id, self.make_of_vehicle, self.type_of_risk, self.insurance_type, self.insurance_payment_due)
