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
     origins=["http://127.0.0.1:5000"]) # add other endpoints you want to be able to communicate with here as well.
     


logging.info("Server start")

@app.route("/api/leaderboard/top=<int:top>")
def get_team(top):
    # try:
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT {top}")

            data = cur.fetchall()
            
            leaderboard = {0:data}

            for i in range(0,top):
                leaderboard.update({i:top})

            return(leaderboard)
    # except Exception:
    #     return {"error": "Could not load data"}, 500



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)