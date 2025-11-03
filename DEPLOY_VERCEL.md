# 🚀 Como Fazer Deploy do BotLeads na Vercel

Este guia te ajudará a fazer deploy da aplicação BotLeads na Vercel de forma simples e rápida.

## 📋 Pré-requisitos

1. ✅ Conta na Vercel (grátis): [vercel.com](https://vercel.com)
2. ✅ Código no GitHub (repositório público ou privado)
3. ✅ Google Maps API Key configurada

## 🔧 Passo 1: Preparar o Projeto

O projeto já está configurado com os arquivos necessários:
- ✅ `vercel.json` - Configuração do build
- ✅ `app.py` - Aplicação Flask
- ✅ `requirements.txt` - Dependências Python

## 📤 Passo 2: Enviar para o GitHub

Se ainda não enviou o código para o GitHub:

```bash
# Adicionar remote do GitHub
git remote add origin https://github.com/SEU_USUARIO/BotLeads.git

# Enviar código
git push -u origin master
```

## 🌐 Passo 3: Fazer Deploy na Vercel

### Opção A: Via Dashboard Web (Mais Fácil) ⭐

1. **Acesse**: [vercel.com/dashboard](https://vercel.com/dashboard)
2. **Clique** em "Add New" → "Project"
3. **Conecte seu GitHub** (se ainda não conectou)
4. **Selecione o repositório** `BotLeads`
5. **Configure o projeto**:
   - Framework Preset: **Other**
   - Root Directory: **./** (raiz do projeto)
   - Build Command: Deixe vazio (Flask detecta automaticamente)
   - Output Directory: Deixe vazio
6. **Configure Environment Variables**:
   ```
   GOOGLE_MAPS_API_KEY = sua_chave_aqui
   ```
7. **Clique** em "Deploy"

### Opção B: Via Vercel CLI (Linha de Comando)

1. **Instale o Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Login na Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Configure a variável de ambiente**:
   ```bash
   vercel env add GOOGLE_MAPS_API_KEY
   # Cole sua chave quando solicitado
   ```

5. **Deploy de produção**:
   ```bash
   vercel --prod
   ```

## 🔐 Passo 4: Configurar Variáveis de Ambiente

Na Vercel, você precisa adicionar sua Google Maps API Key:

1. Vá em **Settings** → **Environment Variables**
2. Adicione:
   - **Name**: `GOOGLE_MAPS_API_KEY`
   - **Value**: sua chave da API
   - **Environment**: Production, Preview, Development (marque todos)
3. Salve e faça **redeploy** se necessário

**Como fazer redeploy**: Dashboard → Seu Projeto → Deployments → "..." (três pontinhos) → Redeploy

## ✅ Passo 5: Testar

Após o deploy, você receberá uma URL como:
```
https://botleads.vercel.app
```

Teste:
- ✅ Página principal carrega
- ✅ Formulário aparece
- ✅ Busca de leads funciona
- ✅ Resultados são exibidos

## 🔍 Troubleshooting

### Erro: "Module not found"

**Solução**: Verifique se todas as dependências estão no `requirements.txt`

```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Atualiza requirements.txt"
git push
```

### Erro: "GOOGLE_MAPS_API_KEY not found"

**Solução**: Configure a variável de ambiente na Vercel:
1. Settings → Environment Variables
2. Adicione `GOOGLE_MAPS_API_KEY` com sua chave
3. Faça redeploy

### Erro: "Build failed"

**Solução**: Verifique logs no dashboard da Vercel:
1. Acesse o deployment que falhou
2. Clique em "Build Logs"
3. Verifique o erro específico

**Problemas comuns**:
- Sintaxe no código Python
- Dependência incompatível com Python 3.11
- Arquivo faltando no `.gitignore`

### Deploy funciona mas a busca não retorna resultados

**Solução**: 
1. Verifique se a API Key está correta
2. Confirme que a Places API está habilitada no Google Cloud
3. Verifique os logs da Vercel: Settings → Functions → View Logs

### Página aparece em branco

**Solução**: Verifique se os arquivos estáticos estão no repositório
```bash
git ls-files static/ templates/
```

### CORS Error

**Solução**: O projeto já tem Flask-CORS configurado. Se houver erros:
```python
# Em app.py
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

## 📊 Monitoramento

### Logs em Tempo Real

Na Vercel Dashboard:
- **Deployments** → Selecione o deploy → **Functions** → Ver logs

Via CLI:
```bash
vercel logs
```

### Métricas

No dashboard, você pode ver:
- ⚡ Performance
- 📈 Tráfego
- 💾 Uso de memória
- 🌐 Requisições

## 🔄 Atualizando o Deploy

Sempre que fizer alterações:

```bash
# Fazer commit
git add .
git commit -m "Sua mensagem"
git push

# A Vercel automaticamente faz redeploy!
```

## 💰 Custos

**Vercel Hobby Plan (Grátis)** inclui:
- ✅ Deploys ilimitados
- ✅ SSL automático
- ✅ Domínio `.vercel.app` grátis
- ✅ 100GB bandwidth/mês
- ✅ Funções Serverless

**Limites importantes**:
- ⚠️ Timeout de função: 10s (Hobby) ou 60s (Pro)
- ⚠️ Memória: 1GB (Hobby) ou 3GB (Pro)
- ⚠️ Requests: 100GB/mês

Para este projeto, o plano gratuito é suficiente!

## 🌐 Domínio Customizado

Para adicionar seu próprio domínio:

1. Vá em **Settings** → **Domains**
2. Adicione seu domínio
3. Configure DNS conforme instruções
4. SSL é ativado automaticamente

## 🎯 Configurações Avançadas

### Headers Personalizados

Adicione em `vercel.json`:
```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        }
      ]
    }
  ]
}
```

### Redirecionamentos

```json
{
  "redirects": [
    {
      "source": "/home",
      "destination": "/",
      "permanent": true
    }
  ]
}
```

## 📱 Mobile-First

Sua aplicação já está totalmente responsiva! Teste em:
- 📱 iPhone/iPad
- 🤖 Android
- 💻 Desktop

## 🔗 Links Úteis

- [Vercel Docs](https://vercel.com/docs)
- [Flask no Vercel](https://vercel.com/docs/python)
- [Google Maps API](https://console.cloud.google.com/apis)

## ✨ Conclusão

Agora você tem o BotLeads rodando na Vercel com:
- ✅ Deploy automático
- ✅ HTTPS gratuito
- ✅ CDN global
- ✅ Interface responsiva
- ✅ Serverless functions

**Pronto para usar!** 🎉

