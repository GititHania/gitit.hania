from os import name
import flask as f

app = f.Flask(__name__)

@app.route('/')
def home():
    return "Wellcome to the home page!"

@app.route('/CV')
def cv():
    return f.redirect('CVgrid.html')

@app.route('/ContactUs')
def cu():
    return f.render_template('forms.html')



if __name__ == '__main__':
    app.run(debug=True)