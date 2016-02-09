
import boto3


class MetaDB:
    def __init__(self, tablename):
        """
        Iniatialize the data base
        :param tablename:  Name of the meta data table
        """
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.table = dynamodb.Table(tablename)

    def writemeta(self, key, value):
        """
        Store meta data in the Dynamo table
        :param key: Meta data key - Combination of the boss data model key and meta data key
        :param value: Meta data value
        """
        response = self.table.put_item(
            Item={
                'metakey': key,
                'metavalue': value,
            }
        )

    def getmeta(self, key):
        """
        Retrieve the meta data for a given key
        :param key:
        :return:
        """
        print (key)
        response = self.table.get_item(
            Key={
                'metakey': key,
            }
        )
        if 'Item' in response:
            return response['Item']
        else:
            return None

    def deletemeta(self, key):
        """
        Delete the meta data item for the specified key
        :param key: Meta data key to be delete
        :return:
        """
        response = self.table.delete_item(
            Key={
                'metakey': key,
            },
            ReturnValues='ALL_OLD'
        )
        return response

    def updatemeta(self, key, newvalue):
        """
        Update the Value for the given key
        :param key: Search key
        :param newvalue: New value for the meta data key
        :return:
        """
        response = self.table.update_item(
            Key={
                'metakey': key,
            },
            UpdateExpression='SET metavalue = :val1',
            ExpressionAttributeValues={
                ':val1': newvalue
            },
            ReturnValues='UPDATED_NEW'
        )
        return response