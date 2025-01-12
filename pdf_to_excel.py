import PyPDF2
import openpyxl
import pandas as pd
import pdfplumber

def read_protected_pdf(pdf_path, password):
    """
    Read a password-protected PDF and extract its text content.
    """
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            
            # Decrypt the PDF with the provided password
            if not reader.decrypt(password):
                raise ValueError("Incorrect password or PDF cannot be decrypted.")
            
            content = []
            
            for page in reader.pages:
                page_text = page.extract_text()  # Use the correct method
                if page_text:
                    content.append(page_text.strip())  # Remove extra whitespace
            
            return content
    except Exception as e:
        raise ValueError(f"Failed to read PDF: {e}")

def convert_to_excel(content, output_excel_path):
    """
    Convert extracted text content to an Excel file.
    """
    try:
        df = pd.DataFrame({'Content': content})  # Store content in a DataFrame
        df.to_excel(output_excel_path, index=False, engine='openpyxl')  # Save as Excel
    except Exception as e:
        raise ValueError(f"Failed to write Excel file: {e}")

def main():
    pdf_path = input("Enter the path of the password-protected PDF: ")
    password = input("Enter the password: ")
    output_excel_path = input("Enter the desired output Excel file path (e.g., output.xlsx): ")

    try:
        pdf_content = read_protected_pdf(pdf_path, password)  # Extract PDF content
        convert_to_excel(pdf_content, output_excel_path)  # Save content to Excel
        print(f"Content successfully extracted and saved to {output_excel_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()