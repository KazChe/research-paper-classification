import pdfplumber
from pathlib import Path

anatomical_structures = {
    "heart": "organ",
    "liver": "organ",
    "kidney": "organ",
    "cardiac muscle": "tissue",
    "epithelial": "tissue",
    "connective": "tissue",
    "muscle tissue": "tissue",
    "nervous tissue": "tissue",
}

def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return " ".join(page.extract_text() for page in pdf.pages)

def analyze_content(text):
    text = text.lower()
    results = {}
    
    for structure, category in anatomical_structures.items():
        if (
            text.count(structure.lower()) > 2 or
            "study of " + structure in text or
            "research on " + structure in text
        ):
            results[structure] = category
    
    return results

def main():
    pdf_dir = Path("research_papers")
    
    for pdf_path in pdf_dir.glob("*.pdf"):
        try:
            text = extract_text(pdf_path)
            categories = analyze_content(text)
            
            print(f"\nPaper: {pdf_path.name}")
            print("Categories found:")
            for structure, category in categories.items():
                print(f"- {structure} ({category})")
                
        except Exception as e:
            print(f"Error processing {pdf_path.name}: {e}")

if __name__ == "__main__":
    main()