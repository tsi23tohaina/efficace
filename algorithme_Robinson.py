"""
    Les trois fonctions:
    -Negation: pour connaitre si une proposition est p ou ¬p (Alt+ 0172)=negation sur clavier
    -Resolution_pair: On resolue deux clauses pour trouvez le resolvant
    -Resolution: applique l'algorithme de resolution à un ensemble de clauses
"""
# p
def negation(literal):
    """Renvoie la negation d'unn littéral."""
    if literal.startswith('¬'):
        return literal[1:]
    else:
        return '¬'+literal # ¬p
    
def resolution_pair(clause1,clause2):
    """Resout une paire de clauses et renvoie le resolvant"""
    for literal in clause1:
        negated_literal = negation(literal) # ¬p
        if negated_literal in clause2: # true
            resolvent = clause1.union(clause2) # p et ¬p
            resolvent.remove(literal)
            resolvent.remove(negated_literal)
            return resolvent
        return None # false pas de resolvent

def resolution(clauses): # le clauses est une list
    """Applique l'algorithme de résolution à un ensemble de clauses"""
    new_clauses =  []
    for i in range(len(clauses)):
        for j in range(i+1,len(clauses)):
            resolvent = resolution_pair(clauses[i],clauses[j]) # return resolvent si il y a negationliteral clause1
            if resolvent is not None:
                if not resolvent : 
                    return False # contradiction trouver
                if resolvent not in clauses and resolvent not in new_clauses:
                    new_clauses.append(resolvent)
        
    if not new_clauses:
        return True # Pas de nouvelles clauses trouvée,satisfiable

    clauses.extend(new_clauses) # miala izay tsy mitovy
    return resolution(clauses) # Fonction recursive

# Exemple de clauses:
# p^q est representé par {p},{q}
# p->(r^q) devient {¬p v r},{¬p v q}
# r->(s v t) devient ¬r v s v t
# ¬r est representé par {¬s}

clauses=[
    set(['p']),
    set(['q']),
    set(['¬p','r']),
    set(['¬p','q']),
    set(['¬r','s','t']),
    set(['¬s'])
]    

# Ajouter la negation de la conclusion que nous voulons prouver (t)
clauses.append(set(['¬t']))
result = resolution(clauses) # return False
print("Peut on prouvez t ?",not result )

















