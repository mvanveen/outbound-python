import json
import requests

API_SERVER = "http://api.outbound.io"
IDENTIFY = "api/v1/identify"
TRACK = "api/v1/track"

class Client(object):
  def __init__(self, api_key):
    self._api_key = api_key

  def identify(self, user_id, traits={}):
    resp = requests.post("%s/%s" % (API_SERVER, IDENTIFY), data=json.dumps({
      "api_key": self._api_key,
      "user_id": user_id,
      "traits": traits
    }), headers={
      "Content-Type": "application/json"
    })
    if not resp.status_code == 200:
      return False
    else:
      return resp.content

  def track(self, user_id, event, payload={}):
    resp = requests.post("%s/%s" % (API_SERVER, TRACK), data=json.dumps({
      "api_key": self._api_key,
      "user_id": user_id,
      "event": event,
      "payload": payload
    }), headers={
      "Content-Type": "application/json"
    })
    if not resp.status_code == 200:
      return False
    else:
      return resp.content
