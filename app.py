import json
import pandas as pd
import requests
import streamlit as st

### ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

### ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

### ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO PRINCIPAL: {perfil['objetivo_principal']}
PATRIMÔNIO TOTAL: R$ {perfil['patrimonio_total']} | RESERVA ATUAL: R$ {perfil['reserva_emergencia_atual']}
ACEITA RISCO: {perfil['aceita_risco']}

METAS DO CLIENTE:
{json.dumps(perfil['metas'], indent=2, ensure_ascii=False)}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS NO BANCO:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

### ============ SYSTEM PROMPT REFINADO PARA INICIANTES ============
SYSTEM_PROMPT = """Você é o Edu, um educador financeiro amigável, paciente e altamente didático, especializado em ajudar iniciantes a entenderem o mundo dos investimentos.

OBJETIVO PRINCIPAL:
Desmistificar os investimentos e ensinar conceitos financeiros de forma simples, acessível e prática, ajudando o cliente iniciante a tomar decisões conscientes baseadas no seu perfil e momento de vida.

DIRETRIZES DE ATUAÇÃO E LINGUAGEM:
1. Didática para Iniciantes: Explique conceitos técnicos (como Selic, CDI, Liquidez, Renda Fixa vs. Renda Variável) usando analogias do dia a dia e linguagem clara, sem "economês".
2. Foco em Passos Graduais: Incentive a consolidação da Reserva de Emergência como primeiro passo indispensável antes de partir para investimentos de maior risco.
3. Exemplos Personalizados: Utilize os dados reais do cliente (patrimônio, reserva, metas e transações) para ilustrar as explicações de maneira prática e próxima da realidade dele.
4. NUNCA Recomende Ativos Diretos: Explique o funcionamento, riscos, prazos e vantagens/desvantagens de cada produto financeiro disponível, mas JAMAIS diga "compre X" ou faça recomendações diretas de investimento.
5. Escopo Estrito: Se o cliente perguntar sobre assuntos fora do universo de finanças, investimentos e educação financeira, decline educadamente e retome o seu papel de educador financeiro.
6. Checagem de Aprendizado: Finalize sempre verificando se a explicação ficou clara ou se o cliente tem alguma dúvida específica sobre os termos explicados.
7. Formatação e Extensão: Mantenha as respostas diretas, estruturadas e concisas (no máximo 3 parágrafos ou tópicos curtos).
"""

### ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta do Cliente: {msg}"""

    try:
        r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
        return r.json().get('response', 'Erro ao obter resposta do modelo.')
    except Exception as e:
        return f"Erro na conexão com o serviço de IA: {str(e)}"

### ============ INTERFACE STREAMLIT ============
st.set_page_config(page_title="Edu - Educador Financeiro", page_icon="🎓")

st.title("🎓 Edu, seu Educador Financeiro")
st.caption("Aprenda a investir e organize suas finanças de forma simples e descomplicada.")

if pergunta := st.chat_input("Sua dúvida sobre investimentos ou finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Edu está pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
