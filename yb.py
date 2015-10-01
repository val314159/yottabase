#!/usr/bin/env python
from gevent import monkey; monkey.patch_all()
from yotta import yottapubsub_client
YottaPubSubClient=yottapubsub_client.YottaPubSubClient

def onpub(a,b,c,d):
    print("ONPUB", repr((a,b,c,d)))
    pass

ps = YottaPubSubClient("ws://localhost:9028/ws").sub(
    [ 'A' ,'B' ] ).loop(callback=onpub)
