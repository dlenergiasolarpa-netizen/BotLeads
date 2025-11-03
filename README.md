# BotLeads - Busca de Leads Multiplataforma 🤖

Sistema para buscar leads de estabelecimentos comerciais em Google Maps, Facebook e Instagram baseado em parâmetros geográficos.

## 🎨 Design

- ✨ Interface moderna e responsiva
- 📱 Totalmente otimizado para dispositivos móveis
- 🎨 Paleta de cores customizada
- 🤖 Logo personalizado BotLeads

## Funcionalidades

- 🗺️ **Busca em Múltiplas Fontes**:
  - Google Maps (obrigatório)
  - Facebook (opcional)
  - Instagram (opcional)

- 📍 **Parâmetros de Busca**:
  - Estado
  - Município
  - Bairro
  - Raio de busca (em metros)
  - Tipo de estabelecimento (mercado, loja de roupa, etc.)

- 📊 **Informações Retornadas**:
  - Nome do estabelecimento
  - Endereço completo
  - Telefone de contato
  - Link do perfil na rede social
  - Localização GPS
  - Fonte do lead (Google/Facebook/Instagram)

## Requisitos

- Python 3.7+
- Conta Google Cloud com Places API habilitada
- Chave de API do Google Maps (obrigatória)
- Facebook Access Token (opcional, para buscar no Facebook/Instagram)

## Instalação

### Pré-requisito: Instalar Python

Se o Python não estiver instalado no seu sistema:

**Opção 1: Via Site Oficial (Recomendado)**
1. Acesse: https://www.python.org/downloads/
2. Baixe a versão mais recente (Python 3.11 ou 3.12)
3. Execute o instalador
4. **IMPORTANTE**: Marque a opção "Add Python to PATH" durante a instalação
5. Reinicie o PowerShell após a instalação

**Opção 2: Via Microsoft Store**
1. Abra a Microsoft Store
2. Procure por "Python 3.11" ou "Python 3.12"
3. Clique em "Instalar"
4. Reinicie o PowerShell após a instalação

**Verificar instalação:**
```powershell
python --version
```

### Instalar Dependências do Projeto

1. Navegue até o diretório do projeto:
```powershell
cd C:\Users\junin\Desktop\BotLeads
```

2. **Opção A - Script Automático (Recomendado):**
```powershell
.\instalar_dependencias.ps1
```

2. **Opção B - Instalação Manual:**
```powershell
pip install -r requirements.txt
```

Se o comando `pip` não funcionar, tente:
```powershell
python -m pip install -r requirements.txt
```

3. Configure a API Key:
   - Copie o arquivo `.env.example` para `.env`
   - Abra o arquivo `.env` e cole sua chave da API do Google Maps:
   ```
   GOOGLE_MAPS_API_KEY=sua_chave_aqui
   ```

## Como obter a API Key

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Habilite a **Places API** no seu projeto
4. Vá em **APIs e Serviços > Credenciais**
5. Crie uma **Chave de API** (API Key)
6. Copie a chave e cole no arquivo `.env`

## Uso

### Versão Web (Recomendado) 🌐

A versão web oferece uma interface moderna, responsiva e profissional.

1. **Instale as dependências atualizadas** (se ainda não instalou Flask):
```bash
pip install -r requirements.txt
```

2. **Execute a aplicação web**:
```bash
python app.py
```

3. **Acesse no navegador**:
```
http://localhost:5000
```

A interface web inclui:
- ✨ Design moderno e totalmente responsivo
- 📱 Layout adaptável para mobile, tablet e desktop
- 🔍 Busca em tempo real com autocomplete
- 🌐 Busca em múltiplas plataformas (Google Maps, Facebook, Instagram)
- 📊 Visualização organizada dos resultados com indicador de fonte
- 🗺️ Links diretos para Google Maps
- 📞 Links para ligação direta
- 🔗 Links para perfis nas redes sociais
- 📥 Exportação para Excel dos resultados
- 🎨 Paleta de cores BotLeads (Verde, Azul Ciano, Cinza Escuro)

### Interface Gráfica (Desktop)

Execute a interface gráfica desktop:
```bash
python interface.py
```

Uma janela será aberta com um formulário onde você pode preencher:
- Estado
- Município
- Bairro
- Raio da busca (em metros)
- Tipo de estabelecimento a buscar

Após preencher, clique em "Buscar Leads" e os resultados aparecerão na área de resultados.

### Linha de Comando

Alternativamente, você pode usar a versão em linha de comando:
```bash
python main.py
```

O sistema irá solicitar os seguintes parâmetros:
- Estado
- Município
- Bairro
- Raio da busca (em metros)
- Tipo de estabelecimento a buscar

## Exemplo

**Versão Web:**
1. Execute `python app.py`
2. Acesse `http://localhost:5000` no navegador
3. Preencha o formulário:
   - Estado: São Paulo
   - Município: São Paulo
   - Bairro: Centro
   - Raio: 1000
   - Tipo: mercado
4. Clique em "Buscar Leads"
5. Veja os resultados na interface web

**Interface Gráfica Desktop:**
1. Execute `python interface.py`
2. Preencha o formulário com os mesmos dados acima
3. Clique em "Buscar Leads"
4. Veja os resultados na área de texto

**Linha de Comando:**
```
Estado: São Paulo
Município: São Paulo
Bairro: Centro
Raio: 1000
Tipo: mercado
```

## Estrutura do Projeto

```
BotLeads/
├── google_maps_searcher.py  # Buscador Google Maps
├── facebook_searcher.py     # Buscador Facebook
├── instagram_searcher.py    # Buscador Instagram
├── app.py                   # Aplicação Flask (versão web)
├── interface.py             # Interface gráfica desktop (GUI)
├── main.py                  # Script linha de comando
├── requirements.txt         # Dependências do projeto
├── vercel.json              # Configuração para deploy na Vercel
├── templates/               # Templates HTML
│   └── index.html          # Página principal web
├── static/                  # Arquivos estáticos
│   ├── css/
│   │   └── style.css       # Estilos CSS
│   ├── js/
│   │   ├── main.js         # JavaScript principal
│   │   └── autocomplete.js # Autocomplete IBGE
│   └── img/
│       └── BotLeadsLogo.png # Logo
├── instalar_dependencias.ps1 # Script de instalação automática
├── env.example              # Exemplo de configuração
├── .env                     # Arquivo de configuração (não versionado)
├── .gitignore              # Arquivos ignorados pelo git
├── INSTALACAO.md           # Guia detalhado de instalação
├── CONECTAR_GITHUB.md      # Guia para conectar ao GitHub
├── DEPLOY_VERCEL.md        # Guia para deploy na Vercel
├── COMO_OBTER_TOKEN_FACEBOOK.md # Como obter token Facebook/Instagram
└── README.md               # Este arquivo
```

## Observações

- No momento, o sistema apenas busca e exibe os resultados
- Os leads não são salvos em banco de dados (implementação futura)
- Certifique-se de que sua API Key tenha créditos suficientes
- A Places API tem limites de uso conforme seu plano

## Troubleshooting

**Erro: "pip não é reconhecido" ou "Python não encontrado"**
- Certifique-se de que o Python está instalado (veja seção Instalação)
- Após instalar, reinicie o PowerShell/Terminal
- Tente usar `python -m pip` em vez de apenas `pip`
- Verifique se o Python foi adicionado ao PATH do sistema

**Erro: "API Key não encontrada"**
- Verifique se o arquivo `.env` existe na raiz do projeto
- Confirme que a variável está escrita corretamente: `GOOGLE_MAPS_API_KEY`
- Certifique-se de que copiou `env.example` para `.env` (com o ponto no início)

**Erro: "Places API not enabled"**
- Habilite a Places API no Google Cloud Console

**Erro: "Facebook Access Token não encontrado"**
- Facebook/Instagram são opcionais
- Se quiser usar, consulte `COMO_OBTER_TOKEN_FACEBOOK.md`
- Configure `FACEBOOK_ACCESS_TOKEN` no `.env`

**Nenhum resultado encontrado**
- Verifique se o endereço está correto
- Tente aumentar o raio de busca
- Confirme que o tipo de busca está bem escrito
- Verifique se selecionou pelo menos uma fonte de busca

**Dúvidas sobre instalação?**
- Consulte o arquivo `INSTALACAO.md` para um guia mais detalhado

## 📦 GitHub

Este projeto está versionado com Git. Para conectar ao GitHub e fazer push do código:

1. Consulte o arquivo `CONECTAR_GITHUB.md` para instruções detalhadas
2. Crie um repositório no GitHub
3. Conecte o repositório local ao remoto
4. Faça push do código

**Comandos rápidos:**
```bash
# Ver status do repositório
git status

# Adicionar mudanças
git add .

# Fazer commit
git commit -m "Sua mensagem aqui"

# Enviar para GitHub
git push
```

## 🚀 Deploy na Vercel

Para fazer deploy em produção na Vercel:

1. Consulte o arquivo `DEPLOY_VERCEL.md` para instruções detalhadas
2. Conecte seu repositório GitHub à Vercel
3. Configure a variável de ambiente `GOOGLE_MAPS_API_KEY`
4. Deploy automático!

**Setup rápido:**
- Acesse [vercel.com](https://vercel.com)
- Importar repositório do GitHub
- Configure `GOOGLE_MAPS_API_KEY` nas Environment Variables
- Deploy!

**Vantagens do deploy na Vercel:**
- ✅ HTTPS automático
- ✅ CDN global
- ✅ Deploy automático a cada push
- ✅ Domínio `.vercel.app` grátis
- ✅ Interface responsiva funcionando perfeitamente

## Observações
