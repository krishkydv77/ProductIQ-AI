import spacy
nlp = spacy.load("en_core_web_sm")

def extract_price_limit(query: str):
    doc = nlp(query)
    for i, t in enumerate(doc):
        if t.lemma_.lower() in {"under","below","less","max","within"}:
            for nxt in doc[i+1:i+4]:
                digits = "".join(c for c in nxt.text if c.isdigit())
                if digits: return int(digits)
    for ent in doc.ents:
        if ent.label_ in {"MONEY","CARDINAL"}:
            digits = "".join(c for c in ent.text if c.isdigit())
            if digits: return int(digits)
    return None
