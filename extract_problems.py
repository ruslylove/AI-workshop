import pandas as pd

file_path = "แบบสอบถามก่อนการอบรม_ การประยุกต์ใช้ Generative AI สำหรับงานสายสนับสนุน คณะวิศวกรรมศาสตร์ (Respon.xlsx"

try:
    df = pd.read_excel(file_path)
    
    # Column 6 name (copy-paste from previous output might be tricky due to formatting, so access by index)
    target_col = df.columns[6]
    print(f"Target Column: {target_col}\n")
    
    # Print all unique non-null values
    responses = df[target_col].dropna().unique()
    for i, resp in enumerate(responses):
        print(f"{i+1}. {resp}")

    # Also check column 4 for general categories
    target_col_4 = df.columns[4]
    print(f"\nTarget Column 4: {target_col_4}\n")
    responses_4 = df[target_col_4].dropna().unique()
    for i, resp in enumerate(responses_4):
        print(f"{i+1}. {resp}")

except Exception as e:
    print(f"Error: {e}")
