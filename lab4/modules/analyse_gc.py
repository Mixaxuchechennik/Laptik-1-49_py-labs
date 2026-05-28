from Bio.SeqUtils import gc_fraction

def analyse_gc(records, output_dir):
    gc_data = []
    
    for record in records:
        gc_val = gc_fraction(record.seq)
        gc_data.append((gc_val, record.id, record.description))
        
    gc_data.sort()
    
    with open("output/gc_composition_report.txt", "w", encoding="utf-8") as f:
        f.write("Последовательности в порядке возрастания их GC-составов:\n\n")
        
        for gc_val, rec_id, desc in gc_data:
            line = f"{rec_id}: {desc}, GC={gc_val:.16f}\n"
            print(line.strip())
            f.write(line)
            