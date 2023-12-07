def cigar_party(cigars, is_weekend):
    return cigars <= 60 and cigars >= 40 or is_weekend and cigars >= 40
