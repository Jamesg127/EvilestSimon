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