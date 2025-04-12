# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde

## Configuração do Ambiente

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure o arquivo .env com suas credenciais
5. Configure o PostgreSQL e crie o banco de dados

## Executando o Projeto

```bash
uvicorn app.main:app --reload
```

O servidor estará disponível em: http://localhost:8000

Documentação Swagger: http://localhost:8000/docs

## Testando os Endpoints

1. Primeiro, obtenha um token JWT fazendo login:
   ```bash
   POST /token
   Form data:
   username: admin@example.com
   password: admin
   ```

2. Use o token recebido no header Authorization de todas as requisições:
   ```
   Authorization: Bearer <seu_token>
   ```

3. Endpoints disponíveis:
   - POST /pacientes - Criar paciente
   - GET /pacientes/{id} - Obter paciente por ID
   - GET /pacientes - Listar todos os pacientes
   - PUT /pacientes/{id} - Atualizar paciente
   - DELETE /pacientes/{id} - Excluir paciente

## Estrutura do Banco de Dados

O sistema usa PostgreSQL como banco de dados. Certifique-se de criar um banco de dados chamado "sghss" antes de executar o aplicativo.

## Segurança

- Todas as rotas são protegidas por autenticação JWT
- As senhas são armazenadas com hash bcrypt
- Os tokens JWT expiram após 30 minutos 