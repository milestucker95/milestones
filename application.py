from flask import Flask, render_template

application = Flask(__name__, template_folder='templates', static_url_path='/static')

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    application.run()
