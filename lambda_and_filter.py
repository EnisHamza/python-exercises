cities = [{"city_id": 1, "city_name": "Prishtina",
           "license_plate": "01", "zip_code": 10000},
          {"city_id": 2, "city_name": "Mitrovica",
           "license_plate": "02", "zip_code": 40000},
          {"city_id": 3, "city_name": "Peja",
           "license_plate": "03", "zip_code": 30000},
          {"city_id": 4, "city_name": "Prizren",
           "license_plate": "04", "zip_code": 20000},
          {"city_id": 5, "city_name": "Ferizaj",
           "license_plate": "05", "zip_code": 70000},
          {"city_id": 6, "city_name": "Gjilan",
           "license_plate": "06", "zip_code": 60000},
          {"city_id": 7, "city_name": "Gjilan",
           "license_plate": "07", "zip_code": 50000}]

print(list(filter(lambda row: row["city_name"].startswith(
    "P") and not "03" in row["license_plate"], cities)))
