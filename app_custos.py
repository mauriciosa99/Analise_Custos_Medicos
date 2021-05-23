import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.linear_model import LinearRegression

# função para carregar o dataset
@st.cache
def get_data():
    return pd.read_csv(r"C:\Users\mauri\Portfolio\Analise_custos_medicos\data_deploy.csv")

# função para treinar o modelo
def train_model():
    df = get_data()
    x = df.drop("charges",axis=1)
    y = df["charges"]
    lin_reg = LinearRegression()
    lin_reg.fit(x, y)
    return lin_reg

# criando um dataframe
df = get_data()

# treinando o modelo
model = train_model()

# título
st.title("Data App - Prevendo Custos de Planos Médicos")

# subtítulo
st.markdown("Este é um site utilizado para exibir a solução de Machine Learning para o problema de predição de valores de planos médicos com base em algumas informações.")

# verificando o dataset
st.subheader("Selecionando apenas um pequeno conjunto de atributos")

# atributos para serem exibidos por padrão
defaultcols = ["age","sex","children","charges"]

# defindo atributos a partir do multiselect
cols = st.multiselect( "Atributos", df.columns.tolist(), default=defaultcols)

# exibindo os top 10 registro do dataframe
st.dataframe(df[cols].head(10))


#titulo do mapeamento dos dados
st.sidebar.subheader("Defina os atributos do imóvel para predição")

# mapeando dados do usuário para cada atributo
AGE = st.sidebar.number_input("Idade", value=df.age.mean())
IMC = st.sidebar.number_input("IMC do paciente", value=df.bmi.mean())
SEXO = st.sidebar.selectbox("Sexo",("Masculino","Feminino"))
FUMANTE = st.sidebar.selectbox("Pessoa Fumante?",("Sim","Não"))
REG_southwest = st.sidebar.selectbox("Região Sudeste?",("Sim","Não"))
REG_southeast = st.sidebar.selectbox("Região Sudoeste?",("Sim","Não"))
REG_northwest = st.sidebar.selectbox("Região Noroeste?",("Sim","Não"))
REG_northeast = st.sidebar.selectbox("Região Nordeste?",("Sim","Não"))
# transformando o dado de entrada em valor binário
SEXO = 1 if SEXO == "Feminino" else 0
FUMANTE = 1 if FUMANTE == "Sim" else 0
REG_southwest = 1 if REG_southwest == "Sim" else 0
REG_southeast = 1 if REG_southeast == "Sim" else 0
REG_northwest = 1 if REG_northwest == "Sim" else 0
REG_northeast = 1 if REG_northeast == "Sim" else 0

DEPENDENTES = st.sidebar.number_input("Número de dependentes", value=df.children.mean())

# inserindo um botão na tela
btn_predict = st.sidebar.button("Realizar Predição")

# verifica se o botão foi acionado
if btn_predict:
    result = model.predict([[AGE,SEXO,IMC,FUMANTE,REG_northeast,REG_northwest,REG_southeast,REG_southwest,DEPENDENTES]])
    st.subheader("O valor previsto para o plano é US $:")
    #result = "US $ "+str(round(result[0]*10,2))
    st.write(result)