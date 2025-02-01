# 🤖 Diobot - Chatbot com OpenAI e Flask

Este repositório contém o **Diobot**, um chatbot inteligente desenvolvido com **Python (Flask)** no backend e integrado com a **API da OpenAI**. O frontend está hospedado na **Vercel**, enquanto o backend roda na **Render**.
---
Demo Live:


![ezgif-12a164f3c73b0](https://github.com/user-attachments/assets/e191a166-0c64-47bf-9e57-e9da867a798c)


---
## 🚀 Tecnologias Utilizadas

- **Backend:** Python, Flask, Flask-CORS  
- **Frontend:** HTML, CSS, JavaScript (com TailwindCSS)  
- **APIs:** OpenAI 
- **Hospedagem:** Render (backend) e Vercel (frontend)  

## ⚙️ Instalação Local

### 1. Clone o repositório
```bash
git clone https://github.com/Diogobitten/chatbot.git
cd chatbot
```

### 2. Crie um ambiente virtual e ative
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Crie um arquivo `.env` com:
```bash
OPENAI_API_KEY=sua-chave-api-da-openai
ASSISTANT_ID=seu-assistant-id
```

### 5. Execute o servidor Flask
```bash
python app.py
```
O servidor estará rodando em `http://127.0.0.1:5000`.

---

## 🌍 Deploy

### 🔗 **Frontend (Vercel)**
1. Conecte o repositório na Vercel.  
2. Configure o `API_URL` no frontend para apontar para o backend da Render:
   ```javascript
   const API_URL = "https://seu-backend-render.onrender.com/chat";
   ```
3. Faça o deploy.

### ☁️ **Backend (Render)**
1. Conecte o repositório no Render.  
2. Configure as variáveis de ambiente:
   - `OPENAI_API_KEY`
   - `ASSISTANT_ID`
3. Faça o deploy.

---

## 💬 Funcionalidades

- 🔍 **Responde perguntas sobre o Diogo** (formação, projetos, experiências).  
- 🌦️ **Consulta o clima atual** usando a API do OpenWeatherMap.  
- 💱 **Exibe taxas de câmbio** (USD/BRL e EUR/BRL).  
- 🤖 **Integração com a OpenAI** para respostas personalizadas.  

## 🛠️ Contribuindo

1. **Fork** este repositório.  
2. Crie uma branch:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Faça suas alterações e commit:
   ```bash
   git commit -m "Adiciona nova funcionalidade"
   ```
4. Envie para o seu fork:
   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. Abra um **Pull Request**.

---

## 📄 Licença

Este projeto é de uso pessoal de [Diogo Bittencourt](https://www.linkedin.com/in/diogo-bittencourt-de-oliveira/).

---

Feito por **Diogo Bittencourt**
