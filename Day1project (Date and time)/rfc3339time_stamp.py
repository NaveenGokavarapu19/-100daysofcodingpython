
from datetime import datetime,timezone

rfc3339 = datetime.now(timezone.utc).astimezone()
print(" the rfc time is :",rfc3339);