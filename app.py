from flask import Flask
from flask import render_template
from flask import Markup
from flask.ext.frozen import Freezer
import my_md


app = Flask(__name__)
app.config['DEBUG'] = False
app.testing = True

freezer = Freezer(app)

@app.route('/')
def index():
    content = Markup(my_md.index())
    title = "index"
    return render_template('index.html', content=content, title=title)

@app.route('/page1.html')
def page1():
    content = Markup(my_md.page1())
    return render_template('page1.html', content=content, title='page1')

@app.route('/page2.html')
def page2():
    content = Markup(my_md.page2())
    extra = Markup(my_md.page2_extra())
    return render_template('page2.html', content=content, extra=extra, title='page2')


if __name__ == '__main__':
    #app.run(debug=True)
    freezer.freeze()
