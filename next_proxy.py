import flask
import json
from flask import Flask, request, jsonify
import logging
import sys
file_handler = logging.FileHandler(filename='proxy.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.DEBUG, 
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=handlers
)

logger = logging.getLogger('LOGGER_NAME')
app = flask.Flask(__name__)

def read_file_proxy():
    f = open("proxy.txt", "r")
    content = f.read()
    proxy_infos = content.split('\n')
    proxys = []
    next_proxy = None
    for info in proxy_infos:
        if ":" not in  info:
            continue
        infos = info.split(':')
        ip = infos[0]
        port, status = infos[1].split("|")
        proxy_info = {"ip":ip, "port": port, "status": status}
        if status == '0' and next_proxy is None:
            next_proxy = proxy_info
            proxy_info["status"] = '1'
        proxys.append(proxy_info)
    f.close()
    return proxys, next_proxy

def save_file_proxy(proxys):
    f = open("proxy.txt", "w")
    for proxy in proxys:
        line = proxy["ip"] + ":" +str(proxy["port"]) + "|" + str(proxy["status"])+'\n'
        f.write(line)
    f.close()

@app.route("/next", methods=['POST'])
def next():
    logger.info("next")
    proxys, next_proxy = read_file_proxy()
    logger.info(next_proxy)
    save_file_proxy(proxys)
    return jsonify(next_proxy)

app.run(host="0.0.0.0", port=8080)