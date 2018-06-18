from rest_framework import serializers

from calculateInsurance.models import Car

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('type_of_risk','id','make_of_vehicle','number_of_seats','registration_number','license_issued_year','insurance_type','insurance_payment_due')
        extra_kwargs = {
            'url':{
                'view_name':'calculateInsurance:car-detail'
            }
        }
