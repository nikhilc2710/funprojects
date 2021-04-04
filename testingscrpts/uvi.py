
import uvicorn
async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'app',
    })


if __name__ == "__main__":
    uvicorn.run("uvi:app", host="127.0.0.1", port=5000, access_log=False)