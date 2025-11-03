"""
Módulo para buscar leads no Instagram
"""
import requests
from typing import List, Dict, Optional
from google_maps_searcher import Lead
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()


class InstagramSearcher:
    """Classe para buscar estabelecimentos no Instagram"""
    
    def __init__(self, access_token: Optional[str] = None):
        """
        Inicializa o buscador do Instagram
        
        Args:
            access_token: Token de acesso do Instagram (mesmo do Facebook)
        """
        self.access_token = access_token or os.getenv('FACEBOOK_ACCESS_TOKEN')
        if not self.access_token:
            raise ValueError("Facebook/Instagram Access Token não encontrado. Configure FACEBOOK_ACCESS_TOKEN no .env")
        
        self.base_url = "https://graph.facebook.com/v18.0"
    
    def buscar_leads(
        self,
        estado: str,
        municipio: str,
        bairro: Optional[str] = None,
        tipo_busca: str = None,
        apenas_com_telefone: bool = False
    ) -> List[Lead]:
        """
        Busca leads no Instagram baseado nos parâmetros fornecidos
        
        Args:
            estado: Nome do estado (ex: "São Paulo")
            municipio: Nome do município (ex: "São Paulo")
            bairro: Nome do bairro (opcional, ex: "Centro")
            tipo_busca: Tipo de estabelecimento a buscar (ex: "mercado", "loja de roupa")
            apenas_com_telefone: Se True, retorna apenas estabelecimentos com telefone
        
        Returns:
            Lista de objetos Lead com os resultados encontrados
        """
        
        try:
            leads = []
            
            # Constrói a query de busca
            if bairro:
                location = f"{bairro}, {municipio}, {estado}, Brasil"
            else:
                location = f"{municipio}, {estado}, Brasil"
            
            search_query = f"{tipo_busca} in {location}"
            
            print(f"Buscando estabelecimentos no Instagram: {search_query}")
            
            # Busca páginas do Facebook (que têm Instagram integrado)
            url = f"{self.base_url}/search"
            params = {
                'q': search_query,
                'type': 'page',
                'fields': 'name,location,phone,link,website,instagram_business_account',
                'access_token': self.access_token,
                'limit': 50
            }
            
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            if 'data' not in data or not data['data']:
                print("Nenhum resultado encontrado no Instagram")
                return []
            
            # Processa os resultados
            for item in data['data']:
                # Verifica se tem conta do Instagram
                if 'instagram_business_account' in item:
                    lead = self._processar_item(item, tipo_busca, apenas_com_telefone, location)
                    if lead:
                        leads.append(lead)
            
            print(f"Total de leads encontrados no Instagram: {len(leads)}")
            return leads
            
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar no Instagram: {e}")
            return []
        except Exception as e:
            print(f"Erro inesperado ao buscar no Instagram: {e}")
            return []
    
    def _processar_item(
        self, 
        item: Dict, 
        tipo_busca: str, 
        apenas_com_telefone: bool,
        location: str
    ) -> Optional[Lead]:
        """
        Processa um item do Instagram e retorna um Lead
        
        Args:
            item: Dados do estabelecimento do Instagram
            tipo_busca: Tipo de busca
            apenas_com_telefone: Se True, só retorna se tiver telefone
            location: Localização usada na busca
        
        Returns:
            Lead ou None se não passar no filtro
        """
        try:
            nome = item.get('name', 'N/A')
            
            # Extrai informações de localização
            location_data = item.get('location', {})
            endereco_completo = self._montar_endereco(location_data, location)
            
            # Extrai telefone
            telefone = self._extrair_telefone(item)
            
            # Filtra por telefone se necessário
            if apenas_com_telefone and not telefone:
                return None
            
            # Extrai coordenadas
            latitude = location_data.get('latitude', 0)
            longitude = location_data.get('longitude', 0)
            
            # Busca informações do Instagram Business Account
            instagram_account = item.get('instagram_business_account', {})
            link_perfil = None
            
            if instagram_account and 'id' in instagram_account:
                # Pega o username do Instagram
                account_id = instagram_account.get('id')
                try:
                    account_url = f"{self.base_url}/{account_id}"
                    account_params = {
                        'fields': 'username',
                        'access_token': self.access_token
                    }
                    account_response = requests.get(account_url, params=account_params, timeout=10)
                    account_response.raise_for_status()
                    account_data = account_response.json()
                    username = account_data.get('username')
                    if username:
                        link_perfil = f"https://www.instagram.com/{username}/"
                except Exception:
                    pass
            
            # Se não conseguiu o link do Instagram, usa o link do Facebook
            if not link_perfil:
                link_perfil = item.get('link') or item.get('website')
            
            if not link_perfil:
                nome_formatado = nome.lower().replace(' ', '').replace('.', '').replace('-', '')
                link_perfil = f"https://www.instagram.com/{nome_formatado}/"
            
            lead = Lead(
                nome=nome,
                endereco=endereco_completo,
                telefone=telefone,
                latitude=latitude,
                longitude=longitude,
                tipo=tipo_busca,
                fonte="Instagram",
                link_perfil=link_perfil
            )
            
            return lead
            
        except Exception as e:
            print(f"Erro ao processar item do Instagram: {e}")
            return None
    
    def _montar_endereco(self, location_data: Dict, location: str) -> str:
        """Monta endereço completo a partir dos dados de localização"""
        try:
            parts = []
            
            street = location_data.get('street')
            city = location_data.get('city')
            state = location_data.get('state')
            country = location_data.get('country')
            zip_code = location_data.get('zip')
            
            if street:
                parts.append(street)
            if city:
                parts.append(city)
            if state:
                parts.append(state)
            if zip_code:
                parts.append(f"CEP {zip_code}")
            if country:
                parts.append(country)
            
            if parts:
                return ", ".join(parts)
            else:
                return location
                
        except Exception:
            return location
    
    def _extrair_telefone(self, item: Dict) -> Optional[str]:
        """Extrai telefone do item do Instagram"""
        try:
            # Tenta phone primeiro
            phone = item.get('phone')
            if phone:
                return phone
            
            # Pode ter em about ou outros campos
            about = item.get('about', '')
            if about:
                # Tenta encontrar telefone no texto
                import re
                phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{2,3}\)?[-.\s]?\d{4,5}[-.\s]?\d{4}'
                matches = re.findall(phone_pattern, about)
                if matches:
                    return ''.join(matches[0]) if isinstance(matches[0], tuple) else matches[0]
            
            return None
            
        except Exception:
            return None


def imprimir_leads_instagram(leads: List[Lead]):
    """Imprime os leads encontrados no Instagram de forma formatada"""
    if not leads:
        print("\nNenhum lead encontrado no Instagram.")
        return
    
    print("\n" + "=" * 60)
    print(f"Total de leads encontrados no Instagram: {len(leads)}")
    print("=" * 60 + "\n")
    
    for i, lead in enumerate(leads, 1):
        print(f"Lead #{i}")
        print(f"  Nome: {lead.nome}")
        print(f"  Endereço: {lead.endereco}")
        print(f"  Telefone: {lead.telefone or 'N/A'}")
        print(f"  Localização: {lead.latitude}, {lead.longitude}")
        print(f"  Tipo: {lead.tipo}")
        print(f"  Fonte: {lead.fonte}")
        print(f"  Link: {lead.link_perfil or 'N/A'}")
        print("-" * 60 + "\n")

