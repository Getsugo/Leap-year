def bisextile(annee):
    if annee % 4 == 0 and annee % 100 != 0:
        return True
    elif annee % 400 == 0:
        return True
    else:
        return False


def main():

    annee = int(input("Entrez une année: "))
    if bisextile(annee):
        print("L'année est bisextile")
        return main()
    else:
        print("L'année n'est pas bisextile")
        while not bisextile(annee):
            annee += 1
        print("La prochaine année bisextile est", annee)
        return main()


if __name__ == "__main__":
    main()
