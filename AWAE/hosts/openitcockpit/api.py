from flask import Flask, request, send_file
from db import create_connection, insert_content, create_db
from flask_cors import CORS


