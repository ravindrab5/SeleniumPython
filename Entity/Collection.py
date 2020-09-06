import datetime
from mongoengine import *



class ManagementCompanies(Document):
    _id=IntField(required=True)
    managementCompanyType=StringField(required=True)
    uniqueManagementCompanyName=StringField(required=True)
    managementCompanyName=StringField(required=True)
    licenceContactInitial=StringField(required=True)
    licenceContactFirstName=StringField(required=True)
    licenceContactLastName=StringField(required=True)
    addressLine1=StringField(required=True)
    country=StringField(required=True)
    diallingPrefix=StringField(required=True)
    city=StringField(required=True)
    postalCode=StringField(required=True)
    areaCode=StringField(required=True)
    phoneNumber=StringField(required=True)
    activationDate=DateTimeField(required=True)
    chimpsId=StringField(required=True)
    uniqueClientCode=StringField(required=True)
    clientCode=StringField(required=True)
    contactTitle=StringField(required=True)
    contactEmail=StringField(required=True)
    addressLine2=StringField(required=True)
    state=StringField(required=True)
    mobileNumber=StringField(required=True)
    admins=ListField(required=True)
    meta = {'collection': 'managementCompany'}

class ManagementCompanyGeoSetupHeaders(Document):
    _id=IntField(required=True)
    managementCompanyId=IntField(required=True)
    name=StringField(required=True)
    meta = {'collection': 'managementCompanyGeoSetupHeader'}

class ManagementCompanyGeoSetups(Document):
    _id=IntField(required=True)
    managementCompanyId=IntField(required=True)
    name=StringField(required=True)
    path=StringField(required=True)
    sequenceNo=IntField(required=True)
    meta = {'collection': 'managementCompanyGeoSetup'}

class OperationalSetups(Document):
    _id=ObjectIdField(required=False)
    managementCompanyId = IntField(required=True)
    operationTierName=StringField(required=True)
    isPropertyDisplay=BooleanField(required=True)
    detailList=ListField(required=True)
    meta={'collection':'operationalSetup'}

class ImpactTypes(Document):
    _id = ObjectIdField(required=False)
    name=StringField(required=True)
    isUserDefined=BooleanField(required=True)

class WeekConfigs(Document):
    weekConfigurationId=StringField(required=True)
    propertyId=IntField(required=True)
    managementCompanyId=IntField(required=True)
    weekDays=ListField(required=True)
    weekEnds=ListField(required=True)


class MarketSegments(Document):
    _id=ObjectIdField(required=False)
    managementCompanyId=IntField(required=True)
    typeId=IntField(required=False)
    typeName=StringField(required=False)
    virtualType=IntField(required=False)
    virtualTypeName=StringField(required=False)
    nameSpace=StringField(required=True)
    categoryName=StringField(required=False)
    categoryRank=IntField(required=False)
    subCategoryName=StringField(required=False)
    subcategoryRank=IntField(required=False)
    companySegmentCode=StringField(required=False)
    segmentDescription=StringField(required=False)
    erpCodeUnit=ListField(required=False)
    erpCodeRev=ListField(required=False)
    forecastMethod=StringField(required=False)
    showCheck=BooleanField(required=False)
    segmentRank=IntField(required=False)
    isPropertyDisplay=BooleanField(required=False)
    combineInto=StringField(required=False)
    propertySegmentCode=StringField(required=False)
    propertyId=IntField(required=False)
    propertySegmentRank=IntField(required=False)
    meta={'collection':'marketSegment'}

class Properties(Document):
    _id=IntField(required=True)
    managementCompanyId=IntField(required=True)
    uniquePropertyName=StringField(required=True)
    propertyName=StringField(required=True)
    licenceContactInitial=StringField(required=True)
    licenceContactFirstName=StringField(required=True)
    licenceContactLastName=StringField(required=True)
    addressLine1=StringField(required=True)
    country=StringField(required=True)
    diallingPrefix=StringField(required=True)
    city=StringField(required=True)
    postalCode=StringField(required=True)
    areaCode=StringField(required=True)
    phoneNumber=StringField(required=True)
    chimpsId=StringField(required=True)
    contactTitle=StringField(required=True)
    contactEmail=StringField(required=True)
    addressLine2=StringField(required=True)
    state=StringField(required=True)
    mobileNumber=StringField(required=True)
    activationStartDate=DateTimeField(required=True)
    activationEndDate=DateTimeField(required=True)
    selectedTypeOfBussiness=StringField(required=True)
    selectedSubTypeOfBussiness=StringField(required=True)
    timezone=StringField(required=True)
    admins=ListField(required=True)
    measurementName=StringField(required=True)
    fiscalCurrency=StringField(required=True)
    timeFormat=StringField(required=True)
    dateFormat=StringField(required=True)
    systemLanguage=StringField(required=True)
    selectedPmsList=StringField(required=True)
    pmsId=StringField(required=True)
    selectedSnCList=StringField(required=True)
    snCId=StringField(required=True)
    selectedRmsList=StringField(required=True)
    rmsId=StringField(required=True)
    selectedFrsList=StringField(required=True)
    frsId=StringField(required=True)
    snCCurrency=StringField(required=True)
    hotelCapacity=StringField(required=True)
    frsStructure=StringField(required=True)
    complex=StringField(required=True)
    complexRegion=StringField(required=True)
    linkToComplex=StringField(required=True)
    propertyOperationSetups=DictField(required=True)
    geoId=StringField(required=True)
    meta = {'collection': 'property'}


class CompanyProfiles(Document):
    _id=ObjectIdField(required=False)
    propertyId=IntField(required=True)
    companyProfileID=StringField(required=True)
    companyProfileName=StringField(required=True)
    contract=BooleanField(required=False)
    createdDate=DateTimeField(required=True)
    dataType=StringField(required=True)
    lastModifiedDate=DateTimeField(required=True)
    status=StringField(required=True)
    masterCompanyProfileID=StringField(required=False)
    meta = {'collection': 'companyProfile'}

class CompanyProfileReservations(Document):
    _id = ObjectIdField(required=False)
    propertyId = IntField(required=True)
    companyProfileID=StringField(required=True)
    confirmationNumber=StringField(required=True)
    occupancyDate=DateTimeField(required=True)
    reservationRoomCount=IntField(required=True)
    reservationStatus=StringField(required=True)
    isPseudoRoom=StringField(required=True)
    meta = {'collection': 'companyProfileReservation'}















