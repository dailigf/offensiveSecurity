import argparse
import sqlite3
import os.path
import sys

def connect_db(filename=r"sqlite.db"):
    """
    Function will be connect to a databse

    :param filename: filenmae of the databse.
    :type filename: string
    :return: connection object to the database
    :rtype: connection object
    """
    conn = None
    try:
        conn = sqlite3.connect(filename)
    except Exception as e:
        print("Unable to connect to database, exiting")
        print(e)
        sys.exit(-1)
    if conn:
        return conn

def get_locations(filename=r"sqlite.db"):
    """
    Function will get the locations stored in the content table of the database

    :param filename: filename of the dataabse
    :type filename: string

    :return: list of locaitons
    :rtype: string list
    """

    conn = connect_db(filename)
    locations_query = "SELECT location FROM content;"
    content = None
    try:
        cursor_obj = conn.execute(locations_query)
        content = cursor_obj.fetchall()
        print(content)
        conn.close()
    except Exception as e:
        print("Could not retrieve locations from the content table")
        print(e)
        conn.close()
        sys.exit(-1)

    return content

def get_content(location, filename=r"sqlite.db"):
    """
    This function will get content form the content table

    :parame location: locatio of the content
    :type location: string
    :param filename: filename of the database
    :type filename: string

    :return: all of the content at a location
    :rtype: list of strings
    """

    conn = connect_db(filename)
    get_query = "SELECT content FROM content WHERE location = (?);"
    content = None

    try:
        args = (location,)
        print("args: {}".format(args))
        cursor_obj = conn.execute(get_query, args)
        content = cursor_obj.fetchall()
        print(content)
        conn.close()
    except Exception as e:
        print("Error getting information from database, exitng")
        print(e)
        conn.close()
        sys.exit(-1)

    return content

def insert_content(location, content, filename=r"sqlite.db"):
    """
    This function will INSERT content INTO TABLE location

    :param filename: filename of the sqlite database
    :type filename: string
    :param location: url location of the content
    :type location: string
    :param content: content 
    :type content: string

    :return: rowid of the new row that was created
    :rtype: int
    """
    conn = connect_db(filename)
    insert_query = "INSERT INTO content (location, content) VALUES (?,?);"
    get_row_id = "SELECT id FROM content WHERE location = ? AND content = ?"
    row_id = None
    try:
        args = (location, content)
        conn.execute(insert_query, args)
        conn.commit()
        cursor_obj = conn.execute(get_row_id, args)
        row_id = cursor_obj.fetchall()[0][0]
        print(row_id)
        conn.close()
    except Error as e:
        print(e)
        print("Could not insert into table, exiting")
        conn.close()
        sys.exit(-1)
    return row_id

def create_db(filename=r"sqlite.db"):
    """
    This function will be used to create a database
    """
    if os.path.isfile(filename):
        print("file {} exists. Skipping Create".format(filename))
    else:
        conn = None

        try:
            conn = sqlite3.connect(filename)
        except Error as e:
            print(e)
        finally:
            if conn:
                createContentTable = """CREATE TABLE IF NOT EXISTS content (
                    id integer PRIMARY KEY,
                    location text NOT NULL,
                    content blob);"""
                try:
                    print("(+) Creating content table.")
                    c = conn.cursor()
                    c.execute(createContentTable)
                except Error as e:
                    print(e)
                conn.close()


def main():
    """
    This is the main function
    """
    print("inside main")

    #Create an argument parser
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--create", help="Create a new Database", action="store_true")
    group.add_argument("--insert", help="Insert Into Table", action="store_true")
    group.add_argument("--get", help="Gets data from content table", action="store_true")
    group.add_argument("--locations", help="Get all locations from content table", action="store_true")

    parser.add_argument("--location", "--L")
    parser.add_argument("--content", "--C")

    args = parser.parse_args()

    filename=r"sqlite.db"
    if args.create:
        print('(+) creating a database')
        create_db()
    elif args.insert:
        print('(+) Inserting into Table')
        if args.location is None or args.content is None:
            parser.error("--insert requires --location and --content")
        else:
            insert_content(args.location, args.content)
    elif args.get:
        print('(+) Getting data from the content table')
        if args.location is None:
            parser.error("--get requires --location")
        else:
            get_content(args.location)
    elif args.locations:
        print("(+) Getting locations from the content table.")
        if args.locations:
            get_locations()

if __name__ == "__main__":
    main()

