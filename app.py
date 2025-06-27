import streamlit as st
from datetime import date

st.set_page_config(page_title="Controle de Parcelas de Carros", layout="centered")

st.markdown("🚗 **Controle de Parcelas de Carros**")

# ============================
# Função para salvar pagamento
# ============================
def registrar_pagamento(carro_key, valor, data):
    if carro_key not in st.session_state:
        st.session_state[carro_key] = []
    st.session_state[carro_key].append((data.strftime("%d/%m/%Y"), f"€ {valor:.2f}"))

# ======================
# CARRO 1 - Semanal
# ======================
st.header("Carro 1 - Pagamento semanal")

carro1_nome = st.text_input("Nome do carro 1", "Fiat Uno")
valor_total1 = st.number_input("Valor total (€)", min_value=0.0, step=100.0, key="total1")
valor_pago1 = st.number_input("Valor já pago (€)", min_value=0.0, step=50.0, key="pago1")
data_pagamento1 = st.date_input("Data do último pagamento", value=date.today(), key="data1")

if st.button("Salvar pagamento do carro 1"):
    registrar_pagamento("historico1", valor_pago1, data_pagamento1)
    st.success("Pagamento salvo com sucesso!")

falta_pagar1 = valor_total1 - valor_pago1
st.success(f"Falta pagar: € {falta_pagar1:.2f}")

# Mostrar histórico de pagamentos do carro 1
if "historico1" in st.session_state:
    st.subheader("📋 Histórico de Pagamentos - Carro 1")
    for data, valor in st.session_state["historico1"]:
        st.text(f"{data} — {valor}")

# ======================
# CARRO 2 - Mensal
# ======================
st.header("Carro 2 - Pagamento mensal")

carro2_nome = st.text_input("Nome do carro 2", "Opel Corsa")
valor_total2 = st.number_input("Valor total (€) do segundo carro", min_value=0.0, step=100.0, key="total2")
valor_pago2 = st.number_input("Valor já pago (€) do segundo carro", min_value=0.0, step=50.0, key="pago2")
data_pagamento2 = st.date_input("Data do último pagamento", value=date.today(), key="data2")

if st.button("Salvar pagamento do carro 2"):
    registrar_pagamento("historico2", valor_pago2, data_pagamento2)
    st.success("Pagamento salvo com sucesso!")

falta_pagar2 = valor_total2 - valor_pago2
st.success(f"Falta pagar: € {falta_pagar2:.2f}")

# Mostrar histórico de pagamentos do carro 2
if "historico2" in st.session_state:
    st.subheader("📋 Histórico de Pagamentos - Carro 2")
    for data, valor in st.session_state["historico2"]:
        st.text(f"{data} — {valor}")
