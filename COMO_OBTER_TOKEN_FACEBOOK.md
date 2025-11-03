# 🔑 Como Obter o Token de Acesso do Facebook/Instagram

Para usar as funcionalidades de busca no Facebook e Instagram, você precisa de um **Access Token** do Facebook Graph API.

## 📋 Requisitos

1. ✅ Conta do Facebook
2. ✅ App criado no [Facebook for Developers](https://developers.facebook.com/)

## 🔧 Passo 1: Criar App no Facebook

1. Acesse [developers.facebook.com](https://developers.facebook.com/)
2. Clique em **"Meus Apps"** → **"Criar App"**
3. Selecione **"Nenhuma"** → **"Próximo"**
4. Preencha:
   - **Nome do App**: BotLeads (ou outro nome)
   - **Email de contato**: Seu email
5. Clique em **"Criar App"**

## 🔧 Passo 2: Obter Access Token

### Opção A: Token Temporário (Testes)

1. No dashboard do seu app, vá em **"Ferramentas"** → **"Explorador de Graph API"**
2. No canto superior direito, em **"Acesso do Token"**, clique em:
   - **"Obter Token de Acesso"** → **"Obter Token de Acesso do Usuário"**
3. Marque as permissões:
   - ✅ `pages_search`
   - ✅ `pages_read_engagement`
   - ✅ `instagram_basic`
4. Clique em **"Gerar Token de Acesso"**
5. Copie o token gerado

**⚠️ IMPORTANTE**: Este token expira em 1-2 horas!

### Opção B: Token de Longa Duração (Produção)

Para produção, você precisará:

1. **Token de Acesso do Usuário** (passo 2A)
2. **App ID** e **App Secret**:
   - Vá em **Configurações Básicas** do app
   - Copie **ID do Aplicativo** e **Chave Secreta do Aplicativo**
3. **Gerar Token de Longa Duração**:
   - Use Graph API Explorer para obter token com validade de 60 dias

```bash
# Exemplo usando curl
curl -X GET "https://graph.facebook.com/v18.0/oauth/access_token?grant_type=fb_exchange_token&client_id=SEU_APP_ID&client_secret=SEU_APP_SECRET&fb_exchange_token=TOKEN_TEMPORARIO"
```

## 🔧 Passo 3: Configurar no BotLeads

### Local (Desenvolvimento)

No arquivo `.env`:
```env
FACEBOOK_ACCESS_TOKEN=seu_token_aqui
```

### Vercel (Produção)

1. Dashboard Vercel → Seu Projeto
2. **Settings** → **Environment Variables**
3. Adicione:
   - **Key**: `FACEBOOK_ACCESS_TOKEN`
   - **Value**: seu token
   - **Environments**: Production, Preview, Development
4. Faça **Redeploy**

## ⚠️ Limitações e Restrições

### Limitações da Graph API

- **Rate Limits**: Facebook limita requisições por minuto
- **Permissões**: Algumas funcionalidades requerem revisão do Facebook
- **Dados Públicos**: Apenas dados públicos são acessíveis

### O que podemos buscar

✅ **Disponível:**
- Páginas públicas
- Nome e informações básicas
- Localização (se disponível)
- Telefone (se disponível)
- Link do perfil

❌ **Não disponível:**
- Posts privados
- Mensagens privadas
- Dados de usuários individuais
- Histórico de interações

## 🐛 Troubleshooting

### "Invalid Access Token"

**Causa**: Token expirou ou é inválido  
**Solução**: Gere um novo token

### "Insufficient Permissions"

**Causa**: Permissões insuficientes  
**Solução**: Solicite permissões `pages_search` e `instagram_basic`

### "Rate Limit Exceeded"

**Causa**: Muitas requisições  
**Solução**: Aguarde alguns minutos ou implemente delay

### Facebook não encontra resultados

**Possíveis causas**:
- Páginas não são públicas
- Nome muito específico
- Localização não está no formato correto

## 📚 Documentação Oficial

- [Facebook Graph API](https://developers.facebook.com/docs/graph-api)
- [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api)
- [Facebook Login](https://developers.facebook.com/docs/facebook-login/)

## 💡 Dica

**Para desenvolvimento/testes**: Use tokens temporários do Graph API Explorer

**Para produção**: Implemente Facebook Login OAuth para obter tokens válidos dos usuários

## ⚖️ Políticas e Termos

⚠️ **IMPORTANTE**: Certifique-se de seguir as [Políticas da Plataforma do Facebook](https://developers.facebook.com/policy/) ao usar a Graph API.

