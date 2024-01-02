import folium

sete_maravilhas_nome = ["Cristo Redentor", "Grande Muralha da China", "Petra", "Coliseu", "Chichén Itzá", "Machu Picchu", "Taj Mahal"]

sete_maravilhas_coordenadas = [[-22.95177766661826, -43.210015134543696],
                               [40.43199750326661, 116.57019250680408],
                               [30.328563229955414, 35.44445611447539],
                               [41.890377894136115, 12.492660050495498],
                               [20.684414648897793, -88.56738256230551],
                               [-13.1630524969655, -72.5442750707414],
                               [27.175345211324835, 78.0424747905004]]

sete_maravilhas_mapa = folium.Map(location = [-22.95177766661826, -43.210015134543696])

sete_maravilhas_mapa