# Guia de Instalação - BotLeads

## Instalando o Python

Como o Python não está instalado no seu sistema, siga os passos abaixo:

### Opção 1: Instalar Python via Microsoft Store (Mais Fácil)

1. Abra a Microsoft Store
2. Procure por "Python 3.11" ou "Python 3.12"
3. Clique em "Obter" ou "Instalar"
4. Aguarde a instalação concluir
5. Reinicie o PowerShell/Terminal

### Opção 2: Instalar Python via Site Oficial (Recomendado)

1. Acesse: https://www.python.org/downloads/
2. Baixe a versão mais recente (Python 3.11 ou 3.12)
3. Execute o instalador
4. **IMPORTANTE**: Marque a opção "Add Python to PATH" durante a instalação
5. Clique em "Install Now"
6. Aguarde a instalação
7. Reinicie o PowerShell/Terminal

### Verificar Instalação

Após instalar, abra um novo PowerShell e execute:

```powershell
python --version
```

Você deve ver algo como: `Python 3.11.x` ou `Python 3.12.x`

## Instalando as Dependências

Após instalar o Python, navegue até a pasta do projeto:

```powershell
cd C:\Users\junin\Desktop\BotLeads
```

Em seguida, instale as dependências:

```powershell
pip install -r requirements.txt
```

Ou se o comando pip não funcionar, tente:

```powershell
python -m pip install -r requirements.txt
```

## Configurando a API Key

1. Copie o arquivo `env.example` e renomeie para `.env`
2. Abra o arquivo `.env` e adicione sua chave da API do Google Maps:

```
GOOGLE_MAPS_API_KEY=sua_chave_aqui
```

### Como obter a API Key do Google Maps

1. Acesse: https://console.cloud.google.com/
2. Crie um novo projeto ou selecione um existente
3. Vá em **APIs e Serviços > Biblioteca**
4. Procure por **Places API** e clique em **Habilitar**
5. Vá em **APIs e Serviços > Credenciais**
6. Clique em **Criar credenciais > Chave de API**
7. Copie a chave gerada e cole no arquivo `.env`

## Testando o Sistema

Após instalar tudo, execute:

```powershell
python main.py
```

## Problemas Comuns

### "pip não é reconhecido"

Se após instalar o Python o comando `pip` ainda não funcionar, tente:

```powershell
python -m pip install -r requirements.txt
```

### "Python não encontrado" após instalação

1. Reinicie o PowerShell/Terminal
2. Se ainda não funcionar, adicione manualmente ao PATH:
   - Pressione `Win + R`
   - Digite: `sysdm.cpl` e pressione Enter
   - Aba "Avançado" > "Variáveis de Ambiente"
   - Em "Variáveis do sistema", encontre "Path" e clique em "Editar"
   - Adicione: `C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python3XX`
   - Adicione também: `C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python3XX\Scripts`
   - Reinicie o terminal

