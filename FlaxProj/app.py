from os import name
import flask as f
import datetime

app = f.Flask(__name__)

@app.route('/')
def home():
    return "Wellcome to the home page!"

@app.route('/firstCV')
def cv1():
    return f.redirect('CVgrid.html')

@app.route('/ContactUs')
def cu():
    return f.render_template('forms.html')

@app.route('/cv')
def cv():
    return f.render_template('cv1.html')


@app.route('/cv2')
def cv2():
    return f.render_template('cv2.html')

@app.route('/assignment8')
def asg8():
    return f.render_template('assignment8.html', time= datetime.datetime.now().time().hour)



if __name__ == '__main__':
    app.run(debug=True)