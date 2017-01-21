from flask import render_template
from . import main
from ..models import NetSign

@main.route('/jnfdc', methods=['GET'])
def index():
    nss = NetSign.query
    return render_template('jnfdc.html', nss = nss)


