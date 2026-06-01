import os
from pypdf import PdfWriter

def combine_pdfs(pdf_list, output_filename="combined_document.pdf"):
    """
    Merges multiple PDF files into a single PDF.
    """
    # Initialize the new PdfWriter object
    merger = PdfWriter()

    print("Starting the merging process...")

    for pdf in pdf_list:
        if os.path.exists(pdf):
            try:
                merger.append(pdf)
                print(f"Successfully appended: {pdf}")
            except Exception as e:
                print(f"Error appending {pdf}: {e}")
        else:
            print(f"Warning: The file '{pdf}' was not found.")

    try:
        merger.write(output_filename)
        print(f"\nSuccess! Merged PDF saved as: {output_filename}")
    except Exception as e:
        print(f"\nFailed to save the merged PDF: {e}")
    finally:
        merger.close()

# --- Example Usage ---
if __name__ == "__main__":
    # Ensure these perfectly match the files in your folder
    files_to_merge = [
        "Research Statement.pdf",
        "CV.pdf",
        "transcript.pdf",
        "STATEMENT OF AWARD.pdf",
        "Contact info.pdf"
    ]
    
    final_output_name = "final_merged_application.pdf"

    combine_pdfs(files_to_merge, final_output_name)