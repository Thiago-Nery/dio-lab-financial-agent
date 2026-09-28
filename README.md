# 🎓 Edu - Agente Educador Financeiro com IA Generativa

Uma experiência digital inovadora de relacionamento e educação financeira voltada para investidores iniciantes, guiada por inteligência artificial generativa e pautada em boas práticas de User Experience (UX).

---

## 📌 Visão Geral do Projeto

Este projeto integra compreensão de linguagem natural, análise contextualizada de dados de clientes e interface conversacional amigável. A solução atua como um assistente inteligente (o **Edu**) focado em descomplicar conceitos financeiros e orientar pessoas que estão iniciando sua jornada de investimentos.

### 🎯 Objetivos Principais
- **Educação Financeira para Iniciantes:** Desmistificar o "economês" (CDI, Selic, Liquidez, Renda Fixa vs. Variável) através de analogias simples e explicações graduais.
- **Contextualização com Dados do Cliente:** Personalizar os exemplos com base no perfil do investidor (ex: João Silva, perfil moderado), seu patrimônio, suas metas financeiras (Reserva de Emergência e Entrada do Apartamento) e extrato de transações.
- **Interação Segura e Pedagógica:** Atuar estritamente no escopo educativo, sem fazer recomendações diretas de compra ou venda de ativos, priorizando a autonomia e o aprendizado do cliente.
- **UX e Transparência:** Proporcionar interações claras, acolhedoras e diretas por meio de uma interface conversacional acessível desenvolvida em Streamlit.

---

## 📁 Estrutura do Projeto

```text
.
├── app.py                       # Aplicação em Streamlit e integração com LLM local
├── README.md                    # Documentação detalhada do projeto
└── data/
    ├── perfil_investidor.json    # Perfil do cliente, patrimônio e metas (ex: João Silva)
    ├── transacoes.csv           # Extrato de receitas e despesas recentes do cliente
    ├── historico_atendimento.csv # Histórico de interações e dúvidas anteriores no banco
    └── produtos_financeiros.json # Catálogo de produtos financeiros (Tesouro Selic, CDB, LCI/LCA, FIIs, etc.)
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** (Linguagem base)
- **Streamlit** (Interface gráfica interativa)
- **Ollama / LLM Local** (Motor de Inteligência Artificial Generativa para execução do modelo `gpt-oss`)
- **Pandas & JSON** (Manipulação e estruturação de dados)
- **Requests** (Comunicação via API com o LLM)

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o **Python** e o **Ollama** instalados no seu ambiente.

### 2. Configuração do Ollama
No terminal, baixe e inicie o modelo de linguagem:

```bash
# 1. Baixar o modelo utilizado no projeto
ollama pull gpt-oss

# 2. Testar o modelo no terminal
ollama run gpt-oss "Olá!"

# 3. Garantir que o serviço do Ollama esteja em execução
ollama serve
```

### 3. Instalação de Dependências do Python
Instale os pacotes necessários:

```bash
pip install streamlit pandas requests
```

### 4. Executando a Aplicação
Com o Ollama rodando em segundo plano, inicie o app em Streamlit:

```bash
streamlit run app.py
```

Acesse a interface no navegador através do endereço exibido no terminal (geralmente `http://localhost:8501`).

---

## 💡 Funcionalidades do Agente Edu

1. **FAQs Inteligentes e Explicação de Produtos:**
   - Explicações didáticas sobre Tesouro Selic, CDB Liquidez Diária, LCI/LCA, Fundo Imobiliário e Fundos de Ações.
2. **Orientação para Reserva de Emergência:**
   - Apoio no entendimento e construção do primeiro pilar de segurança antes da migração para renda variável.
3. **Respostas Personalizadas:**
   - Referencia diretamente o momento atual do cliente (ex: meta de R$ 15.000 para a reserva de emergência).
4. **Validação de Aprendizado:**
   - Checagem ao final de cada resposta para verificar se o cliente compreendeu o conceito explicado.

---

## 🔒 Diretrizes de Segurança e Privacidade

- **Sem Recomendações Indevidas:** O agente ensina o funcionamento e características dos produtos, mas jamais indica compras ou vendas de ativos.
- **Processamento 100% Local:** Processamento via Ollama garante a privacidade dos dados financeiros do cliente.
- **Ancoragem nos Dados:** O modelo atua fundamentado exclusivamente no contexto do cliente e nas diretrizes do prompt.
