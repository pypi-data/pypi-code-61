import glob
import json
import os
import xml.etree.ElementTree as ET
import xmltodict

class __ValidationData:
    netValue =0
    taxes = []
    def setNetValue(self,netValue):
        self.netValue=netValue
    def addTaxInformation(self,taxRate,taxMoney):
        self.taxes.append({'taxRate':taxRate,'taxMoney': taxMoney})
def __xmlEnhancer(xmlData):
    if(type(xmlData) == type(list())):
        return xmlData
    else:
        tempList = list()
        tempList.append(xmlData)
        return tempList
def __getDataForTaxValidation(dictTransactionData):
    requiredValidationData = []
    for itemNumber in range(0,len(dictTransactionData['itemization'])):
        itemData = __ValidationData()
        try:
            itemData.setNetValue(int(dictTransactionData['itemization'][itemNumber]['net_sales_money']['amount']))
            for taxNumber in range(0,len(dictTransactionData['itemization'][itemNumber]['taxes'])):
                taxRate =  float(dictTransactionData['itemization'][itemNumber]['taxes'][taxNumber]['rate'])
                taxMoney = int(dictTransactionData['itemization'][itemNumber]['taxes'][taxNumber]['applied_money']['amount'])
                itemData.addTaxInformation(taxRate,taxMoney)
        except ValueError as verr:
            print(verr)
        except Exception as ex:
            print(ex)
        requiredValidationData.append(itemData)
    return requiredValidationData
def __validateTransactionTaxData(listedTransaction):
    validatedData = __getDataForTaxValidation(listedTransaction)
    for item in (validatedData):
        for tax in item.taxes:
            if int((tax['taxRate'] * item.netValue)+0.5) == tax['taxMoney']:
                continue
            else:
                return False
    return True
def __validate(transactionFile):
    extension = os.path.splitext(transactionFile)[1]
    if (extension == '.xml'):
        return __validateXmlTransactionFile(transactionFile)
    if (extension == '.json'):
           return __validateJsonTransactionFile(transactionFile)
    raise Exception("Only accepting json/xml files")

def __validateJsonTransactionFile(jsonTransactionFile):
    jsonData = __readJsonFile(jsonTransactionFile)
    return __validateTransactionTaxData(jsonData)
def __readJsonFile(jsonFile):
    try:
        file = open(jsonFile, )
        JSONdata = json.load(file)
    except IOError as io:
        print(io)
    except Exception as ex:
        print(ex)
    finally:
        file.close()
    return JSONdata

def __validateXmlTransactionFile(xmlTransactionFile):
    xmlData = __readXmlFile(xmlTransactionFile)
    return __validateTransactionTaxData(xmlData)
def __readXmlFile(xmlFile):
    try:
        file = open(xmlFile, )
        tree = ET.parse(file)
    except IOError as io:
        print(io)
    except Exception as ex:
        print(ex)
    finally:
        file.close()
    xml_data = tree.getroot()
    xmlstr = ET.tostring(xml_data, encoding='utf8', method='xml')
    xml_data_dict = dict(xmltodict.parse(xmlstr, dict_constructor=dict))['root']
    xml_data_dict['itemization']=  __xmlEnhancer(xml_data_dict['itemization']['element'])
    xml_data_dict['taxes']=  __xmlEnhancer(xml_data_dict['taxes']['element'])
    for item in range(0,len(xml_data_dict['itemization'])):
        xml_data_dict['itemization'][item]['taxes']=  __xmlEnhancer(xml_data_dict['itemization'][item]['taxes']['element'])
        xml_data_dict['itemization'][item]['modifiers']=  __xmlEnhancer(xml_data_dict['itemization'][item]['modifiers']['element'])
    return xml_data_dict

def validateTransactionsFolder(transactionsFolder):
    validationresults = []
    try:
        transactionFiles =  glob.glob(transactionsFolder+"*.*")
    except Exception as ex:
        print(ex)
    for transactionFile in transactionFiles:
        validationresult = __validate(transactionFile)
        validationresults.append({transactionFile,validationresult})
    return validationresults
def validateTransactionsFile(transactionFile):
    return __validate(transactionFile)

def validateTransaction(dictTransaction):
    return __ValidationData(dictTransaction)
