from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/nsttopics")
def nsttopics():
    return render_template("nsttopics.html")


@app.route("/assignment")
def assignment():
    return render_template("assignment.html")


@app.route("/ussersac")
def usersac():
    return render_template("usersac.html")

@app.route("/surveysc")
def surveysc():
    return render_template("surveysc.html")

@app.route("/chatbotsc")
def chatbotsc():
    return render_template("chatbotsc.html")

@app.route('/aiedu')
def aiedu():
    return render_template("aiedu.html")

@app.route("/nisot")
def nisot():
    return render_template("nisot.html")

@app.route("/ainusc")
def ainusc():
    return render_template("ainusc.html")



if __name__=="__main__":
    #run the flask app on local server
    app.run(host='0.0.0.0', debug=True)
