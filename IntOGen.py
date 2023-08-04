# %%
import pandas as pd
import os
import glob

# %%
# Get a list of all file names in the folder
# Folder path containing the files
folder_path = '/Users/tingyang/Desktop/IntOGen_OL/LK'

# Get a list of all file names in the folder
file_names = [os.path.basename(file_path) for file_path in glob.glob(folder_path + '/*')]

# %%
# Function to transform the vcf dataframe
def transform_values(row):
    if len(row[2]) == len(row[3]): # SNP
        return [row[0], row[1], row[1], "SNP", row[2], row[2], row[3]]
    elif len(row[2]) > len(row[3]): # DEL
        return [row[0], row[1]+ 1, row[1] + len(row[2]) -1, "DEL", row[2][1:len(row[2])], row[2][1:len(row[2])], "-"]
    else: # INS
        return [row[0], row[1], row[1] + 1, "INS", "-", row[3][1:len(row[3])], row[3][1:len(row[3])]]

# %%
def IntOGen_input(file):
    header = ['Chromosome', 'Start_position', 'End_position', 'Variant_Type', 'Reference_Allele',
          'Tumor_Seq_Allele1', 'Tumor_Seq_Allele2', 'Tumor_Sample_Barcode']
    # Read desired columns from vcf files
    df = pd.read_csv(folder_path + '/' + file, sep='\t', header=None, usecols=[0, 1, 3, 4])
    # Remove "chr" in Chromosome column
    df[0] = df[0].str.replace('chr', '')
    # Renidex 
    df = df.set_axis(range(len(df.columns)), axis=1)
    # Creating desired IntOGen info
    df = df.apply(transform_values, axis=1, result_type='expand')
    # Add a new column and remove "_final.vcf"
    df[7] = df.apply(lambda row: file[:-10], axis=1)
    # Add the new headers to the dataframe
    df.columns = header  
    return df

    

# %%
dataframes = []
for file in file_names:
    matrix = IntOGen_input(file)
    matrix
    dataframes.append(matrix)
# Concatenate the dataframes vertically with only the first dataframe's header
result_df = pd.concat(dataframes, axis=0, ignore_index=True)

# Save the dataframe as a tab-delimited text file with headers
result_df.to_csv('data_mutations_extended.txt', sep='\t', index=False)   


