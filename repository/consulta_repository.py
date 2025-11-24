import os
import boto3
from boto3.dynamodb.conditions import Key

class ConsultaRepository:

    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(os.environ["TABLE_NAME"])
        self.index_name = os.environ["STATUS_CREATED_AT_INDEX"]

    def buscar_expirados(self, limite_ts: int):
        """
        Busca apenas consultas com:
        - status = EM_ANALISE
        - createdAt < limite_ts

        Usando Query no GSI status + createdAt.
        """
        response = self.table.query(
            IndexName=self.index_name,
            KeyConditionExpression=(
                Key("status").eq("EM_ANALISE") &
                Key("createdAt").lt(limite_ts)
            )
        )

        return response.get("Items", [])

    def atualizar_status(self, consulta_id: str, novo_status: str):
        self.table.update_item(
            Key={"id": consulta_id},
            UpdateExpression="SET #s = :s, updatedAt = :u",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={
                ":s": novo_status,
                ":u": int(__import__("time").time())
            }
        )