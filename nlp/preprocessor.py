import spacy
nlp = spacy.load("en_core_web_sm")

VOCAB = {
    "product": {"shoes","jacket","shirt","pants","t-shirt","jeans","sneakers"},
    "color": {"black","brown","white","red","blue","grey","green"},
    "style": {"formal","sports","casual","partywear","winter","slim"},
    "gender": {"men","women","kids","unisex"}
}

def extract_dynamic_entities(query: str):
    doc = nlp(query.lower())
    return {k: t.text for t in doc for k,v in VOCAB.items() if t.text in v}
