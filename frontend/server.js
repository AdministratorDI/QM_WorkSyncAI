const express = require('express');
const path = require('path');
const history = require('connect-history-api-fallback');

const app = express();
const port = 3000;

// Permite fallback para index.html em rotas como /login ou /dashboard
app.use(history());

// Serve os ficheiros estáticos do build da aplicação Vite
app.use(express.static(path.join(__dirname, 'dist')));

// Fallback para index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

// Inicia o servidor
app.listen(port, () => {
  console.log(`Servidor de produção ativo: http://localhost:${port}`);
});