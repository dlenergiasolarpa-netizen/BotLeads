# Como Habilitar as APIs Necessárias

O erro "REQUEST_DENIED (This API project is not authorized to use this API.)" indica que as APIs necessárias não estão habilitadas no seu projeto Google Cloud.

## APIs Necessárias

1. **Geocoding API** (Geocoding API) - Para converter endereços em coordenadas
2. **Places API** - Para buscar estabelecimentos próximos

## Passo a Passo para Habilitar

### 1. Acesse o Google Cloud Console

Abra seu navegador e vá para:
```
https://console.cloud.google.com/apis/library
```

Ou:
1. Acesse: https://console.cloud.google.com/
2. Certifique-se de estar no projeto correto (o mesmo que gerou a API Key)
3. No menu lateral, clique em **"APIs e Serviços"** > **"Biblioteca"**

### 2. Habilite a Geocoding API

1. Na barra de pesquisa, digite: **"Geocoding API"**
2. Clique no resultado **"Geocoding API"**
3. Clique no botão **"HABILITAR"** (ou "ENABLE")
4. Aguarde alguns segundos até aparecer a mensagem de confirmação

### 3. Habilite a Places API

1. Na barra de pesquisa, digite: **"Places API"**
2. Clique no resultado **"Places API"** (ou "Places API (New)")
3. Clique no botão **"HABILITAR"** (ou "ENABLE")
4. Aguarde alguns segundos até aparecer a mensagem de confirmação

### 4. Verifique se as APIs estão habilitadas

1. No menu lateral, clique em **"APIs e Serviços"** > **"APIs habilitadas"**
2. Você deve ver ambas as APIs na lista:
   - Geocoding API
   - Places API

### 5. Aguarde a Propagação

- Após habilitar, aguarde **1-2 minutos** para que as mudanças sejam propagadas
- Tente executar o bot novamente

## Verificar a API Key

Certifique-se de que sua API Key está associada ao projeto correto:

1. Vá em **"APIs e Serviços"** > **"Credenciais"**
2. Encontre sua API Key na lista
3. Clique nela para ver os detalhes
4. Verifique se está no projeto correto

## Limites e Cobrança

⚠️ **IMPORTANTE**: 
- A Geocoding API tem limites gratuitos
- A Places API tem limites gratuitos
- Após os limites, há cobrança por uso
- Consulte os preços em: https://developers.google.com/maps/billing

### Limites Gratuitos (por mês):
- **Geocoding API**: 40.000 requisições grátis/mês
- **Places API** (Nearby Search): Geralmente $0.032 por requisição após o crédito grátis

## Troubleshooting

**"Ainda não funciona após habilitar"**
- Aguarde mais alguns minutos (propagação pode demorar até 5 minutos)
- Verifique se você está no projeto correto do Google Cloud
- Verifique se a API Key é do mesmo projeto onde habilitou as APIs

**"Preciso criar um novo projeto?"**
- Não é necessário, você pode usar um projeto existente
- Mas se preferir, pode criar um novo projeto e gerar uma nova API Key

**"Como saber qual projeto usar?"**
- Quando você criou a API Key, ela foi associada a um projeto
- Verifique em "APIs e Serviços" > "Credenciais" qual projeto está associado à sua chave

## Links Rápidos

- [Biblioteca de APIs](https://console.cloud.google.com/apis/library)
- [Geocoding API - Habilitação Direta](https://console.cloud.google.com/apis/library/geocoding-backend.googleapis.com)
- [Places API - Habilitação Direta](https://console.cloud.google.com/apis/library/places-backend.googleapis.com)
- [Credenciais (API Keys)](https://console.cloud.google.com/apis/credentials)

