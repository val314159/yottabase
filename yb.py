import yotta
from yotta.yottapubsub_client import YottaPubSubClient

def onpub(a,b,c,d):
    print("ONPUB", repr((a,b,c,d)))
    pass

ps = YottaPubSubClient("ws://localhost:9028/ws")
ps.sub( [ 'A' ,'B' ] )
ps.loop(callback=onpub)
