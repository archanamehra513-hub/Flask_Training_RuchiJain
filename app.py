from flask import Flask, render_template, request , redirect ,url_for

app=Flask(__name__)
@app.route('/')
def home():
    return "<h1>Archana this Side</h1>"

@app.route('/welcome')
def welcome():
    return "<h1>Welcome to Flask Training class</h1>"

@app.route('/sucess/<int:a>')
def sucess(a):
    return "the person is pass and the score is"+str(a)

@app.route('/fail/<int:a>')
def fail(a):
    return "<h1>the person is fail and the score is</h1><br>"+str(a)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        dsa=float(request.form['dsa'])
        science=float(science.form['science'])
        datascience=float(datascience.form['datascience'])
        avg=(dsa+science+datascience)/3
        result=""
        if avg>=80:
            result="sucess"
        else:
            result="fail"
        return redirect(url_for(result,a=avg))    
                                
if __name__=='__main__':
    app.run(debug=True)
