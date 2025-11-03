"""
Script principal para buscar leads no Google Maps
"""
from google_maps_searcher import GoogleMapsSearcher


def main():
    """Função principal para testar a busca de leads"""
    
    # Exemplo de uso
    print("=" * 60)
    print("BotLeads - Busca de Leads no Google Maps")
    print("=" * 60)
    print()
    
    # Parâmetros de busca
    estado = input("Digite o estado (ex: São Paulo): ").strip()
    municipio = input("Digite o município (ex: São Paulo): ").strip()
    bairro = input("Digite o bairro (ex: Centro): ").strip()
    
    raio_input = input("Digite o raio da busca em metros (ex: 1000): ").strip()
    try:
        raio = int(raio_input)
    except ValueError:
        print("Raio inválido. Usando 1000 metros como padrão.")
        raio = 1000
    
    tipo_busca = input("Digite o que buscar (ex: mercado, loja de roupa): ").strip()
    
    print("\nBuscando leads...")
    print("-" * 60)
    
    try:
        # Inicializa o buscador
        searcher = GoogleMapsSearcher()
        
        # Busca os leads
        leads = searcher.buscar_leads(
            estado=estado,
            municipio=municipio,
            bairro=bairro,
            raio=raio,
            tipo_busca=tipo_busca
        )
        
        # Imprime os resultados
        searcher.imprimir_leads(leads)
        
    except Exception as e:
        print(f"\nErro: {e}")
        print("\nCertifique-se de que:")
        print("1. Você configurou a variável GOOGLE_MAPS_API_KEY no arquivo .env")
        print("2. A API Key está válida e tem permissões para Places API")
        print("3. A Places API está habilitada no seu projeto Google Cloud")


if __name__ == "__main__":
    main()

