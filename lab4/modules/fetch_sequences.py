from Bio import SeqIO

def fetch_sequences(file_path):
    records = list(SeqIO.parse(file_path, "genbank"))
    unique_organisms = set()
    total_cds_count = 0
    
    for record in records:
        organism = record.annotations.get("organism")
        if organism:
            unique_organisms.add(organism)
            
        for feature in record.features:
            if feature.type == "CDS":
                total_cds_count += 1
                
    print(f"Найдено организмов: {len(unique_organisms)} {list(unique_organisms)}")
    print(f"Всего кодирующих последовательностей (CDS): {total_cds_count}")
    
    if len(unique_organisms) < 2:
        print("Внимание! В файле менее 2 различных видов организмов.")
        
    if total_cds_count < 10:
        print("Внимание! Суммарное количество областей CDS в файле меньше 10.")
        
    return records
    