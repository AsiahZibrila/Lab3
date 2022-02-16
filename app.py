from flask import Flask, render_template, request

app = Flask(__name__)

app.config['SECRET_KEY'] = 'random-secret-key'
#app.config['FLASK_ENV']='development'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="POST" and 'single' in request.form:
        sdate = request.form['single']
        api_s = "https://data.calgary.ca/resource/c2es-76ed.geojson?issueddate="+ sdate +"T00:00:00.000"
        return render_template('opencalgary.html', sdate=sdate, api_s=api_s)

    elif request.method=="POST" and 'startdate' in request.form:
        startdate = request.form['startdate']
        enddate = request.form['enddate']
        api_r= "https://data.calgary.ca/resource/c2es-76ed.geojson?$where=issueddate%20%3E%20%27"+ startdate + "%27%20and%20issueddate%20%3C%20%27"+  enddate + "%27"
        return render_template('opencalgary.html', startdate=startdate, enddate=enddate, api_r=api_r)
    else:
        return render_template('opencalgary.html')

if __name__ == "__main__":
    app.run()

