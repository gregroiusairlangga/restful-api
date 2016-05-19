# DATABASE SETTINGS
pg_db_username = 'sgikorjcysilrb'
pg_db_password = '_jeqTwwvAwrCY9Xq64utW162wK'
pg_db_name = 'd38o3g93k84hmj'
pg_db_hostname = 'ec2-54-243-208-3.compute-1.amazonaws.com'

#pg_db_username = 'ewzfjmtnvyupfk'
#pg_db_password = 'eR5YdCtMOatBRNi6JSpz6jSgSX'
#pg_db_name = 'df1miggflnsos1'
#pg_db_hostname = 'ec2-54-243-249-154.compute-1.amazonaws.com'


#pg_db_username = 'postgres'
#pg_db_password = 'admin'
#pg_db_name = 'mybd1'
#pg_db_hostname = 'localhost'


# MYSQL
mysql_db_username = 'root'
mysql_db_password = ''
mysql_db_name = 'fscaffold'
mysql_db_hostname = 'localhost'

DEBUG = False
#PORT = 5000
#HOST = "127.0.0.1"
PORT=80
HOST="http://obscure-journey-25836.herokuapp.com/"
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
#SECRET_KEY = "SOME SECRET"
# PostgreSQL
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=pg_db_username,
                                                                                        DB_PASS=pg_db_password,
                                                                                        DB_ADDR=pg_db_hostname,
                                                                                        DB_NAME=pg_db_name)

# MySQL
"""SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=mysql_db_username,
                                                                                        DB_PASS=mysql_db_password,
                                                                                        DB_ADDR=mysql_db_hostname,
                                                                                        DB_NAME=mysql_db_name)"""
