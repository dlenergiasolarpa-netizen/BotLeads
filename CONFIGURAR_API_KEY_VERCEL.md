# 🔑 Como Configurar a API Key na Vercel

## Problema

Após o deploy funcionar, aparece o erro:
```
Erro ao buscar leads: API Key do Google Maps não encontrada. 
Configure GOOGLE_MAPS_API_KEY no .env ou passe como parâmetro.
```

## ✅ Solução: Configurar Variável de Ambiente

### Passo 1: Acessar Configurações

1. Acesse [vercel.com/dashboard](https://vercel.com/dashboard)
2. Clique no seu projeto **BotLeads**
3. Vá em **Settings** (Configurações)
4. Clique em **Environment Variables** (Variáveis de Ambiente)

### Passo 2: Adicionar a Variável

1. Clique no botão **"Add"** ou **"Add New"**
2. Preencha os campos:
   - **Key (Chave)**: `GOOGLE_MAPS_API_KEY`
   - **Value (Valor)**: Cole sua chave da API do Google Maps
   - **Environment (Ambiente)**: 
     - ✅ Marque **Production**
     - ✅ Marque **Preview** 
     - ✅ Marque **Development**
3. Clique em **Save** (Salvar)

### Passo 3: Fazer Redeploy

**IMPORTANTE**: Após adicionar a variável, você precisa fazer redeploy!

**Opção A - Via Dashboard (Mais Fácil):**
1. Vá em **Deployments** (Implantações)
2. Clique nos **três pontinhos** (...) do último deploy
3. Selecione **Redeploy**
4. Aguarde o processo terminar

**Opção B - Via Push para GitHub:**
Se você tiver integração automática:
```bash
git commit --allow-empty -m "Trigger redeploy"
git push
```

**Opção C - Via Vercel CLI:**
```bash
vercel --prod
```

## 🔍 Verificar se Funcionou

1. Aguarde o redeploy terminar
2. Acesse sua URL no Vercel
3. Tente fazer uma busca de leads
4. Deve funcionar sem erros!

## 📍 Onde Obter a API Key?

Se você ainda não tem a chave da API:

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um projeto ou selecione existente
3. Habilite a **Places API**:
   - Vá em **APIs & Services** → **Library**
   - Procure por "Places API"
   - Clique em **Enable**
4. Crie a chave:
   - Vá em **APIs & Services** → **Credentials**
   - Clique em **Create Credentials** → **API Key**
   - Copie a chave gerada
5. Configure restrições (recomendado):
   - Clique na chave criada
   - Em **API restrictions**, selecione **Restrict key**
   - Marque apenas **Places API**
   - Salve

## 🔒 Segurança

**IMPORTANTE**: Nunca compartilhe sua API Key publicamente!

- ✅ A chave está segura no Vercel
- ✅ Não versionamos o arquivo `.env` no Git
- ✅ Configure restrições na chave no Google Cloud

## 🆘 Ainda com Problemas?

### Verificar se a variável foi salva

No Vercel Dashboard:
1. **Settings** → **Environment Variables**
2. Deve aparecer `GOOGLE_MAPS_API_KEY`

### Verificar se fez redeploy

1. Vá em **Deployments**
2. O último deploy deve ser **DEPOIS** de adicionar a variável
3. Se não foi, faça um redeploy manual

### Ver logs de erro

1. **Deployments** → Selecione o deploy
2. Clique em **Functions** → Ver logs
3. Procure por mensagens de erro

### Testar localmente primeiro

Se estiver com dúvidas se a chave funciona:

1. Crie arquivo `.env` na raiz do projeto:
   ```
   GOOGLE_MAPS_API_KEY=sua_chave_aqui
   ```
2. Teste localmente:
   ```bash
   python app.py
   ```
3. Se funcionar localmente, a chave está correta!

## ✨ Pronto!

Depois de configurar a API Key na Vercel e fazer redeploy, seu BotLeads estará funcionando perfeitamente! 🚀

