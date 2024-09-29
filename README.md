# Dashboard de Incêndios Florestais no Brasil

Este é um projeto de dashboard interativo desenvolvido com [Streamlit](https://streamlit.io/), que visualiza dados sobre incêndios florestais no Brasil. O usuário pode carregar um arquivo Excel contendo informações sobre o estado, data e número de incêndios, e então interagir com filtros para visualizar os dados de forma dinâmica.

## Funcionalidades

- **Carregamento de Arquivo**: Permite que o usuário faça upload de um arquivo Excel contendo dados de incêndios.
- **Filtros Dinâmicos**:
  - Filtro por Estado.
  - Filtro de Período (com um controle deslizante para selecionar a data).
- **Métricas e Gráficos**:
  - Exibe o maior número de queimadas e a data do maior pico de incêndios.
  - Gráfico de linha mostrando a evolução dos incêndios ao longo do tempo.
  - Exibição dos dados processados em uma tabela interativa.

## Pré-requisitos

Antes de começar, você precisará ter instalado o Python 3.7+ e as bibliotecas necessárias listadas abaixo:

### Bibliotecas Python

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

Você pode instalar todas as dependências usando o arquivo `requirements.txt` fornecido:

```bash
pip install -r requirements.txt
```

## Execução do Dashboard 
```bash
streamlit run app.py
```

