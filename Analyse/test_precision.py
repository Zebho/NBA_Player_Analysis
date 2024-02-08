###################################################################################################
########################### Mise en place de fonctions Utiles #####################################
###################################################################################################

def custom_predict(nouveau_joueur_scaled,model, custom_threshold=0.8472):
    """
    Input :
    - nouveau_joueur_scaled : dataframe composée des données du joueurs
    - model : model que l'on souhaite utiliser pour classifier
    - custom_threshold = 0.8472 : valeur calculé du seuil, qu'on peut modifier au besoin

    Output : Booléen
        True : Il est intéressant de le garder, car jeu sur les 5 prochaines années.
        False : Il n'est pas intéressant de le garder, il risque de ne pas jouer dans 5 ans

    """
    probs = model.predict_proba(nouveau_joueur_scaled)
    proba_1 = probs[:, 1]
    return (proba_1 > custom_threshold)
