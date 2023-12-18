# Don't change the Libraries
import os
import sys

#Your Code Here
class ORFFinder:
    def __init__(self):
    # Correctly initialize class
        pass
    def read_fasta_file():   # Implement code to read fasta file and return sequences
        open_fasta_file = open("randomDNA.txt", "r")
        read_fasta_file = open_fasta_file.read()
    def find_longest_orf():  # Implement code to find the longest DNA ORF in a given sequence
        start_codon = "ATG"
        stop_codon = ["TAA", "TAG", "TGA"]
        for i in range(0, len(read_fasta_file), 3):
            if read_fasta_file[i:i+3] == start_codon:
                for j in range(i+3, len(read_fasta_file), 3):
                    if read_fasta_file[j:j+3] in stop_codon:
                        print(read_fasta_file[i:j+3])
                        break
    def process_sequences(): #Implement code to process all sequences and find the overall longest DNA ORF
        pass

def main(): # initialize to let various arguments pass
    
