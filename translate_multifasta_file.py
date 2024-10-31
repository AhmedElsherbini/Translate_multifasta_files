import os
import fnmatch
from Bio import SeqIO
import argparse

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Tool to translate multifasta files')
    parser.add_argument('-i', '--input_file', type=str, help='Path to a single DNA file')
    parser.add_argument('-b', '--batch_files', type=str, help='Extension for your multifasta files .afa, .fasta , .fna')
    return parser.parse_args()

def translate_input_file(input_file):
    """Translate sequences in a single DNA file to a new FASTA file."""
    output_file = f"translated_{input_file}_file.fasta"
    with open(output_file, "w") as aa_fa:
        for dna_record in SeqIO.parse(input_file, "fasta"):
            aa_fa.write(f">{dna_record.id}\n")
            aa_fa.write(str(dna_record.seq.replace("-", "").translate(to_stop=True)) + "\n")

    

def translate_multiple_files(batch_files):
    """Translate sequences in all files matching a given extension to new FASTA files."""
    for f in os.listdir():
        if fnmatch.fnmatch(f,'*%s'%(batch_files)):
            output_file ="translated_%s_file.fasta"%(str(f).split(str(batch_files))[0])
            with open(output_file, "w") as aa_fa:
                for dna_record in SeqIO.parse(f, "fasta"):
                    aa_fa.write(f">{dna_record.id}\n")
                    aa_fa.write(str(dna_record.seq.replace("-", "").translate(to_stop=True)) + "\n")

def main():
    args = parse_arguments()
    
    if args.input_file:
        translate_input_file(args.input_file)
        print("Your file was translated successfuly!")

    elif args.batch_files:
        batch_files = args.batch_files if args.batch_files else "*.fasta"
        translate_multiple_files(batch_files)
        print("Your files were translated successfuly!")

    else:
        print("Please provide a valid mode and file path or extension.")

if __name__ == "__main__":
    main()
