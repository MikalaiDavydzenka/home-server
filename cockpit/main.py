from aiohttp import web
from server import app

if __name__ == "__main__":
    web.run_app(app.init(), host="0.0.0.0", port=8082)
