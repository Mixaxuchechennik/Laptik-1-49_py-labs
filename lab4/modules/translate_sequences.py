def translate_sequences(records, output_dir):
    with open("output/translation_report.txt", "w", encoding="utf-8") as f:
        f.write("Трансляция кодирующих областей (CDS):\n\n")
        
        for record in records:
            for feature in record.features:
                if feature.type == "CDS":
                    header = f"{record.id}: {record.description}\n"
                    f.write(header)
                    print(header.strip())
                    
                    location = feature.location
                    strand_sign = "+" if location.strand >= 0 else "-"
                    
                    loc_str = f"Расположение кодирующей последовательности = [{location.start}:{location.end}]({strand_sign})\n"
                    f.write(loc_str)
                    print(loc_str.strip())
                    
                    protein_seq = feature.qualifiers.get("translation", [None])[0]
                    if not protein_seq:
                        cds_nucleotides = feature.extract(record.seq)
                        protein_seq = str(cds_nucleotides.translate(cds=True))
                    
                    trans_str = f"Трансляция =\n{protein_seq}\n"
                    f.write(trans_str + "\n\n")
                    print(trans_str)
                    