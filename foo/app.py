
from flask import Flask
import sys
sys.path.append('./direction')
from forward import forward
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello a!'

@app.route('/car/forward')
def forwards():
    return forward()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

