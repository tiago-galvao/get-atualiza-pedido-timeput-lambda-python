from service.consulta_service import ConsultaService

def handler(event, context):
    service = ConsultaService()
    expirados = service.processar_expirados()

    return {
        "statusCode": 200,
        "message": f"{len(expirados)} consultas expiradas.",
        "ids": expirados
    }