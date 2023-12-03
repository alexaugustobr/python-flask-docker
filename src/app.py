from flask import Flask,render_template
import socket
import os

app = Flask(__name__)

@app.route("/")
def index():
    print('--ENV BEGIN--')
    for k, v in os.environ.items():
        print(f'{k}={v}')
    print('--ENV END--')
    print('OS=',os.environ.get('OS'))
    print('DB_NAME_TP=',os.environ.get('DB_NAME_TP'))
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
