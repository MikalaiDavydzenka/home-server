import requests
from requests.auth import HTTPBasicAuth


def req(prev_resp=None):
    session_id = "0"
    if prev_resp is not None:
        session_id = prev_resp.headers.get("X-Transmission-Session-Id", "0")

    resp = requests.post(
        url="http://192.168.1.109:9091/transmission/rpc",
        json={
            "arguments": {
                "fields": [
                   "name",
                ]
            },
            "method": "torrent-get",
        },
        auth=HTTPBasicAuth("torrent", "torrent"),
        headers={
            "X-Transmission-Session-Id": session_id,
        }
    )
    if resp.status_code == 409 and not prev_resp:
        resp = req(resp)

    return resp

# breakpoint()
print(req().json())