from . import api
from flask import json
from ..models import NetSign

@api.route('/get_jnfdc', methods=['POST'])
def get_jnfdc():
    nss = NetSign.query.order_by(NetSign.date)
    result = []
    for ns in nss:
        item = {'signnum': ns.signnum, 'date': ns.date}
        result.append(item)
    return json.dumps({'rows':result})
