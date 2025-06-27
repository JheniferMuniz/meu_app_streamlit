import streamlit as st

st.set_page_config(page_title="Controle de Parcelas", page_icon="🚗")

st.title("🚗 Controle de Parcelas de Carros")

# Carro 1 - Pagamento semanal
st.header("Carro 1 - Pagamento semanal")
nome1 = st.text_input("Nome do carro 1", "Fiat Uno")
valor_total1 = st.number_input("Valor total (€)", min_value=0.0)
valor_pago1 = st.number_input("Valor já pago (€)", min_value=0.0)
restante1 = valor_total1 - valor_pago1
st.success(f"Falta pagar: € {restante1:.2f}")

# Carro 2 - Pagamento mensal
st.header("Carro 2 - Pagamento mensal")
nome2 = st.text_input("Nome do carro 2", "Opel Corsa")
valor_total2 = st.number_input("Valor total (€) do segundo carro", min_value=0.0)
valor_pago2 = st.number_input("Valor já pago (€)", min_value=0.0, key="carro2")
restante2 = valor_total2 - valor_pago2
st.success(f"Falta pagar: € {restante2:.2f}")
import streamlit as st
from datetime import date

st.title("🚗 Controle de Parcelas de Carros")

st.header("Carro 1 - Pagamento semanal")

# Entrada normal
carro1_nome = st.text_input("Nome do carro 1", "Fiat Uno")
carro1_valor_total = st.number_input("Valor total (€)", min_value=0.0, step=0.01, key="valor_total1")
carro1_valor_pago = st.number_input("Valor já pago (€)", min_value=0.0, step=0.01, key="valor_pago1")
st.success(f"Falta pagar: € {carro1_valor_total - carro1_valor_pago:.2f}")

st.subheader("Registrar parcelas já pagas")

# Data e valor da parcela paga
nova_data = st.date_input("📅 Data do pagamento", value=date.today())
novo_valor = st.number_input("💰 Valor pago nesta data", min_value=0.0, step=0.01)

# Lista de pagamentos
if "pagamentos" not in st.session_state:
    st.session_state["pagamentos"] = []

if st.button("Registrar Pagamento"):
    st.session_state["pagamentos"].append((str(nova_data), novo_valor))
    st.success("Pagamento registrado!")

# Mostrar lista de pagamentos
if st.session_state["pagamentos"]:
    st.markdown("### 🔹 Pagamentos feitos:")
    for data, valor in st.session_state["pagamentos"]:
        st.write(f"• {data} - €{valor:.2f}")
