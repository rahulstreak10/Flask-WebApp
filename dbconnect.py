import MySQLdb

def connection():
	conn = MySQLdb.connect(host="localhost",user="root", passwd="os.environ[password_db]",db="flaskDatabase")

	c=conn.cursor()

	return c, conn
