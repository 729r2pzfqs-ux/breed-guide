#!/usr/bin/env python3
"""Fix JSON-LD schema translations in Spanish breed pages."""

import os
import re
import json
from pathlib import Path

ES_BREEDS_DIR = Path(__file__).parent / "es" / "breeds"

# Translation mappings for common English phrases to Spanish
TRANSLATIONS = [
    # Multi-word phrases first (order matters!)
    (r"\bdog breeds\b", "razas de perros"),
    (r"\bdog breed\b", "raza de perros"),
    (r"\bperro razas\b", "razas de perros"),
    (r"\bfamily pets\b", "mascotas familiares"),
    (r"\bfamily pet\b", "mascota familiar"),
    (r"\bfamily dogs\b", "perros de familia"),
    (r"\bfamily dog\b", "perro de familia"),
    (r"\bworking dogs\b", "perros de trabajo"),
    (r"\bworking dog\b", "perro de trabajo"),
    (r"\btherapy dogs\b", "perros de terapia"),
    (r"\btherapy dog\b", "perro de terapia"),
    (r"\bguard dogs\b", "perros guardianes"),
    (r"\bguard dog\b", "perro guardián"),
    (r"\bwatchdogs\b", "perros guardianes"),
    (r"\bwatchdog\b", "perro guardián"),
    (r"\bworking perros\b", "perros de trabajo"),
    (r"\btherapy perros\b", "perros de terapia"),
    (r"\bfamily perros\b", "perros de familia"),
    
    # Sentence starters
    (r"\bThey're\b", "Son"),
    (r"\bThey are\b", "Son"),
    (r"\bTheir\b", "Su"),
    (r"\bThey\b", "Son"),
    (r"\bThe\b", "El"),
    (r"\bThis\b", "Esta"),
    (r"\bThese\b", "Estos"),
    
    # Common phrases
    (r"\bis one of\b", "es una de"),
    (r"\bare one of\b", "son una de"),
    (r"\bmost popular\b", "las más populares"),
    (r"\bmakes them\b", "los hace"),
    (r"\bmake them\b", "los hacen"),
    (r"\bmake excellent\b", "son excelentes"),
    (r"\bmakes excellent\b", "son excelentes"),
    (r"\bis known for being\b", "es conocido por ser"),
    (r"\bare known for being\b", "son conocidos por ser"),
    (r"\bis known for\b", "es conocido por"),
    (r"\bare known for\b", "son conocidos por"),
    (r"\bwith children\b", "con niños"),
    (r"\bwho enjoy\b", "que disfrutan de"),
    (r"\bwho love\b", "que aman"),
    (r"\bwho want\b", "que quieren"),
    (r"\bwho need\b", "que necesitan"),
    (r"\btheir intelligence\b", "su inteligencia"),
    
    # Health section
    (r"\bGenerally healthy\b", "Generalmente saludables"),
    (r"\bCommon concerns include\b", "Las preocupaciones comunes incluyen"),
    (r"\bRegular veterinary checkups\b", "Los chequeos veterinarios regulares"),
    (r"\bpreventive care\b", "el cuidado preventivo"),
    (r"\bare important\b", "son importantes"),
    (r"\bis important\b", "es importante"),
    (r"\bMaintaining a healthy weight\b", "Mantener un peso saludable"),
    (r"\bhelps prevent\b", "ayuda a prevenir"),
    (r"\bhealth issues\b", "problemas de salud"),
    (r"\bhip dysplasia\b", "displasia de cadera"),
    (r"\bbloat\b", "torsión gástrica"),
    (r"\blifespan of\b", "esperanza de vida de"),
    
    # Exercise section
    (r"\bHigh energy\b", "Alta energía"),
    (r"\brequiring vigorous daily exercise\b", "que requiere ejercicio vigoroso diario"),
    (r"\brequiring daily exercise\b", "que requiere ejercicio diario"),
    (r"\brequiring\b", "que requiere"),
    (r"\bat least an hour\b", "al menos una hora"),
    (r"\bof activity\b", "de actividad"),
    (r"\bThey thrive with\b", "Prosperan con"),
    (r"\bthrive with\b", "prosperan con"),
    (r"\bactive families\b", "familias activas"),
    (r"\bactivo families\b", "familias activas"),
    (r"\boutdoor activities\b", "actividades al aire libre"),
    (r"\bMental stimulation\b", "La estimulación mental"),
    (r"\bthrough training\b", "a través del entrenamiento"),
    (r"\bpuzzle toys\b", "juguetes de rompecabezas"),
    (r"\bis equally important\b", "es igualmente importante"),
    (r"\bWithout adequate exercise\b", "Sin ejercicio adecuado"),
    (r"\bthey may develop\b", "pueden desarrollar"),
    (r"\bbehavioral issues\b", "problemas de comportamiento"),
    
    # Grooming section
    (r"\bHeavy shedders\b", "Sueltan mucho pelo"),
    (r"\bregular brushing\b", "cepillado regular"),
    (r"\bdaily during shedding season\b", "diario durante la temporada de muda"),
    (r"\bfeathered coat\b", "pelaje emplumado"),
    (r"\bneeds attention\b", "necesita atención"),
    (r"\bto prevent matting\b", "para evitar enredos"),
    (r"\bLow maintenance\b", "Bajo mantenimiento"),
    (r"\blow maintenance\b", "bajo mantenimiento"),
    (r"\bminimal grooming\b", "aseo mínimo"),
    (r"\boccasional brushing\b", "cepillado ocasional"),
    (r"\bweekly brushing\b", "cepillado semanal"),
    
    # History section
    (r"\bDeveloped in\b", "Desarrollado en"),
    (r"\bOriginated in\b", "Originado en"),
    (r"\bBred in\b", "Criado en"),
    (r"\bmid-19th century\b", "mediados del siglo XIX"),
    (r"\b19th century\b", "el siglo XIX"),
    (r"\b20th century\b", "el siglo XX"),
    (r"\bmediados del siglo XIX siglo\b", "mediados del siglo XIX"),
    (r"\bwho crossed\b", "que cruzó"),
    (r"\bto create\b", "para crear"),
    (r"\bfor retrieving\b", "para recuperar"),
    (r"\bwaterfowl\b", "aves acuáticas"),
    (r"\bScotland\b", "Escocia"),
    (r"\bEngland\b", "Inglaterra"),
    (r"\bGermany\b", "Alemania"),
    (r"\bFrance\b", "Francia"),
    
    # Temperament section
    (r"\bmature slowly\b", "maduran lentamente"),
    (r"\benergy well into adulthood\b", "energía hasta bien entrada la edad adulta"),
    (r"\bGreat with kids\b", "Geniales con niños"),
    (r"\bgreat with kids\b", "geniales con niños"),
    (r"\bGreat with children\b", "Geniales con niños"),
    (r"\bgreat with children\b", "geniales con niños"),
    (r"\bloyal to family\b", "leales a la familia"),
    (r"\bleal to family\b", "leal a la familia"),
    (r"\bto family\b", "a la familia"),
    (r"\bother pets\b", "otras mascotas"),
    (r"\bnature makes them\b", "naturaleza los hace"),
    
    # Socialization
    (r"\bEarly socialization\b", "La socialización temprana"),
    (r"\bearly socialization\b", "la socialización temprana"),
    (r"\bare recommended\b", "son recomendados"),
    (r"\bis recommended\b", "es recomendado"),
    
    # Adjectives
    (r"\bfriendly\b", "amigable"),
    (r"\btolerant\b", "tolerante"),
    (r"\bfabulous\b", "fabulosas"),
    (r"\bintelligent\b", "inteligente"),
    (r"\bhighly capable\b", "altamente capaces"),
    (r"\boutgoing\b", "extrovertidos"),
    (r"\btrustworthy\b", "confiables"),
    (r"\beager to please\b", "deseosos de complacer"),
    (r"\bwonderful\b", "maravillosos"),
    (r"\bpatient\b", "paciente"),
    (r"\bgentle\b", "gentil"),
    (r"\bexcellent\b", "excelentes"),
    (r"\bfun-loving\b", "amantes de la diversión"),
    (r"\bplayful\b", "juguetón"),
    (r"\bloyal\b", "leal"),
    (r"\bprotective\b", "protector"),
    (r"\baffectionate\b", "cariñoso"),
    (r"\balert\b", "alerta"),
    (r"\bbrave\b", "valiente"),
    (r"\bcalm\b", "tranquilo"),
    (r"\bconfident\b", "seguro"),
    (r"\bcurious\b", "curioso"),
    (r"\bdetermined\b", "determinado"),
    (r"\bdignified\b", "digno"),
    (r"\benergetic\b", "enérgico"),
    (r"\bindependent\b", "independiente"),
    (r"\bstubborn\b", "terco"),
    (r"\bsensitive\b", "sensible"),
    (r"\breserved\b", "reservado"),
    (r"\bspirited\b", "animado"),
    (r"\bsweet\b", "dulce"),
    (r"\bversatile\b", "versátil"),
    (r"\bactive\b", "activo"),
    (r"\bstrong\b", "fuerte"),
    (r"\bathletic\b", "atlético"),
    (r"\bgraceful\b", "elegante"),
    (r"\belegant\b", "elegante"),
    (r"\bwary\b", "desconfiado"),
    (r"\bclever\b", "inteligente"),
    (r"\bsmart\b", "inteligente"),
    (r"\bbold\b", "audaz"),
    (r"\bfearless\b", "intrépido"),
    (r"\bnoble\b", "noble"),
    (r"\bdevoted\b", "devoto"),
    (r"\bsociable\b", "sociable"),
    (r"\bfrisky\b", "juguetón"),
    (r"\blively\b", "vivaz"),
    (r"\bquiet\b", "tranquilo"),
    (r"\bmellow\b", "tranquilo"),
    (r"\brelaxed\b", "relajado"),
    (r"\bcheerful\b", "alegre"),
    (r"\bhappy\b", "feliz"),
    (r"\bcharming\b", "encantador"),
    (r"\bcourageous\b", "valiente"),
    (r"\badaptable\b", "adaptable"),
    (r"\bobedient\b", "obediente"),
    (r"\bresponsive\b", "receptivo"),
    (r"\bperfect\b", "perfecto"),
    
    # Common verbs
    (r"\bmaintain\b", "mantienen"),
    (r"\bare\b", "son"),
    
    # Dog-related terms
    (r"\bdogs\b", "perros"),
    (r"\bdog\b", "perro"),
    (r"\bpuppies\b", "cachorros"),
    (r"\bpuppy-like\b", "de cachorro"),
    (r"\bpuppy\b", "cachorro"),
    (r"\bpups\b", "cachorros"),
    (r"\bpup\b", "cachorro"),
    (r"\bgunperro\b", "perro de caza"),
    (r"\bgundog\b", "perro de caza"),
    (r"\bbreed\b", "raza"),
    (r"\bbreeds\b", "razas"),
    
    # Common words
    (r"\birresistible\b", "irresistibles"),
    (r"\bcompanion\b", "compañero"),
    (r"\bcompanions\b", "compañeros"),
    (r"\battitude\b", "actitud"),
    (r"\bfaces\b", "caras"),
    (r"\bexpressive\b", "expresivas"),
    (r"\bintelligence\b", "inteligencia"),
    (r"\bnature\b", "naturaleza"),
    (r"\bsocialization\b", "socialización"),
    (r"\btraining\b", "entrenamiento"),
    (r"\bfamilies\b", "familias"),
    (r"\bchildren\b", "niños"),
    (r"\byears\b", "años"),
    (r"\bcentury\b", "siglo"),
    (r"\bduring\b", "durante"),
    (r"\btherapy\b", "terapia"),
    (r"\bworking\b", "de trabajo"),
    
    # Function words (be careful with these - at end)
    (r"\bmany\b", "muchos"),
    (r"\btheir\b", "su"),
    (r"\bwith a\b", "con una"),
    (r"\bwith\b", "con"),
    (r"\band\b", "y"),
    (r"\bfor\b", "para"),
    (r"\bof\b", "de"),
    (r"\bor\b", "o"),
    (r"\bin\b", "en"),
    (r"\bon\b", "en"),
    (r"\bas\b", "como"),
    (r"\bbut\b", "pero"),
    (r"\bfrom\b", "de"),
    (r"\bby\b", "por"),
    
    # "a" as article when followed by noun - don't translate standalone "a" as it might be Spanish preposition
    (r"\ba yellow\b", "un amarillo"),
    (r"\ba retriever\b", "un retriever"),
    (r"\ba healthy\b", "un saludable"),
]

def translate_text(text: str) -> str:
    """Apply all translations to text."""
    result = text
    
    for pattern, replacement in TRANSLATIONS:
        result = re.sub(pattern, replacement, result)
    
    # Post-processing fixes for common issues
    post_fixes = [
        (r"\bun la familia\b", "a la familia"),
        (r"\bayuda un prevenir\b", "ayuda a prevenir"),
        (r"\bun través del\b", "a través del"),
        (r"\bmedial del siglo XIX siglo\b", "mediados del siglo XIX"),
        (r"\bleal un\b", "leal a"),
        (r"\bto the\b", "a la"),
        (r"\bto be\b", "ser"),
        (r"\bto prevent\b", "para prevenir"),
        (r"\bhelps to\b", "ayuda a"),
    ]
    
    for pattern, replacement in post_fixes:
        result = re.sub(pattern, replacement, result)
    
    # Fix double spaces
    result = re.sub(r'\s+', ' ', result).strip()
    
    return result

def extract_jsonld_blocks(content: str) -> list:
    """Extract all JSON-LD script blocks from HTML content."""
    pattern = r'<script type="application/ld\+json">\s*(.*?)\s*</script>'
    return re.findall(pattern, content, re.DOTALL)

def fix_jsonld_in_file(filepath: Path) -> bool:
    """Fix JSON-LD in a single HTML file. Returns True if changes were made."""
    content = filepath.read_text(encoding='utf-8')
    original_content = content
    
    # Find all JSON-LD blocks
    pattern = r'(<script type="application/ld\+json">)\s*(.*?)\s*(</script>)'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    for match in reversed(matches):  # Reverse to preserve positions
        json_str = match.group(2)
        
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            continue
        
        # Check if this has the about.description structure we need
        if 'about' not in data or 'description' not in data.get('about', {}):
            continue
        
        desc = data['about']['description']
        if not isinstance(desc, dict):
            continue
        
        changed = False
        
        # Translate each field
        for field in ['overview', 'temperament', 'health', 'exercise', 'history', 'grooming']:
            if field in desc and isinstance(desc[field], str):
                original = desc[field]
                translated = translate_text(original)
                if translated != original:
                    desc[field] = translated
                    changed = True
        
        if changed:
            # Reconstruct JSON with proper formatting
            new_json = json.dumps(data, ensure_ascii=False, indent=4)
            new_block = f'{match.group(1)}\n    {new_json}\n    {match.group(3)}'
            content = content[:match.start()] + new_block + content[match.end():]
    
    if content != original_content:
        filepath.write_text(content, encoding='utf-8')
        return True
    return False

def main():
    html_files = list(ES_BREEDS_DIR.glob("*.html"))
    print(f"Found {len(html_files)} HTML files in es/breeds/")
    
    fixed = 0
    for filepath in sorted(html_files):
        if fix_jsonld_in_file(filepath):
            print(f"  Fixed: {filepath.name}")
            fixed += 1
    
    print(f"\nFixed {fixed} files")

if __name__ == "__main__":
    main()
