class StrandsDNA:
    def __init__(self):
        """
        Initialize an instance of the StrandsDNA class.
        
        Parameters:
            self: Instance of the class
        """
        self.all_strands = []

    def add_strands(self, strands):
        """
        Add DNA strands to the list of all_strands.
        
        Parameters:
            strands (str): A string containing DNA strands separated by whitespace.
        """
        lst_strands = strands.split()
        for i in lst_strands:
            self.all_strands.append(i)

    def get_max_strands(self):
        """
        Get DNA strands with the maximum length.
        
        Parameters:
            None
        
        Returns:
            str: A string containing the DNA strands with the maximum length, sorted alphabetically and separated by whitespace.
        """
        m_len_strand = max(map(len, self.all_strands))
        lst_mlen = []
        for i in self.all_strands:
            if len(i) == m_len_strand:
                lst_mlen.append(i)
        return ' '.join(sorted(set(lst_mlen)))
    
    def __str__(self):
        return ' '.join(x for x in self.all_strands)


gen = StrandsDNA()
gen.add_strands('ANDG AM FUGHJDS ZDS ASDJPV ASGSAZD')
print(gen)
gen.add_strands('GJSU EWJFSN FUGHJDS')
gen.add_strands('MGRSDN RUFM')
print(gen)
print(gen.get_max_strands())