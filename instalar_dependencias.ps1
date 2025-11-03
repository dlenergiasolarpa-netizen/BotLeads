# Script PowerShell para instalar dependências do BotLeads
# Este script verifica se o Python está instalado e instala as dependências

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "BotLeads - Instalação de Dependências" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se o Python está instalado
Write-Host "Verificando instalação do Python..." -ForegroundColor Yellow

try {
    $pythonVersion = python --version 2>&1
    if ($pythonVersion -match "Python (\d+\.\d+)") {
        Write-Host "Python encontrado: $pythonVersion" -ForegroundColor Green
        $pythonInstalled = $true
    } else {
        throw "Python não encontrado"
    }
} catch {
    Write-Host "Python não está instalado ou não está no PATH!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Por favor, instale o Python primeiro:" -ForegroundColor Yellow
    Write-Host "1. Acesse: https://www.python.org/downloads/" -ForegroundColor White
    Write-Host "2. Baixe e instale a versão mais recente" -ForegroundColor White
    Write-Host "3. IMPORTANTE: Marque 'Add Python to PATH' durante a instalação" -ForegroundColor White
    Write-Host "4. Reinicie o PowerShell após a instalação" -ForegroundColor White
    Write-Host ""
    Write-Host "Ou instale via Microsoft Store:" -ForegroundColor Yellow
    Write-Host "1. Abra a Microsoft Store" -ForegroundColor White
    Write-Host "2. Procure por 'Python 3.11' ou 'Python 3.12'" -ForegroundColor White
    Write-Host "3. Clique em 'Instalar'" -ForegroundColor White
    Write-Host ""
    exit 1
}

# Verifica se pip está disponível
Write-Host ""
Write-Host "Verificando pip..." -ForegroundColor Yellow

try {
    $pipVersion = pip --version 2>&1
    Write-Host "pip encontrado: $pipVersion" -ForegroundColor Green
    $pipCmd = "pip"
} catch {
    Write-Host "pip não encontrado diretamente. Tentando via python -m pip..." -ForegroundColor Yellow
    try {
        $pipVersion = python -m pip --version 2>&1
        Write-Host "pip encontrado via python -m pip: $pipVersion" -ForegroundColor Green
        $pipCmd = "python -m pip"
    } catch {
        Write-Host "Erro: pip não está disponível!" -ForegroundColor Red
        Write-Host "Tente reinstalar o Python com pip incluído." -ForegroundColor Yellow
        exit 1
    }
}

# Verifica se o arquivo requirements.txt existe
if (-Not (Test-Path "requirements.txt")) {
    Write-Host ""
    Write-Host "Erro: Arquivo requirements.txt não encontrado!" -ForegroundColor Red
    Write-Host "Certifique-se de estar na pasta do projeto BotLeads." -ForegroundColor Yellow
    exit 1
}

# Instala as dependências
Write-Host ""
Write-Host "Instalando dependências do requirements.txt..." -ForegroundColor Yellow
Write-Host ""

try {
    if ($pipCmd -eq "pip") {
        pip install -r requirements.txt
    } else {
        python -m pip install -r requirements.txt
    }
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Green
        Write-Host "Dependências instaladas com sucesso!" -ForegroundColor Green
        Write-Host "========================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "Próximos passos:" -ForegroundColor Yellow
        Write-Host "1. Copie o arquivo 'env.example' para '.env'" -ForegroundColor White
        Write-Host "2. Adicione sua chave da API do Google Maps no arquivo '.env'" -ForegroundColor White
        Write-Host "3. Execute 'python main.py' para começar a usar o bot" -ForegroundColor White
        Write-Host ""
    } else {
        throw "Erro ao instalar dependências"
    }
} catch {
    Write-Host ""
    Write-Host "Erro ao instalar dependências!" -ForegroundColor Red
    Write-Host "Tente instalar manualmente com:" -ForegroundColor Yellow
    Write-Host "  pip install -r requirements.txt" -ForegroundColor White
    Write-Host "ou" -ForegroundColor White
    Write-Host "  python -m pip install -r requirements.txt" -ForegroundColor White
    exit 1
}

