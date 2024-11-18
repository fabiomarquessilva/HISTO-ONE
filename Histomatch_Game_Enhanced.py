
import streamlit as st
import random

# Configuração inicial do aplicativo
st.set_page_config(page_title="Histomatch: Explore o Microcosmo", layout="wide")

# Cabeçalho do jogo
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Histomatch: Explore o Microcosmo</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FF5722;'>Teste seus conhecimentos em Histologia!</h3>", unsafe_allow_html=True)

# Introdução do jogo
st.write("Bem-vindo ao Histomatch! Responda às perguntas abaixo e veja o quanto você sabe sobre tecidos e células.")

# Lista de perguntas
questions = [
    {"question": "Qual tecido possui células cilíndricas com microvilosidades e é encontrado no intestino?",
     "options": ["Tecido Epitelial de Revestimento", "Tecido Conjuntivo", "Tecido Muscular", "Tecido Nervoso", "Tecido Adiposo"],
     "answer": "Tecido Epitelial de Revestimento"},
    {"question": "Qual corante é utilizado para evidenciar fibras colágenas?",
     "options": ["Hematoxilina", "Eosina", "Tricrômico de Masson", "Azul de Toluidina", "Fucsina ácida"],
     "answer": "Tricrômico de Masson"},
    {"question": "Qual tecido armazena lipídeos e fornece isolamento térmico?",
     "options": ["Tecido Muscular", "Tecido Adiposo", "Tecido Nervoso", "Tecido Conjuntivo Denso", "Tecido Cartilaginoso"],
     "answer": "Tecido Adiposo"},
    {"question": "Qual estrutura do tecido epitelial aumenta a absorção no intestino?",
     "options": ["Microvilosidades", "Cílios", "Junções Oclusivas", "Desmossomos", "Placas de adesão"],
     "answer": "Microvilosidades"},
    {"question": "Qual tecido conecta músculos aos ossos?",
     "options": ["Tecido Conjuntivo Denso", "Tecido Adiposo", "Tecido Epitelial", "Tecido Nervoso", "Tecido Cartilaginoso"],
     "answer": "Tecido Conjuntivo Denso"}
]

# Variável para armazenar pontuação
score = 0

# Variável para armazenar respostas dos usuários
user_answers = {}

# Embaralhamento inicial das opções
shuffled_options = {}
for i, q in enumerate(questions):
    options = q["options"].copy()
    random.shuffle(options)
    shuffled_options[i] = options

# Exibição das perguntas
for i, q in enumerate(questions):
    st.markdown(f"<h4 style='color: #2196F3;'>Pergunta {i+1}: {q['question']}</h4>", unsafe_allow_html=True)
    user_answers[i] = st.radio("", shuffled_options[i], key=i)

# Botão para finalizar o jogo
if st.button("Finalizar Jogo"):
    # Cálculo da pontuação
    for i, q in enumerate(questions):
        selected_answer = user_answers[i]
        correct_answer = q["answer"]
        if selected_answer == correct_answer:
            score += 1

    # Exibição da pontuação final
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Resultado Final</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: #FF9800;'>Você acertou {score}/{len(questions)} perguntas!</h2>", unsafe_allow_html=True)

    # Feedback com base na pontuação
    if score == len(questions):
        st.balloons()
        st.markdown("<h4 style='text-align: center; color: #4CAF50;'>Parabéns! Você acertou tudo!</h4>", unsafe_allow_html=True)
    elif score > len(questions) // 2:
        st.markdown("<h4 style='text-align: center; color: #FFEB3B;'>Bom trabalho! Continue estudando!</h4>", unsafe_allow_html=True)
    else:
        st.markdown("<h4 style='text-align: center; color: #F44336;'>Não desista! Pratique mais e tente novamente!</h4>", unsafe_allow_html=True)
