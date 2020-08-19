#!/usr/bin/python

#Remap SDK module
from remapSDK import remapSDK
#from remapSDK import Sdk


print('##################################### ReMAP WP5 Model PoC #####################################')

remapSdk=remapSDK.Sdk()

start=remapSdk.getStartTime()
print(start)

end_date=remapSdk.getEndTime()
print(end_date)

tailno=remapSdk.getTailNumber()
print(tailno)

partNo=remapSdk.getParamPartNumber("param1")
print(partNo)

metadata=remapSdk.getMetadata()
print(metadata)

replacements=remapSdk.getReplacements()
print(replacements)

jsonoutput={"rulUnit":"test_rul_unit", "rulValue":5, "probabilityOfFailure":44, "confidenceInterval":55}
output=remapSdk.sendOutput( jsonoutput)
print(output)