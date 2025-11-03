# Como Conectar o BotLeads ao GitHub

## Passo 1: Criar repositório no GitHub

1. Acesse [github.com](https://github.com) e faça login
2. Clique no botão **"+"** no canto superior direito e selecione **"New repository"**
3. Configure o repositório:
   - **Repository name**: `BotLeads` (ou o nome que preferir)
   - **Description**: "Sistema de busca de leads no Google Maps com interface responsiva"
   - **Visibility**: Escolha Public ou Private
   - **NÃO marque** a opção "Initialize this repository with a README" (já temos arquivos)
4. Clique em **"Create repository"**

## Passo 2: Conectar repositório local ao GitHub

Após criar o repositório no GitHub, você receberá uma URL como:
- HTTPS: `https://github.com/SEU_USUARIO/BotLeads.git`
- SSH: `git@github.com:SEU_USUARIO/BotLeads.git`

Execute os seguintes comandos no terminal (na pasta do projeto):

```bash
# Adicionar o repositório remoto (substitua pela sua URL)
git remote add origin https://github.com/SEU_USUARIO/BotLeads.git

# Verificar se foi adicionado corretamente
git remote -v

# Fazer push do código para o GitHub
git push -u origin master
```

**Nota**: Se estiver usando o GitHub recentemente, use `main` em vez de `master`:

```bash
git branch -M main
git push -u origin main
```

## Passo 3: Configurar Git (se necessário)

Se você ainda não configurou seu nome e email no Git:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

## Passo 4: Autenticação

Dependendo da configuração do GitHub, você pode precisar:

### Opção A: Personal Access Token (PAT)
1. Vá em GitHub > Settings > Developer settings > Personal access tokens > Tokens (classic)
2. Gere um novo token com permissões de `repo`
3. Use o token como senha quando solicitado no `git push`

### Opção B: GitHub CLI
Instale o GitHub CLI:
- Windows: Use winget ou baixe de [github.com/cli/cli](https://github.com/cli/cli)

```bash
winget install GitHub.cli
```

Depois autentique:
```bash
gh auth login
```

### Opção C: SSH Keys
Configure chaves SSH se preferir autenticação mais segura:
1. Gere uma chave SSH: `ssh-keygen -t ed25519 -C "seu-email@exemplo.com"`
2. Adicione a chave pública ao GitHub em Settings > SSH and GPG keys

## Próximos Passos

Depois de conectar ao GitHub, você pode:

```bash
# Ver status do repositório
git status

# Adicionar arquivos modificados
git add .

# Fazer commit das alterações
git commit -m "Descrição das alterações"

# Enviar para o GitHub
git push

# Baixar atualizações do GitHub
git pull
```

## Branch Principal

O GitHub agora usa `main` como branch padrão. Se você criou o repositório com `master`:

```bash
# Renomear branch local
git branch -M main

# Fazer push para main
git push -u origin main
```

## Estatísticas do Projeto

O repositório inclui:
- ✅ Interface web responsiva (Flask)
- ✅ Interface gráfica desktop (Tkinter)
- ✅ Logo personalizado
- ✅ Paleta de cores BotLeads
- ✅ Suporte completo a dispositivos móveis
- ✅ Integração com Google Maps Places API
- ✅ Exportação para Excel
- ✅ Autocomplete de estados, municípios e bairros (IBGE)

