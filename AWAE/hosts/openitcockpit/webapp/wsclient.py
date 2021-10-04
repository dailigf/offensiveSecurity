import websocket
import argparse
import ssl
import json
import _thread as thread

uniqid = ""
key = ""

def on_open(ws):
    def run():
        while True:
            print("Enter a command:")
            cmd = input()
            ws.send(toJson("execute_nagios_command", cmd))
    thread.start_new_thread(run, ())

def toJson(task, data):
    req = {
            "task": task,
            "data": data,
            "uniqid": uniqid,
            "key": key
            }

    return json.dumps(req)

def on_message(ws, message):
    mes = json.loads(message)
    print(mes)
    if "uniqid" in mes:
        uniqid = mes["uniqid"]

    if mes["type"] == "dispatcher":
        pass
    elif mes["type"] == "connection":
        print("[+] Connected")
    elif mes["type"] == "response":
        #print(mes["payload"], end = '')
        print(mes)
    else:
        print(mes)


def on_error(ws, error):
    print(error)

def on_close(ws):
    print('[+] Connection Closed.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--url', '-u',
            required=True,
            dest='url',
            help='WebSocket url')
    
    parser.add_argument('--key','-k',
            required=True,
            dest='key',
            help='WebScoket key')

    parser.add_argument('--verbose', '-V',
            help='Print more data',
            action='store_true')

    args = parser.parse_args()

    key = args.key
    websocket.enableTrace(args.verbose)
    ws = websocket.WebSocketApp(args.url,
                               on_message = on_message,
                               on_error = on_error,
                               on_close = on_close,
                               on_open = on_open)
    ws.run_forever(sslopt={"cert_reqs":ssl.CERT_NONE})
