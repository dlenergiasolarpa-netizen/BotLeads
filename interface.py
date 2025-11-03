"""
Interface gráfica para busca de leads no Google Maps
"""
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from google_maps_searcher import GoogleMapsSearcher
import threading
from PIL import Image, ImageTk
import os


class BotLeadsInterface:
    """Interface gráfica para o BotLeads"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("BotLeads - Busca de Leads no Google Maps")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Cores da paleta BotLeads
        self.colors = {
            'primary': '#66BB6A',      # Verde Principal
            'primary_dark': '#4CAF50',
            'bot_blue': '#00BCD4',     # Azul Ciano Destaque
            'tech_grey': '#37474F',    # Cinza Escuro
            'white': '#FFFFFF',         # Branco Neutro
            'text_primary': '#37474F',
            'text_secondary': '#546E7A'
        }
        
        # Configura estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        # Aplica cores ao estilo
        self.configurar_cores(style)
        
        self.criar_interface()
        self.searcher = None
    
    def configurar_cores(self, style):
        """Configura as cores da interface"""
        # Configura cores dos botões
        style.configure('Primary.TButton',
                       background=self.colors['primary'],
                       foreground=self.colors['white'],
                       borderwidth=0,
                       focuscolor='none')
        style.map('Primary.TButton',
                 background=[('active', self.colors['primary_dark']),
                            ('pressed', self.colors['primary_dark'])])
        
        # Configura cores dos frames
        style.configure('Header.TFrame',
                       background=self.colors['tech_grey'])
        
        style.configure('Card.TLabelFrame',
                       background=self.colors['white'],
                       foreground=self.colors['text_primary'],
                       borderwidth=2,
                       relief='flat')
        
        style.configure('Card.TLabelFrame.Label',
                       background=self.colors['white'],
                       foreground=self.colors['tech_grey'],
                       font=('Arial', 10, 'bold'))
        
    def criar_interface(self):
        """Cria os elementos da interface"""
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Header com logo
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky=(tk.W, tk.E))
        header_frame.columnconfigure(1, weight=1)
        
        # Logo
        logo_path = os.path.join(os.path.dirname(__file__), 'BotLeadsLogo.png')
        if os.path.exists(logo_path):
            try:
                logo_img = Image.open(logo_path)
                logo_img = logo_img.resize((50, 50), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(logo_img)
                logo_label = ttk.Label(header_frame, image=self.logo_photo, background=main_frame['background'])
                logo_label.grid(row=0, column=0, padx=(0, 10), sticky=tk.W)
            except Exception as e:
                print(f"Erro ao carregar logo: {e}")
        
        # Título com cores
        title_frame = ttk.Frame(header_frame)
        title_frame.grid(row=0, column=1, sticky=tk.W)
        
        bot_label = ttk.Label(
            title_frame,
            text="Bot",
            font=('Arial', 18, 'bold'),
            foreground=self.colors['bot_blue']
        )
        bot_label.pack(side=tk.LEFT)
        
        leads_label = ttk.Label(
            title_frame,
            text="Leads",
            font=('Arial', 18, 'bold'),
            foreground=self.colors['primary']
        )
        leads_label.pack(side=tk.LEFT, padx=(0, 10))
        
        subtitle_label = ttk.Label(
            header_frame,
            text="Busca de Leads no Google Maps",
            font=('Arial', 12),
            foreground=self.colors['text_secondary']
        )
        subtitle_label.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(5, 0))
        
        # Formulário de busca
        form_frame = ttk.LabelFrame(main_frame, text="Parâmetros de Busca", padding="10", style='Card.TLabelFrame')
        form_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        form_frame.columnconfigure(1, weight=1)
        
        # Estado
        ttk.Label(form_frame, text="Estado:").grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
        self.estado_entry = ttk.Entry(form_frame, width=40)
        self.estado_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Município
        ttk.Label(form_frame, text="Município:").grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)
        self.municipio_entry = ttk.Entry(form_frame, width=40)
        self.municipio_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Bairro
        ttk.Label(form_frame, text="Bairro:").grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)
        self.bairro_entry = ttk.Entry(form_frame, width=40)
        self.bairro_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Raio
        ttk.Label(form_frame, text="Raio (metros):").grid(row=3, column=0, sticky=tk.W, pady=5, padx=5)
        raio_frame = ttk.Frame(form_frame)
        raio_frame.grid(row=3, column=1, sticky=tk.W, pady=5, padx=5)
        self.raio_entry = ttk.Entry(raio_frame, width=20)
        self.raio_entry.insert(0, "1000")
        self.raio_entry.pack(side=tk.LEFT)
        ttk.Label(raio_frame, text="(ex: 1000, 2000, 5000)").pack(side=tk.LEFT, padx=5)
        
        # Tipo de busca
        ttk.Label(form_frame, text="Tipo de estabelecimento:").grid(row=4, column=0, sticky=tk.W, pady=5, padx=5)
        tipo_frame = ttk.Frame(form_frame)
        tipo_frame.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=5)
        tipo_frame.columnconfigure(0, weight=1)
        self.tipo_entry = ttk.Entry(tipo_frame, width=40)
        self.tipo_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        ttk.Label(tipo_frame, text="(ex: mercado, loja de roupa, padaria)").grid(row=1, column=0, sticky=tk.W, pady=(2, 0))
        
        # Botão de busca
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.buscar_button = ttk.Button(
            button_frame,
            text="🔍 Buscar Leads",
            command=self.buscar_leads,
            width=20,
            style='Primary.TButton'
        )
        self.buscar_button.pack(side=tk.LEFT, padx=5)
        
        self.limpar_button = ttk.Button(
            button_frame,
            text="Limpar Resultados",
            command=self.limpar_resultados,
            width=20
        )
        self.limpar_button.pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_label = ttk.Label(main_frame, text="Pronto", relief=tk.SUNKEN)
        self.status_label.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Área de resultados
        results_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="10", style='Card.TLabelFrame')
        results_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        self.resultados_text = scrolledtext.ScrolledText(
            results_frame,
            width=80,
            height=20,
            wrap=tk.WORD,
            font=('Consolas', 9)
        )
        self.resultados_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Barra de progresso (inicialmente oculta)
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            length=400
        )
        self.progress.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        self.progress.grid_remove()
    
    def validar_campos(self):
        """Valida se todos os campos obrigatórios foram preenchidos"""
        estado = self.estado_entry.get().strip()
        municipio = self.municipio_entry.get().strip()
        bairro = self.bairro_entry.get().strip()
        raio = self.raio_entry.get().strip()
        tipo = self.tipo_entry.get().strip()
        
        if not estado:
            messagebox.showerror("Erro", "Por favor, preencha o campo Estado.")
            self.estado_entry.focus()
            return False
        
        if not municipio:
            messagebox.showerror("Erro", "Por favor, preencha o campo Município.")
            self.municipio_entry.focus()
            return False
        
        if not bairro:
            messagebox.showerror("Erro", "Por favor, preencha o campo Bairro.")
            self.bairro_entry.focus()
            return False
        
        if not raio:
            messagebox.showerror("Erro", "Por favor, preencha o campo Raio.")
            self.raio_entry.focus()
            return False
        
        try:
            raio_int = int(raio)
            if raio_int <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "O Raio deve ser um número positivo.")
            self.raio_entry.focus()
            return False
        
        if not tipo:
            messagebox.showerror("Erro", "Por favor, preencha o campo Tipo de estabelecimento.")
            self.tipo_entry.focus()
            return False
        
        return True
    
    def buscar_leads(self):
        """Inicia a busca de leads em thread separada"""
        if not self.validar_campos():
            return
        
        # Desabilita botão durante busca
        self.buscar_button.config(state='disabled')
        self.progress.grid()
        self.progress.start()
        self.status_label.config(text="Buscando leads...")
        
        # Limpa resultados anteriores
        self.resultados_text.delete(1.0, tk.END)
        
        # Inicia busca em thread separada para não travar a interface
        thread = threading.Thread(target=self.executar_busca, daemon=True)
        thread.start()
    
    def executar_busca(self):
        """Executa a busca de leads"""
        try:
            # Obtém valores dos campos
            estado = self.estado_entry.get().strip()
            municipio = self.municipio_entry.get().strip()
            bairro = self.bairro_entry.get().strip()
            raio = int(self.raio_entry.get().strip())
            tipo_busca = self.tipo_entry.get().strip()
            
            # Inicializa o buscador
            if not self.searcher:
                self.searcher = GoogleMapsSearcher()
            
            # Busca os leads
            leads = self.searcher.buscar_leads(
                estado=estado,
                municipio=municipio,
                bairro=bairro,
                raio=raio,
                tipo_busca=tipo_busca
            )
            
            # Atualiza interface com resultados (deve ser feito na thread principal)
            self.root.after(0, self.exibir_resultados, leads)
            
        except Exception as e:
            self.root.after(0, self.exibir_erro, str(e))
    
    def exibir_resultados(self, leads):
        """Exibe os resultados na interface"""
        self.progress.stop()
        self.progress.grid_remove()
        self.buscar_button.config(state='normal')
        
        if not leads:
            self.resultados_text.insert(tk.END, "Nenhum lead encontrado.\n")
            self.status_label.config(text="Busca concluída - Nenhum resultado encontrado")
            return
        
        # Formata e exibe os resultados
        self.resultados_text.insert(tk.END, f"{'='*70}\n")
        self.resultados_text.insert(tk.END, f"Total de leads encontrados: {len(leads)}\n")
        self.resultados_text.insert(tk.END, f"{'='*70}\n\n")
        
        for i, lead in enumerate(leads, 1):
            self.resultados_text.insert(tk.END, f"Lead #{i}\n")
            self.resultados_text.insert(tk.END, f"  Nome: {lead.nome}\n")
            self.resultados_text.insert(tk.END, f"  Endereço: {lead.endereco}\n")
            self.resultados_text.insert(tk.END, f"  Telefone: {lead.telefone or 'N/A'}\n")
            self.resultados_text.insert(tk.END, f"  Localização: {lead.latitude}, {lead.longitude}\n")
            self.resultados_text.insert(tk.END, f"  Tipo: {lead.tipo}\n")
            self.resultados_text.insert(tk.END, "-" * 70 + "\n\n")
        
        self.status_label.config(text=f"Busca concluída - {len(leads)} lead(s) encontrado(s)")
    
    def exibir_erro(self, erro_msg):
        """Exibe erro na interface"""
        self.progress.stop()
        self.progress.grid_remove()
        self.buscar_button.config(state='normal')
        
        self.resultados_text.insert(tk.END, f"ERRO: {erro_msg}\n\n")
        self.status_label.config(text="Erro ao buscar leads")
        
        messagebox.showerror("Erro", f"Erro ao buscar leads:\n\n{erro_msg}")
    
    def limpar_resultados(self):
        """Limpa a área de resultados"""
        self.resultados_text.delete(1.0, tk.END)
        self.status_label.config(text="Resultados limpos")


def main():
    """Função principal para iniciar a interface"""
    root = tk.Tk()
    app = BotLeadsInterface(root)
    root.mainloop()


if __name__ == "__main__":
    main()

