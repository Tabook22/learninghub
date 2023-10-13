from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<p> In The Name of Allah"


if __name__=="__main__":
    #run the flask app on local server
    app.run(host='0.0.0.0', debug=True)
