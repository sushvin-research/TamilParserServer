import re

noun_ud_map_hash = {
    "0": "Case=Nom",  # cm in ssf
    "Al": "Case=Ins",  # cm in ssf
    "E": "Case=Acc",  # cm in ssf
    "il": "Case=Loc",  # cm in ssf
    "ilirunwu": "Case=Abl",  # cm in ssf
    "inY": "Case=Gen",  # cm in ssf
    "kkAka": "Case=Ben",  # cm in ssf
    "kkAnYa": "Case=Ben",  # cm in ssf
    "kku": "Case=Dat",  # cm in ssf
    "ulY": "Case=Ill",  # cm in ssf
    "utanY": "Case=Com",  # cm in ssf
    "pl": "Number=Plur",
    "sg": "Number=Sing"
}

pronoun_ud_map_hash = {
    "0": "Case=Nom",  # cm in ssf
    "Al": "Case=Ins",  # cm in ssf
    "E": "Case=Acc",  # cm in ssf
    "il": "Case=Loc",  # cm in ssf
    "ilirunwu": "Case=Abl",  # cm in ssf
    "inY": "Case=Gen",  # cm in ssf
    "kkAka": "Case=Ben",  # cm in ssf
    "kkAnYa": "Case=Ben",  # cm in ssf
    "kku": "Case=Dat",  # cm in ssf
    "ulY": "Case=Ill",  # cm in ssf
    "utanY": "Case=Com",  # cm in ssf
    "pl": "Number=Plur",
    "sg": "Number=Sing",
    "m": "Gender=Masc",
    "f": "Gender=Fem",
    "n": "Gender=Neut",
    "mf": "Gender=Fem, Masc",
    "1": "Person=1",
    "2": "Person=2",
    "3": "Person=3"
}
verb_ud_map_hash = {
    "pl": "Number=Plur",
    "sg": "Number=Sing",
    "m": "Gender=Masc",
    "f": "Gender=Fem",
    "n": "Gender=Neut",
    "mf": "Gender=Fem, Masc",
    "1": "Person=1",
    "2": "Person=2",
    "3": "Person=3",
    # tam part
    "0": "Mood=Imp|Polarity=Pos|VerbForm=Fin",
    "Awe": "Mood=Imp|Polarity=Neg|VerbForm=Fin",
    "nw": "Tense=Past|VerbForm=Fin",
    "kirY": "Tense=Pres|VerbForm=Fin",
    "pp": "Tense=Fut|VerbForm=Fin",
    "lAm": "Mood=Pot|VerbForm=Fin",
    "a": "VerbForm=Inf",
    "Al": " Mood=Cnd|Polarity=Pos",
    "A_vittAl": "Mood=Cnd|Polarity=Neg",
    "Alum": "Mood=Cnd|Polairy=Pos",
    "A_vittAlum": "Mood=Cnd|Polarity=Neg",
    "i": "Polarity=Pos|VerbForm=Conv",
    "Amal": "Polarity=Neg|VerbForm=Conv",
    "kirY_a": "Polarity=Pos|Tense=Pres|VerbForm=Part",
    "nw_a": "Polarity=Pos|Tense=Past|VerbForm=Part",
    "pp_a": "Polarity=Pos|Tense=Fut|VerbForm=Part",
    "Awa": "Polarity=Neg|VerForm=Part"
}


def ssfToUD(lines):
    result = []
    for line in lines:
        if (line == ""):
            result.append(line + "\n")
            continue
        # NOUN|PRON|PROPN|VERB|AUX
        line = line.strip()
        if (re.search('<fs', line)):
            cols = line.split("\t")
            try:
                pickone = cols[3]
            except:
                result.append(line + "\n")
                continue
            # sample pickone=<fs af='punYiwam,n,any,sg,3,o,a,a'>
            m = re.match(r'<fs af=\'(.*),(.*),(.*),(.*),(.*),(.*),(.*),([A-Za-z_0-9]*)\'', pickone)
            UD_format = 'None'
            flag = 0
            try:
                lcat = m[2]
            except:
                lcat = 'none'

            try:
                case = m[7]
            except:
                case = 'none'
            try:
                suff = m[8]
            except:
                suff = 'none'
            try:
                number = m[4]
            except:
                number = 'none'

            try:
                gender = m[3]
            except:
                gender = 'none'

            try:
                person = m[5]
            except:
                person = 'none'

            if (re.match(r'n$', lcat)):
                if (re.match(r'(0$|Al$|E$|il|ilirunwu$|inY$|kkAka$|kkAnYa$|kku$|ulY$|utanY$)', case)):
                    UD_format = noun_ud_map_hash[case]
                    flag = 1
                if (re.match(r'(sg$|pl$)', number)):
                    if (flag == 1):
                        UD_format += "|" + noun_ud_map_hash[number]
                    else:
                        UD_format = noun_ud_map_hash[number]

                udformat_arr = UD_format.split("|")
                udformat_arr.sort()
                UD_format = "|".join(udformat_arr)
            elif (re.match(r'pn$', lcat)):
                if (re.match(r'(0$|Al$|E$|il|ilirunwu$|inY$|kkAka$|kkAnYa$|kku$|ulY$|utanY$)', case)):
                    UD_format = pronoun_ud_map_hash[case]
                    flag = 1
                if (re.match(r'(sg$|pl$)', number)):
                    if (flag == 1):
                        UD_format += "|" + pronoun_ud_map_hash[number]
                        flag = 2
                    else:
                        UD_format = pronoun_ud_map_hash[number]
                        flag = 2
                if (re.match(r'(m$|f$|n$)', gender)):
                    if (flag == 2 or flag == 1):
                        UD_format += "|" + pronoun_ud_map_hash[gender]
                        flag = 3
                    else:
                        UD_format = pronoun_ud_map_hash[gender]
                        flag = 3
                if (re.match(r'(1$|2$|3$)', person)):
                    if (flag == 2 or flag == 1 or flag == 3):
                        UD_format += "|" + pronoun_ud_map_hash[person]
                        flag = 3
                    else:
                        UD_format = pronoun_ud_map_hash[person]
                        flag = 3
                    udformat_arr = UD_format.split("|")
                    udformat_arr.sort()
                    UD_format = "|".join(udformat_arr)
            elif (re.match(r'v$', lcat)):
                if (re.match(
                        r'(0$|Awe$|nw$|kirY$|pp$|lAm$|a$|Al$|A_vittAl$|Alum$|A_vittAlum$|i$|Amal$|kirY_a$|nw_a$|pp_a$|Awa$)',
                        suff)):
                    UD_format = verb_ud_map_hash[suff]
                    flag = 1
                if (re.match(r'(sg$|pl$)', number)):
                    if (flag == 1):
                        UD_format += "|" + verb_ud_map_hash[number]
                        flag = 2
                    else:
                        UD_format = verb_ud_map_hash[number]
                        flag = 2
                if (re.match(r'(m$|f$|n$)', gender)):
                    if (flag == 2 or flag == 1):
                        UD_format += "|" + verb_ud_map_hash[gender]
                        flag = 3
                    else:
                        UD_format = verb_ud_map_hash[gender]
                        flag = 3
                if (re.match(r'(1$|2$|3$)', person)):
                    if (flag == 2 or flag == 1 or flag == 3):
                        UD_format += "|" + verb_ud_map_hash[person]
                        flag = 4
                    else:
                        UD_format = verb_ud_map_hash[person]
                        flag = 4
                if (flag == 1 or flag == 2 or flag == 3 or flag == 4 or flag == 5):
                    udformat_arr = UD_format.split("|")
                    udformat_arr.sort()
                    UD_format = "|".join(udformat_arr)

            ##hon='y' then change to Polite=Form
            if (re.search(r' hon=\'?y\'?', pickone)):
                if (UD_format != ""):
                    UD_format += "|" + 'Polite=Form'
                    udformat_arr = UD_format.split("|")
                    udformat_arr.sort()
                    UD_format = "|".join(udformat_arr)
                else:
                    UD_format = 'Polite=Form'

            elif (re.match(r'num$', lcat)):
                if (re.match(r'(Avawu$)', suff)):
                    UD_format = 'NumType=Ord'
                elif (re.match(r'(0$)', suff)):
                    UD_format = 'NumType=Card'

            result.append("\t".join(cols[:3]) + "\t" + UD_format + "\t" + "\t".join(cols[3:6]))
        else:
            result.append(line + "\n")
    return result
