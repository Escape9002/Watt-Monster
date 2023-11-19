import server_interfaces

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    status = server_interfaces.check_ping()

    if request.method == 'POST':
        if request.form['onBtn']:
            server_interfaces.turn_on()       

    return render_template("index.html", status=status)
    


if __name__ == '__main__':
    app.run()