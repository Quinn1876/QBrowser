from flask import Flask, request, render_template
import requests
app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
  response = requests.get(request.json['query'])
  return response.text

@app.route('/example1')
def example1():
  return render_template('example1.html')

app.run()
