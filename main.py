import uvicorn
import json
from zoneinfo import ZoneInfo
from datetime import datetime
tzinfo = ZoneInfo("Australia/Melbourne")

class BytesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode('utf-8')
        return json.JSONEncoder.default(self, obj)

async def app(scope, receive, send):
    datetime_str = datetime.now(tz=tzinfo).strftime('%Y%m%d%H%M%S')
    path = f'/data/request-{datetime_str}.json'
    # path = f'C:\\Code\\home-server\\request-logger\\data\\request-{datetime_str}.json'
    print(scope)
    with open(path,'w') as json_record:
        json.dump(scope,json_record,indent=4,cls=BytesEncoder)
    return None # ASGI callable should return None

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host = '0.0.0.0', 
        port=12345, 
        log_level="info"
    )