import os
from repository.consulta_repository import ConsultaRepository
from utils.datetime_utils import ts_limite

class ConsultaService:

    def __init__(self):
        self.repository = ConsultaRepository()
        self.ttl_minutes = int(os.environ["TTL_MINUTES"])

    def processar_expirados(self):
        limite_ts = ts_limite(self.ttl_minutes)
        expirados = self.repository.buscar_expirados(limite_ts)

        ids_expirados = []

        for item in expirados:
            consulta_id = item["id"]
            self.repository.atualizar_status(consulta_id, "EXPIRADO")
            ids_expirados.append(consulta_id)

        return ids_expirados