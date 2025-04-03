import streamlit as st
import pandas as pd

def calcular_ganhos(odd_time1, odd_time2, valor_total):
    aposta_time1 = valor_total / (odd_time1 + odd_time2) * odd_time2
    aposta_time2 = valor_total / (odd_time1 + odd_time2) * odd_time1
    ganho_time1 = aposta_time1 * odd_time1
    ganho_time2 = aposta_time2 * odd_time2
    lucro_time1 = ganho_time1 - valor_total
    lucro_time2 = ganho_time2 - valor_total
    percentual_time1 = (lucro_time1 / valor_total) * 100
    percentual_time2 = (lucro_time2 / valor_total) * 100

    return {
        "Time": ["Time 1", "Time 2"],
        "Aposta (R$)": [aposta_time1, aposta_time2],
        "Ganho Potencial (R$)": [ganho_time1, ganho_time2],
        "Lucro (R$)": [lucro_time1, lucro_time2],
        "% do Valor Total": [percentual_time1, percentual_time2]
    }

def calcular_aposta_lucro_odd_menor(odd_time1, odd_time2, valor_total):
    if odd_time1 < odd_time2:
        aposta_time1 = valor_total - (valor_total / odd_time2)
        aposta_time2 = valor_total / odd_time2
    else:
        aposta_time2 = valor_total - (valor_total / odd_time1)
        aposta_time1 = valor_total / odd_time1

    ganho_time1 = aposta_time1 * odd_time1
    ganho_time2 = aposta_time2 * odd_time2
    lucro_time1 = ganho_time1 - valor_total
    lucro_time2 = ganho_time2 - valor_total
    percentual_time1 = (lucro_time1 / valor_total) * 100
    percentual_time2 = (lucro_time2 / valor_total) * 100

    return {
        "Time": ["Time 1", "Time 2"],
        "Aposta (R$)": [aposta_time1, aposta_time2],
        "Ganho Potencial (R$)": [ganho_time1, ganho_time2],
        "Lucro (R$)": [lucro_time1, lucro_time2],
        "% do Valor Total": [percentual_time1, percentual_time2]
    }

def calcular_aposta_lucro_odd_maior(odd_time1, odd_time2, valor_total):
    if odd_time1 > odd_time2:
        aposta_time1 = valor_total - (valor_total / odd_time2)
        aposta_time2 = valor_total / odd_time2
    else:
        aposta_time2 = valor_total - (valor_total / odd_time1)
        aposta_time1 = valor_total / odd_time1

    ganho_time1 = aposta_time1 * odd_time1
    ganho_time2 = aposta_time2 * odd_time2
    lucro_time1 = ganho_time1 - valor_total
    lucro_time2 = ganho_time2 - valor_total
    percentual_time1 = (lucro_time1 / valor_total) * 100
    percentual_time2 = (lucro_time2 / valor_total) * 100

    return {
        "Time": ["Time 1", "Time 2"],
        "Aposta (R$)": [aposta_time1, aposta_time2],
        "Ganho Potencial (R$)": [ganho_time1, ganho_time2],
        "Lucro (R$)": [lucro_time1, lucro_time2],
        "% do Valor Total": [percentual_time1, percentual_time2]
    }

st.title("Calculadora de Apostas com Odds")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    odds_time1 = st.number_input("Odd do Time 1", min_value=1.01, value=2.0, step=0.01)
with col2:
    odds_time2 = st.number_input("Odd do Time 2", min_value=1.01, value=2.0, step=0.01)
with col3:
    valor_total = st.number_input("Valor total a ser apostado (R$)", min_value=1.0, value=100.0, step=1.0)

calcular = st.button("Calcular")

if calcular:
    resultados = calcular_ganhos(odds_time1, odds_time2, valor_total)
    df_resultados = pd.DataFrame(resultados)
    st.subheader("Tabela Padrão de Ganhos")
    st.table(df_resultados)

    resultados_ajustados_menor = calcular_aposta_lucro_odd_menor(odds_time1, odds_time2, valor_total)
    df_resultados_ajustados_menor = pd.DataFrame(resultados_ajustados_menor)
    st.subheader("Tabela Ajustada (Lucro Total no Time de Odd Menor)")
    st.table(df_resultados_ajustados_menor)

    resultados_ajustados_maior = calcular_aposta_lucro_odd_maior(odds_time1, odds_time2, valor_total)
    df_resultados_ajustados_maior = pd.DataFrame(resultados_ajustados_maior)
    st.subheader("Tabela Ajustada (Lucro Total no Time de Odd Maior)")
    st.table(df_resultados_ajustados_maior)

st.markdown("---")
st.markdown("<p style='font-size: 12px; text-align: center;'>📌 Créditos: <b>Assuero Ximenes</b></p>", unsafe_allow_html=True)






