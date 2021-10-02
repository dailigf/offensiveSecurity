from db import connect_db, get_locations, get_content
import os

database = r"sqlite.db"
content_dir = os.getcwd() + "/content"

def write_to_file(url, content):
    """
    This function will write the contents to a file in  the local directory

    :param url: url of the location
    :type url: string
    :param content: content of the html 
    :type content: blob
    """


    fileName = url.replace("https://", "")
    if not fileName.endswith(".html"):
        fileName = fileName + ".html"
    fullname = os.path.join(content_dir, fileName)
    path, basename =  os.path.split(fullname)

    if not os.path.exists(path):
        os.makedirs(path)
    with open(fullname, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    conn = connect_db(database)
    locations = get_locations(conn)
    for l in locations:
        print("{}".format(l[0]))
        content = get_content(l[0], conn)
        print("content[0]:{}".format(content[0][0]))
        write_to_file(l[0], '\n'.join("{}".format(x[0]) for x in content))

