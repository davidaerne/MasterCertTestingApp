import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "yoursecretkey"
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://Thor\\SQLEXPRESS/CertDB?driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
