from rest_framework import serializers
from django.contrib.auth.models import User
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

class UserSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ('id', 'username', 'cars','owner')
