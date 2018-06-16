from django.db import models
import uuid
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

    def __str__(self):
        return "{} {}".format(self.type_of_risk, self.insurance_type)



def mainPremiumFunction():
    """Selects a particular premium function based on certain conditions"""

    theRiskType = str(Car.objects.earliest('type_of_risk'))
    theInsuranceType = str(Car.objects.earliest('insurance_type'))


    if theRiskType.lower().split()[0] == 'taxi' and theInsuranceType.lower() == 'third party':
        result = premiumForTaxiThirdParty()
    elif theRiskType.lower().split()[0] == 'x1' and theInsuranceType.lower().split()[1] == 'third party':
        result = premiumForPrivateThirdParty()
    elif theRiskType.lower().split()[0] == 'maxi bus' and theInsuranceType.lower().split()[1] == 'third party':
        result = premiumForMaxiBusThirdParty()
    elif theRiskType.lower().split()[0] == 'motor cycle' and theInsuranceType.lower().split()[1] == 'third party':
        result = premiumForMotorCycleThirdParty()
    elif theRiskType.lower().split()[0] == 'x4' and theInsuranceType.lower().split()[1] == 'comprehensive':
        result = comprehensivePremiumForX4()
    elif theRiskType.lower().split()[0] == 'maxi bus' and theInsuranceType.lower().split()[1] == 'comprehensive':
        result = comprehensivePremiumForMaxiBus()
    elif theRiskType.lower().split()[0] == 'motor cycle' and theInsuranceType.lower().split()[1] == 'comprehensive':
        result = comprehensivePremiumForMotorCycles()
    else:
        result = 0
    return result
