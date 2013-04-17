import os
import json
try:
  from google.appengine.api import urlfetch
except:
  pass
try:
  import requests
except:
  pass

API_SERVER = "http://api.outbound.io"
IDENTIFY = "api/v1/identify"
TRACK = "api/v1/track"


class Client(object):
  def __init__(self, api_key):
    self._api_key = api_key

  def fetch_response(self, url, payload):
    return requests.post(
      url,
      data=payload,
      headers={'Content-Type': 'application/json'}
    )

  def identify(self, user_id, traits={}):
    resp = self.fetch_response(
      "%s/%s" % (API_SERVER, IDENTIFY), json.dumps({
        "api_key": self._api_key,
        "user_id": user_id,
        "traits": traits
      }))

    if not resp.status_code == 200:
      return False
    else:
      return resp.content

  def track(self, user_id, event, payload={}):
    resp = self.fetch_response(
      "%s/%s" % (API_SERVER, TRACK),
      json.dumps({
        "api_key": self._api_key,
        "user_id": user_id,
        "event": event,
        "payload": payload
      }))

    if not resp.status_code == 200:
      return False
    else:
      return resp.content


class GAEClient(Client):
  """Google App Engine-specific client"""
  def fetch_response(self, url, payload):
    return urlfetch.fetch(
      url,
      payload=payload,
      method=urlfetch.POST,
      headers={
        "Content-Type": "application/json"
      })

