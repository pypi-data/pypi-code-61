import boto3, json, pickle, logging
class Database:
  def __init__(self, user, pw, stackName = 'villa-wallet-dev-WalletDatabase-1IGM93I0V85AH'):
    self.lambdaClient = boto3.client(
            'lambda',
            aws_access_key_id = user,
            aws_secret_access_key = pw ,
            region_name = 'ap-southeast-1'
      )
    self.stackName = stackName

  def invoke(self, functionName, payload):
    response = self.lambdaClient.invoke(
      FunctionName = functionName,
      InvocationType = 'RequestResponse',
      LogType = 'Tail',
      Payload = json.dumps(payload).encode()
    )
    if 'Payload' in response.keys():
      responsePayload = json.loads(response.get('Payload').read())
      logging.info(f'invocation successful to function{functionName}')
      return responsePayload
    logging.error(f'invocation unsuccessful to function{functionName}, {response}')
    return response
  def addMember(self,
                functionName = '',
                data:dict={}):
    if not functionName: functionName = '-'.join([self.stackName, 'add-member'])
    logging.info(f'functionName is {functionName}')
    result = self.invoke(functionName, data)
    return result

  def getMember(self,
                functionName = '',
                data:dict={}):
    if not functionName: functionName = '-'.join([self.stackName, 'get-member'])
    logging.info(f'functionName is {functionName}')
    result = self.invoke(functionName, data)
    return result

  def setMember(self,
                functionName = '',
                data:dict={}):
    if not functionName: functionName = '-'.join([self.stackName, 'set-member'])
    logging.info(f'functionName is {functionName}')
    result = self.invoke(functionName, data)
    return result

  def removeMember(self,
                functionName = '',
                data:dict={}):
    if not functionName: functionName = '-'.join([self.stackName, 'remove-member'])
    logging.info(f'functionName is {functionName}')
    result = self.invoke(functionName, data)
    return result
