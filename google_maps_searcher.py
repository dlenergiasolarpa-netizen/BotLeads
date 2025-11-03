"""
Módulo para buscar leads no Google Maps
"""
import googlemaps
from typing import List, Dict, Optional
from dataclasses import dataclass
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()


@dataclass
class Lead:
    """Classe para representar um lead"""
    nome: str
    endereco: str
    telefone: Optional[str]
    latitude: float
    longitude: float
    tipo: str
    fonte: str = "Google Maps"  # Fonte: Google Maps, Facebook, Instagram
    link_perfil: Optional[str] = None  # Link para perfil na fonte


class GoogleMapsSearcher:
    """Classe para buscar estabelecimentos no Google Maps"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Inicializa o buscador do Google Maps
        
        Args:
            api_key: Chave da API do Google Maps. Se não fornecida, busca na variável de ambiente
        """
        api_key = api_key or os.getenv('GOOGLE_MAPS_API_KEY')
        if not api_key:
            raise ValueError("API Key do Google Maps não encontrada. Configure GOOGLE_MAPS_API_KEY no .env ou passe como parâmetro.")
        
        self.client = googlemaps.Client(key=api_key)
    
    def buscar_leads(
        self,
        estado: str,
        municipio: str,
        bairro: Optional[str] = None,
        tipo_busca: str = None,
        apenas_com_telefone: bool = False
    ) -> List[Lead]:
        """
        Busca leads no Google Maps baseado nos parâmetros fornecidos
        
        Args:
            estado: Nome do estado (ex: "São Paulo")
            municipio: Nome do município (ex: "São Paulo")
            bairro: Nome do bairro (opcional, ex: "Centro")
            tipo_busca: Tipo de estabelecimento a buscar (ex: "mercado", "loja de roupa")
            apenas_com_telefone: Se True, retorna apenas estabelecimentos com telefone
        
        Returns:
            Lista de objetos Lead com os resultados encontrados
        """
        
        # Busca lugares próximos
        try:
            leads = []
            next_page_token = None
            max_pages = 3  # Limita a 3 páginas (máximo 60 resultados)
            
            # Se não tiver bairro, usa Text Search que retorna mais resultados
            if not bairro:
                # Usa Places Text Search para buscar no município inteiro
                query = f"{tipo_busca} em {municipio}, {estado}, Brasil"
                
                print(f"Buscando estabelecimentos no município inteiro: {query}")
                
                try:
                    for page in range(max_pages):
                        if page == 0:
                            # Usa places() com query para text search
                            places_result = self.client.places(query=query, language='pt-BR')
                        elif next_page_token:
                            # Aguarda antes de buscar próxima página (requisito da API)
                            import time
                            time.sleep(2)
                            places_result = self.client.places(query=query, page_token=next_page_token, language='pt-BR')
                        else:
                            break
                        
                        # Verifica se há resultados
                        if 'results' not in places_result:
                            print("Nenhum resultado encontrado na API")
                            break
                        
                        # Processa resultados
                        for place in places_result.get('results', []):
                            place_id = place.get('place_id')
                            if place_id:
                                lead = self._processar_place(place_id, place, tipo_busca, apenas_com_telefone)
                                if lead:
                                    leads.append(lead)
                        
                        # Verifica se há próxima página
                        next_page_token = places_result.get('next_page_token')
                        if not next_page_token:
                            break
                    
                    print(f"Total de leads encontrados: {len(leads)}")
                    
                except Exception as e:
                    error_msg = str(e)
                    print(f"Erro ao buscar lugares com text search: {error_msg}")
                    # Se falhar, tenta fallback com geocoding do município + text search
                    try:
                        endereco_busca = f"{municipio}, {estado}, Brasil"
                        geocode_result = self.client.geocode(endereco_busca)
                        if geocode_result:
                            # Tenta buscar novamente com query diferente
                            query_fallback = f"{tipo_busca} {municipio} {estado} Brasil"
                            places_result = self.client.places(query=query_fallback, language='pt-BR')
                            
                            for place in places_result.get('results', []):
                                place_id = place.get('place_id')
                                if place_id:
                                    lead = self._processar_place(place_id, place, tipo_busca, apenas_com_telefone)
                                    if lead:
                                        leads.append(lead)
                    except Exception as e2:
                        print(f"Erro no fallback: {e2}")
            else:
                # Quando tem bairro, busca no bairro específico
                query = f"{tipo_busca} em {bairro}, {municipio}, {estado}, Brasil"
                
                print(f"Buscando estabelecimentos no bairro: {query}")
                
                try:
                    for page in range(max_pages):
                        if page == 0:
                            # Usa places() com query para buscar no bairro
                            places_result = self.client.places(query=query, language='pt-BR')
                        elif next_page_token:
                            # Aguarda antes de buscar próxima página (requisito da API)
                            import time
                            time.sleep(2)
                            places_result = self.client.places(query=query, page_token=next_page_token, language='pt-BR')
                        else:
                            break
                        
                        # Verifica se há resultados
                        if 'results' not in places_result:
                            print("Nenhum resultado encontrado na API")
                            break
                        
                        # Processa resultados
                        for place in places_result.get('results', []):
                            place_id = place.get('place_id')
                            if place_id:
                                lead = self._processar_place(place_id, place, tipo_busca, apenas_com_telefone)
                                if lead:
                                    leads.append(lead)
                        
                        # Verifica se há próxima página
                        next_page_token = places_result.get('next_page_token')
                        if not next_page_token:
                            break
                    
                    print(f"Total de leads encontrados: {len(leads)}")
                    
                except Exception as e:
                    error_msg = str(e)
                    print(f"Erro ao buscar lugares no bairro: {error_msg}")
                    
                    if "REQUEST_DENIED" in error_msg or "not authorized" in error_msg.lower():
                        print("\n" + "="*60)
                        print("ERRO: API não autorizada!")
                        print("="*60)
                        print("Você precisa habilitar as seguintes APIs no Google Cloud Console:")
                        print("1. Geocoding API")
                        print("2. Places API")
                        print("\nSiga os passos:")
                        print("1. Acesse: https://console.cloud.google.com/apis/library")
                        print("2. Procure por 'Geocoding API' e clique em 'Habilitar'")
                        print("3. Procure por 'Places API' e clique em 'Habilitar'")
                        print("4. Aguarde alguns segundos e tente novamente")
                        print("="*60 + "\n")
            
            return leads
            
        except Exception as e:
            error_msg = str(e)
            print(f"Erro ao buscar lugares: {error_msg}")
            
            if "REQUEST_DENIED" in error_msg or "not authorized" in error_msg.lower():
                print("\n" + "="*60)
                print("ERRO: API não autorizada!")
                print("="*60)
                print("Você precisa habilitar a Places API no Google Cloud Console:")
                print("\nSiga os passos:")
                print("1. Acesse: https://console.cloud.google.com/apis/library")
                print("2. Procure por 'Places API' e clique em 'Habilitar'")
                print("3. Aguarde alguns segundos e tente novamente")
                print("="*60 + "\n")
            
            return []
    
    def _processar_place(self, place_id: str, place: Dict, tipo_busca: str, apenas_com_telefone: bool) -> Optional[Lead]:
        """
        Processa um lugar do Google Maps e retorna um Lead
        
        Args:
            place_id: ID do lugar
            place: Dados do lugar da API
            tipo_busca: Tipo de busca
            apenas_com_telefone: Se True, só retorna se tiver telefone
        
        Returns:
            Lead ou None se não passar no filtro
        """
        try:
            place_details = self.client.place(
                place_id=place_id,
                fields=['name', 'formatted_address', 'formatted_phone_number', 'international_phone_number'],
                language='pt-BR'
            )
            
            result = place_details.get('result', {})
            nome = result.get('name', 'N/A')
            endereco_completo = result.get('formatted_address', '')
            
            # Busca telefone (prioriza formatted_phone_number, senão usa international_phone_number)
            telefone = result.get('formatted_phone_number') or result.get('international_phone_number')
            
            # Filtra por telefone se necessário
            if apenas_com_telefone and not telefone:
                return None
            
            geometry = place.get('geometry', {})
            location = geometry.get('location', {})
            
            lead = Lead(
                nome=nome,
                endereco=endereco_completo,
                telefone=telefone,
                latitude=location.get('lat', 0),
                longitude=location.get('lng', 0),
                tipo=tipo_busca,
                fonte="Google Maps",
                link_perfil=place.get('url') or f"https://www.google.com/maps/place/?q=place_id:{place_id}"
            )
            
            return lead
        except Exception as e:
            print(f"Erro ao processar lugar {place_id}: {e}")
            return None
    
    def imprimir_leads(self, leads: List[Lead]):
        """Imprime os leads encontrados de forma formatada"""
        if not leads:
            print("\nNenhum lead encontrado.")
            return
        
        print(f"\n{'='*60}")
        print(f"Total de leads encontrados: {len(leads)}")
        print(f"{'='*60}\n")
        
        for i, lead in enumerate(leads, 1):
            print(f"Lead #{i}")
            print(f"  Nome: {lead.nome}")
            print(f"  Endereço: {lead.endereco}")
            print(f"  Telefone: {lead.telefone or 'N/A'}")
            print(f"  Localização: {lead.latitude}, {lead.longitude}")
            print(f"  Tipo: {lead.tipo}")
            print("-" * 60)

