class DatabaseFunction:
  def __init__(self,stackName= 'villa-wallet-dev-WalletDatabase-1IGM93I0V85AH', user=None, pw=None):
    self.lambdaClient = boto3.client(
        'lambda',
        aws_access_key_id = user,
        aws_secret_access_key = pw ,
        region_name = 'ap-southeast-1'
      )
    self.stackName = stackName

  def invoke(self, functionName, data):
    response = self.lambdaClient.invoke(
        FunctionName = functionName,
        InvocationType = 'RequestResponse',
        Payload=json.dumps(data)
    )
    return json.loads(response['Payload'].read())

  def addMember(self, data:dict):
    functionName = f'{self.stackName}-add-member'
    return self.invoke(functionName = functionName, data=data)

  def getMember(self, data:dict):
    functionName = f'{self.stackName}-get-member'
    return self.invoke(functionName = functionName, data=data)

  def setMember(self, data:dict):
    functionName = f'{self.stackName}-set-member'
    return self.invoke(functionName = functionName, data=data)

  def removeMember(self, data:dict):
    functionName = f'{self.stackName}-remove-member'
    return self.invoke(functionName = functionName, data=data)
