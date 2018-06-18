# from django.shortcuts import render
from calculateInsurance.models import Car
from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.reverse import reverse
from calculateInsurance.serializers import CarSerializer
from calculateInsurance.serializers import UserSerializer
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from calculateInsurance.permissions import IsOwnerOrReadOnly



# Create your views here.

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    # def perform_create(self, serializer):
    #     serializer.save()

    def post(self, request, format=None):
        theRiskType = request.data['type_of_risk']
        theInsuranceType = request.data['insurance_type']

        serializer = CarSerializer(data=request.data)
        insurancePaymentData = mainPremiumFunction(theRiskType, theInsuranceType)

        if serializer.is_valid():
            serializer.save(insurance_payment_due = insurancePaymentData, owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


    def get_queryset(self):
        return Car.objects.all()


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# manual function views for the various functions
# POST

# @csrf_exempt
# @api_view(['GET','POST'])
# def car_list(request,format=None):
#     """List all cars or add new ones"""
#     if request.method == "GET":
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars,many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         # data = JSONParser().parse(request)
#         theRiskType = request.data['type_of_risk']
#         theInsuranceType = request.data['insurance_type']
#
#         serializer = CarSerializer(data = request.data,)
#         insurancePaymentData = mainPremiumFunction(theRiskType, theInsuranceType)
#
#         if serializer.is_valid():
#             serializer.save(insurance_payment_due = insurancePaymentData)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# @api_view(['GET','PUT','DELETE'])
# def car_detail(request,pk,format=None):
#     """Retrieve, update or delete an existing car"""
#     try:
#         car = Car.objects.get(pk=pk)
#     except Car.DoesNotExist:
#         return Response(status=status.HTTP_400_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = CarSerializer(car)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         # data = JSONParser().parse(request)
#         serializer = CarSerializer(car, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




def mainPremiumFunction(theRiskType, theInsuranceType):
    """Selects a particular premium function based on certain conditions"""
    if theRiskType.lower() == 'taxi' and theInsuranceType.lower() == 'third party':
        return premiumForTaxiThirdParty()
    elif theRiskType.lower() == 'x1' and theInsuranceType.lower() == 'third party':
        return premiumForPrivateThirdParty()
    elif theRiskType.lower() == 'maxi bus' and theInsuranceType.lower() == 'third party':
        return premiumForMaxiBusThirdParty()
    elif theRiskType.lower() == 'motor cycle' and theInsuranceType.lower() == 'third party':
        return premiumForMotorCycleThirdParty()
    elif theRiskType.lower() == 'x4' and theInsuranceType.lower() == 'comprehensive':
        return comprehensivePremiumForX4()
    elif theRiskType.lower() == 'maxi bus' and theInsuranceType.lower() == 'comprehensive':
        return comprehensivePremiumForMaxiBus()
    elif theRiskType.lower() == 'motor cycle' and theInsuranceType.lower() == 'comprehensive':
        return comprehensivePremiumForMotorCycles()
    else:
        return 0




def premiumForTaxiThirdParty():
    """Calculates the premium for a third party insured Taxi"""
    TP_basic_premium = 310
    TPPDL = 3000
    old_age_loading = TP_basic_premium * 0.075
    inexperienced_driver_loading = 0
    additional_perils = 5
    ecowas_perils = 10
    PA_benefits = 20
    nicNhisNrscEcowas = 12
    extraTTPD = 20
    extraSeatLoading = 0
    firstResult = TP_basic_premium + old_age_loading
    ncd = firstResult * 0.2
    secondResult = firstResult - ncd
    Total = secondResult + extraTTPD + additional_perils + \
    ecowas_perils + PA_benefits + nicNhisNrscEcowas
    return Total

# Third party insurance premiums
def premiumForPrivateThirdParty():
    """Calculates the premium for a third party X1 vehicle"""
    TP_basic_premium = 210
    TPPDL = 3000
    old_age_loading = TP_basic_premium * 0.05
    inexperienced_driver_loading = 0.1 * TP_basic_premium
    additional_perils = 5
    ecowas_perils = 5
    PA_benefits = 20
    nicNhisNrscEcowas = 12
    extraTTPD = 20
    extraSeatLoading = 5
    firstResult = TP_basic_premium + old_age_loading
    Total = firstResult + extraSeatLoading + inexperienced_driver_loading + \
    extraTTPD + additional_perils + ecowas_perils + \
    PA_benefits + nicNhisNrscEcowas
    # perDay = Total/365
    return [Total]

def premiumForMaxiBusThirdParty():
    """Calculates the premium for a third party MAXI BUS"""
    TP_basic_premium = 320
    TPPDL = 10000
    old_age_loading = TP_basic_premium * 0.05
    inexperienced_driver_loading = 0
    additional_perils = 5
    ecowas_perils = 10
    PA_benefits = 20
    nicNhisNrscEcowas = 12
    extraTTPD = 160
    extraSeatLoading = 8
    firstResult = TP_basic_premium + old_age_loading
    ncd = firstResult * 0.2
    secondResult = firstResult - ncd
    Total = secondResult + extraTTPD + inexperienced_driver_loading + \
    additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
    # perDay = Total/365
    return Total


def premiumForMotorCycleThirdParty():
    """Calculates the premium for a third party motor cycle"""
    TP_basic_premium = 110
    TPPDL = 3000
    old_age_loading = 0
    inexperienced_driver_loading = 0.1 * TP_basic_premium
    additional_perils = 5
    ecowas_perils = 10
    PA_benefits = 20
    nicNhisNrscEcowas = 12
    extraTTPD = 160
    extraSeatLoading = 8
    firstResult = TP_basic_premium + old_age_loading
    ncd = firstResult * 0.1
    secondResult = firstResult - ncd
    Total = secondResult + extraTTPD + inexperienced_driver_loading +\
    additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
    # perDay = Total/365
    return Total


#Comprehensive insurance premiums
def comprehensivePremiumForX4():
    """Calculates the comprehensive premium for X4 category vehicles"""
    sumInsured = 220000
    ownDamageRate = 0.06
    old_age_loading = 0
    inexperienced_driver_loading = 0
    TP_basic_premium = 210
    extraSeatLoading = 8
    TPPDL = 7500

    ownDamageBasicPremium = sumInsured * ownDamageRate
    cc_loadings = 0.1 * ownDamageBasicPremium

    comprehensiveBasic = ownDamageBasicPremium + cc_loadings + \
    old_age_loading + TP_basic_premium
    ncd = 0.45 * comprehensiveBasic
    fleetDiscount = 0.05 * comprehensiveBasic

    firstResult = comprehensiveBasic - (ncd+fleetDiscount)

    excessBroughtBack = 0.1 * ownDamageBasicPremium
    extraSeatLoading = 8
    inexperienced_driver_loading = 0
    extraTTPD = 110
    additional_perils = 5
    ecowas_perils = 5
    PA_benefits = 20
    nicNhisNrscEcowas = 12

    Total = firstResult + excessBroughtBack + \
    extraSeatLoading + inexperienced_driver_loading + \
    extraTTPD + additional_perils + ecowas_perils + \
    PA_benefits + nicNhisNrscEcowas
    # perDay = Total/365
    return Total


def comprehensivePremiumForMaxiBus():
    """Calculates the comprehensive premium for maxi buses"""
    sumInsured = 220000
    ownDamageRate = 0.08

    inexperienced_driver_loading = 0
    TP_basic_premium = 320
    extraSeatLoading = 8
    TPPDL = 5000

    ownDamageBasicPremium = sumInsured * ownDamageRate
    cc_loadings = 0.1 * ownDamageBasicPremium
    old_age_loading = 0.05 * ownDamageBasicPremium

    comprehensiveBasic = ownDamageBasicPremium + \
    cc_loadings + old_age_loading + TP_basic_premium

    ncd = 0.2 * comprehensiveBasic
    fleetDiscount = 0.1 * comprehensiveBasic

    firstResult = comprehensiveBasic - (ncd + fleetDiscount)

    excessBroughtBack = 0
    extraSeatLoading = 400
    inexperienced_driver_loading = 0
    extraTTPD = 75
    additional_perils = 5
    ecowas_perils = 5
    PA_benefits = 20
    nicNhisNrscEcowas = 12

    Total = firstResult + excessBroughtBack + \
    extraSeatLoading + inexperienced_driver_loading + \
    extraTTPD + additional_perils + ecowas_perils + PA_benefits + \
    nicNhisNrscEcowas
    # perDay = Total/365
    return Total

def comprehensivePremiumForMotorCycles():
    """Calculates the comprehensive premium for motor cycles"""
    sumInsured = 15000
    ownDamageRate = 0.03
    old_age_loading = 0
    inexperienced_driver_loading = 0.1
    TP_basic_premium = 110
    extraSeatLoading = 0
    TPPDL = 3000

    ownDamageBasicPremium = sumInsured * ownDamageRate
    cc_loadings = 0 * ownDamageBasicPremium

    comprehensiveBasic = ownDamageBasicPremium + cc_loadings + \
    old_age_loading + TP_basic_premium
    ncd = 0.1 * comprehensiveBasic
    fleetDiscount = 0

    firstResult = comprehensiveBasic - (ncd+fleetDiscount)
    excessBroughtBack = 0
    extraSeatLoading = 0
    inexperienced_driver_loading = 45
    extraTTPD = 20
    additional_perils = 5
    ecowas_perils = 5
    PA_benefits = 20
    nicNhisNrscEcowas = 12

    Total = firstResult + excessBroughtBack + \
    extraSeatLoading + inexperienced_driver_loading + \
    extraTTPD + additional_perils+ ecowas_perils+PA_benefits + nicNhisNrscEcowas
    # perDay = Total/365
    return Total
