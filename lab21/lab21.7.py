
def analyse_dna(sequences):
    def gc_content():
        g_count=sequences.count('G')
        c_count=sequences.count('C')
        total_len=len(sequences)

        if total_len ==0:
             return 0
        percentage=(g_count+c_count)/total_len*100
        return percentage
     gc_percent=gc_content()
    if gc_percent > 50:
        print('the content is GC rich')
    else:
        print('the content is AT rich')