import re


def lt2ssf(lines):
    count = 0
    result = []
    for line in lines:
        if line == "":
            result.append(line + "\n")
            continue
        line = line.strip()
        line = re.sub(r' ?\t ?', '\t', line)
        arr1 = line.split("\t")
        try:
            three = arr1[3]
        except:
            three = ''

        if (len(arr1) > 1 and not re.search(r'\t\-', line) and not re.search(r'\tSPLIT', line) and not re.search(
                r'^#|\.\.\.', line)):
            token = re.sub(r'^\^(.*?)\/.*', r'\1', three)
            fs = re.sub(r'^\^(.*?)\/(.*)', r'\2', three)
            arr = fs.split("/")
            feature_ssf = ''
            sandhi_flag = 0
            clitic_flag = 0
            pro_clitic_flag = 0
            deri_flag = 0
            hon_flag = 0
            unk_flag = 0
            for a in arr:
                if not re.search(r'lcat', a):
                    unk_flag = 1
                if re.search(r'<rcat:', a):
                    deri_flag = 1
                    rcats = re.findall(r'<rcat:([a-z]+)>', a)
                    rcats.reverse()
                    frcats = ''
                    i = 1
                    for rcat in rcats:
                        # print(rcat)
                        a = re.sub(r'<rcat:' + rcat + r'>', '', a)
                        if (len(rcats) == 1):
                            frcats = ' rcat=\'' + rcat + '\''
                        else:
                            frcats += ' rcat' + str(i) + '=\'' + rcat + '\''
                            i = i + 1
                if (re.search(r'<sandhi:', a) and unk_flag == 0):
                    sandhi_flag = 1
                    m = re.match(r'.*<sandhi:([kctwp])>.*', a)
                    sandhi_token = m.group(1)
                    a = re.sub(r'<sandhi:' + sandhi_token + r'>', '', a)
                if (re.search(r'<clitic:', a) and unk_flag == 0):
                    clitic_flag = 1
                    m = re.match(r'.*<clitic:(.*?)>.*', a)
                    clitic_token = m.group(1)
                    a = re.sub(r'<clitic:' + clitic_token + r'>', '', a)
                if (re.search(r'<hon:', a) and unk_flag == 0):
                    hon_flag = 1
                    m = re.match(r'.*<hon:(.*?)>.*', a)
                    a = re.sub(r'<hon:y>', '', a)
                if (re.search(r'<pro_clitic:', a) and unk_flag == 0):
                    pro_clitic_flag = 1
                    m = re.match(r'.*<pro_clitic:(.*?)>.*', a)
                    pro_clitic_token = m.group(1)
                    a = re.sub(r'<pro_clitic:' + pro_clitic_token + r'>', '', a)
                if (re.search(r'(lcat:noun|lcat:pronoun|lcat:adv)', a)):
                    m = re.match(r'(.*?)<lcat:(.*)><gen:(.*)><num:(.*)><per:(.*)><case:(.*)><cm:(.*)><suffix:(.*)>',
                                 a)
                    if (m.group(2) == "pronoun"):
                        cat = re.sub(r'pronoun', r'pn', m.group(2))
                    elif (m.group(2) == "noun"):
                        cat = re.sub(r'noun', r'n', m.group(2))
                    elif (m.group(2) == "numeric"):
                        cat = re.sub(r'num', r'num', m.group(2))
                    else:
                        cat = m.group(2)
                    feature_ssf += '<fs af=\'' + m.group(1) + ',' + cat + ',' + m.group(3) + ',' + m.group(
                        4) + ',' + m.group(5) + ',' + m.group(6) + ',' + m.group(7) + ',' + m.group(8) + '\'>'
                elif (re.search(r'lcat:num><gen', a)):
                    m = re.match(r'(.*?)<lcat:(.*)><gen:(.*)><num:(.*)><per:(.*)><cm:(.*)><suffix:(.*)>', a)
                    cat = re.sub(r'num', r'num', m.group(2))
                    feature_ssf += '<fs af=\'' + m.group(1) + ',' + cat + ',' + m.group(3) + ',' + m.group(
                        4) + ',' + m.group(5) + ',' + ',' + m.group(6) + ',' + m.group(7) + '\'>'
                elif (re.search(r'lcat:adj', a)):
                    m = re.match(r'(.*?)<lcat:(.*)><gen:(.*)><num:(.*)><per:(.*)><cm:(.*)><suffix:(.*)>', a)
                    cat = re.sub(r'verb', r'v', m.group(2))
                    feature_ssf += '<fs af=\'' + m.group(1) + ',' + cat + ',' + m.group(3) + ',' + m.group(
                        4) + ',' + m.group(5) + ',' + ',' + m.group(6) + ',' + m.group(7) + '\'>'
                elif (re.search(r'lcat:verb', a)):
                    m = re.match(r'(.*?)<lcat:(.*)><gen:(.*)><num:(.*)><per:(.*)><tam:(.*)><suffix:(.*)>', a)
                    cat = re.sub(r'verb', r'v', m.group(2))
                    feature_ssf += '<fs af=\'' + m.group(1) + ',' + cat + ',' + m.group(3) + ',' + m.group(
                        4) + ',' + m.group(5) + ',' + ',' + m.group(6) + ',' + m.group(7) + '\'>'
                elif (re.search(r'(lcat:avy|lcat:punc|lcat:num|lcat:det)', a)):
                    m = re.match(r'(.*?)<lcat:(.*)>', a)
                    feature_ssf += '<fs af=\'' + m.group(1) + ',' + m.group(2) + ',,,,,,\'>'
                elif (re.search(r'SYM|PUNCT', arr1[2]) or re.search(r'([\[\]\|\$])', arr1[1])):
                    feature_ssf += '<fs af=\'' + arr1[1] + ',punc,,,,,,\'>'
                elif (re.search(r'\*' + token + r'\$', a) or re.search(r'MOUNK', a) or unk_flag == 1):
                    feature_ssf += '<fs af=\'' + arr1[1] + ',unk,,,,,,\'>'
                    unk_flag = 0
                feature_ssf += '|'

                if (hon_flag == 1 and unk_flag == 0):
                    feature_ssf = re.sub(r'>\|$', r' hon=' + '\'y\'>', feature_ssf)
                    hon_flag = 0
            count = count + 1
            if (sandhi_flag == 1 and unk_flag == 0):
                feature_ssf = re.sub(r'>', r' sandhi=' + '\'' + sandhi_token + '\'>', feature_ssf)
                sandhi_flag = 0
            if (clitic_flag == 1 and unk_flag == 0):
                feature_ssf = re.sub(r'>', r' clitic=' + '\'' + clitic_token + '\'>', feature_ssf)
                clitic_flag = 0
            if (pro_clitic_flag == 1 and unk_flag == 0):
                feature_ssf = re.sub(r'>', r' pro_clitic=' + '\'' + pro_clitic_token + '\'>', feature_ssf)
                pro_clitic_flag = 0
            if (deri_flag == 1):
                feature_ssf = re.sub(r'>', r'' + frcats + '>', feature_ssf)
                deri_flag = 0
            feature_ssf = re.sub(r'\t\|', '\t', feature_ssf)
            feature_ssf = re.sub(r'\|$', '', feature_ssf)
            feature_ssf = re.sub(r'^\|+', '', feature_ssf)
            result.append(arr1[0] + "\t" + arr1[1] + "\t" + arr1[2] + "\t" + feature_ssf)
        else:
            if (re.search(r'\t\.\.\.\t', line)):
                result.append(arr1[0] + "\t" + arr1[1] + "\t" + arr1[2] + "\t" + '<fs af=\'' + arr1[1] + ',punc,,,,,,\'>')
            else:
                result.append(line)

    return result
