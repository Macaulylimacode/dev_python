from flask import Flask, render_template # estrutura para criar o site
from flask_socketio import SocketIO, send # estrutura para criar o chat

app = Flask(__name__) # cria o site
app.config["SECRET"] = "teguwyberubi1854946487986318" # chave de segurança, pode ser qualquer coisa, algo difícil
socketio = SocketIO(app, cors_allowed_origins="*") # cria a conexão entre diferentes máquinas que estão no mesmo site

@socketio.on("message") # difine que função abaixo vai ser acionada
def gerenciar_mensagens(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast=True) # envia a mensagem a todo mundo conectado no site

@app.route("/") #cria a pagina do site
def home():
    return render_template("index.html") # essa página vai carregar esse arquivo html
if __name__ == "_main_":
    run_simple("localhost", 5000, app, use_reloader=True, threaded=True, allow_unsafe=True)
    socketio.run(app, host="localhost")
app.run()