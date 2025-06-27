import streamlit as st
from datetime import date

st.set_page_config(page_title="Controle de Parcelas de Carros", page_icon="🚗", layout="centered")

st.markdown("# 🚗 Controle de Parcelas de Carros")

# -------------------------
# Carro 1 - Pagamento semanal
# -------------------------
st.header("Carro 1 - Pagamento semanal")

carro1_nome = st.text_input("Nome do carro 1", "Fiat Uno", key="carro1_nome")
carro1_valor_total = st.number_input("Valor total (€)", min_value=0.0, step=0.01, key="valor_total1")
carro1_valor_pago = st.number_input("Valor já pago (€)", min_value=0.0, step=0.01, key="valor_pago1")
carro1_data_pagamento = st.date_input("Data do último pagamento", value=date.today(), key="data_pagamento1")

carro1_falta = carro1_valor_total - carro1_valor_pago
st.success(f"Falta pagar: € {carro1_falta:.2f}")
st.info(f"Último pagamento registrado: {carro1_data_pagamento.strftime('%d/%m/%Y')}")

st.markdown("---")

# -------------------------
# Carro 2 - Pagamento mensal
# -------------------------
st.header("Carro 2 - Pagamento mensal")

carro2_nome = st.text_input("Nome do carro 2", "Opel Corsa", key="carro2_nome")
carro2_valor_total = st.number_input("Valor total (€) do segundo carro", min_value=0.0, step=0.01, key="valor_total2")
carro2_valor_pago = st.number_input("Valor já pago (€) do segundo carro", min_value=0.0, step=0.01, key="valor_pago2")
carro2_data_pagamento = st.date_input("Data do último pagamento", value=date.today(), key="data_pagamento2")

carro2_falta = carro2_valor_total - carro2_valor_pago
st.success(f"Falta pagar: € {carro2_falta:.2f}")
st.info(f"Último pagamento registrado: {carro2_data_pagamento.strftime('%d/%m/%Y')}")

st.markdown("---")
