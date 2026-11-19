import os

import psycopg
from dotenv import load_dotenv
from flask import Flask, request, render_template
from flask_login import (LoginManager, UserMixin, current_user,
                        login_required, login_user, logout_user)
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import requests
import logging

from flask_cors import CORS

load_dotenv()
conn_str = os.environ["DATABASE_URL"]

app = Flask(__name__)

CORS(app,
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization"],
     origins=["http://127.0.0.1:5000", "http://192.168.110.157:5500, http://192.168.111.253, http://localhost:5000, http://127.0.0.1:5500"])
     


logging.info("Server start")

@app.route("/api/leaderboard/top=<int:top>")
def leaderboard(top):
    # try:
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT playerName, score, timeTaken FROM runInfo ORDER BY score DESC, timeTaken, playerName")

            data = cur.fetchall()
            
            leaderboard = {0:{
                            "Name":"",
                            "Score":0,
                            "Time":0.00}}
            try:
                for i in range(0,top):
                    leaderboard.update({i:{"Name":data[i][0]}})
                    leaderboard[i]["Score"] = data[i][1]
                    leaderboard[i]["Time"] = data[i][2]
            except Exception:
                pass

            return(leaderboard)
# except Exception:
    #     return {"error": "Could not load data"}, 500

id = 0
@app.route("/api/addtoruninfo", methods=["POST", "GET"])
def addToRunInfo():
    # try:
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            global id
            # data = request.get_json()
            id = cur.execute("SELECT id FROM runInfo ORDER BY id DESC LIMIT 1;").fetchone()
            if (id == None):
                id = 0
            else:
                id = int(id[0])+1
            name = "testname3"
            score = 1
            timeTaken = 1500000.05
            # return({"t":cur.execute("SELECT * FROM player WHERE playerName = %s;", (name, )).fetchall() == []})
            if (cur.execute("SELECT * FROM player WHERE playerName = %s;", (name, )).fetchall() == []):
                cur.execute("INSERT INTO player (playerName) VALUES (%s);", (name, ))
            
            cur.execute("INSERT INTO runInfo (id, playerName, score, timeTaken) VALUES (%s, %s, %s, %s);", (id, name, score, timeTaken))

            return (cur.execute("SELECT * FROM runInfo;").fetchall())


    # except Exception:
    #     return {"error": "Could not load data"}, 500

@app.route("/api/colors", methods=["POST", "GET"])
def addToColors():
    # try:
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:

            runID = id
            round = cur.execute(f"SELECT round FROM colors WHERE runID = {runID} ORDER BY round DESC LIMIT 1;").fetchone()
            if (round == None):
                round = 1
            else:
                round = int(round[0])+1
            color = 'red'
            timeTaken = .10
            cur.execute("INSERT INTO colors (runId, round, color, timeTaken) VALUES (%s, %s, %s, %s);", (runID, round, color, timeTaken, ))

            return (cur.execute("SELECT * FROM colors").fetchall())


    # except Exception:
    #     return {"error": "Could not load data"}, 500

#Remove later
@app.route("/api/clear", methods=["POST", "GET"])
def clearTables():
    # try:
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM runInfo;")
            cur.execute("DELETE FROM runInfo;")
            cur.execute("DELETE FROM colors;")

            return "Cleared tables"

@app.after_request
def add_cors_headers(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    resp.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return resp
        
          

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)