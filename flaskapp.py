from flask import Flask
import pymysql

app = Flask(__name__)

@app.route("/")
def flask_main():
    return "<h1>Flask is running</h1>"

@app.route("/sermons")
def sermons():
    dbopts = {
	'db' : os.environ['MYSQL_DB'],
	'user' : os.environ['MYSQL_USER'],
	'password' : os.environ['MYSQL_PASSWORD'],
	'host' : os.environ['MYSQL_HOST'],
	'port' : os.environ['MYSQL_PORT'],
    }
    con = pymysql.connect(**dbopts)
    cursor = con.cursor()
    try:
        SQL = """SELECT * FROM sermons"""
        cursor.execute(SQL)
        rows = cursor.fetchall()
        jdata = json.dumps(rows)
        return jdata
    except Exception as e:
        return str(e)
    finally:
        try:
            cursor.close()
            con.close()
        except Exception as e:
            pass
