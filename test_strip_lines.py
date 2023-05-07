with open('16s_full_length281isolates.fasta', 'r') as f:
    current_name = None
    current_seq = []
    for line in f:
        if line.startswith('>'):
            if current_name is not None:
                with open(current_name + '.ab1', 'w') as out_file:
                    out_file.write('\n'.join(current_seq) + '\n')
            current_name = line.strip()[1:]
            current_seq = []
        else:
            stripped_line = line.strip()
            if stripped_line:
                current_seq.append(stripped_line)
            else:
                continue
    if current_name is not None:
        with open(current_name + '.fasta', 'w') as out_file:
            out_file.write('\n'.join(current_seq) + '\n')
