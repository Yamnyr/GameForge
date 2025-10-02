from huggingface_hub import InferenceApi

# Exemple : générer un scénario
def generer_scenario(prompt):
    api = InferenceApi(repo_id="nom_du_modele", token="TON_TOKEN")
    resultat = api(prompt)
    return resultat
