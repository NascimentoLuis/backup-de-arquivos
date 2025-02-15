# Backup Automático com Python

Este é um script Python que permite fazer backup de arquivos e pastas de forma simples e automatizada. O usuário pode definir a pasta de origem e destino diretamente pelo terminal.

##  Funcionalidades

- Copiar arquivos e subpastas automaticamente.
- Criar backups organizados por data e hora.
- Exibe mensagens de erro e sucesso.

---

##  Requisitos

Antes de executar o script, verifique se você tem o **Python 3** instalado. Se não tiver, faça o download [aqui](https://www.python.org/downloads/).

##  Instalação

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seu-usuario/backup-automatico.git
   ```

2. **Entre na pasta do projeto:**

   ```bash
   cd backup-automatico
   ```

3. **(Opcional) Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   ```

   **Ative o ambiente:**

   - No Windows: `venv\Scripts\activate`
   - No Mac/Linux: `source venv/bin/activate`

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

---

##  Como Executar

1. **Execute o script**:
   ```bash
   python backup.py
   ```
2. **Passos para utilizar:**
   - O script solicitará a **pasta de origem**.
   - O script solicitará a **pasta de destino**.
   - O backup será iniciado automaticamente.

📡 Os arquivos serão copiados automaticamente para a pasta escolhida, organizados com a data e hora do backup.

---

##  Melhorias Futuras

- Adicionar opção para compactar arquivos em `.zip`.
- Criar uma versão com interface gráfica.
- Agendar backups automáticos em determinado horário.
- Integração com armazenamento em nuvem (Google Drive, Dropbox, etc.).

Se gostou do projeto, deixe um ⭐ no repositório e contribua com melhorias!

---

 **Desenvolvido por **[**Luís Nascimento**](https://github.com/NascimentoLuis)

