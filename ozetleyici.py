import requests

def ozet_cikar(api_key, yorumlar):
    API_URL = "https://openrouter.ai/api/v1/chat/completions"

    yorum_metni = "\n".join(yorumlar)
    istek_verisi = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": "Sen kullanıcı yorumlarını özetleyen yardımcı bir asistansın."},
            {"role": "user", "content": f"Şu yorumları özetle: {yorum_metni}"}
        ]
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, json=istek_verisi)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("API Hatası:", response.status_code)
        print(response.text)
        return None
