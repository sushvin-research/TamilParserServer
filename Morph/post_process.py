import pandas
import re
import io


def repair_rules(data):
    df = pandas.read_csv(io.StringIO(data), sep='\t', skip_blank_lines=True,
                         names=['tokenno', 'token', 'root', 'pos', 'pos2', 'feat', 'relno', 'DEP', 'ud', 'misc'],
                         converters={'relno': str, 'morph': str, 'tokenno': str, 'ud': str})
    nsubj_flag = 0
    nsubj_dict = {}
    for index, row in df.iterrows():
        current_pos = str(row['pos'])
        current_root = str(row['root'])
        feats = str(row['feat'])
        current_tokenno = row['tokenno']
        current_token = row['token']

        try:
            previous_feats = str(df.loc[int(index) - 1, 'feat'])
        except:
            previous_feats = ''
        try:
            previous_pos = str(df.loc[int(index) - 1, 'pos'])
        except:
            previous_pos = ''

        try:
            current_rel = str(df.loc[int(index), 'DEP'])
        except:
            current_rel = ''

        try:
            previous_rel = str(df.loc[int(index) - 1, 'DEP'])
        except:
            previous_rel = ''

        try:
            current_rel_no = str(df.loc[int(index), 'relno'])
        except:
            current_rel_no = ''

        try:
            previous_rel_no = str(df.loc[int(index) - 1, 'relno'])
        except:
            previous_rel_no = ''

        try:
            previous_token_no = str(df.loc[int(index) - 1, 'tokenno'])
        except:
            previous_token_no = ''

        try:
            immediate_pos = str(df.loc[int(index) + 1, 'pos'])
        except:
            immediate_pos = ''

        try:
            immediate_pos2 = str(df.loc[int(index) + 2, 'pos'])
        except:
            immediate_pos2 = ''

        try:
            immediate_token = str(df.loc[int(index) + 1, 'token'])
        except:
            immediate_token = ''

        try:
            immediate_tokenno = str(df.loc[int(index) + 1, 'tokenno'])
        except:
            immediate_tokenno = ''

        try:
            current_ud = str(df.loc[int(index), 'DEP'])
        except:
            current_ud = ''

        try:
            previous_ud = str(df.loc[int(index) - 1, 'DEP'])
        except:
            previous_ud = ''

        try:
            immediate_ud = str(df.loc[int(index) + 1, 'DEP'])
        except:
            immediate_ud = ''

        try:
            current_head = str(df.loc[int(index), 'relno'])
        except:
            current_head = ''

        if "-" in row['tokenno']:
            continue
        if re.search(r'#', row['tokenno']):
            nsubj_flag = 0
            nsubj_dict = {}
            continue

        same_row_flag = 0
        if re.search(r'NOUN', current_pos) and immediate_pos == "ADP":
            if current_ud == "nsubj":
                nsubj_flag = 1
                same_row_flag = 1
                nsubj_dict[index] = {"index": index, 'head': current_head}
        if re.search(r'NOUN', current_pos) and nsubj_flag == 1 and same_row_flag == 0:
            if current_ud == "nsubj" and len(nsubj_dict) > 0:
                for i in nsubj_dict:
                    get_index = nsubj_dict[i]['index']
                    get_head = nsubj_dict[i]['head']
                    if get_head == current_head:
                        df.loc[get_index, 'DEP'] = 'obl'
                        df.loc[get_index, 'ud'] = get_head + ":obl"
        if re.search(r'ADP', current_pos) and previous_pos == "NOUN":
            df.loc[index, 'DEP'] = 'case'
            df.loc[index, 'relno'] = previous_token_no
            df.loc[index, 'ud'] = previous_token_no + ":case"

    return df.to_csv(sep="\t", index=False, header=None)
