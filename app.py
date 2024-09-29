import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Exibe o logo da empresa no topo do dashboard
    # st.logo("figs/acc_logo.png")

    # Exibe o título principal do dashboard
    st.title("Incêndios Florestais no Brasil")

    # Cria um uploader de arquivo na barra lateral para carregar arquivos Excel
    # file = st.sidebar.file_uploader("Carregue seu arquivo:")
    file = "data/brazilFire.xlsx"
    # Se um arquivo for carregado, ele será lido como um DataFrame do pandas
    if file is not None:
        df_file = pd.read_excel(file)

        # Converte a coluna "data" para o formato datetime para facilitar o filtro por datas
        df_file["data"] = df_file["data"].apply(lambda x: pd.to_datetime(x))

        # Filtro de Estado - Cria um dropdown na barra lateral com os estados únicos
        state = st.sidebar.selectbox("Estado", df_file["estado"].unique(), None)

        # Se o usuário selecionar um estado, filtra o DataFrame por esse estado
        if state is not None:
            df_new = df_file[df_file["estado"] == state]
        else:
            # Caso contrário, usa todos os dados
            df_new = df_file

        # Filtro de Período - Cria um slider para selecionar o intervalo de datas
        min_date = df_new["data"].min()
        max_date = df_new["data"].max()

        # Configura o slider com o período mínimo e máximo do dataset
        period = st.slider(
            "Período",
            value=(
                min_date.to_pydatetime(),
                max_date.to_pydatetime(),
            ),  # Define o valor inicial do slider
            format="DD/MM/YY",  # Formato da data exibido
            min_value=min_date.to_pydatetime(),  # Data mínima do slider
            max_value=max_date.to_pydatetime(),  # Data máxima do slider
        )

        # Filtra os dados com base no período selecionado pelo usuário
        if period is not None:
            df_new = df_new[
                (df_new["data"] >= period[0]) & (df_new["data"] <= period[1])
            ]

        # Agrupamento dos dados por ano, mês e data, somando o total de incêndios
        group = ["ano", "mes", "data"]
        df_viz = df_new.groupby(group, as_index=False).agg({"total_incendios": sum})

        # Encontra o maior número de incêndios em um único dia
        max_fires = max(df_viz["total_incendios"])

        # Determina o ano e mês em que ocorreu o maior número de incêndios
        max_fires_year = df_viz[df_viz["total_incendios"] == max_fires]["ano"].values[0]
        max_fires_month = df_viz[df_viz["total_incendios"] == max_fires]["mes"].values[
            0
        ]

        # Criação de métricas para exibição no dashboard
        w1, w2 = st.columns(2)  # Cria duas colunas para exibir métricas lado a lado

        # Exibe a data com o maior pico de queimadas
        w1.metric(
            label="Data com maior pico de queimadas",
            value=f"{max_fires_month} - {max_fires_year}",
        )

        # Exibe o maior número de queimadas registrado
        w2.metric(label="Maior número de queimadas", value=f"{max_fires:,.0f}")

        # Cria um gráfico de linha com os dados de incêndios por data usando o Streamlit
        st.line_chart(df_viz, x="data", y="total_incendios")

        # Exibe os dados agrupados em formato de tabela interativa
        st.dataframe(df_viz, use_container_width=True)


# O código só será executado se o script for rodado diretamente, e não importado como módulo
if __name__ == "__main__":
    main()
