import os

def create_city_folders(cities):
    for city in cities:
        city_folder = os.path.join("Photos", city)
        os.makedirs(city_folder, exist_ok=True)

        for subfolder in ["Landmarks", "Restaurants", "Hotels"]:
            subfolder_path = os.path.join(city_folder, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)

if __name__ == "__main__":
    cities = input("Введите названия городов через запятую: ").split(",")
    create_city_folders([city.strip() for city in cities])
