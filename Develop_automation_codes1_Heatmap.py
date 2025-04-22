import pandas as pd

# File path
file_path = "D:\\Ssendi\\Week4\\wk4data.xls"

# Load the Excel file
adata = pd.read_excel(file_path)

# Rename dictionary
rename_columns = {
    "033B-CD02a. Dysentery - Cases": "Dysentery",
    "033B-CD03a. SARI - Cases": "SARI",
    "033B-CD04a. Acute Flaccid Paralysis - Cases": "AFP",
    "033B-CD05a. AEFI - Cases": "AEFI",
    "033B-CD06a. Animal bites(Suspected rabies) - Cases": "Animal_Bites(Susp_Rabies",
    "033B-CD07a. Bacterial Meningitis - Cases": "Bacterial_Meningitis",
    "033B-CD08a. Cholera - Cases": "Cholera",
    "033B-CD09a. Guinea Worm - Cases": "Guinea_Worm",
    "033B-CD10a. Measles - Cases": "Measles",
    "033B-CD11a. Neonatal tetanus - Cases": "Neonatal_Tetanus",
    "033B-CD13a. Typhoid Fever - Cases": "Typhoid_Fever",
    "033B-CD14a. Hepatitis B - Cases": "Hepatitis_B",
    "HMIS 033b - Weekly Epidemiological Surveillance Report - Reporting rate": "Completeness",
    "HMIS 033b - Weekly Epidemiological Surveillance Report - Reporting rate on time": "Timeliness",
    "033B-CD12a. Plague - Cases": "Plague",
    "033B-CD16a. Yellow Fever - Cases": "Yellow_Fever",
    "033B-CD17a. Other VHF - Cases": "Other_VHF",
    "033B-CD18a. Leprosy - Cases": "Leprosy",
    "033B-CD19a. Anthrax - Cases": "Anthrax",
    "033B-EP01a. Chikungunya - Cases": "Chikungunya",
    "033B-EP02a. Dengue - Cases": "Dengue",
    "033B-EP04a. Acute viral hepatitis - Cases": "Acute_Viral_Hepatitis",
    "033B-HI01a. Diarrhoea with dehydration <5 - Cases": "Diarr_DH20_<5",
    "033B-HI02a. Severe pneumonia <5 - Cases": "Svr_Pneumonia_<5",
    "033B-HI03a. Human African Trypanosomiasis - Cases": "Trypanosomiasis",
    "033B-HI04a. Trachoma - Cases": "Trachoma",
    "033B-HI05a. Schistosomiasis - Cases": "Schistosomiasis",
    "033B-HI08a. Brucellosis - Cases": "Brucellosis",
    "033B-TE01a. Dracunculiasis - Cases": "Dracunculiasis",
    "033B-TE03a. Buruli ulcer - Cases": "Buruli_Ulcer",
    "033B-TE05a. Noma - Cases": "Noma",
    "033B-TE08a. Smallpox - Cases": "Smallpox"
}

# Check original column names
print("Original column names:")
print(adata.columns)

# Apply renaming
adata.rename(columns=rename_columns, inplace=True)

# Check unmatched columns
unmatched_columns = [col for col in rename_columns.keys() if col not in adata.columns]
if unmatched_columns:
    print("Warning: The following columns were not found in the dataset for renaming:")
    print(unmatched_columns)

# Verify renaming
print("\nRenamed column names:")
print(adata.columns)



# Display dataset
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print("\nDataset with renamed columns:")
print(adata)
