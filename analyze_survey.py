import pandas as pd
import sys

# Set file path
file_path = "แบบสอบถามก่อนการอบรม_ การประยุกต์ใช้ Generative AI สำหรับงานสายสนับสนุน คณะวิศวกรรมศาสตร์ (Respon.xlsx"

try:
    # Read Excel file
    df = pd.read_excel(file_path)
    
    # Print column names to identify relevant columns
    print("Columns:")
    for i, col in enumerate(df.columns):
        print(f"{i}: {col}")
    
    # Print first few rows of potential 'problem' or 'expectation' columns
    # Assuming columns like "สิ่งที่คาดหวัง" or "ปัญหาที่พบ" might exist. 
    # Let's print the first 5 rows to see data
    print("\n--- First 5 rows ---")
    print(df.head())
    
    # Try to identify text input columns (usually open-ended questions)
    print("\n--- Unique values in text columns ---")
    for col in df.columns:
        if df[col].dtype == 'object':
            print(f"\nColumn: {col}")
            print(df[col].dropna().unique()[:10]) # Show first 10 unique answers

except Exception as e:
    print(f"Error: {e}")
