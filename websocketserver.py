from websocket_server import WebsocketServer
import time

f = open('values.json', 'r')
msg = f.read()
f.close()

def open_file(msg):
  global f
  f = open('values.json', 'r')
  msg = f.read()
  f.close()
  return msg

def new_client(client, message):
  while True:
    message = open_file(msg)
    server.send_message(client, message)
    time.sleep(1/20)

server = WebsocketServer(9001)
server.set_fn_new_client(new_client)
server.run_forever()
