from modules.fetch_sequences import fetch_sequences
from modules.analyse_gc import analyze_gc
from modules.translate_sequences import translate_sequences

def main():
    input_file = "example_cds.gb"
    output_dir = "output"
    
    biopython_records = load_and_validate_genbank(input_file)
    analyze_and_sort_gc(biopython_records, output_dir)
    translate_cds_features(biopython_records, output_dir)
    
    print("Лабораторная работа выполнена.")

if __name__ == "__main__":
    main()
    