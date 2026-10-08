from flask import Flask

app = Flask(__name__)


def mensagem():
    return "Bem-vindo à revisão de DevOps!"


@app.route("/")
def home():
    return mensagem()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)