# 🌐 Projeto IoT — Coleta, Armazenamento e Visualização de Dados de Sensores

Este repositório contém o desenvolvimento completo de um sistema distribuído para **coleta**, **armazenamento** e **visualização** de dados provenientes de sensores IoT simulados, disponibilizados pelo Professor Eldair Fabrício Dornelles.  
O projeto foi desenvolvido como parte de uma atividade avaliativa cujo objetivo é implementar:

- Uma **API REST** responsável por receber e armazenar leituras de sensores.
- Uma **aplicação web (dashboard)** capaz de consumir e exibir essas informações de forma interativa, você pode acessar o repositório referente ao front-end <a href="https://github.com/isabeckmann/projeto-iot-front">clicando aqui</a>

---

## 📌 Visão Geral da Atividade Avaliativa

A atividade propõe a criação de um sistema distribuído que demonstre conceitos como:

- Comunicação entre serviços  
- Integração de componentes  
- Persistência de dados  
- Exposição de informações por meio de APIs REST  

Durante a execução, um simulador em formato `.jar` envia leituras periódicas de sensores IoT para o endpoint:
`http://localhost:8080/api/sensor/data`

Cada leitura possui o seguinte formato JSON:

```json
{ 
  "sensorId": "T010",
  "type": "temperature",
  "value": 23.5,
  "timestamp": "2025-01-18T14:32:55Z"
}
```
As leituras representam quatro tipos de sensores:
- Temperatura
- Umidade
- Luminosidade
- Movimento

## 🚀 Funcionalidades Implementadas
<b>1. API REST</b>

A API foi desenvolvida para:
- Receber dados enviados pelo simulador via HTTP
- Processar JSONs recebidos
- Armazenar as leituras em um banco SQLite
- Fornecer endpoints para consulta pelas aplicações cliente

A API está hospedada na nuvem e pode ser acessada em:

🔗 <a href="https://projeto-iot-fork-production.up.railway.app/api/sensor/data">https://projeto-iot-fork-production.up.railway.app/api/sensor/data</a>

<b>2. Dashboard Web</b>

A aplicação web:
- Consome os dados diretamente da API
- Lista todas as leituras
- Exibe gráficos e visualizações resumidas (últimas leituras, evolução temporal etc.)
- Funciona como interface principal para acompanhamento dos sensores

## 🛠️ Tecnologias Utilizadas
<b>Back-end (API)</b> </br>
- Python 
- Banco de dados SQLite

<b>Front-end (Dashboard)</b> </br>
- React
  
<b>Infraestrutura</b> </br>
- Hospedagem da API em Railway
- Banco SQLite acessado pela API
