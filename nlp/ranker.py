from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_products(user_query, products):
    if not products: return []
    texts = [f"{p['name']} {p['description']} {p['category']} {p['color']} {p['style']}" for p in products]
    tfidf = TfidfVectorizer().fit_transform([user_query] + texts)
    scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()
    for p, s in zip(products, scores): p["match_score"] = round(s*100, 2)
    return sorted(products, key=lambda x: x["match_score"], reverse=True)
