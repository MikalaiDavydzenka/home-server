import transmission_rpc
from server.torrent.model import Model as TorrentModel
from weakref import WeakSet


from functools import partial
import json
from aiohttp_sse import EventSourceResponse, sse_response
from aiohttp.web_request import Request
from datetime import datetime
import asyncio
import base64


class SSEResponse(EventSourceResponse):
    @property
    def last_event_id(self):
        return self._req.headers.get("Last-Event-Id")

    async def send_json(
        self,
        data,
        id=None,
        event=None,
        retry=None,
        json_dumps=partial(json.dumps, indent=2),
    ):
        await self.send(json_dumps(data), id=id, event=event, retry=retry)


class Torrent:

    def __init__(self):
        self.client = transmission_rpc.Client(
            host="localhost",
            port=9091,
            username="torrent",
            password="torrent"
        )

        self.streams: WeakSet[SSEResponse] = WeakSet()

    def torrents_list(self):
        torrents = []
        for torrent in self.client.get_torrents():
            torrents.append({
                "id": torrent.id,
                "name": torrent.name,
                "progress": torrent.progress / 100.0,
                "rateDownload": torrent.rateDownload,
                "rateUpload": torrent.rateUpload,
                "totalSize": torrent.total_size,
            })
        return torrents

    def handle_subscriptions(self):
        torrents = self.torrents_list()

        now = datetime.now()

        for stream in self.streams:
            data = {
                "time": f"Server Time : {now}",
                "torrents": torrents,
                "last_event_id": stream.last_event_id,
            }
            yield stream.send_json(data, id=now.timestamp())

    async def worker(self):
        while True:
            delay = asyncio.create_task(asyncio.sleep(1))  # Fire
            # Run in parallel
            await asyncio.gather(*self.handle_subscriptions())
            # Sleep 1s - n
            await delay

    async def subscribe(self, request: Request):
        stream: SSEResponse = await sse_response(request, response_cls=SSEResponse)
        self.streams.add(stream)
        try:
            await stream.wait()
        finally:
            self.streams.discard(stream)
        return stream

    async def add(self, request: Request):
        data = await request.json()
        torrent = base64.b64decode(data["torrent"])
        self.client.add_torrent(torrent)

    async def delete(self, request: Request):
        data = await request.json()
        torrent_ids = data["torrentIds"]
        self.client.remove_torrent(torrent_ids, delete_data=True)

    def routes(self):
        yield ("GET", "/cockpit/torrent", self.subscribe)
        yield ("POST", "/cockpit/torrent", self.add)
        yield ("DELETE", "/cockpit/torrent", self.delete)
