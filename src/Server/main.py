# 標準ライブラリ

# 関連外部ライブラリ
from flask import Flask, render_template
from flask_uploads import configure_uploads
import ssl

# 内部ライブラリ
from uploads.route import uploads, files
from engine.route import engine
from api.api import api

# 1. Flask 2. Django
# アプリケーションのインスタンス生成
app = Flask(__name__,
            instance_relative_config=True,
            static_folder="../Client/static",
            template_folder="../Client/templates")

# Application settings
# ssl setting
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.crt', 'server_secret_wo_pass.key')

app.config.from_pyfile('flask.cfg')

# Settings for uploading files
configure_uploads(app, files)

# Route setting
app.register_blueprint(uploads)
app.register_blueprint(engine)
app.register_blueprint(api)


ssl._create_default_https_context = ssl._create_unverified_context

# URL setting
@app.route('/')
def main():
    return render_template('index.html')

# TODO: Duy need to confirm
# Confirmation: What does the source code in the following line mean? Can I delete it if it is unnecessary?
# @app.route('/statistic')


if __name__ == "__main__":
    # Application start
    # TODO: Trungとの確認が必要
<<<<<<< HEAD
    # Confirmation: It is better to change to threaded = True
    app.run(host='0.0.0.0', port=3000, ssl_context=context, threaded=False, debug=False)