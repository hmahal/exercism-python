def valid_dna_strand(dna_strand):
  for n in dna_strand:
    if n not in ['C', 'G', 'T', 'A']:
      raise ValueError('Invalid DNA strand')
  return True

def to_rna(dna_strand):
  try:
    if valid_dna_strand(dna_strand):
      return dna_strand.translate(str.maketrans({'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}))
  except ValueError:
    raise ValueError