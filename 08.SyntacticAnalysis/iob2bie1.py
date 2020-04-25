def iob2bie1(taglist):
    """
    elso megoldas
    - egy uj listaba pakoljuk az atalakitott tageket
    - B-vel kezdodo es O cimkek maradnak
    - I-vel kezdodoknel ellenorizni kell, hogy mi van korulotte
    """
    
    output_list = []
    for ind, tag in enumerate(taglist):
        prev_tag = taglist[ind-1] if ind > 0 else None
        next_tag = taglist[ind+1] if ind < len(taglist)-1 else None
        # az O és B maradnak
        if tag[0] in ['B', 'O']:
            output_list.append(tag)
        # ha I tag, es utana is I jon, es elotte B vagy I volt --> belso elem
        elif tag.startswith('I') and tag == next_tag and (prev_tag == tag or prev_tag.startswith('B')):
            output_list.append(tag)
        # ha I tag, es elotte B vagy I volt (de utana nem ugyanaz jon) --> utolso elem
        elif tag.startswith('I') and (prev_tag.startswith('B') or prev_tag == tag):
            output_list.append('E' + tag[1:])
        # ha I tag, egyebkent --> egyelemu (1-)
        elif tag.startswith('I'):
            output_list.append('1' + tag[1:])
    return output_list

def iob2bie1_2(taglist):
    """
    masodik megoldas
    - lemasoljuk az input listat
      es csak azokat az elemeket csereljuk ki benne,
      amiket ki kell cserelni (B, O marad)
    """
    
    output_list = taglist[:] # lemasoljuk a listat
    # csak lecsereljuk a megfelelo elemeket
    for ind, tag in enumerate(output_list):
        prev_tag = output_list[ind-1] if ind > 0 else None
        next_tag = output_list[ind+1] if ind < len(output_list)-1 else None
        # csak az I elemet kell lecserelni
        if tag.startswith('I'):
            # ha nem belso elemet jelol
            if tag != next_tag:
                # ha nem egyelemu (E-)
                if prev_tag.startswith('B') or prev_tag == tag:
                    output_list[ind] = 'E' + tag[1:]
                # ha egyelemu (1-)
                else:
                    output_list[ind] = '1' + tag[1:]
    return output_list


if __name__ == '__main__':
    # iob tagek listaja, ezen tesztelunk
    input_iob = ['O', 'B-PERS', 'I-PERS', 'I-PERS', 'I-PERS', 'O', 'I-LOC', 'O',
                 'B-ORG', 'I-ORG', 'O', 'I-LOC', 'I-ORG', 'B-LOC', 'I-LOC', 'I-ORG',
                 'B-PERS', 'I-PERS']
    # ezzel kell, hogy megegyezzen a kimenet
    output_bie1 = ['O', 'B-PERS', 'I-PERS', 'I-PERS', 'E-PERS', 'O', '1-LOC', 'O',
                   'B-ORG', 'E-ORG', 'O', '1-LOC', '1-ORG', 'B-LOC', 'E-LOC', '1-ORG',
                   'B-PERS', 'E-PERS']
    output = iob2bie1(input_iob)
    output2 = iob2bie1_2(input_iob)
    if output_bie1 == output == output2:
        print('Működik mindkét konverter.')
    else:
        print(input_iob)
        print(output)
        print(output2)
