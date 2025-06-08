

import requests
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(text):
    return model.encode(text, convert_to_tensor=True)

def is_conceptually_similar(idea, search_results, threshold=0.65):
    idea_embedding = get_embeddings(idea)
    found_match = False

    sim_con=[]

    # print("\n🔍 Conceptual similarity results:\n" + "-" * 60)

    for index, item in enumerate(search_results.get("data", []), start=1):
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        combined = f"{title}. {snippet}"
        link = item.get("url", "")

        search_embedding = get_embeddings(combined)
        similarity = util.pytorch_cos_sim(idea_embedding, search_embedding).item()

    #     print(f"\nResult #{index}")
    #     print(f"Title   : {title}")
    #     print(f"Concept : {combined}")
    #     print(f"Score   : {similarity:.2f}")

        if similarity >= threshold:
            # print("🔴 Conceptually Similar → Possible Match")
            
            sim_dic = { "concept": combined, "score": f"{similarity:.2f}","link":link}
            sim_con.append(sim_dic)
            # print(sim_dic)
        

    # print("\n" + "=" * 60)
    # if found_match:
    #     # print("🚨 Summary: One or more conceptually similar ideas found.")
    #     sim_con.append(title)
    # else:
        # print("✅ Summary: No significant conceptual match detected.")

    print(sim_con)

    # print(search_results["data"])

def web_search(query, rapidapi_key):
    url = "https://real-time-web-search.p.rapidapi.com/search-advanced"
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "real-time-web-search.p.rapidapi.com"
    }
    params = {
        "q": query,
        "num": 10,
        "start": 0,
        "gl": "us",
        "hl": "en",
        "nfpr": 0
    }

    response = requests.get(url, headers=headers, params=params)
    
    # print("Status Code:", response.status_code)
    if response.status_code != 200:
        print("Error: Failed to retrieve data.")
        return {}

    try:
        return response.json()
    except ValueError:
        print("Error: Response is not valid JSON.")
        return {}


rapidapi_key = 'your api key '  
idea = input("Enter your idea to check for plagiarism: ")

# Search 1: Original idea
results1 = web_search(idea, rapidapi_key)

# Search 2: Idea + " ieee"
results2 = web_search(f"{idea} ieee", rapidapi_key)

# Combine the data lists safely
combined_data = []
if "data" in results1:
    combined_data.extend(results1["data"])
if "data" in results2:
    combined_data.extend(results2["data"])

combined_results = {"data": combined_data}

# Run plagiarism check on combined results
is_conceptually_similar(idea, combined_results, threshold=0.65)


