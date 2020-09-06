import json
from mongoengine import *
from Entity.Collection import ManagementCompanies
from Entity.Collection import ManagementCompanyGeoSetupHeaders
from Entity.Collection import ManagementCompanyGeoSetups
from Entity.Collection import OperationalSetups
from Entity.Collection import MarketSegments
from Entity.Collection import Properties
from Entity.Collection import CompanyProfiles
from Entity.Collection import CompanyProfileReservations


class DataLoader:

    def __init__(self,file,env):
        self.file=file
        self.env=env
        self.managementCompanyList = set()
        self.propertyIdList = set()
        with open('resources/testdata/'+self.file) as f:
            self.data=json.load(f)
        connect(self.env['db'], host=self.env['db.url'], port=4023)
        self.initData()

    def deleteManagementAndPropertySetup(self):
        for id in self.managementCompanyList:
            ManagementCompanies.objects.filter(_id=int(id)).delete()
            ManagementCompanyGeoSetupHeaders.objects.filter(managementCompanyId=int(id)).delete()
            ManagementCompanyGeoSetups.objects.filter(managementCompanyId=int(id)).delete()
            OperationalSetups.objects.filter(managementCompanyId=int(id)).delete()
            MarketSegments.objects.filter(managementCompanyId=int(id)).delete()
            Properties.objects.filter(managementCompanyId=int(id)).delete()

    def deleteAccountIntelData(self):
        for id in self.propertyIdList:
            CompanyProfiles.objects.filter(propertyId=int(id)).delete()
            CompanyProfileReservations.objects.filter(propertyId=int(id)).delete()

    def _insertData(self,cls,data):
        for dat in data:
            bsondata=cls(**dat)
            bsondata.save()

    def createManagementAndProperty(self):
        managementCompany = self.data['managementCompanies']
        properties = self.data['properties']
        managementCompanyHeader = self.data['managementCompanyGeoSetupHeaders']
        managementCompanyGeoSetup = self.data['managementCompanyGeoSetups']
        operationalSetup = self.data['operationalSetups']
        marketSegments = self.data['marketSegments']
        self._insertData(ManagementCompanies,managementCompany)
        self._insertData(Properties,properties)
        self._insertData(ManagementCompanyGeoSetupHeaders,managementCompanyHeader)
        self._insertData(ManagementCompanyGeoSetups,managementCompanyGeoSetup)
        self._insertData(OperationalSetups,operationalSetup)
        self._insertData(MarketSegments,marketSegments)

    def createAccountIntelData(self):
        companyProfiles = self.data['companyProfiles']
        companyProfileReservations = self.data['companyProfileReservations']
        self._insertData(CompanyProfiles,companyProfiles)
        self._insertData(CompanyProfileReservations,companyProfileReservations)

    def initData(self):
        managementCompany = self.data['managementCompanies']
        properties = self.data['properties']
        for dat in managementCompany:
            self.managementCompanyList.add(dat['_id'])
        for dat in properties:
            self.propertyIdList.add(dat['_id'])

    def getData(self):
        return self.data