import requests

from flask import Flask, render_template
app = Flask(__name__)

def checkStatus():
	try:
		time = requests.get('https://pgorelease.nianticlabs.com/plfe/').elapsed.total_seconds()
		if time < 3:
			return True
		else:
			return False
	except:
		return True

@app.route('/')
def index():
    if checkStatus():
    	return render_template('index.html', status=True)
    else:
    	return render_template('index.html', status=False)

if __name__ == "__main__":
    app.run()

