from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")  # pag de inicio para mostrar un tablero de 8*8
def index():
    return render_template("index.html",horizontal=8 , vertical=8)

@app.route("/<x>")  # pag para mostrar un tablero de 8*4
def index4(x):
    return render_template("index.html",horizontal=int(x), vertical=8)

@app.route("/<x>/<y>") # pag para mostrar tablero de x*y
def play(x,y):
    return render_template("index.html",horizontal=int(x),vertical=int(y))


if __name__=="__main__":   
    app.run(debug=True)  