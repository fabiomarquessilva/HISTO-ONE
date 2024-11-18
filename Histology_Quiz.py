
import streamlit as st

# Configuração inicial do aplicativo
st.set_page_config(page_title="Quiz de Histologia: Tecidos Fundamentais", layout="wide")

# Título do jogo
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Quiz de Histologia: Tecidos Fundamentais</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FF5722;'>Teste seus conhecimentos sobre os tecidos epitelial, conjuntivo, muscular e nervoso!</h3>", unsafe_allow_html=True)

# Introdução
st.write("Bem-vindo ao Quiz de Histologia! Escolha a alternativa correta para cada pergunta e clique em **Finalizar** ao final para ver seu desempenho.")

# Lista de perguntas sobre os tecidos fundamentais
questions = [
    {"question": "Qual é a principal característica do tecido epitelial?",
     "options": ["a) Alta vascularização", "b) Produção de impulsos elétricos", "c) Contração voluntária", "d) Presença de matriz extracelular abundante", "e) Células justapostas e pouca matriz extracelular"],
     "answer": "e) Células justapostas e pouca matriz extracelular"},
    {"question": "Qual tipo de tecido conjuntivo é responsável pelo armazenamento de gordura?",
     "options": ["a) Tecido Cartilaginoso", "b) Tecido Adiposo", "c) Tecido Muscular", "d) Tecido Nervoso", "e) Tecido Epitelial"],
     "answer": "b) Tecido Adiposo"},
    {"question": "Qual tecido é especializado na contração para produzir movimento?",
     "options": ["a) Tecido Epitelial", "b) Tecido Conjuntivo", "c) Tecido Muscular", "d) Tecido Nervoso", "e) Tecido Adiposo"],
     "answer": "c) Tecido Muscular"},
    {"question": "Qual é a função principal do tecido nervoso?",
     "options": ["a) Sustentação mecânica", "b) Condução de impulsos elétricos", "c) Armazenamento de energia", "d) Transporte de nutrientes", "e) Produção de colágeno"],
     "answer": "b) Condução de impulsos elétricos"},
    {"question": "Qual tipo de tecido epitelial reveste os alvéolos pulmonares?",
     "options": ["a) Epitélio Simples Pavimentoso", "b) Epitélio Cilíndrico", "c) Epitélio Estratificado Cuboide", "d) Epitélio de Transição", "e) Epitélio Simples Cuboide"],
     "answer": "a) Epitélio Simples Pavimentoso"}
]

# Variáveis para armazenar pontuação e respostas do usuário
score = 0
correct_answers = 0
wrong_answers = 0
user_answers = {}

# Exibição das perguntas
for i, q in enumerate(questions):
    st.markdown(f"<h4 style='color: #2196F3;'>Pergunta {i+1}: {q['question']}</h4>", unsafe_allow_html=True)
    user_answers[i] = st.radio("", q["options"], key=i)

# Botão para finalizar o quiz
if st.button("Finalizar Quiz"):
    # Verificar respostas
    for i, q in enumerate(questions):
        selected_answer = user_answers[i]
        if selected_answer == q["answer"]:
            correct_answers += 1
        else:
            wrong_answers += 1

    # Exibir resultado final
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Resultado Final</h3>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center; color: #4CAF50;'>Respostas Corretas: {correct_answers}</h4>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center; color: #F44336;'>Respostas Erradas: {wrong_answers}</h4>", unsafe_allow_html=True)

    # Feedback com base no desempenho
    if correct_answers == len(questions):
        st.balloons()
        st.markdown("<h4 style='text-align: center; color: #4CAF50;'>Excelente! Você acertou todas as perguntas!</h4>", unsafe_allow_html=True)
    elif correct_answers > len(questions) // 2:
        st.markdown("<h4 style='text-align: center; color: #FFEB3B;'>Bom trabalho! Continue praticando para melhorar ainda mais.</h4>", unsafe_allow_html=True)
    else:
        st.markdown("<h4 style='text-align: center; color: #F44336;'>Não desista! Revise os conceitos e tente novamente.</h4>", unsafe_allow_html=True)