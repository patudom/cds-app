from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from solara.server import settings

import solara.server.starlette

routes = [
    Mount("/", routes=solara.server.starlette.routes),
]

app = Starlette(routes=routes, middleware=solara.server.starlette.middleware)
