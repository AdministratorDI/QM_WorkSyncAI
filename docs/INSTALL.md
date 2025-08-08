# WorkSync AI — Guia de Instalação

Este documento fornece instruções passo-a-passo para configurar o ambiente de desenvolvimento da plataforma WorkSync AI.

---

## 🧰 Requisitos

- Python 3.10+
- Node.js 18+
- PostgreSQL
- Docker e Docker Compose (opcional, recomendado)
- Git

---

## 📁 Estrutura do Projeto

```
worksync_ai/
├── backend/
│   ├── app/
│   ├── alembic/
│   ├── alembic.ini
│   └── ...
├── frontend/
│   ├── public/
│   ├── src/
│   └── ...
├── docs/
│   └── INSTALL.md
└── README.md
```

---

## 🚀 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/worksync_ai.git
cd worksync_ai
```

---

### 2. Configurar o Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> Crie um ficheiro `.env` com as variáveis de ambiente necessárias (ver `.env.example`).

Inicializar base de dados (com Alembic):

```bash
alembic upgrade head
```

Executar o servidor:

```bash
uvicorn app.main:app --reload
```

---

### 3. Configurar o Frontend

```bash
cd ../frontend
npm install
npm run dev
```

---

## 🔗 Endpoints

- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`

---

## 🐳 Docker (opcional)

```bash
docker-compose up --build
```

---

## ✅ Verificar

- Aceder ao `http://localhost:5173` e testar a interface.
- Verificar a API: `http://localhost:8000/docs`

---

## 📌 Notas

- Certifica-te que o PostgreSQL está em execução.
- Para produção, será necessário configurar variáveis de ambiente e deploy na AWS.

---
