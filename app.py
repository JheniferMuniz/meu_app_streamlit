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
# CARRO 1 - TESLA (semanal)
# ======================
carro1_nome = "TESLA"

st.header(f"{carro1_nome} - Pagamento semanal")

valor_total1 = st.number_input("Valor total do TESLA (€)", min_value=0.0, step=100.0, key="total1")
valor_pago1 = st.number_input("Valor já pago (€)", min_value=0.0, step=50.0, key="pago1")
data_pagamento1 = st.date_input("Data do último pagamento do TESLA", value=date.today(), key="data1")

if st.button("Salvar pagamento do TESLA"):
    registrar_pagamento("historico1", valor_pago1, data_pagamento1)
    st.success("Pagamento salvo com sucesso!")

falta_pagar1 = valor_total1 - valor_pago1
st.success(f"Falta pagar: € {falta_pagar1:.2f}")

# Mostrar histórico de pagamentos do carro 1
if "historico1" in st.session_state:
    st.subheader(f"📋 Histórico de Pagamentos - {carro1_nome}")
    for data, valor in st.session_state["historico1"]:
        st.text(f"{data} — {valor}")

st.markdown("---")

# ======================
# CARRO 2 - PEUGEOT 508 (mensal)
# ======================
carro2_nome = "PEUGEOT 508"

st.header(f"{carro2_nome} - Pagamento mensal")

valor_total2 = st.number_input("Valor total do PEUGEOT (€)", min_value=0.0, step=100.0, key="total2")
valor_pago2 = st.number_input("Valor já pago (€)", min_value=0.0, step=50.0, key="pago2")
data_pagamento2 = st.date_input("Data do último pagamento do PEUGEOT", value=date.today(), key="data2")

if st.button("Salvar pagamento do PEUGEOT"):
    registrar_pagamento("historico2", valor_pago2, data_pagamento2)
    st.success("Pagamento salvo com sucesso!")

falta_pagar2 = valor_total2 - valor_pago2
st.success(f"Falta pagar: € {falta_pagar2:.2f}")

# Mostrar histórico de pagamentos do carro 2
if "historico2" in st.session_state:
    st.subheader(f"📋 Histórico de Pagamentos - {carro2_nome}")
    for data, valor in st.session_state["historico2"]:
        st.text(f"{data} — {valor}")
