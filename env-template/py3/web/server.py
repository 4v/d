#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
from bottle import app, route, template, Response

app = app()

@route('/')
def index():
    return Response("Hello, It works!")


@route('/ip')
def index():
    import subprocess
    p1 = subprocess.Popen(['ip', 'addr', 'show', 'eth0'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(
        ['sed', '-rn', r's/\s*inet\s(([0-9]{1,3}\.){3}[0-9]{1,3}).*/\1/p'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    ip_addr = p2.communicate()[0].strip()
    p1.wait()
    return template('index', ip_addr=ip_addr)


@route('/json')
def json_reply():
    import os
    heads = bottle.request.headers
    bottle.response.content_type = 'application/json'
    response = {'headers': dict(heads),
                'environment': dict(os.environ),
                'response': dict(bottle.response.headers)}
    return response
