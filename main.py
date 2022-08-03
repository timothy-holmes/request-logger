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
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': (f'Scope received: {datetime_str}').encode('utf-8'),
    })
    return None # ASGI callable should return None

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host = '0.0.0.0', 
        port=12345, 
        log_level="info"
    )