from app import app, mensagem


def test_mensagem():
    assert mensagem() == "Bem-vindo à revisão de DevOps!"


def test_rota_principal():
    resposta = app.test_client().get("/")
    assert resposta.status_code == 200