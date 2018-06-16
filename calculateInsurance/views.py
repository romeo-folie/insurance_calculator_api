from django.shortcuts import render
from calculateInsurance.models import Car
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from calculateInsurance.serializers import CarSerializer

# Create your views here.

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all()


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
    Total = secondResult + extraTTPD + additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
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
    Total = firstResult + extraSeatLoading + inexperienced_driver_loading + extraTTPD + additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
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
    Total = secondResult + extraTTPD + inexperienced_driver_loading + additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
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
    Total = secondResult + extraTTPD + inexperienced_driver_loading +additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
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

    comprehensiveBasic = ownDamageBasicPremium + cc_loadings + old_age_loading + TP_basic_premium
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

    Total = firstResult + excessBroughtBack + extraSeatLoading + inexperienced_driver_loading + extraTTPD + additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
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

    comprehensiveBasic = ownDamageBasicPremium + cc_loadings + old_age_loading + TP_basic_premium

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

    Total = firstResult + excessBroughtBack + extraSeatLoading + inexperienced_driver_loading + extraTTPD + additional_perils + ecowas_perils + PA_benefits + nicNhisNrscEcowas
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

    comprehensiveBasic = ownDamageBasicPremium + cc_loadings + old_age_loading + TP_basic_premium
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

    Total = firstResult + excessBroughtBack + extraSeatLoading + inexperienced_driver_loading + extraTTPD + additional_perils+ ecowas_perils+PA_benefits + nicNhisNrscEcowas
    # perDay = Total/365
    return Total
