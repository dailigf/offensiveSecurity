#!/bin/env/python3
import hashlib, string, itertools, re, sys

def main():
    """
    This is the main function
    """

    if len(sys.argv) != 5:
        print('(+) usage: %s <domain name> <id> <creation_date> <prefix_length>' % (sys.argv[0]))
        print('(+) e.g: %s offsec.local 3 "2018-06-10 23:59:59" 3' % sys.argv[0])
        sys.exit(-1)

if __name__ == "__main__":
    main()
