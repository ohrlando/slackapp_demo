# Slack API

## Slack App
1. Primeiro, é necessário [criar um novo appp](https://api.slack.com/apps/new)
    1. AppName: Nome do App
    1. Development Slack Workspace: Caso o criador deixe o WS, ele perderá a habilidade de gerenciar o app
    1. Você pode add colaboradores do app
    1. Instale o app na Wokrspace
1. Acesse seu dashboard de apps e entre no [seu novo app](https://api.slack.com/apps/A01R6SZHLAX/)

### App Credentials
#### Checando autenticidade das requisições
Reuest body:

     token=gIkuvaNzQIHg97ATvDxqgjtO
     &team_id=T0001
     &team_domain=example
     &enterprise_id=E0001
     &enterprise_name=Globular%20Construct%20Inc
     &channel_id=C2147483705
     &channel_name=test
     &user_id=U2147483697
     &user_name=Steve
     &command=/weather
     &text=94070
     &response_url=https://hooks.slack.com/commands/1234/5678
     &trigger_id=13345224609.738474920.8088930838d88f008e0
     &api_app_id=A123456

É necessário [verificar as requests recebidas](https://api.slack.com/authentication/verifying-requests-from-slack).
* Ingredientes: : (X-Slack-Request-Timestamp, Request Body, X-Slack-Signature, X-Slack-Signature)
    - HTTP request
    - signing secret
* Como:
    - Verificar se o timestamp recebido é recente (evitando replays)
    - gerar basestring: 'v0:' + timestamp + ':' + request_body (ex: 'v0:1531420618:token=xyzz0WbapA4vBCDEFasx0q6G&team_id=T1DC2JH3J&team_domain=testteamnow&channel_id=G8PSS9T3V&channel_name=foobar&user_id=U2CERLKJA&user_name=roadrunner&command=%2Fwebhook-collect&text=&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT1DC2JH3J%2F397700885554%2F96rGlfmibIGlgcZRskXaIFfN&trigger_id=398738663015.47445629121.803a0bc887a14d10d2c447fce8b6703c')
    - Tirar o hash:
      
          my_signature = 'v0=' + hmac.compute_hash_sha256(
            slack_signing_secret,
            sig_basestring
          ).hexdigest()
    - Comparar com X-Slack-Signature

### OAuth & Permissions
#### Bot Token Scopes
Capabilites do app:
Event, Métodos, Comandos, etc 

| [API Methods](https://api.slack.com/methods)                  | Descrição                           |
|--------------------------------------------------------------:|------------------------------------:|
|  [app_mentions:read](https://api.slack.com/scopes/app_mentions:read)| Send messages as @demo1       |
| [chat:write](https://api.slack.com/scopes/chat:write)         | Send messages as @demo1             |
| [commands](https://api.slack.com/scopes/commands)             | Add shortcuts and/or slash commands that people can use |
| [groups:write](https://api.slack.com/scopes/groups:write)     | Manage private channels that Demo1 has been added to and create new ones |
| [im:history](https://api.slack.com/scopes/im:history)         | View messages and other content in direct messages that Demo1 has been added to |
| [users:read](https://api.slack.com/scopes/users:read)         | View people in a workspace |

### Slash commands

- Permite interações com apps através da [Message Compose Box](https://api.slack.com/messaging/composing#message_structure)
- Gera um payload enviado pelo Slack
- Ponto de entrada para fluxos, integrações e serviços externos

**Estrutura:**

     /comando text

1. Vá em **Features** > Slash Commands e cadastre todos os comandos para sua aplicação
