from datetime import datetime, timedelta, timezone
import time

def agora_epoch():
    """Retorna o timestamp UNIX atual em segundos (UTC)."""
    return int(time.time())

def ts_limite(minutos: int) -> int:
    """Retorna o timestamp mínimo aceito antes de expirar."""
    return agora_epoch() - (minutos * 60)