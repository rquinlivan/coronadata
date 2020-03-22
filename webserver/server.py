from flask import Flask
from jinja2 import Environment, PackageLoader, select_autoescape

jinja = Environment(
    loader=PackageLoader('server', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
app = Flask(__name__)


def render_view(name, args={}):
    template = jinja.get_template(name + '.jinja')
    return template.render(args)


@app.route("/")
def index():
    return render_view('index')
