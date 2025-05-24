import requests
from openpyxl import Workbook


search_text = "python"
url = "https://api.hh.ru/vacancies"
params = {
    "text": search_text,
    "area": 1,  
    "per_page": 20  
}


response = requests.get(url, params=params)
data = response.json()


wb = Workbook()
ws = wb.active
ws.append(["Название вакансии", "Компания", "Зарплата от", "Зарплата до", "Ссылка"])


for item in data["items"]:
    name = item["name"]
    company = item["employer"]["name"]
    salary_from = item["salary"]["from"] if item["salary"] else "не указана"
    salary_to = item["salary"]["to"] if item["salary"] else "не указана"
    link = item["alternate_url"]
    ws.append([name, company, salary_from, salary_to, link])


wb.save("hh_python_vacancies.xlsx")

