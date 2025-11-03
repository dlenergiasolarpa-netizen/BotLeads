// BotLeads - JavaScript Principal

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('searchForm');
    const searchBtn = document.getElementById('searchBtn');
    const clearBtn = document.getElementById('clearBtn');
    const resultsSection = document.getElementById('resultsSection');
    const loading = document.getElementById('loading');
    const errorMessage = document.getElementById('errorMessage');
    const leadsContainer = document.getElementById('leadsContainer');
    const resultsCount = document.getElementById('resultsCount');
    const exportBtn = document.getElementById('exportBtn');
    let currentLeads = []; // Armazena leads atuais para exportação

    // Event Listeners
    form.addEventListener('submit', handleSearch);
    clearBtn.addEventListener('click', handleClear);
    exportBtn.addEventListener('click', handleExport);

    /**
     * Manipula o envio do formulário
     */
    async function handleSearch(e) {
        e.preventDefault();
        
        // Esconde resultados anteriores e erros
        hideError();
        hideResults();
        
        // Validação do formulário
        if (!form.checkValidity()) {
            form.reportValidity();
            return;
        }
        
        // Coleta dados do formulário
        const formData = {
            estado: document.getElementById('estado').value.trim(),
            municipio: document.getElementById('municipio').value.trim(),
            bairro: document.getElementById('bairro').value.trim() || null,
            tipo: document.getElementById('tipo').value.trim(),
            apenas_com_telefone: document.getElementById('apenas_com_telefone').checked,
            fontes: Array.from(document.querySelectorAll('input[name="fontes"]:checked')).map(cb => cb.value)
        };
        
        // Validações adicionais
        if (!formData.estado || !formData.municipio || !formData.tipo) {
            showError('Por favor, preencha todos os campos obrigatórios (Estado, Município e Tipo de estabelecimento).');
            return;
        }
        
        // Valida se pelo menos uma fonte foi selecionada
        if (formData.fontes.length === 0) {
            showError('Por favor, selecione pelo menos uma fonte de busca (Google Maps, Facebook ou Instagram).');
            return;
        }
        
        // Inicia busca
        showLoading();
        disableButton(true);
        
        try {
            const response = await fetch('/api/buscar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.erro || 'Erro ao buscar leads');
            }
            
            // Exibe resultados
            displayResults(data);
            
        } catch (error) {
            console.error('Erro:', error);
            showError(error.message || 'Erro ao buscar leads. Tente novamente.');
        } finally {
            hideLoading();
            disableButton(false);
        }
    }
    
    /**
     * Exibe os resultados da busca
     */
    function displayResults(data) {
        if (!data.sucesso || !data.leads || data.leads.length === 0) {
            showEmptyState();
            currentLeads = []; // Limpa leads
            exportBtn.style.display = 'none';
            return;
        }
        
        // Armazena leads para exportação
        currentLeads = data.leads;
        
        // Atualiza contador
        resultsCount.textContent = `${data.total} lead(s) encontrado(s)`;
        
        // Mostra botão de exportar
        exportBtn.style.display = 'flex';
        
        // Limpa container
        leadsContainer.innerHTML = '';
        
        // Cria cards para cada lead
        data.leads.forEach((lead, index) => {
            const leadCard = createLeadCard(lead, index + 1);
            leadsContainer.appendChild(leadCard);
        });
        
        // Mostra seção de resultados
        showResults();
        
        // Scroll suave para resultados
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    
    /**
     * Cria um card para exibir um lead
     */
    function createLeadCard(lead, number) {
        const card = document.createElement('div');
        card.className = 'lead-card';
        
        // Define ícone e cor da fonte
        const fonteIcon = lead.fonte === 'Facebook' ? '📘' : lead.fonte === 'Instagram' ? '📷' : '🗺️';
        const fonteClass = lead.fonte ? `fonte-${lead.fonte.toLowerCase().replace(' ', '-')}` : '';
        
        card.innerHTML = `
            <div class="lead-header">
                <div class="lead-number ${fonteClass}">Lead #${number}</div>
                <h3 class="lead-name">${escapeHtml(lead.nome)}</h3>
            </div>
            <div class="lead-info">
                <div class="lead-item">
                    <span class="lead-icon">📍</span>
                    <span class="lead-label">Endereço:</span>
                    <span class="lead-value">${escapeHtml(lead.endereco)}</span>
                </div>
                <div class="lead-item">
                    <span class="lead-icon">📞</span>
                    <span class="lead-label">Telefone:</span>
                    <span class="lead-value">${escapeHtml(lead.telefone)}</span>
                </div>
                <div class="lead-item">
                    <span class="lead-icon">🌐</span>
                    <span class="lead-label">Localização:</span>
                    <span class="lead-value">${lead.latitude.toFixed(6)}, ${lead.longitude.toFixed(6)}</span>
                </div>
                <div class="lead-item">
                    <span class="lead-icon">🏷️</span>
                    <span class="lead-label">Tipo:</span>
                    <span class="lead-value">${escapeHtml(lead.tipo)}</span>
                </div>
                <div class="lead-item">
                    <span class="lead-icon">${fonteIcon}</span>
                    <span class="lead-label">Fonte:</span>
                    <span class="lead-value">${escapeHtml(lead.fonte || 'Google Maps')}</span>
                </div>
            </div>
            <div class="lead-actions">
                ${lead.link_perfil && lead.link_perfil !== 'N/A' ? `
                    <a 
                        href="${lead.link_perfil}" 
                        target="_blank" 
                        rel="noopener noreferrer"
                        class="btn btn-small btn-outline"
                    >
                        <span class="btn-icon">🔗</span>
                        Ver ${lead.fonte === 'Facebook' ? 'Facebook' : lead.fonte === 'Instagram' ? 'Instagram' : 'Perfil'}
                    </a>
                ` : ''}
                ${lead.latitude && lead.longitude && (lead.latitude !== 0 || lead.longitude !== 0) ? `
                    <a 
                        href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(lead.latitude + ',' + lead.longitude)}" 
                        target="_blank" 
                        rel="noopener noreferrer"
                        class="btn btn-small btn-outline"
                    >
                        <span class="btn-icon">🗺️</span>
                        Ver no Maps
                    </a>
                ` : ''}
                ${lead.telefone && lead.telefone !== 'N/A' ? `
                    <a 
                        href="tel:${lead.telefone.replace(/\s/g, '')}" 
                        class="btn btn-small btn-outline"
                    >
                        <span class="btn-icon">📞</span>
                        Ligar
                    </a>
                ` : ''}
            </div>
        `;
        
        return card;
    }
    
    /**
     * Exibe estado vazio quando não há resultados
     */
    function showEmptyState() {
        leadsContainer.innerHTML = `
            <div class="empty-state">
                <div class="empty-state-icon">🔍</div>
                <h3>Nenhum lead encontrado</h3>
                <p>Tente ajustar os parâmetros de busca e tente novamente.</p>
            </div>
        `;
        showResults();
    }
    
    /**
     * Mostra mensagem de erro
     */
    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
        showResults();
    }
    
    /**
     * Esconde mensagem de erro
     */
    function hideError() {
        errorMessage.style.display = 'none';
    }
    
    /**
     * Mostra loading
     */
    function showLoading() {
        loading.style.display = 'block';
        leadsContainer.innerHTML = '';
        showResults();
    }
    
    /**
     * Esconde loading
     */
    function hideLoading() {
        loading.style.display = 'none';
    }
    
    /**
     * Mostra seção de resultados
     */
    function showResults() {
        resultsSection.style.display = 'block';
    }
    
    /**
     * Esconde seção de resultados
     */
    function hideResults() {
        resultsSection.style.display = 'none';
    }
    
    /**
     * Desabilita/habilita botão
     */
    function disableButton(disabled) {
        searchBtn.disabled = disabled;
        if (disabled) {
            searchBtn.innerHTML = `
                <div class="spinner" style="width: 20px; height: 20px; border-width: 2px;"></div>
                <span class="btn-text">Buscando...</span>
            `;
        } else {
            searchBtn.innerHTML = `
                <span class="btn-icon">🔍</span>
                <span class="btn-text">Buscar Leads</span>
            `;
        }
    }
    
    /**
     * Limpa o formulário e resultados
     */
    function handleClear() {
        form.reset();
        document.getElementById('apenas_com_telefone').checked = true; // Restaura checkbox marcado
        hideResults();
        hideError();
        leadsContainer.innerHTML = '';
        currentLeads = [];
        exportBtn.style.display = 'none';
    }
    
    /**
     * Exporta leads para Excel
     */
    async function handleExport() {
        if (!currentLeads || currentLeads.length === 0) {
            showError('Nenhum lead para exportar.');
            return;
        }
        
        try {
            // Desabilita botão durante exportação
            exportBtn.disabled = true;
            exportBtn.innerHTML = '<span class="btn-icon">⏳</span><span class="btn-text">Exportando...</span>';
            
            // Faz requisição para exportar
            const response = await fetch('/api/exportar-excel', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ leads: currentLeads })
            });
            
            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.erro || 'Erro ao exportar Excel');
            }
            
            // Obtém o blob do arquivo
            const blob = await response.blob();
            
            // Cria link para download
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `leads_${new Date().toISOString().slice(0, 19).replace(/:/g, '-')}.xlsx`;
            document.body.appendChild(a);
            a.click();
            
            // Limpa
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            
        } catch (error) {
            console.error('Erro ao exportar:', error);
            showError(error.message || 'Erro ao exportar para Excel. Tente novamente.');
        } finally {
            // Restaura botão
            exportBtn.disabled = false;
            exportBtn.innerHTML = '<span class="btn-icon">📊</span><span class="btn-text">Exportar para Excel</span>';
        }
    }
    
    /**
     * Escapa HTML para prevenir XSS
     */
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
});

