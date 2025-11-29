# Projeto IoT — API REST para Coleta e Gerenciamento de Dados de Sensores

Este repositório contém uma **API REST** completa desenvolvida com **FastAPI** para **coleta**, **armazenamento** e **gerenciamento** de dados de sensores IoT.  
O projeto implementa um sistema backend robusto com autenticação, persistência de dados e múltiplos endpoints para consumo por aplicações cliente.

**Funcionalidades principais:**

- **API REST segura** com autenticação via Bearer Token
- **Simulador Python** integrado para testes e demonstrações
- **Persistência de dados** em banco SQLite com SQLAlchemy ORM
- **Múltiplos endpoints** para consulta, filtragem e agrupamento de dados
- **CORS configurado** para integração com aplicações frontend

A aplicação web (dashboard) que consome esta API está disponível em: <a href="https://github.com/isabeckmann/projeto-iot-front">projeto-iot-front</a>

---

## Visão Geral do Sistema

Este sistema backend implementa uma arquitetura RESTful completa com:

- **Recebimento de dados** de sensores IoT via HTTP POST
- **Armazenamento persistente** em banco de dados SQLite
- **Autenticação por token** para segurança dos endpoints
- **Múltiplas formas de consulta** (todos os dados, por sensor, últimos registros, agrupados)
- **Simulador integrado** para geração de dados de teste

### Formato de Dados

Cada leitura de sensor segue o formato JSON:

```json
{
  "sensorId": "T010",
  "type": "temperature",
  "value": 23.5,
  "timestamp": "2025-01-18T14:32:55Z"
}
```

### Tipos de Sensores Suportados

- **T010** - Temperatura (18°C a 30°C)
- **H010** - Umidade (30% a 90%)
- **L010** - Luminosidade (0 a 1000 lux)
- **M010** - Movimento (0 ou 1, booleano)

## Funcionalidades Implementadas

### Sistema de Autenticação

- **Bearer Token Authentication** em todos os endpoints
- Token configurável via variável de ambiente `AUTH_TOKEN`
- Proteção contra acessos não autorizados

### API REST - Endpoints Disponíveis

| Método   | Endpoint                       | Descrição                                       |
| -------- | ------------------------------ | ----------------------------------------------- |
| `POST`   | `/api/sensor/data`             | Recebe e armazena leituras de sensores          |
| `GET`    | `/api/sensor/data`             | Lista todas as leituras armazenadas             |
| `GET`    | `/api/sensor/data/latest`      | Retorna a última leitura de cada sensor         |
| `GET`    | `/api/sensor/data/grouped`     | Retorna dados agrupados por sensor              |
| `GET`    | `/api/sensor/data/{sensorId}`  | Lista todas as leituras de um sensor específico |
| `DELETE` | `/api/sensor/data/{record_id}` | Remove um registro específico                   |
| `POST`   | `/api/sensor/register`         | Cadastra um novo sensor no sistema              |

### API em Produção

A API está hospedada na **Railway** e pode ser acessada em:

**Base URL:** `https://projeto-iot-fork-production.up.railway.app`

**Exemplo de requisição:**

```bash
curl -X POST "https://projeto-iot-fork-production.up.railway.app/api/sensor/data" \
  -H "Authorization: Bearer seu-token-aqui" \
  -H "Content-Type: application/json" \
  -d '{
    "sensorId": "T010",
    "type": "temperature",
    "value": 23.5,
    "timestamp": "2025-01-18T14:32:55Z"
  }'
```

### Simulador de Sensores

O projeto inclui um **simulador Python** (`simulator/send_data.py`) que:

- Gera dados simulados para os 4 tipos de sensores
- Envia leituras automaticamente para a API
- Utiliza timestamps em formato ISO 8601 (UTC)
- Configura autenticação via arquivo `.env`
- Permite ajustar o intervalo de envio (padrão: 5 segundos)

## Tecnologias Utilizadas

### Back-end (API)

- **Python 3.x** - Linguagem de programação
- **FastAPI 0.121.3** - Framework web moderno e de alta performance
- **Uvicorn 0.38.0** - Servidor ASGI
- **SQLAlchemy 2.0.44** - ORM para manipulação do banco de dados
- **SQLite** - Banco de dados relacional leve
- **Pydantic 2.12.4** - Validação de dados e serialização
- **python-dotenv 1.2.1** - Gerenciamento de variáveis de ambiente

### Simulador

- **Requests 2.32.5** - Cliente HTTP para envio de dados
- **Python random/datetime** - Geração de dados simulados

### Infraestrutura

- **Railway** - Hospedagem da API em produção
- **CORS** - Configurado para múltiplas origens (localhost e produção)
- **Bearer Token Authentication** - Segurança dos endpoints

## 📦 Estrutura do Projeto

```
projeto-iot-fork/
├── main.py                     # Ponto de entrada da aplicação
├── requirements.txt            # Dependências Python
├── README.md                   # Documentação do projeto
├── db/
│   ├── __init__.py
│   └── database.py            # Configuração do SQLAlchemy e engine
├── simulator/
│   └── send_data.py           # Simulador de sensores IoT
└── src/
    ├── __init__.py
    ├── index.py               # Inicialização do FastAPI e middlewares
    ├── config/
    │   └── settings.py        # Configurações (DATABASE_URL)
    ├── controllers/
    │   └── sensor_controller.py  # Lógica de negócio e operações CRUD
    ├── models/
    │   └── sensor_model.py    # Modelo SQLAlchemy (SensorData)
    └── routes/
        └── routes_model.py    # Definição de rotas e autenticação
```

## Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/isabeckmann/projeto-iot.git
cd projeto-iot
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Configure o token de autenticação:**

Crie um arquivo `.env` na raiz do projeto:

```env
AUTH_TOKEN=seu-token-secreto-aqui
```

4. **Execute a API:**

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em: `http://localhost:8000`

### Executando o Simulador

Para testar a API localmente com dados simulados:

1. **Configure o simulador** editando `simulator/send_data.py` para apontar para localhost:

```python
BASE_URL = "http://localhost:8000"
```

2. **Execute o simulador:**

```bash
python simulator/send_data.py
```

O simulador começará a enviar dados automaticamente para a API.

## 📊 Consumindo a API

### Autenticação

Todos os endpoints requerem um token Bearer no header:

```
Authorization: Bearer seu-token-aqui
```

### Exemplos de Uso

**Listar todos os dados:**

```bash
curl -X GET "http://localhost:8000/api/sensor/data" \
  -H "Authorization: Bearer seu-token-aqui"
```

**Obter últimas leituras de cada sensor:**

```bash
curl -X GET "http://localhost:8000/api/sensor/data/latest" \
  -H "Authorization: Bearer seu-token-aqui"
```

**Consultar dados de um sensor específico:**

```bash
curl -X GET "http://localhost:8000/api/sensor/data/T010" \
  -H "Authorization: Bearer seu-token-aqui"
```

## Integração com Frontend

Esta API foi projetada para ser consumida por aplicações frontend. O projeto frontend está disponível em:

[projeto-iot-front](https://github.com/isabeckmann/projeto-iot-front)

## Autores

- **Nícolas Haas Soares** - [GitHub](https://github.com/NicolauHS)
- **Isabela Beckmann** - Frontend - [GitHub](https://github.com/isabeckmann)
