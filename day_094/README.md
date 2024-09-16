# Desafio 94

Trabalhando com mapas e geodados com Folium

## Explicação

### Ferramentas Utilizadas

- `folium`: Biblioteca para criação de mapas interativos.
- `os`: Biblioteca padrão do Python para interações com o sistema operacional.

### Funções Principais

- `folium.Map()`: Cria um mapa.
- `folium.Marker()`: Adiciona um marcador ao mapa.
- `m.save()`: Salva o mapa em um arquivo HTML.

## Resultado

```python
import folium
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)
html_path = os.path.join(assets_dir, 'mapa.html')

# Cria um mapa centrado em São Paulo, Brasil
m = folium.Map(location=[-23.55052, -46.633308], zoom_start=12)

# Adiciona um marcador ao mapa
folium.Marker(
    location=[-23.55052, -46.633308],
    popup='São Paulo, Brasil',
    icon=folium.Icon(icon='cloud')
).add_to(m)

# Salva o mapa em um arquivo HTML
m.save(html_path)

print(f"Mapa salvo em: {html_path}")
```