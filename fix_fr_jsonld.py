#!/usr/bin/env python3
"""Fix JSON-LD schema translations in French breed pages."""

import os
import re
import json
from pathlib import Path

FR_BREEDS_DIR = Path(__file__).parent / "fr" / "breeds"

# Translation mappings for common English phrases to French
TRANSLATIONS = [
    # Multi-word phrases first (order matters!)
    (r"\bdog breeds\b", "races de chiens"),
    (r"\bdog breed\b", "race de chien"),
    (r"\bchien races\b", "races de chiens"),
    (r"\bfamily pets\b", "animaux de compagnie"),
    (r"\bfamily pet\b", "animal de compagnie"),
    (r"\bfamily dogs\b", "chiens de famille"),
    (r"\bfamily dog\b", "chien de famille"),
    (r"\bworking dogs\b", "chiens de travail"),
    (r"\bworking dog\b", "chien de travail"),
    (r"\btherapy dogs\b", "chiens de thérapie"),
    (r"\btherapy dog\b", "chien de thérapie"),
    (r"\bguard dogs\b", "chiens de garde"),
    (r"\bguard dog\b", "chien de garde"),
    (r"\bwatchdogs\b", "chiens de garde"),
    (r"\bwatchdog\b", "chien de garde"),
    (r"\bworking chiens\b", "chiens de travail"),
    (r"\btherapy chiens\b", "chiens de thérapie"),
    (r"\bfamily chiens\b", "chiens de famille"),
    (r"\bmonkey chien\b", "chien-singe"),
    (r"\blittle terrier\b", "petit terrier"),
    (r"\bbig personality\b", "grande personnalité"),
    
    # Health-related phrases
    (r"\bRegular dental care is essential due to\b", "Des soins dentaires réguliers sont essentiels en raison de"),
    (r"\bRegular dental care\b", "Des soins dentaires réguliers"),
    (r"\bis essential due to\b", "est essentiel en raison de"),
    (r"\bflat face can cause breathing issues\b", "face plate peut causer des problèmes respiratoires"),
    (r"\bflat face\b", "face plate"),
    (r"\bcan cause breathing issues\b", "peut causer des problèmes respiratoires"),
    (r"\bbreathing issues\b", "problèmes respiratoires"),
    (r"\bextreme temperatures\b", "températures extrêmes"),
    (r"\bProne to\b", "Sujet à"),
    (r"\bprone to\b", "sujet à"),
    (r"\bpatellar luxation\b", "luxation de la rotule"),
    (r"\bheart murmurs\b", "souffles cardiaques"),
    (r"\bsmall mouth\b", "petite bouche"),
    (r"\bsmall size\b", "petite taille"),
    
    # Exercise-related phrases
    (r"\bModerate exercise needs\b", "Besoins d'exercice modérés"),
    (r"\bshort daily walks\b", "de courtes promenades quotidiennes"),
    (r"\bindoor play sessions\b", "séances de jeu en intérieur"),
    (r"\bis ideal\b", "est idéal"),
    (r"\bAffen means monkey in German\b", "Affen signifie singe en allemand"),
    (r"\bAffen means monkey en German\b", "Affen signifie singe en allemand"),
    
    # Additional phrases
    (r"\bform strong bonds\b", "forment des liens forts"),
    (r"\bform liens forts\b", "forment des liens forts"),
    (r"\bwith their family\b", "avec leur famille"),
    (r"\bwith leur family\b", "avec leur famille"),
    
    # Sentence starters
    (r"\bThey're\b", "Ils sont"),
    (r"\bThey are\b", "Ils sont"),
    (r"\bTheir\b", "Leur"),
    (r"\bThey\b", "Ils"),
    (r"\bthey\b", "ils"),
    (r"\bThe\b", "Le"),
    (r"\bThis\b", "Cette"),
    (r"\bThese\b", "Ces"),
    (r"\bDespite\b", "Malgré"),
    (r"\bdespite\b", "malgré"),
    (r"\bA\b", "Un"),
    
    # Common phrases
    (r"\bis one of\b", "est l'une des"),
    (r"\bare one of\b", "sont parmi les"),
    (r"\bmost popular\b", "les plus populaires"),
    (r"\bmakes them\b", "les rend"),
    (r"\bmake them\b", "les rendent"),
    (r"\bmake excellent\b", "font d'excellents"),
    (r"\bmakes excellent\b", "fait d'excellents"),
    (r"\bis known for being\b", "est connu pour être"),
    (r"\bare known for being\b", "sont connus pour être"),
    (r"\bis known for\b", "est connu pour"),
    (r"\bare known for\b", "sont connus pour"),
    (r"\bwith children\b", "avec les enfants"),
    (r"\bwho enjoy\b", "qui apprécient"),
    (r"\bwho love\b", "qui aiment"),
    (r"\bwho want\b", "qui veulent"),
    (r"\bwho need\b", "qui ont besoin"),
    (r"\btheir intelligence\b", "leur intelligence"),
    (r"\balways entertaining\b", "toujours divertissants"),
    
    # Health section
    (r"\bGenerally healthy\b", "Généralement en bonne santé"),
    (r"\bCommon concerns include\b", "Les préoccupations courantes incluent"),
    (r"\bRegular veterinary checkups\b", "Les examens vétérinaires réguliers"),
    (r"\bpreventive care\b", "les soins préventifs"),
    (r"\bare important\b", "sont importants"),
    (r"\bis important\b", "est important"),
    (r"\bMaintaining a healthy weight\b", "Maintenir un poids santé"),
    (r"\bhelps prevent\b", "aide à prévenir"),
    (r"\bhealth issues\b", "problèmes de santé"),
    (r"\bhip dysplasia\b", "dysplasie de la hanche"),
    (r"\bbloat\b", "torsion de l'estomac"),
    (r"\blifespan of\b", "espérance de vie de"),
    
    # Exercise section
    (r"\bHigh energy\b", "Haute énergie"),
    (r"\brequiring vigorous daily exercise\b", "nécessitant un exercice quotidien vigoureux"),
    (r"\brequiring daily exercise\b", "nécessitant un exercice quotidien"),
    (r"\brequiring\b", "nécessitant"),
    (r"\bat least an hour\b", "au moins une heure"),
    (r"\bof activity\b", "d'activité"),
    (r"\bThey thrive with\b", "Ils s'épanouissent avec"),
    (r"\bthrive with\b", "s'épanouissent avec"),
    (r"\bactive families\b", "familles actives"),
    (r"\bactif families\b", "familles actives"),
    (r"\boutdoor activities\b", "activités de plein air"),
    (r"\bMental stimulation\b", "La stimulation mentale"),
    (r"\bstimulation mentale\b", "stimulation mentale"),
    (r"\bthrough training\b", "grâce au dressage"),
    (r"\bpuzzle toys\b", "jouets de réflexion"),
    (r"\bis equally important\b", "est tout aussi importante"),
    (r"\bWithout adequate exercise\b", "Sans exercice adéquat"),
    (r"\bthey may develop\b", "ils peuvent développer"),
    (r"\bbehavioral issues\b", "des problèmes de comportement"),
    (r"\binteractif toys\b", "jouets interactifs"),
    (r"\binteractive toys\b", "jouets interactifs"),
    (r"\bbursts of energy\b", "bouffées d'énergie"),
    (r"\blove to play\b", "adorent jouer"),
    (r"\bescape artists\b", "artistes de l'évasion"),
    (r"\bfenced yard\b", "jardin clôturé"),
    
    # Grooming section
    (r"\bHeavy shedders\b", "Perdent beaucoup de poils"),
    (r"\bregular brushing\b", "brossage régulier"),
    (r"\bdaily during shedding season\b", "quotidien pendant la saison de mue"),
    (r"\bfeathered coat\b", "pelage à franges"),
    (r"\bneeds attention\b", "nécessite de l'attention"),
    (r"\bto prevent matting\b", "pour éviter les nœuds"),
    (r"\bLow maintenance\b", "Faible entretien"),
    (r"\blow maintenance\b", "faible entretien"),
    (r"\bminimal grooming\b", "toilettage minimal"),
    (r"\boccasional brushing\b", "brossage occasionnel"),
    (r"\bweekly brushing\b", "brossage hebdomadaire"),
    (r"\brough, harsh, wiry coat\b", "pelage rude et dur"),
    (r"\bRequires regular grooming appropriate for their\b", "Nécessite un toilettage régulier approprié pour leur"),
    
    # History section
    (r"\bDeveloped in\b", "Développé en"),
    (r"\bOriginated in\b", "Originaire de"),
    (r"\boriginated in\b", "originaire de"),
    (r"\bBred in\b", "Élevé en"),
    (r"\bmid-19th century\b", "milieu du XIXe siècle"),
    (r"\b19th century\b", "XIXe siècle"),
    (r"\b20th century\b", "XXe siècle"),
    (r"\bwho crossed\b", "qui a croisé"),
    (r"\bto create\b", "pour créer"),
    (r"\bfor retrieving\b", "pour rapporter"),
    (r"\bwaterfowl\b", "gibier d'eau"),
    (r"\bScotland\b", "Écosse"),
    (r"\bEngland\b", "Angleterre"),
    (r"\bGermany\b", "Allemagne"),
    (r"\bFrance\b", "France"),
    
    # Temperament section
    (r"\bmature slowly\b", "mûrissent lentement"),
    (r"\benergy well into adulthood\b", "énergie jusqu'à l'âge adulte"),
    (r"\bGreat with kids\b", "Super avec les enfants"),
    (r"\bgreat with kids\b", "super avec les enfants"),
    (r"\bGreat with children\b", "Super avec les enfants"),
    (r"\bgreat with children\b", "super avec les enfants"),
    (r"\bloyal to family\b", "loyaux envers la famille"),
    (r"\bto family\b", "envers la famille"),
    (r"\bother pets\b", "autres animaux"),
    (r"\bnature makes them\b", "nature les rend"),
    (r"\bterrier-like personality\b", "personnalité de type terrier"),
    (r"\btoy size\b", "taille toy"),
    (r"\bstrong bonds\b", "liens forts"),
    (r"\bform strong bonds\b", "forment des liens forts"),
    (r"\bcomedic expressions\b", "expressions comiques"),
    (r"\bearned them\b", "leur ont valu"),
    (r"\bnickname\b", "surnom"),
    
    # Socialization
    (r"\bEarly socialization\b", "Une socialisation précoce"),
    (r"\bearly socialization\b", "une socialisation précoce"),
    (r"\bare recommended\b", "sont recommandés"),
    (r"\bis recommended\b", "est recommandé"),
    
    # Adjectives
    (r"\bfriendly\b", "amical"),
    (r"\btolerant\b", "tolérant"),
    (r"\bfabulous\b", "fabuleux"),
    (r"\bintelligent\b", "intelligent"),
    (r"\bhighly capable\b", "très capables"),
    (r"\boutgoing\b", "extravertis"),
    (r"\btrustworthy\b", "dignes de confiance"),
    (r"\beager to please\b", "désireux de plaire"),
    (r"\bwonderful\b", "merveilleux"),
    (r"\bpatient\b", "patient"),
    (r"\bgentle\b", "doux"),
    (r"\bexcellent\b", "excellents"),
    (r"\bfun-loving\b", "qui aiment s'amuser"),
    (r"\bplayful\b", "joueur"),
    (r"\bloyal\b", "loyal"),
    (r"\bprotective\b", "protecteur"),
    (r"\baffectionate\b", "affectueux"),
    (r"\balert\b", "alerte"),
    (r"\bbrave\b", "courageux"),
    (r"\bcalm\b", "calme"),
    (r"\bconfident\b", "confiant"),
    (r"\bcurious\b", "curieux"),
    (r"\bcurieux\b", "curieux"),
    (r"\bdetermined\b", "déterminé"),
    (r"\bdignified\b", "digne"),
    (r"\benergetic\b", "énergique"),
    (r"\bindependent\b", "indépendant"),
    (r"\bstubborn\b", "têtu"),
    (r"\bsensitive\b", "sensible"),
    (r"\breserved\b", "réservé"),
    (r"\bspirited\b", "plein d'entrain"),
    (r"\bsweet\b", "doux"),
    (r"\bversatile\b", "polyvalent"),
    (r"\bactive\b", "actif"),
    (r"\bstrong\b", "fort"),
    (r"\bathletic\b", "athlétique"),
    (r"\bgraceful\b", "gracieux"),
    (r"\belegant\b", "élégant"),
    (r"\bwary\b", "méfiant"),
    (r"\bclever\b", "intelligent"),
    (r"\bsmart\b", "intelligent"),
    (r"\bbold\b", "audacieux"),
    (r"\bfearless\b", "intrépide"),
    (r"\bnoble\b", "noble"),
    (r"\bdevoted\b", "dévoué"),
    (r"\bsociable\b", "sociable"),
    (r"\bfrisky\b", "vif"),
    (r"\blively\b", "vif"),
    (r"\bquiet\b", "calme"),
    (r"\bmellow\b", "calme"),
    (r"\brelaxed\b", "détendu"),
    (r"\bcheerful\b", "joyeux"),
    (r"\bhappy\b", "heureux"),
    (r"\bcharming\b", "charmant"),
    (r"\bcourageous\b", "courageux"),
    (r"\badaptable\b", "adaptable"),
    (r"\bobedient\b", "obéissant"),
    (r"\bresponsive\b", "réceptif"),
    (r"\bperfect\b", "parfait"),
    (r"\bentertaining\b", "divertissant"),
    (r"\bjoueur\b", "joueur"),
    
    # Common verbs
    (r"\bmaintain\b", "maintiennent"),
    (r"\bare\b", "sont"),
    (r"\bcan be\b", "peut être"),
    (r"\bdespite\b", "malgré"),
    
    # Dog-related terms
    (r"\bdogs\b", "chiens"),
    (r"\bdog\b", "chien"),
    (r"\bpuppies\b", "chiots"),
    (r"\bpuppy-like\b", "de chiot"),
    (r"\bpuppy\b", "chiot"),
    (r"\bpups\b", "chiots"),
    (r"\bpup\b", "chiot"),
    (r"\bgundog\b", "chien de chasse"),
    (r"\bbreed\b", "race"),
    (r"\bbreeds\b", "races"),
    
    # Common words
    (r"\birresistible\b", "irrésistibles"),
    (r"\bcompanion\b", "compagnon"),
    (r"\bcompanions\b", "compagnons"),
    (r"\battitude\b", "attitude"),
    (r"\bfaces\b", "visages"),
    (r"\bexpressive\b", "expressifs"),
    (r"\bintelligence\b", "intelligence"),
    (r"\bnature\b", "nature"),
    (r"\bsocialization\b", "socialisation"),
    (r"\btraining\b", "dressage"),
    (r"\bfamilies\b", "familles"),
    (r"\bchildren\b", "enfants"),
    (r"\byears\b", "ans"),
    (r"\bcentury\b", "siècle"),
    (r"\bduring\b", "pendant"),
    (r"\btherapy\b", "thérapie"),
    (r"\bworking\b", "de travail"),
    (r"\bterritorial\b", "territorial"),
    (r"\btheir\b", "leur"),
    (r"\bits\b", "sa"),
    
    # Function words
    (r"\bmany\b", "beaucoup"),
    (r"\bwith a\b", "avec une"),
    (r"\bwith\b", "avec"),
    (r"\band\b", "et"),
    (r"\bfor\b", "pour"),
    (r"\bof\b", "de"),
    (r"\bor\b", "ou"),
    (r"\bin\b", "en"),
    (r"\bon\b", "sur"),
    (r"\bas\b", "comme"),
    (r"\bbut\b", "mais"),
    (r"\bfrom\b", "de"),
    (r"\bby\b", "par"),
    (r"\bhave\b", "ont"),
    (r"\bhas\b", "a"),
    
    # Additional words/phrases
    (r"\bis\b", "est"),
    (r"\bform\b", "forment"),
    (r"\bfamily\b", "famille"),
    (r"\bcan cause\b", "peut causer"),
    (r"\bcan be\b", "peut être"),
    (r"\benjoy\b", "apprécient"),
    (r"\bgames\b", "jeux"),
    (r"\bideal\b", "idéal"),
    (r"\brace\b", "race"),
    (r"\bsmall\b", "petit"),
    (r"\bshort\b", "courte"),
    (r"\bdaily\b", "quotidien"),
    (r"\bwalks\b", "promenades"),
    (r"\bto\b", "à"),
]

def translate_text(text: str) -> str:
    """Apply all translations to text."""
    result = text
    
    for pattern, replacement in TRANSLATIONS:
        result = re.sub(pattern, replacement, result)
    
    # Post-processing fixes for common issues
    post_fixes = [
        (r"\bà la famille\b", "envers la famille"),
        (r"\bun à prévenir\b", "à prévenir"),
        (r"\bà travers le\b", "grâce au"),
        (r"\bsont confiants\b", "est confiant"),
        (r"\bLe Affenpinscher\b", "L'Affenpinscher"),
        (r"\bde de\b", "de"),
        (r"\best un un\b", "est un"),
        (r"'s\b", ""),  # Remove possessive 's
        (r"\bcomme ils\b", "car ils"),
        (r"\bUn jardin\b", "Un jardin"),
        (r"\bUn Un\b", "Un"),
        (r"\bpour Un\b", "pour un"),
        (r"\bavec Un\b", "avec un"),
        (r"\best Un\b", "est un"),
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
    html_files = list(FR_BREEDS_DIR.glob("*.html"))
    print(f"Found {len(html_files)} HTML files in fr/breeds/")
    
    fixed = 0
    for filepath in sorted(html_files):
        if fix_jsonld_in_file(filepath):
            print(f"  Fixed: {filepath.name}")
            fixed += 1
    
    print(f"\nFixed {fixed} files")

if __name__ == "__main__":
    main()
