import pandas as pd
import os
import glob

# Folder path containing the files
folder_path = '/tscc/lustre/restricted/alexandrov-ddn/users/tiy002/projects/OC_OL/NIH_AHEAD/Second_1123/ANALYSIS/final_vcfs'

# Get a list of all file names in the folder
file_names = [os.path.basename(file_path) for file_path in glob.glob(folder_path + '/*')]

def transform_values(row):
    """Transform VCF values into IntOGen format"""
    if len(row['REF']) == len(row['ALT']): # SNP
        return pd.Series({
            'Chromosome': row['CHROM'],
            'Start_position': row['POS'],
            'End_position': row['POS'],
            'Variant_Type': 'SNP',
            'Reference_Allele': row['REF'],
            'Tumor_Seq_Allele1': row['REF'],
            'Tumor_Seq_Allele2': row['ALT']
        })
    elif len(row['REF']) > len(row['ALT']): # DEL
        return pd.Series({
            'Chromosome': row['CHROM'],
            'Start_position': row['POS'] + 1,
            'End_position': row['POS'] + len(row['REF']) - 1,
            'Variant_Type': 'DEL',
            'Reference_Allele': row['REF'][1:],
            'Tumor_Seq_Allele1': row['REF'][1:],
            'Tumor_Seq_Allele2': '-'
        })
    else: # INS
        return pd.Series({
            'Chromosome': row['CHROM'],
            'Start_position': row['POS'],
            'End_position': row['POS'] + 1,
            'Variant_Type': 'INS',
            'Reference_Allele': '-',
            'Tumor_Seq_Allele1': row['ALT'][1:],
            'Tumor_Seq_Allele2': row['ALT'][1:]
        })

def IntOGen_input(file):
    """Process a single VCF file into IntOGen format"""
    # Define column names for VCF
    vcf_columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']
    
    # Read VCF file, skipping header lines that start with '#'
    df = pd.read_csv(
        os.path.join(folder_path, file), 
        sep='\t',
        comment='#',
        names=vcf_columns,
        usecols=['CHROM', 'POS', 'REF', 'ALT']
    )
    
    # Remove "chr" prefix from chromosome column
    df['CHROM'] = df['CHROM'].str.replace('chr', '')
    
    # Transform the data
    result = df.apply(transform_values, axis=1)
    
    # Add sample name (filename without '.vcf')
    result['Tumor_Sample_Barcode'] = file[:-4]
    
    return result

# Process all files
dataframes = []
for file in file_names:
    try:
        matrix = IntOGen_input(file)
        dataframes.append(matrix)
        print(f"Processed {file} successfully")
    except Exception as e:
        print(f"Error processing {file}: {str(e)}")

# Concatenate all dataframes
if dataframes:
    result_df = pd.concat(dataframes, axis=0, ignore_index=True)
    
    # Save the result
    output_file = os.path.join(folder_path, 'data_mutations_extended.txt')
    result_df.to_csv(output_file, sep='\t', index=False)
    print(f"\nResults saved to: {output_file}")
else:
    print("No data was processed successfully")
