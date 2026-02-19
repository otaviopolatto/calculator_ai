#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interface Streamlit para a Calculadora Python
Interface amigável com cores pastéis
"""

import streamlit as st
import math


# Configuração da página
st.set_page_config(
    page_title="Calculadora Python",
    page_icon="🔢",
    layout="centered",
    initial_sidebar_state="expanded"
)

# CSS personalizado com cores pastéis
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #ffeef8 0%, #e0f2fe 50%, #f0fdf4 100%);
    }
    h1, .main h1, .stApp h1, [data-testid="stMarkdownContainer"] h1 {
        color: #1f879c !important;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        text-shadow: 3px 3px 6px rgba(255, 255, 255, 0.8), 
                     -1px -1px 2px rgba(0, 0, 0, 0.3),
                     1px 1px 2px rgba(255, 255, 255, 0.6);
    }
    h2, h3, .main h2, .main h3, .stApp h2, .stApp h3, [data-testid="stMarkdownContainer"] h2, [data-testid="stMarkdownContainer"] h3 {
        color: #1f879c !important;
        text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7),
                     -1px -1px 1px rgba(0, 0, 0, 0.2),
                     1px 1px 1px rgba(255, 255, 255, 0.5);
    }
    label {
        color: #34cceb !important;
        font-weight: 500;
        text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.6),
                     -0.5px -0.5px 1px rgba(0, 0, 0, 0.2);
    }
    .stButton>button {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        color: #2d3748;
        border: none;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        background: linear-gradient(135deg, #fed6e3 0%, #a8edea 100%);
    }
    .result-box {
        background: linear-gradient(135deg, #fff5f7 0%, #f0f9ff 100%);
        padding: 2rem;
        border-radius: 20px;
        border: 2px solid #e0e7ff;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-top: 2rem;
    }
    .number-input {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)


# Título principal
st.markdown("<h1 style='color: #1f879c !important; text-align: center; font-size: 3rem; margin-bottom: 0.5rem; text-shadow: 3px 3px 6px rgba(255, 255, 255, 0.8), -1px -1px 2px rgba(0, 0, 0, 0.3), 1px 1px 2px rgba(255, 255, 255, 0.6);'>🔢 Calculadora Python</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #34cceb; font-size: 1.2rem; margin-bottom: 2rem; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>Uma calculadora completa e amigável para todas as suas necessidades matemáticas</p>", unsafe_allow_html=True)


# Sidebar para seleção de operação
st.sidebar.title("📋 Operações")
st.sidebar.markdown("---")

operacao = st.sidebar.radio(
    "Escolha uma operação:",
    [
        "➕ Adição",
        "➖ Subtração",
        "✖️ Multiplicação",
        "➗ Divisão",
        "🔺 Potenciação",
        "√ Raiz Quadrada",
        "∛ Raiz Cúbica",
        "ⁿ√ Raiz N-ésima",
        "📊 Módulo",
        "📈 Logaritmo Natural",
        "📉 Logaritmo Base 10",
        "📐 Seno",
        "📐 Cosseno",
        "📐 Tangente",
        "❗ Fatorial"
    ],
    label_visibility="visible"
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
    <div style='text-align: center; color: #64748b; font-size: 0.9rem;'>
        <p>💡 Dica: Use a calculadora para realizar cálculos matemáticos complexos!</p>
    </div>
""", unsafe_allow_html=True)


# Container principal
container = st.container()

with container:
    resultado = None
    expressao = ""
    
    # Adição
    if operacao == "➕ Adição":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>➕ Adição</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Primeiro número", value=0.0, step=0.1, key="add1")
        with col2:
            num2 = st.number_input("Segundo número", value=0.0, step=0.1, key="add2")
        
        if st.button("Calcular", key="btn_add"):
            resultado = num1 + num2
            expressao = f"{num1} + {num2}"
    
    # Subtração
    elif operacao == "➖ Subtração":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>➖ Subtração</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Minuendo", value=0.0, step=0.1, key="sub1")
        with col2:
            num2 = st.number_input("Subtraendo", value=0.0, step=0.1, key="sub2")
        
        if st.button("Calcular", key="btn_sub"):
            resultado = num1 - num2
            expressao = f"{num1} - {num2}"
    
    # Multiplicação
    elif operacao == "✖️ Multiplicação":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>✖️ Multiplicação</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Primeiro número", value=0.0, step=0.1, key="mult1")
        with col2:
            num2 = st.number_input("Segundo número", value=0.0, step=0.1, key="mult2")
        
        if st.button("Calcular", key="btn_mult"):
            resultado = num1 * num2
            expressao = f"{num1} × {num2}"
    
    # Divisão
    elif operacao == "➗ Divisão":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>➗ Divisão</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Dividendo", value=0.0, step=0.1, key="div1")
        with col2:
            num2 = st.number_input("Divisor", value=0.0, step=0.1, key="div2")
        
        if st.button("Calcular", key="btn_div"):
            if num2 == 0:
                st.error("❌ Erro: Divisão por zero não é permitida!")
            else:
                resultado = num1 / num2
                expressao = f"{num1} ÷ {num2}"
    
    # Potenciação
    elif operacao == "🔺 Potenciação":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>🔺 Potenciação</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base", value=0.0, step=0.1, key="pot_base")
        with col2:
            expoente = st.number_input("Expoente", value=0.0, step=0.1, key="pot_exp")
        
        if st.button("Calcular", key="btn_pot"):
            resultado = base ** expoente
            expressao = f"{base} ^ {expoente}"
    
    # Raiz Quadrada
    elif operacao == "√ Raiz Quadrada":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>√ Raiz Quadrada</h2>", unsafe_allow_html=True)
        numero = st.number_input("Número", value=0.0, min_value=0.0, step=0.1, key="sqrt")
        
        if st.button("Calcular", key="btn_sqrt"):
            if numero < 0:
                st.error("❌ Erro: Não é possível calcular raiz quadrada de número negativo!")
            else:
                resultado = math.sqrt(numero)
                expressao = f"√{numero}"
    
    # Raiz Cúbica
    elif operacao == "∛ Raiz Cúbica":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>∛ Raiz Cúbica</h2>", unsafe_allow_html=True)
        numero = st.number_input("Número", value=0.0, step=0.1, key="cbrt")
        
        if st.button("Calcular", key="btn_cbrt"):
            resultado = numero ** (1/3)
            expressao = f"∛{numero}"
    
    # Raiz N-ésima
    elif operacao == "ⁿ√ Raiz N-ésima":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>ⁿ√ Raiz N-ésima</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            numero = st.number_input("Número", value=0.0, step=0.1, key="nroot_num")
        with col2:
            indice = st.number_input("Índice da raiz", value=2.0, min_value=0.1, step=0.1, key="nroot_idx")
        
        if st.button("Calcular", key="btn_nroot"):
            if indice <= 0:
                st.error("❌ Erro: O índice deve ser positivo!")
            else:
                resultado = numero ** (1/indice)
                expressao = f"{int(indice) if indice.is_integer() else indice}√{numero}"
    
    # Módulo
    elif operacao == "📊 Módulo":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>📊 Módulo (Resto da Divisão)</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Primeiro número", value=0.0, step=0.1, key="mod1")
        with col2:
            num2 = st.number_input("Segundo número", value=0.0, step=0.1, key="mod2")
        
        if st.button("Calcular", key="btn_mod"):
            if num2 == 0:
                st.error("❌ Erro: Divisão por zero não é permitida!")
            else:
                resultado = num1 % num2
                expressao = f"{num1} % {num2}"
    
    # Logaritmo Natural
    elif operacao == "📈 Logaritmo Natural":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>📈 Logaritmo Natural (ln)</h2>", unsafe_allow_html=True)
        numero = st.number_input("Número", value=1.0, min_value=0.0001, step=0.1, key="ln")
        
        if st.button("Calcular", key="btn_ln"):
            if numero <= 0:
                st.error("❌ Erro: O número deve ser positivo!")
            else:
                resultado = math.log(numero)
                expressao = f"ln({numero})"
    
    # Logaritmo Base 10
    elif operacao == "📉 Logaritmo Base 10":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>📉 Logaritmo na Base 10 (log)</h2>", unsafe_allow_html=True)
        numero = st.number_input("Número", value=1.0, min_value=0.0001, step=0.1, key="log10")
        
        if st.button("Calcular", key="btn_log10"):
            if numero <= 0:
                st.error("❌ Erro: O número deve ser positivo!")
            else:
                resultado = math.log10(numero)
                expressao = f"log({numero})"
    
    # Seno
    elif operacao == "📐 Seno":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>📐 Seno</h2>", unsafe_allow_html=True)
        st.info("ℹ️ Nota: O ângulo deve ser em radianos. Para converter graus em radianos: radianos = graus × π / 180")
        angulo = st.number_input("Ângulo (em radianos)", value=0.0, step=0.1, key="sin")
        
        if st.button("Calcular", key="btn_sin"):
            resultado = math.sin(angulo)
            expressao = f"sin({angulo})"
    
    # Cosseno
    elif operacao == "📐 Cosseno":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>📐 Cosseno</h2>", unsafe_allow_html=True)
        st.info("ℹ️ Nota: O ângulo deve ser em radianos. Para converter graus em radianos: radianos = graus × π / 180")
        angulo = st.number_input("Ângulo (em radianos)", value=0.0, step=0.1, key="cos")
        
        if st.button("Calcular", key="btn_cos"):
            resultado = math.cos(angulo)
            expressao = f"cos({angulo})"
    
    # Tangente
    elif operacao == "📐 Tangente":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>📐 Tangente</h2>", unsafe_allow_html=True)
        st.info("ℹ️ Nota: O ângulo deve ser em radianos. Para converter graus em radianos: radianos = graus × π / 180")
        angulo = st.number_input("Ângulo (em radianos)", value=0.0, step=0.1, key="tan")
        
        if st.button("Calcular", key="btn_tan"):
            resultado = math.tan(angulo)
            expressao = f"tan({angulo})"
    
    # Fatorial
    elif operacao == "❗ Fatorial":
        st.markdown("<h2 style='color: #1f879c !important; text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7), -1px -1px 1px rgba(0, 0, 0, 0.2), 1px 1px 1px rgba(255, 255, 255, 0.5);'>❗ Fatorial</h2>", unsafe_allow_html=True)
        numero = st.number_input("Número inteiro não negativo", value=0, min_value=0, max_value=170, step=1, key="fact")
        
        if st.button("Calcular", key="btn_fact"):
            if numero < 0 or not numero.is_integer():
                st.error("❌ Erro: O número deve ser um inteiro não negativo!")
            else:
                resultado = math.factorial(int(numero))
                expressao = f"{int(numero)}!"
    
    # Exibir resultado
    if resultado is not None:
        st.markdown("---")
        st.markdown(f"""
            <div class="result-box">
                <h2 style='text-align: center; color: #6b73ff; margin-bottom: 1rem;'>Resultado</h2>
                <p style='text-align: center; font-size: 1.5rem; color: #2d3748; margin-bottom: 0.5rem;'>{expressao}</p>
                <h1 style='text-align: center; color: #10b981; font-size: 3rem; margin-top: 1rem;'>= {resultado}</h1>
            </div>
        """, unsafe_allow_html=True)


# Rodapé
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #64748b; padding: 2rem 0;'>
        <p>✨ Calculadora Python - Desenvolvida com ❤️ usando Streamlit</p>
    </div>
""", unsafe_allow_html=True)
