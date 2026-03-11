import requests
import json

HH_API_URL = "https://api.hh.ru/vacancies"

def fetch_hh_vacancies(url: str, page: int = 0):
    query_params = {
        "text": "fastapi OR django",
        "per_page": 100,
        "page": page,
    }
    resp = requests.get(url, query_params)
    if resp.status_code != 200:
        raise Exception(resp.status_code)
    print(f"Получены вакансии {page=}")
    result = resp.json()
    return result

def fetch_all_hh_vacancies(url: str):
    page = 0
    vacancies_data = []
    while True:
        if page == 20:
            break
        vacancies = fetch_hh_vacancies(url, page)
        if len(vacancies["items"]) == 0:
            break

        vacancies_data += vacancies["items"]
        page += 1

    with open("vacancies.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(vacancies_data, ensure_ascii=False))


def main():
    fetch_all_hh_vacancies(HH_API_URL)

if __name__ == "__main__":
    main()