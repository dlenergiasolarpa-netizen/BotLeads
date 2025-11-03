// Autocomplete para Estados, Municípios e Bairros

// Variáveis globais
let estadosList = [];
let municipiosList = [];
let estadoSelecionado = null;
let municipioSelecionado = null;

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    initializeAutocomplete();
});

/**
 * Inicializa os autocompletes
 */
function initializeAutocomplete() {
    const estadoInput = document.getElementById('estado');
    const municipioInput = document.getElementById('municipio');
    const bairroInput = document.getElementById('bairro');
    
    // Carrega estados ao iniciar
    loadEstados();
    
    // Event listeners para estados
    estadoInput.addEventListener('input', debounce((e) => {
        filterEstados(e.target.value);
    }, 300));
    
    estadoInput.addEventListener('focus', () => {
        if (estadosList.length > 0) {
            showDropdown('estadoDropdown', estadosList.map(e => ({
                id: e.id,
                nome: e.nome,
                sigla: e.sigla
            })));
        }
    });
    
    estadoInput.addEventListener('blur', () => {
        // Delay para permitir clique no dropdown
        setTimeout(() => hideDropdown('estadoDropdown'), 200);
    });
    
    // Event listeners para municípios
    municipioInput.addEventListener('input', debounce((e) => {
        if (estadoSelecionado) {
            filterMunicipios(e.target.value);
        }
    }, 300));
    
    municipioInput.addEventListener('focus', () => {
        if (!estadoSelecionado) {
            alert('Por favor, selecione primeiro um estado.');
            municipioInput.blur();
            return;
        }
        
        if (municipiosList.length > 0) {
            showMunicipiosDropdown(municipiosList);
        }
    });
    
    municipioInput.addEventListener('blur', () => {
        setTimeout(() => hideDropdown('municipioDropdown'), 200);
    });
    
    // Event listeners para bairros
    bairroInput.addEventListener('input', debounce((e) => {
        if (municipioSelecionado && estadoSelecionado) {
            searchBairros(e.target.value);
        }
    }, 500));
    
    bairroInput.addEventListener('focus', () => {
        if (!municipioSelecionado) {
            alert('Por favor, selecione primeiro um município.');
            bairroInput.blur();
            return;
        }
    });
    
    bairroInput.addEventListener('blur', () => {
        setTimeout(() => hideDropdown('bairroDropdown'), 200);
    });
}

/**
 * Carrega todos os estados
 */
async function loadEstados() {
    try {
        const response = await fetch('/api/estados');
        const data = await response.json();
        
        if (data.sucesso && data.estados) {
            estadosList = data.estados;
            console.log('Estados carregados:', estadosList.length);
        } else {
            console.error('Erro ao carregar estados:', data.erro);
        }
    } catch (error) {
        console.error('Erro ao carregar estados:', error);
    }
}

/**
 * Filtra estados por texto
 */
function filterEstados(query) {
    const dropdown = document.getElementById('estadoDropdown');
    
    if (!query || query.length < 2) {
        if (estadosList.length > 0) {
            showDropdown('estadoDropdown', estadosList.map(e => ({
                id: e.id,
                nome: e.nome,
                sigla: e.sigla
            })));
        }
        return;
    }
    
    const queryLower = query.toLowerCase();
    const filtered = estadosList.filter(estado => 
        estado.nome.toLowerCase().includes(queryLower) ||
        estado.sigla.toLowerCase().includes(queryLower)
    );
    
    showDropdown('estadoDropdown', filtered.map(e => ({
        id: e.id,
        nome: e.nome,
        sigla: e.sigla
    })));
}

/**
 * Carrega municípios do estado selecionado
 */
async function loadMunicipios(estadoId) {
    const municipioInput = document.getElementById('municipio');
    const dropdown = document.getElementById('municipioDropdown');
    
    // Mostra loading
    dropdown.innerHTML = '<div class="autocomplete-loading">Carregando municípios...</div>';
    dropdown.classList.add('show');
    
    try {
        const response = await fetch(`/api/municipios?estado_id=${estadoId}`);
        const data = await response.json();
        
        if (data.sucesso && data.municipios) {
            municipiosList = data.municipios;
            
            // Habilita campo de município
            municipioInput.disabled = false;
            municipioInput.placeholder = 'Digite para buscar o município';
            
            // Limpa valor anterior
            municipioInput.value = '';
            document.getElementById('municipio_id').value = '';
            
            // Mostra dropdown com todos os municípios
            showMunicipiosDropdown(municipiosList);
            
            // Desabilita e limpa bairro
            const bairroInput = document.getElementById('bairro');
            bairroInput.disabled = true;
            bairroInput.value = '';
            bairroInput.placeholder = 'Selecione primeiro um município';
            municipioSelecionado = null;
            
        } else {
            dropdown.innerHTML = '<div class="autocomplete-item-empty">Erro ao carregar municípios</div>';
            console.error('Erro ao carregar municípios:', data.erro);
        }
    } catch (error) {
        dropdown.innerHTML = '<div class="autocomplete-item-empty">Erro ao carregar municípios</div>';
        console.error('Erro ao carregar municípios:', error);
    }
}

/**
 * Mostra dropdown de municípios
 */
function showMunicipiosDropdown(municipios) {
    showDropdown('municipioDropdown', municipios.map(m => ({
        id: m.id,
        nome: m.nome
    })));
}

/**
 * Filtra municípios por texto
 */
function filterMunicipios(query) {
    const dropdown = document.getElementById('municipioDropdown');
    
    if (!query || query.length < 2) {
        if (municipiosList.length > 0) {
            showMunicipiosDropdown(municipiosList);
        }
        return;
    }
    
    const queryLower = query.toLowerCase();
    const filtered = municipiosList.filter(municipio => 
        municipio.nome.toLowerCase().includes(queryLower)
    );
    
    showMunicipiosDropdown(filtered);
}

/**
 * Busca bairros por município
 */
async function searchBairros(query) {
    if (!municipioSelecionado || !estadoSelecionado || !query || query.length < 2) {
        hideDropdown('bairroDropdown');
        return;
    }
    
    const dropdown = document.getElementById('bairroDropdown');
    
    // Mostra loading
    dropdown.innerHTML = '<div class="autocomplete-loading">Buscando bairros...</div>';
    dropdown.classList.add('show');
    
    try {
        const response = await fetch('/api/buscar-bairros', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                municipio: municipioSelecionado.nome,
                estado: estadoSelecionado.nome,
                query: query
            })
        });
        
        const data = await response.json();
        
        if (data.sucesso && data.bairros && data.bairros.length > 0) {
            const bairros = data.bairros.map(b => ({
                id: b,
                nome: b
            }));
            showDropdown('bairroDropdown', bairros);
        } else {
            // Permite que o usuário digite o bairro mesmo sem resultados
            hideDropdown('bairroDropdown');
        }
    } catch (error) {
        console.error('Erro ao buscar bairros:', error);
        hideDropdown('bairroDropdown');
    }
}

/**
 * Mostra dropdown genérico
 */
function showDropdown(dropdownId, items) {
    const dropdown = document.getElementById(dropdownId);
    const container = dropdown.closest('.searchbox-container');
    const input = container.querySelector('.searchbox-input');
    
    if (!items || items.length === 0) {
        dropdown.innerHTML = '<div class="autocomplete-item-empty">Nenhum resultado encontrado</div>';
        dropdown.classList.add('show');
        input?.classList.add('dropdown-open');
        return;
    }
    
    dropdown.innerHTML = '';
    
    items.forEach((item, index) => {
        const div = document.createElement('div');
        div.className = 'autocomplete-item';
        div.innerHTML = `<span class="autocomplete-icon">📍</span><span>${escapeHtml(item.nome)}</span>`;
        
        div.addEventListener('click', () => {
            selectItem(dropdownId, item, index);
        });
        
        dropdown.appendChild(div);
    });
    
    dropdown.classList.add('show');
    input?.classList.add('dropdown-open');
}

/**
 * Esconde dropdown
 */
function hideDropdown(dropdownId) {
    const dropdown = document.getElementById(dropdownId);
    const container = dropdown.closest('.searchbox-container');
    const input = container?.querySelector('.searchbox-input');
    
    dropdown.classList.remove('show');
    input?.classList.remove('dropdown-open');
}

/**
 * Seleciona item do dropdown
 */
function selectItem(dropdownId, item, index) {
    if (dropdownId === 'estadoDropdown') {
        const estadoInput = document.getElementById('estado');
        estadoInput.value = item.nome;
        document.getElementById('estado_id').value = item.id;
        estadoSelecionado = item;
        
        // Limpa e desabilita municípios e bairros
        const municipioInput = document.getElementById('municipio');
        municipioInput.value = '';
        municipioInput.disabled = true;
        municipioInput.placeholder = 'Selecione primeiro um estado';
        document.getElementById('municipio_id').value = '';
        municipioSelecionado = null;
        
        const bairroInput = document.getElementById('bairro');
        bairroInput.value = '';
        bairroInput.disabled = true;
        bairroInput.placeholder = 'Selecione primeiro um município';
        
        hideDropdown(dropdownId);
        
        // Carrega municípios do estado
        loadMunicipios(item.id);
        
    } else if (dropdownId === 'municipioDropdown') {
        const municipioInput = document.getElementById('municipio');
        municipioInput.value = item.nome;
        document.getElementById('municipio_id').value = item.id;
        municipioSelecionado = item;
        
        // Habilita campo de bairro
        const bairroInput = document.getElementById('bairro');
        bairroInput.disabled = false;
        bairroInput.placeholder = 'Digite para buscar o bairro (opcional - deixe em branco para buscar no município inteiro)';
        bairroInput.value = '';
        bairroInput.removeAttribute('required');
        
        hideDropdown(dropdownId);
        
    } else if (dropdownId === 'bairroDropdown') {
        const bairroInput = document.getElementById('bairro');
        bairroInput.value = item.nome;
        hideDropdown(dropdownId);
    }
}

/**
 * Escapa HTML
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Fecha dropdowns ao clicar fora
document.addEventListener('click', (e) => {
    if (!e.target.closest('.searchbox-container')) {
        hideDropdown('estadoDropdown');
        hideDropdown('municipioDropdown');
        hideDropdown('bairroDropdown');
    }
});

