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
