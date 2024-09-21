import spacy

nlp = spacy.load("pt_core_news_sm")

def analisar_texto(texto):
    doc = nlp(texto)

    print("Tokens:")
    for token in doc:
        print(f"{token.text} (Lemma: {token.lemma_}, POS: {token.pos_})")

    print("\nEntidades Nomeadas:")
    for ent in doc.ents:
        print(f"{ent.text} (Label: {ent.label_})")

if __name__ == '__main__':
    texto = "A Apple está considerando comprar uma startup do Reino Unido por 1 bilhão de dólares."
    analisar_texto(texto)