import asyncio
from typing import Coroutine
from weakref import WeakSet
from contextlib import suppress

from aiohttp import web
from aiohttp import web_request

import logging

from server.torrent import Torrent

log = logging.getLogger(__name__)


class WebRequest(web_request.Request):

    @property
    def app(self) -> "WebApp":
        return super().app


class WebApp(web.Application):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.workers_to_run: list = []
        self.workers: list[asyncio.Task] = []
        self.stream_sets: list[WeakSet] = []

    @property
    def torrent(self) -> Torrent:
        return self["torrent_client"]

    @torrent.setter
    def torrent(self, torrent: Torrent):
        self["torrent_client"] = torrent
        # registration
        for route in torrent.routes():
            self.router.add_route(*route)

        self.stream_sets.append(torrent.streams)
        self.workers_to_run.append(torrent.worker)


async def on_startup(app: WebApp):
    log.info("worker start")

    for worker in app.workers_to_run:
        app.workers.append(app.loop.create_task(worker()))


async def on_cleanup(app: WebApp):
    log.info("worker cleanup")

    for worker in app.workers:
        worker.cancel()
        with suppress(asyncio.CancelledError):
            await worker


async def on_shutdown(app: WebApp):
    log.info("worker shutdown")

    waiters = []
    for streams in app.stream_sets:
        for stream in streams:
            stream.stop_streaming()
            waiters.append(stream.wait())

    await asyncio.gather(*waiters)
    for streams in app.stream_sets:
        streams.clear()


def init():
    app = WebApp()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    app.on_cleanup.append(on_cleanup)

    app.torrent = Torrent()
    return app
