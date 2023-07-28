# Dev_Python

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Macaulylimacode/dev_python/blob/master/LICENSE) 

## Sobre o projeto
Projeto de criação de chat ao vivo,que será o HashZap. Uma espécie de Whatsapp. Vai ser um chat ao vivo, 
onde as pessoas podem entrar e conversar como se fosse um chat normal. Para isso nós vamos criar um site e criar o chat dentro do site.

### OBS:
```bash
use com responsabilidade, lembrando que as mensagens permanecem apenas quando os participante estão ao vivo
```
# Dá uma olhada como vai ficar o nosso chat "front".
![1](https://github.com/Macaulylimacode/dev_python/assets/139823222/8ee6e65e-88f4-49dc-9dd1-cb32a9ee5df6)
![2](https://github.com/Macaulylimacode/dev_python/assets/139823222/56142577-b463-457e-8a1b-fbb6083207af)

## Dá uma olhada como vai ficar o nosso chat "back".
![WhatsApp Image 2023-07-27 at 22 22 42](https://github.com/Macaulylimacode/dev_python/assets/139823222/c001fa3b-1e19-467f-8c84-e44f5f46922d)

### OBS:
A mensagem "Werkzeug não foi projetado para ser executado em produção. Passe allow_unsafe werkzeug-True para o método run() para desativar" é um aviso para os desenvolvedores que estão usando o framework Werkzeug em um ambiente de produção. O Werkzeug é um framework web que é projetado para desenvolvimento e teste, e não é tão seguro quanto outros frameworks web. O método run() do Werkzeug aceita um parâmetro allow_unsafe que, quando definido como True, desativa algumas das proteções de segurança do Werkzeug. Isso pode ser necessário para fins de desenvolvimento, mas não é recomendado para uso em produção.
Para desativar as proteções de segurança do Werkzeug em um ambiente de produção, você pode adicionar o seguinte código ao seu código:
```bash
from werkzeug.serving import run_simple
if _name_ == "_main_":
    run_simple("localhost", 5000, app, use_reloader=True, threaded=True, allow_unsafe=True)
```
No entanto, é importante notar que isso pode tornar seu aplicativo mais vulnerável a ataques. Você deve apenas fazer isso se estiver ciente dos riscos e se sentir confortável em assumi-los.
Aqui estão algumas razões pelas quais você pode querer desativar as proteções de segurança do Werkzeug em um ambiente de produção:
```bash
• Você está usando uma versão antiga do Werkzeug que não possui as mesmas
proteções de segurança que as versões mais recentes.
• Você precisa usar um recurso do Werkzeug que
 não é seguro, mas de que você precisa.
• Você está ciente dos riscos de desativar as
proteções de segurança e se sente confortável em assumi-los
```
Se você decidir desativar as proteções de segurança do Werkzeug em um ambiente de produção, 
é importante tomar medidas para mitigar os riscos. Isso pode incluir:
```bash
• Usar um framework web mais seguro.
• Implementar suas próprias proteções de segurança.
• Monitorar seu aplicativo de perto para quaisquer vulnerabilidades.
• Manter seu aplicativo atualizado com as últimas versões do Werkzeug.
```
É importante pesar os riscos e benefícios de desativar as proteções de segurança do 
Werkzeug em um ambiente de produção antes de tomar uma decisão.

# Tecnologias utilizadas
## Linguagem
- Python
- Html
- CSS
- Javascript
  
## Bibliotecas
• Flask – pip install flask

• Socketio – pip install python-socketio / pip install flask-socketio

• Simple Websocket – pip install simple-websocket 

### Caso queira se aprofundar nas bibliotecas
• Flask - https://flask.palletsprojects.com/en/2.3.x/

• Flask no Visual Studio Code - https://code.visualstudio.com/docs/python/tutorial-flask

• Socketio - https://socket.io/pt-br/docs/v4/

## Implantação em produção
- jupyter
- pycharm
# Como executar o projeto

```bash
# clonar repositório
git clone https://github.com/Macaulylimacode/dev_python/blob/master/Python%20DEV.py

# entrar na pasta do projeto
cd dev_python

# executar o projeto
./mvnw spring-boot:run
```

# Autor

### Macauly lima

[![linkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/macauly-lima-75984a269)

