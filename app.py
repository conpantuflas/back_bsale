from flask_cors import CORS
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
CORS(app)

def connection():
	return mysql.connector.connect(
		host="mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com",
		user="bsale_test",
		password="bsale_test",
		database="bsale_test"
	)

@app.route('/category', methods=['GET'])
def get_category():
	mydb = connection()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM category")
	category = mycursor.fetchall()
	return jsonify(category),200

@app.route('/product', methods=['GET'])
def get_product():
	mydb = connection()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM product")
	product = mycursor.fetchall()
	return jsonify(product),200

@app.route('/a_category/<int:id>', methods=['GET'])
def a_category(id):
	mydb = connection()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM product WHERE product.category = %(id)s", {'id': id})
	products = mycursor.fetchall()
	return jsonify(products),200


@app.route('/search/<string:search>', methods=['GET'])
def search(search):
	mydb = connection()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM product WHERE name LIKE '%"+search+"%';")
	results = mycursor.fetchall()
	return jsonify(results),200



if __name__ == "__main__":
	app.run(host="localhost", port="5000")
