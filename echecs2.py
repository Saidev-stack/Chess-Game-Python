from qtido import *
def dessiner_cases_vide(f, ligne, colonne):
	if (ligne + colonne) % 2 == 0:
		couleur(f, 0.5, 0.5, 0.5)
	else:
		couleur(f, 1, 1, 1)
	
	rectangle(f, ligne * 100, colonne * 100, (ligne + 1) * 100, (colonne + 1) * 100)
	
def tracer_plateau(f):
	for i in range(8):
		for j in range(8):
			dessiner_cases_vide(f, i, j)

def initialiser_echiquier():
	echiquier = []
	echiquier.append(["tour-N", "fou-N", "chevalier-N", "reine-N", "roi-N", "chevalier-N", "fou-N", "tour-N"])
	echiquier.append(["pion-N"] * 8)
	for i in range(4):
		echiquier.append([""] * 8)	
	echiquier.append(["pion-B"] * 8)
	echiquier.append(["tour-B", "fou-B", "chevalier-B", "reine-B", "roi-B", "chevalier-B", "fou-B", "tour-B"])	
	return echiquier

'''def remplir_et_tracer_echiquier(f, echiquier):
	for i in range(8):
		for j in range(8):
			piece = echiquier[7 - i][j]
			if piece != "":
				couleur(f, 0, 0, 0)
				texte(f, j * 100 + 10, 100 * i + 50, 12, piece)'''

def afficher_code_cases(f):
	lettre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	for i in range(8):
		texte(f, 810, i * 100 + 50, 12, str(i + 1))
	for j in range(8):
		texte(f, j * 100 + 50, 850, 12, lettre[j])

def de_code_a_num_case(code_case):
	lettre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	colonne = lettre.index(code_case[0])
	ligne = 8 - int(code_case[1])
	return [ligne, colonne]

def verifier_num_case(code):
	if len(code) != 2:
		return False	
	lettres = ['A','B','C','D','E','F','G','H']
	if code[0] not in lettres:
		return False	
	if code[1] not in ['1','2','3','4','5','6','7','8']:
		return False	
	return True

def mise_a_jour_echiquier(echi, case_a_bouger, nouvelle_case):
	cca = de_code_a_num_case(case_a_bouger)
	ccn = de_code_a_num_case(nouvelle_case)
	echi[ ccn[0] ][ ccn[1] ] = echi[ cca[0] ][ cca[1]] 
	echi[ cca[0] ][ cca[1] ] = ""
	return echi

'''f1 = creer(800, 800)
dessiner_cases_vide(f1, 0, 0)
tracer_plateau(f1)
remplir_et_tracer_echiquier(f1, initialiser_echiquier())
afficher_code_cases(f1)
attendre_fermeture(f1)'''

def tracer_pion(f, x, y):
	disque(f, x + 50, y + 40, 15)
	rectangle(f, x + 30, y + 40, x + 60, y + 80)

def tracer_tour(f, x, y):
	rectangle(f, x + 30, y + 40, x + 70, y + 80)
	rectangle(f, x + 25, y + 30, x + 75, y + 40)

def tracer_fou(f, x, y):
	disque(f, x + 50, y + 35, 10)
	rectangle(f, x + 45, y + 40, x + 55, y + 75)
	rectangle(f, x + 35, y + 75, x + 65, y + 85)

def tracer_chevalier(f, x, y):
	disque(f, x + 45, y + 40, 12)
	rectangle(f, x + 45, y + 40, x + 60, y + 80)
	rectangle(f, x + 35, y + 75, x + 65, y + 85)

def tracer_reine(f, x, y):
	disque(f, x + 35, y + 40, 5)
	disque(f, x + 50, y + 35, 5)
	disque(f, x + 65, y + 40, 5)
	rectangle(f, x + 30, y + 50, x + 70, y + 80)

def tracer_roi(f, x, y):
	disque(f, x + 40, y + 45, 8)
	disque(f, x + 60, y + 45, 8)
	rectangle(f, x + 47, y + 25, x + 53, y + 40)
	rectangle(f, x + 35, y + 50, x + 65, y + 85)

def dessiner_piece(f, l, c, col, p):
	x = c * 100
	y = l * 100
	if col == 'N' :
		couleur(f, 0, 0, 1)
	else :
		couleur(f, 1, 0, 0)
	if p == "pion" :
		tracer_pion(f, x, y)
	elif p == "tour" :
		tracer_tour(f, x, y)
	elif p == "fou" :
		tracer_fou(f, x, y)
	elif p == "chevalier" :
		tracer_chevalier(f, x, y)
	elif p == "reine" :
		tracer_reine(f, x, y)
	elif p == "roi" :
		tracer_roi(f, x, y)

def remplir_et_tracer_echiquier(f, echiquier):
	for i in range(8):
		for j in range(8):
			piece = echiquier[7 - i][j]
			if piece != "":
				ind_tri = piece.index('-')
				p_type = piece[:ind_tri]
				p_couleur = piece[ind_tri + 1]
				dessiner_piece(f, i, j, p_couleur, p_type)
#Test
print(de_code_a_num_case("A2"))
print(de_code_a_num_case("A3"))
print(de_code_a_num_case("B7"))

def mouvement_valider(echiquier, aboujer, ouboujer):
	l1, c1 = de_code_a_num_case(aboujer)
	l2, c2 = de_code_a_num_case(ouboujer)
	piece = echiquier[l1][c1]
	if piece == "":
		return False
	ind_tri = piece.index('-')
	p_type = piece[:ind_tri]
	p_couleur = piece[ind_tri + 1]
	if p_type == "pion":
		if p_couleur == "N":
			return (l2 == l1 + 1 and c2 == c1)
		else:
			return (l2 == l1 - 1 and c2 == c1)
	elif p_type == "tour":
		return (l1 == l2 or c1 == c2)
	elif p_type == "fou":
		return abs(l2 - l1) == abs(c2 - c1)
	elif p_type == "reine":
		return (l1 == l2 or c1 == c2 or abs(l2 - l1) == abs(c2 - c1))
	elif p_type == "roi":
		return abs(l2 - l1) <= 1 and abs(c2 - c1) <= 1
	elif p_type == "chevalier":
		return (abs(l2 - l1), abs(c2 - c1)) in [(2, 1), (1, 2)]
	else:
		return False
#Test
print(mouvement_valider(initialiser_echiquier(), "B1", "C3"))

def click_au_codecase(x, y):
	lettre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	col = x // 100
	lgn = y // 100
	lgn = 7 - lgn
	return lettre[col] + str(lgn + 1)

f = creer(900, 900)
echiquier = initialiser_echiquier()

tracer_plateau(f)
remplir_et_tracer_echiquier(f, echiquier)

mode = input("Choisir mode : clavier ou souris ? ")
if mode == "clavier":
	rep = "oui"

	while(rep == "oui"):

		print("C’est au tour du joueur 1 : ")

		case_a_bouger_j1 = input("Quel est le code de la pièce à déplacer ?")
		while not verifier_num_case(case_a_bouger_j1):
			case_a_bouger_j1 = input("Quel est le code de la pièce à déplacer ?")
	
		nouvelle_case_j1 = input("Quel est le code de la case destinataire ?")
		while not verifier_num_case(nouvelle_case_j1):
			nouvelle_case_j1 = input("Quel est le code de la case destinataire ?")

		while not mouvement_valider(echiquier, case_a_bouger_j1, nouvelle_case_j1):
			print("deplacement interdit")
			case_a_bouger_j1 = input("Quel est le code de la pièce à déplacer ?")
			nouvelle_case_j1 = input("Quel est le code de la case destinataire ?")

		mise_a_jour_echiquier(echiquier, case_a_bouger_j1, nouvelle_case_j1)
		tracer_plateau(f)
		remplir_et_tracer_echiquier(f, echiquier)

		print("C’est au tour du joueur 2 : ")
	
		case_a_bouger_j2 = input("Quel est le code de la pièce à déplacer ?")
		while not verifier_num_case(case_a_bouger_j2):
			case_a_bouger_j2 = input("Quel est le code de la pièce à déplacer ?")

		nouvelle_case_j2 = input("Quel est le code de la case destinataire ?")
		while not verifier_num_case(nouvelle_case_j2):
			nouvelle_case_j2 = input("Quel est le code de la case destinataire ?")

		while not mouvement_valider(echiquier, case_a_bouger_j2, nouvelle_case_j2):
			print("deplacement interdit")
			case_a_bouger_j2 = input("Quel est le code de la pièce à déplacer ?")
			nouvelle_case_j2 = input("Quel est le code de la case destinataire ?")

		mise_a_jour_echiquier(echiquier, case_a_bouger_j2, nouvelle_case_j2)
		tracer_plateau(f)
		remplir_et_tracer_echiquier(f, echiquier)
		rep = input("Souhaitez-vous continuer ? oui/non : ")
elif mode == "souris":
    rep = "oui"
    joueur = 1

    while rep == "oui":
        print("Tour du joueur", joueur)
        clic_valide = False
        while not clic_valide:
            attendre_evenement(f, 100)
            e = dernier_evenement(f)
            if est_souris(f, e, "PRESS"):
                x1, y1 = coordonnees_souris(f, e)
                case_a_bouger = click_au_codecase(x1, y1)

                if verifier_num_case(case_a_bouger):
                    l, c = de_code_a_num_case(case_a_bouger)
                    if echiquier[l][c] != "":
                        clic_valide = True
                    else:
                        print("Pas de pièce ici")
                else:
                    print("Case invalide")

        print("Piece choisie :", case_a_bouger)
        clic_valide = False
        while not clic_valide:
            attendre_evenement(f, 100)
            e = dernier_evenement(f)
            if est_souris(f, e, "PRESS"):
                x2, y2 = coordonnees_souris(f, e)
                nouvelle_case = click_au_codecase(x2, y2)

                if verifier_num_case(nouvelle_case):
                    clic_valide = True
                else:
                    print("Case invalide")

        print("Destination :", nouvelle_case)

        if mouvement_valider(echiquier, case_a_bouger, nouvelle_case):
            mise_a_jour_echiquier(echiquier, case_a_bouger, nouvelle_case)

            tracer_plateau(f)
            remplir_et_tracer_echiquier(f, echiquier)

            # changer joueur
            if joueur == 1:
                joueur = 2
            else:
                joueur = 1
        else:
            print("Deplacement interdit")

        rep = input("Continuer ? oui/non : ")

attendre_fermeture(f)



