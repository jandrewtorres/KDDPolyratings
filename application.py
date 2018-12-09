from flask import Flask, request, jsonify
import psycopg2
import json
import configparser
from psycopg2.extras import RealDictCursor

parser = configparser.ConfigParser()
parser.read('./config.ini')

application = Flask(__name__)
host = parser.get('DEFAULT', 'host')
db_name = parser.get('DEFAULT', 'db_name') 
user = parser.get('DEFAULT', 'user')
password = parser.get('DEFAULT', 'password')
config = f"host='{host}' dbname='{db_name}' user='{user}' password='{password}'"
conn = psycopg2.connect(config)
cursor = conn.cursor(cursor_factory=RealDictCursor)


@application.route('/artisan', methods=['POST'])
def post_artisan():
    email = request.args['email']
    first_name = request.args['first_name']
    last_name = request.args['last_name']

    cursor.execute(
        f"""INSERT INTO public.artisan(email, first_name, last_name)
        VALUES (\'{email}\', \'{first_name}\', \'{last_name}\')"""
    )
    conn.commit()
    return "success"

@application.route('/artisan')
def get_artisans():
    cursor.execute(f"SELECT * FROM public.artisan")
    results = cursor.fetchall()
    return json.dumps(results)


if __name__ == '__main__':
    application.run()
