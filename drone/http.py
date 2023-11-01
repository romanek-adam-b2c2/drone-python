import json
import requests

from . import config
from .decorators import jsonargs


def create_session() -> requests.Session:
    return requests.Session()


@jsonargs
def get(url, params=None, session=None):
    session = session or requests
    headers = {"Authorization": "Bearer %s" % config.api_token()}
    r = session.get(url, headers=headers, params=params)
    if not r.ok:
        r.raise_for_status()
    return r.json()


@jsonargs
def post(url, params=None, data=None, session=None):
    session = session or requests
    headers = {"Authorization": "Bearer %s" % config.api_token()}
    r = session.post(url, headers=headers, params=params, data=data)
    if not r.ok:
        r.raise_for_status()
    return r.json()


@jsonargs
def patch(url, params=None, data=None, session=None):
    session = session or requests
    headers = {"Authorization": "Bearer %s" % config.api_token()}
    r = session.patch(url, headers=headers, params=params, data=data)
    if not r.ok:
        r.raise_for_status()
    return r.json()


def delete(url, session=None):
    session = session or requests
    headers = {"Authorization": "Bearer %s" % config.api_token()}
    r = session.delete(url, headers=headers)
    if not r.ok:
        r.raise_for_status()
    try:
        return r.json()
    except json.JSONDecodeError:
        return r.text
