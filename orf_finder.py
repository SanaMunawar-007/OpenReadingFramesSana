# Don't change the Libraries
import os
import sys

#Your Code Here
class ORFFinder:
    def __init__(self):
        self.sequences = []
    # Correctly initialize class

    def read_fasta_file(self, filename):  # Implement code to read fasta file and return sequences
        with open(filename, 'r') as file:
            seq = ''
            for line in file:
                if line.startswith('>'):
                    if seq:
                        self.sequences.append(seq)
                        seq = ''
                else:
                    seq = seq + line.strip()
            if seq:
                self.sequences.append(seq)

    def find_longest_orf(self, sequence):  # Implement code to find the longest DNA ORF in a given sequence
        start_codon = 'ATG'
        stop_codons = ['TAA', 'TAG', 'TGA']
        longest_orf = ''

        for i in range(len(sequence) - 2):
            if sequence[i:i+3] == start_codon:
                for j in range(i+3, len(sequence) - 2, 3):
                    if sequence[j:j+3] in stop_codons:
                        orf = sequence[i:j+3]
                        if len(orf) > len(longest_orf):
                            longest_orf = orf
                        break
        return longest_orf

        

    def process_sequences(self):  #Implement code to process all sequences and find the overall longest DNA ORF
        longest_orf = ''
        for seq in self.sequences:
            orf = self.find_longest_orf(seq)
            if len(orf) > len(longest_orf):
                longest_orf = orf
        return longest_orf


def main(): # initialize to let various arguments pass

    filename = sys.argv[1]
    print_length = '--print_length' in sys.argv

    orf_finder = ORFFinder()
    orf_finder.read_fasta_file(filename)
    longest_orf = orf_finder.process_sequences()

    if longest_orf:
        print("Longest ORF:", longest_orf)
        if print_length:
            print("Length:", len(longest_orf))
    else:
        print("No ORFs found.")

if __name__ == "__main__":
    main()
    
