import re
import subprocess

morphbin = "Morph/tam_apertium_v2.1.moobj"


def process_text(data):
    result = {}
    lines = data.split("\n")
    print(lines)

    command = 'lt-proc -c ' + morphbin + " < in.tmp > out.tmp"
    # print(command)
    for line in lines:
        if line == "":
            # print(line)
            continue
        line = line.strip()
        # print(line)
        arr = line.split("\t")
        clitic_flag = 0
        sandhi_flag = 0
        pro_clitic_flag = 0
        if len(arr) > 1 and not re.search(r'\t\-', line) and not re.search(r'^#|\.\.\.|\/', line):
            # print(":iam her" +line)
            input_token = arr[1]
            input_token = re.sub(r'@', '', input_token)
            fpw = open("in.tmp", "w", encoding='utf-8')
            fpw.write(input_token + "\n")
            fpw.close()
            pid = subprocess.Popen([command],
                                   shell=True,
                                   executable="/bin/bash",
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )  # Call subprocess
            (output, err) = pid.communicate()
            pid_status = pid.wait()
            if (pid.wait() == 0):
                fp2 = open("out.tmp", "r", encoding='utf-8')
                mo = fp2.read().split("\n")
                fp2.close()
                mo = mo[0]
                try:
                    pos = arr[2]
                except:
                    pos = "POSUNK"
                if (re.search(r'\*', mo) or re.search(r'\$\^', mo)):
                    # print(arr[1])
                    if (re.search(r'[kcwp]$', arr[1])):
                        replaced_token = re.sub(r'[kcwp]$', r'', arr[1])
                        kctwp_token = re.sub(r'^.*([kcwp])$', r'\1', arr[1])
                        replaced_token = re.sub(r'@', '', replaced_token)
                        fpw = open("in.tmp", "w", encoding='utf-8')
                        fpw.write(replaced_token + "\n")
                        fpw.close()
                        pid = subprocess.Popen([command],
                                               shell=True,
                                               executable="/bin/bash",
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)  # Call subprocess
                        (output, err) = pid.communicate()
                        pid_status = pid.wait()
                        fp2 = open("out.tmp", "r", encoding='utf-8')
                        mo = fp2.read().split("\n")
                        fp2.close()
                        mo = mo[0]  # re.sub(r'^\n', '', mo)
                        if (re.search(r'\*', mo) or re.search(r'\$\^', mo)):
                            dont_print = 0
                            # print(arr[0] + "\t" + arr[1] + "\t" + pos + "\t" + "MOUNK")
                        else:
                            # mo = mo + "^" + kctwp_token + "$"
                            mo = re.sub(r'<suffix:(.*?)>', r'<suffix:\1><sandhi:' + kctwp_token + '>', mo)
                            print(arr[0] + "\t" + arr[1] + "\t" + pos + "\t" + mo)
                            result[f"{arr[1]}"] = [f"{arr[1]}\t{pos}\t{mo}"]
                            sandhi_flag = 1
                    if (re.search(r'[iIE]yum$|[iIE]yA$|[iIE]ye$|[iIE]yo$', arr[1]) or re.search(
                            r'([aAeoOV]+)vum$|([aAeoOV]+)vA$|([aAeoOV]+)ve$|([aAeoOV]+)vo$', arr[1]) or re.search(
                        r'([^aeiouAEIOV]+)um$|([^aeiouAEIOV]+)A$|([^aeiouAEIOV]+)e$|([^aeiouAEIOV]+)o$',
                        arr[1] or re.search(
                            r'[iIE]yeye$|([aAeoOV]+)veye$|([^aeiouAEIOV]+)eye$|[iIE]yume$|([aAeoOV]+)vume$|([^aeiouAEIOV]+)ume$',
                            arr[1])) and sandhi_flag == 0):
                        if (re.search(r'ume$', arr[1])):
                            replaced_token = re.sub(r'([vy]?)ume$', r'', arr[1])
                            clitic_token = re.sub(r'^(.*)([vy]?)ume$', r'um_e', arr[1])
                            replaced_token = re.sub(r'@', '', replaced_token)
                        elif (re.search(r'um$', arr[1])):
                            replaced_token = re.sub(r'([vy]?)um$', r'', arr[1])
                            clitic_token = re.sub(r'^(.*)([vy]?)um$', r'um', arr[1])
                            replaced_token = re.sub(r'@', '', replaced_token)
                        elif (re.search(r'A$', arr[1])):
                            replaced_token = re.sub(r'([vy]?)A$', r'', arr[1])
                            clitic_token = re.sub(r'^(.*)([vy]?)A$', r'A', arr[1])
                            replaced_token = re.sub(r'@', '', replaced_token)
                        elif (re.search(r'eye$', arr[1])):
                            replaced_token = re.sub(r'([vy]?)eye$', r'', arr[1])
                            clitic_token = re.sub(r'^(.*)([vy]?)eye$', r'e_e', arr[1])
                            replaced_token = re.sub(r'@', '', replaced_token)
                        elif (re.search(r'e$', arr[1])):
                            replaced_token = re.sub(r'([vy]?)e$', r'', arr[1])
                            clitic_token = re.sub(r'^(.*)([vy]?)e$', r'e', arr[1])
                            replaced_token = re.sub(r'@', '', replaced_token)
                        elif (re.search(r'o$', arr[1])):
                            replaced_token = re.sub(r'([vy]?)o$', r'', arr[1])
                            clitic_token = re.sub(r'^(.*)([vy]?)o$', r'o', arr[1])
                            replaced_token = re.sub(r'@', '', replaced_token)
                        fpw = open("in.tmp", "w", encoding='utf-8')
                        fpw.write(replaced_token + "\n")
                        fpw.close()
                        pid = subprocess.Popen([command],
                                               shell=True,
                                               executable="/bin/bash",
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)  # Call subprocess
                        (output, err) = pid.communicate()
                        pid_status = pid.wait()
                        fp2 = open("out.tmp", "r", encoding='utf-8')
                        mo = fp2.read().split("\n")
                        fp2.close()
                        mo = mo[0]  # re.sub(r'^\n', '', mo)
                        if (re.search(r'\*', mo) or re.search(r'\$\^', mo)):
                            if (
                                    re.search(
                                        r'([^aeiouAEIOV]+)um$|([^aeiouAEIOV]+)A$|([^aeiouAEIOV]+)e$|([^aeiouAEIOV]+)o$',
                                        arr[1])):
                                if (re.search(r'um$', arr[1])):
                                    replaced_token = re.sub(r'm$', r'', arr[1])
                                    clitic_token = re.sub(r'^(.*)m$', r'um', arr[1])
                                    replaced_token = re.sub(r'@', '', replaced_token)
                                elif (re.search(r'A$', arr[1])):
                                    replaced_token = re.sub(r'A$', r'u', arr[1])
                                    clitic_token = re.sub(r'^(.*)A$', r'A', arr[1])
                                    replaced_token = re.sub(r'@', '', replaced_token)
                                elif (re.search(r'e$', arr[1])):
                                    replaced_token = re.sub(r'e$', r'u', arr[1])
                                    clitic_token = re.sub(r'^(.*)e$', r'e', arr[1])
                                    replaced_token = re.sub(r'@', '', replaced_token)
                                elif (re.search(r'o$', arr[1])):
                                    replaced_token = re.sub(r'o$', r'u', arr[1])
                                    clitic_token = re.sub(r'^(.*)o$', r'o', arr[1])
                                    replaced_token = re.sub(r'@', '', replaced_token)
                                fpw = open("in.tmp", "w", encoding='utf-8')
                                fpw.write(replaced_token + "\n")
                                fpw.close()
                                pid = subprocess.Popen([command],
                                                       shell=True,
                                                       executable="/bin/bash",
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)  # Call subprocess
                                (output, err) = pid.communicate()
                                pid_status = pid.wait()
                                fp2 = open("out.tmp", "r", encoding='utf-8')
                                mo = fp2.read().split("\n")
                                fp2.close()
                                mo = mo[0]  # re.sub(r'^\n', '', mo)
                                if (re.search(r'\*', mo) and sandhi_flag == 0):
                                    dont_print = 0
                                    # print(arr[0] + "\t" + arr[1] + "\t" + pos + "\t" + "MOUNK")
                                else:
                                    mo = re.sub(r'<suffix:(.*?)>', r'<suffix:\1><clitic:' + clitic_token + '>', mo)
                                    print(arr[0] + "\t" + arr[1] + "\t" + pos + "\t" + mo)
                                    result[f"{arr[1]}"] = [f"{arr[1]}\t{pos}\t{mo}"]
                                    clitic_flag = 1
                        else:
                            # mo = mo + "^" + kctwp_token + "$"
                            mo = re.sub(r'<suffix:(.*?)>', r'<suffix:\1><clitic:' + clitic_token + '>', mo)
                            print(arr[0] + "\t" + arr[1] + "\t" + pos + "\t" + mo)
                            result[f"{arr[1]}"] = [f"{arr[1]}\t{pos}\t{mo}"]
                            clitic_flag = 1
                    # for split words ak,ik
                    if (re.search(
                            r'^ak|^ik|^eVk|^ac|^eVc|^ic|^aw|^eVw|^iw|^an|^in|^eVn|^ap|^eVp|^ip|^am|^eVm|^im|^av|^avv|^eVv|^eVvv|^iv|^ivv',
                            arr[1]) and sandhi_flag == 0 and clitic_flag == 0):
                        replaced_token = re.sub(
                            r'^ak|^ik|^eVk|^ac|^eVc|^ic|^aw|^eVw|^iw|^an|^in|^eVn|^ap|^eVp|^ip|^am|^eVm|^im|^av|^avv|^eVv|^eVvv|^iv|^ivv',
                            r'', arr[1])
                        pro_clitic_token = re.sub(
                            r'(^ak|^ik|^eVk|^ac|^eVc|^ic|^aw|^eVw|^iw|^an|^in|^eVn|^ap|^eVp|^ip|^am|^eVm|^im|^av|^avv|^eVv|^eVvv|^iv|^ivv).*',
                            r'\1', arr[1])
                        replaced_token = re.sub(r'@', '', replaced_token)
                        if (replaced_token == ""):
                            replaced_token = arr[1]
                        fpw = open("in.tmp", "w", encoding='utf-8')
                        fpw.write(replaced_token + "\n")
                        fpw.close()
                        pid = subprocess.Popen([command],
                                               shell=True,
                                               executable="/bin/bash",
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)  # Call subprocess
                        (output, err) = pid.communicate()
                        pid_status = pid.wait()
                        fp2 = open("out.tmp", "r", encoding='utf-8')
                        mo = fp2.read().split("\n")
                        fp2.close()
                        mo = mo[0]  # re.sub(r'^\n', '', mo)
                        if (re.search(r'\*', mo) or re.search(r'\$\^', mo)):
                            dont_print = 0
                            print(arr[0] + "\t" + arr[1] + "\t" + pos + "\t" + "MOUNK")
                            result[f"{arr[1]}"] = [f"{arr[1]}\t{pos}\t{arr[1]}"]
                        else:
                            # mo = mo + "^" + kctwp_token + "$"
                            mo = re.sub(r'<suffix:(.*?)>', r'<suffix:\1><pro_clitic:' + pro_clitic_token + '>$', mo)
                            print(arr[0] + "\t" + arr[1] + "\t" + pos + "\t" + mo)
                            result[f"{arr[1]}"] = [f"{arr[1]}\t{pos}\t{mo}"]
                            pro_clitic_flag = 1
                    else:
                        if sandhi_flag == 0 and clitic_flag == 0 and pro_clitic_flag == 0:
                            print(arr[0] + "\t" + arr[1] + "\t" + pos + "\t" + "MOUNK")
                            result[f"{arr[1]}"] = [f"{arr[1]}\t{pos}\t{arr[1]}"]
                else:
                    print(arr[0] + "\t" + arr[1] + "\t" + pos + "\t" + mo)
                    result[f"{arr[1]}"] = [f"{arr[1]}\t{pos}\t{mo}"]
            else:
                print(line)
        else:
            if (len(arr) > 1 and re.search(r'(\@|\/|\.\.\.)', arr[1])):
                print(arr[0] + "\t" + arr[1] + "\t" + arr[2] + "\t^" + arr[1] + "/" + arr[1] + "<lcat:punc>$")
                result[f"{arr[1]}"] = [f"{arr[1]}\t{arr[2]}\t^{arr[1]}/{arr[1]}<lcat:punc>$"]
            else:
                print(line)
    return result
