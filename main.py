import uvicorn
import json
from zoneinfo import ZoneInfo
from datetime import datetime
tzinfo = ZoneInfo("Australia/Melbourne")

async def app(scope, receive, send):
    datetime_str = datetime.now(tz=tzinfo).strftime('%Y%m%d%H%M%S')
    path = f'/data/request-{datetime_str}.json'
    with open(path,'w') as json_record:
        json.dump(scope,json_record,indent=4)
    return 'Request received'

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host = '0.0.0.0', 
        port=12345, 
        log_level="info"
    )