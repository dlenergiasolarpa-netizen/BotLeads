# 🚀 Guia Rápido BotLeads

## 📌 Uso Básico (Google Maps)

1. **Execute o app**:
   ```bash
   python app.py
   ```

2. **Acesse**: `http://localhost:5000`

3. **Preencha**:
   - Estado: Ex: "São Paulo"
   - Município: Ex: "São Paulo"
   - Bairro: (opcional)
   - Tipo: Ex: "mercado"
   - Selecione **Google Maps**
   
4. **Clique** em "Buscar Leads"

5. **Veja** os resultados e exporte para Excel!

## 🌐 Busca Multiplataforma

### Como Usar Facebook e Instagram

**Pré-requisito**: Token do Facebook (consulte `COMO_OBTER_TOKEN_FACEBOOK.md`)

1. Configure o token no `.env`:
   ```
   FACEBOOK_ACCESS_TOKEN=seu_token_aqui
   ```

2. Na interface, **selecione** as fontes desejadas:
   - ✅ Google Maps (sempre funciona)
   - ✅ Facebook (opcional)
   - ✅ Instagram (opcional)

3. **Busque** e veja resultados de todas as fontes!

### Diferenças entre Fontes

| Fonte | Disponível | Limitações |
|-------|-----------|------------|
| **Google Maps** | ✅ Sim | Funciona sem configuração extra |
| **Facebook** | ⚠️ Opcional | Requer Access Token, apenas páginas públicas |
| **Instagram** | ⚠️ Opcional | Requer Access Token, apenas contas comerciais |

## 💡 Dicas

### Para Melhores Resultados

✅ **Google Maps**: Melhor cobertura, dados mais completos  
✅ **Facebook**: Bom para negócios locais  
✅ **Instagram**: Ideal para restaurantes e lojas  

### Quando Usar Cada Fonte

- **Apenas Google Maps**: Para uso básico e máximo de resultados
- **Google + Facebook**: Para verificar presença online
- **Todas as Fontes**: Para análise completa de mercado

## 🔍 Interpretando Resultados

### Cores dos Badges

- 🔵 **Azul**: Google Maps
- 📘 **Azul Facebook**: Facebook
- 🌈 **Gradiente**: Instagram

### Informações Disponíveis

✅ **Sempre**: Nome, Endereço, Tipo  
⚠️ **Opcional**: Telefone (depende da fonte)  
🔗 **Links**: Perfil na rede social + Google Maps  

## 📊 Exportação Excel

Colunas incluídas:
1. Nome
2. Endereço
3. Telefone
4. Latitude
5. Longitude
6. Tipo
7. **Fonte** (novo!)
8. **Link** (novo!)

## 🆘 Problemas Comuns

**"Facebook não disponível"**
- Configure `FACEBOOK_ACCESS_TOKEN` no `.env` ou Vercel
- Token pode ter expirado

**"Nenhum resultado no Facebook"**
- Facebook tem menos dados que Google
- Use Google Maps como fonte principal

**"Instagram não encontra nada"**
- Instagram requer conta comercial
- Nem todos os negócios têm Instagram Business

## ⚡ Recomendação

**Para produção**: Use **Google Maps + Facebook** para melhor cobertura!

