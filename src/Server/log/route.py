from flask import Blueprint
from flask import jsonify, render_template, request

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .logger import SystemLogger

from mail.mailer import Mailer

log = Blueprint('log', __name__)
mail = Mailer()
systemLogger = SystemLogger()


@log.route("/api/log/error", methods=['GET'])
def send_err_file():
    attachment_file = systemLogger.zip_log_file()
    status_code = mail.send_email_with_attachment(
        {},
        attachment_file
    )
    print(status_code)

    if status_code == 202:
        msg = str("The error log has communicated to the developer! Please wait for a reply.")
        return jsonify(msg=msg), 202
    else:
        msg = str("Unable to communicate error log!")
        return jsonify(msg=msg), 500
