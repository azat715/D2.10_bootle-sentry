import logging
from os import environ

import sentry_sdk
from bottle import HTTPError, request, route, template, default_app, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

env = environ

sentry_sdk.init(dsn=env["SENTRY_DSN"], integrations=[BottleIntegration()])

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s bottle_app %(levelname)s %(message)s"
)

default_app.push()

@route("/success")
def success():
    logging.info("/success")
    logging.info(request.headers.get("User-Agent"))
    logging.info(request.headers.get("Host"))
    return HTTPResponse(status=200)

@route("/error")
def error_():
    logging.info("/error")
    logging.info(request.headers.get("User-Agent"))
    logging.info(request.headers.get("Host"))
    return HTTPError(500, "Error, ошибка сервера")


@route("/fail")
def fail():
    logging.info("/fail")
    logging.info(request.headers.get("User-Agent"))
    logging.info(request.headers.get("Host"))
    raise RuntimeError("There is an error!")


app = default_app()
