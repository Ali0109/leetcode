import math


def haversine(lat1, lon1, coords_list):
    R = 6371  # радиус Земли в километрах

    # Преобразование координат в радианы
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)

    distances = []
    for lat2, lon2 in coords_list:
        # Преобразование координат в радианы
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        # Разница между широтой и долготой точек
        delta_lat = lat2_rad - lat1_rad
        delta_lon = lon2_rad - lon1_rad

        # Вычисление гаверсинусов
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Расстояние между точками
        distance = R * c
        distance = int(distance * 1000)
        distances.append(distance)

    return distances

# Пример использования функции
lat1 = 41.332666
lon1 = 69.285591
coords_list = [
    (41.272945, 69.306677),
    (41.272945, 69.321322)
]

distances = haversine(lat1, lon1, coords_list)
print("Расстояния до точек:", distances)
