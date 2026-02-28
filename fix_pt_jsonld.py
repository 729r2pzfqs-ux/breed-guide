#!/usr/bin/env python3
"""Fix JSON-LD schema translations in Portuguese breed pages."""

import os
import re
import json
from pathlib import Path

PT_BREEDS_DIR = Path(__file__).parent / "pt" / "breeds"

# Translation mappings for common English phrases to Portuguese
TRANSLATIONS = [
    # Multi-word phrases first (order matters!)
    (r"\bdog breeds\b", "raças de cães"),
    (r"\bdog breed\b", "raça de cão"),
    (r"\bcão raças\b", "raças de cães"),
    (r"\bcão raça\b", "raça de cão"),
    (r"\bfamily pets\b", "animais de estimação"),
    (r"\bfamily pet\b", "animal de estimação"),
    (r"\bfamily dogs\b", "cães de família"),
    (r"\bfamily dog\b", "cão de família"),
    (r"\bworking dogs\b", "cães de trabalho"),
    (r"\bworking dog\b", "cão de trabalho"),
    (r"\bworking cãos\b", "cães de trabalho"),
    (r"\bworking cão\b", "cão de trabalho"),
    (r"\btherapy dogs\b", "cães de terapia"),
    (r"\btherapy dog\b", "cão de terapia"),
    (r"\btherapy cãos\b", "cães de terapia"),
    (r"\btherapy cão\b", "cão de terapia"),
    (r"\bguard dogs\b", "cães de guarda"),
    (r"\bguard dog\b", "cão de guarda"),
    (r"\bwatchdogs\b", "cães de guarda"),
    (r"\bwatchdog\b", "cão de guarda"),
    (r"\bmonkey cão\b", "cão-macaco"),
    (r"\blittle terrier\b", "pequeno terrier"),
    (r"\bbig personality\b", "grande personalidade"),
    (r"\bneighbor cãos\b", "cães vizinhos"),
    (r"\bneighbor dogs\b", "cães vizinhos"),
    
    # Health-related phrases
    (r"\bRegular dental care is essential due to\b", "Os cuidados dentários regulares são essenciais devido a"),
    (r"\bRegular dental care\b", "Cuidados dentários regulares"),
    (r"\bis essential due to\b", "é essencial devido a"),
    (r"\bflat face can cause breathing issues\b", "focinho achatado pode causar problemas respiratórios"),
    (r"\bflat face\b", "focinho achatado"),
    (r"\bcan cause breathing issues\b", "pode causar problemas respiratórios"),
    (r"\bbreathing issues\b", "problemas respiratórios"),
    (r"\bextreme temperatures\b", "temperaturas extremas"),
    (r"\bProne to\b", "Propenso a"),
    (r"\bprone to\b", "propenso a"),
    (r"\bpatellar luxation\b", "luxação patelar"),
    (r"\bheart murmurs\b", "sopros cardíacos"),
    (r"\bheart disorders\b", "distúrbios cardíacos"),
    (r"\bsmall mouth\b", "boca pequena"),
    (r"\bsmall size\b", "tamanho pequeno"),
    (r"\bhip dysplasia\b", "displasia de quadril"),
    (r"\bhip and elbow dysplasia\b", "displasia de quadril e cotovelo"),
    (r"\belbow dysplasia\b", "displasia de cotovelo"),
    (r"\beye conditions\b", "problemas oculares"),
    (r"\bexercise-induced collapse\b", "colapso induzido por exercício"),
    (r"\bObesity is common\b", "A obesidade é comum"),
    (r"\bwatch their diet\b", "controle a dieta deles"),
    
    # Exercise-related phrases
    (r"\bModerate exercise needs\b", "Necessidades moderadas de exercício"),
    (r"\bshort daily walks\b", "caminhadas curtas diárias"),
    (r"\bindoor play sessions\b", "sessões de brincadeiras internas"),
    (r"\bis ideal\b", "é ideal"),
    (r"\bAffen means monkey in German\b", "Affen significa macaco em alemão"),
    (r"\binterativo toys\b", "brinquedos interativos"),
    (r"\binteractive toys\b", "brinquedos interativos"),
    (r"\bestimulação mental\b", "estimulação mental"),
    (r"\bmental stimulation\b", "estimulação mental"),
    (r"\bMental stimulation\b", "Estimulação mental"),
    
    # Additional phrases
    (r"\bform strong bonds\b", "formam laços fortes"),
    (r"\bstrong bonds\b", "laços fortes"),
    (r"\bwith their family\b", "com sua família"),
    (r"\bwith whole family\b", "com toda a família"),
    
    # Sentence starters
    (r"\bThey're\b", "Eles são"),
    (r"\bThey are\b", "Eles são"),
    (r"\bTheir\b", "Sua"),
    (r"\bThey\b", "Eles"),
    (r"\bthey\b", "eles"),
    (r"\bThe\b", "O"),
    (r"\bThis\b", "Esta"),
    (r"\bThese\b", "Estes"),
    (r"\bDespite\b", "Apesar de"),
    (r"\bdespite\b", "apesar de"),
    (r"\bDespite name\b", "Apesar do nome"),
    
    # Common phrases
    (r"\bis one of\b", "é uma das"),
    (r"\bare one of\b", "são uma das"),
    (r"\bmost popular\b", "mais populares"),
    (r"\bmakes them\b", "os torna"),
    (r"\bmake them\b", "os tornam"),
    (r"\bmake excellent\b", "são excelentes"),
    (r"\bmakes excellent\b", "é excelente"),
    (r"\bis known for being\b", "é conhecido por ser"),
    (r"\bare known for being\b", "são conhecidos por ser"),
    (r"\bis known for\b", "é conhecido por"),
    (r"\bare known for\b", "são conhecidos por"),
    (r"\bwith children\b", "com crianças"),
    (r"\bwith other pets\b", "com outros animais"),
    (r"\bother pets\b", "outros animais"),
    (r"\bwho enjoy\b", "que gostam de"),
    (r"\bwho love\b", "que amam"),
    (r"\bwho want\b", "que querem"),
    (r"\bwho need\b", "que precisam de"),
    (r"\bwho have\b", "que têm"),
    (r"\bwho bond\b", "que se conectam"),
    (r"\btheir intelligence\b", "sua inteligência"),
    (r"\balways entertaining\b", "sempre divertidos"),
    (r"\bfor good reason\b", "por boas razões"),
    (r"\bfor a family looking for\b", "para uma família que procura"),
    (r"\bmore than enough\b", "mais do que suficiente"),
    (r"\bto go around\b", "para todos"),
    
    # Health section
    (r"\bGenerally healthy\b", "Geralmente saudável"),
    (r"\bCommon concerns include\b", "Preocupações comuns incluem"),
    (r"\bRegular veterinary checkups\b", "Exames veterinários regulares"),
    (r"\bpreventive care\b", "cuidados preventivos"),
    (r"\bare important\b", "são importantes"),
    (r"\bis important\b", "é importante"),
    (r"\bMaintaining a healthy weight\b", "Manter um peso saudável"),
    (r"\bhelps prevent\b", "ajuda a prevenir"),
    (r"\bhealth issues\b", "problemas de saúde"),
    (r"\bmany health issues\b", "muitos problemas de saúde"),
    (r"\bbloat\b", "torção gástrica"),
    (r"\blifespan of\b", "expectativa de vida de"),
    (r"\bwith a lifespan of\b", "com expectativa de vida de"),
    
    # Exercise section
    (r"\bHigh energy\b", "Alta energia"),
    (r"\bhigh-animado\b", "cheios de energia"),
    (r"\bhigh-spirited\b", "cheios de energia"),
    (r"\brequiring vigorous daily exercise\b", "necessitando de exercício diário intenso"),
    (r"\brequiring daily exercise\b", "necessitando de exercício diário"),
    (r"\brequiring\b", "necessitando"),
    (r"\bat least an hour\b", "pelo menos uma hora"),
    (r"\bof activity\b", "de atividade"),
    (r"\bThey thrive with\b", "Eles prosperam com"),
    (r"\bthrive with\b", "prosperam com"),
    (r"\bactive families\b", "famílias ativas"),
    (r"\boutdoor activities\b", "atividades ao ar livre"),
    (r"\bthrough training\b", "através do treinamento"),
    (r"\bpuzzle toys\b", "brinquedos de quebra-cabeça"),
    (r"\bis equally important\b", "é igualmente importante"),
    (r"\bWithout adequate exercise\b", "Sem exercício adequado"),
    (r"\bthey may develop\b", "eles podem desenvolver"),
    (r"\bbehavioral issues\b", "problemas comportamentais"),
    (r"\bbursts of energy\b", "explosões de energia"),
    (r"\blove to play\b", "adoram brincar"),
    (r"\bescape artists\b", "artistas de fuga"),
    (r"\bfenced yard\b", "quintal cercado"),
    
    # Grooming section
    (r"\bHeavy shedders\b", "Perdem muito pelo"),
    (r"\bregular brushing\b", "escovação regular"),
    (r"\bdaily during shedding season\b", "diária durante a época de queda de pelo"),
    (r"\bfeathered coat\b", "pelagem emplumada"),
    (r"\bneeds attention\b", "precisa de atenção"),
    (r"\bto prevent matting\b", "para evitar nós"),
    (r"\bLow maintenance\b", "Baixa manutenção"),
    (r"\blow maintenance\b", "baixa manutenção"),
    (r"\bminimal grooming\b", "cuidados mínimos"),
    (r"\boccasional brushing\b", "escovação ocasional"),
    (r"\bweekly brushing\b", "escovação semanal"),
    (r"\brough, harsh, wiry coat\b", "pelagem áspera e dura"),
    (r"\bRequires regular grooming appropriate for their\b", "Requer cuidados regulares apropriados para sua"),
    
    # History section
    (r"\bDeveloped in\b", "Desenvolvido em"),
    (r"\bOriginated in\b", "Originário de"),
    (r"\boriginated in\b", "originário de"),
    (r"\bactually originated in\b", "na verdade se originou em"),
    (r"\bBred in\b", "Criado em"),
    (r"\bmid-19th century\b", "meados do século XIX"),
    (r"\b19th century\b", "século XIX"),
    (r"\b20th century\b", "século XX"),
    (r"\bwho crossed\b", "que cruzou"),
    (r"\bto create\b", "para criar"),
    (r"\bfor retrieving\b", "para recuperar"),
    (r"\bwaterfowl\b", "aves aquáticas"),
    (r"\bScotland\b", "Escócia"),
    (r"\bEngland\b", "Inglaterra"),
    (r"\bGermany\b", "Alemanha"),
    (r"\bFrance\b", "França"),
    (r"\bCanadá\b", "Canadá"),
    (r"\bNewfoundland\b", "Terra Nova"),
    (r"\bBritish nobles\b", "nobres britânicos"),
    (r"\bvisiting Canada\b", "visitando o Canadá"),
    (r"\bfell in love with\b", "se apaixonaram pela"),
    (r"\bbrought them to\b", "os trouxeram para"),
    (r"\bhelped fishermen\b", "ajudavam pescadores"),
    (r"\bretrieve nets\b", "recuperar redes"),
    (r"\bcatch escaping fish\b", "pegar peixes fugindo"),
    (r"\bescaping fish\b", "peixes fugindo"),
    (r"\bperfect guncão\b", "cão de caça perfeito"),
    (r"\bperfect gundog\b", "cão de caça perfeito"),
    
    # Temperament section
    (r"\bmature slowly\b", "amadurecem lentamente"),
    (r"\benergy well into adulthood\b", "energia até a idade adulta"),
    (r"\bGreat with kids\b", "Ótimos com crianças"),
    (r"\bgreat with kids\b", "ótimos com crianças"),
    (r"\bGreat with children\b", "Ótimos com crianças"),
    (r"\bgreat with children\b", "ótimos com crianças"),
    (r"\bloyal to family\b", "leais à família"),
    (r"\bto family\b", "à família"),
    (r"\bnature makes them\b", "natureza os torna"),
    (r"\bterrier-like personality\b", "personalidade tipo terrier"),
    (r"\btoy size\b", "tamanho toy"),
    (r"\bcomedic expressions\b", "expressões cômicas"),
    (r"\bearned them\b", "lhes rendeu"),
    (r"\bhave earned them\b", "lhes renderam"),
    (r"\bnickname\b", "apelido"),
    (r"\bwonderful with children\b", "maravilhosos com crianças"),
    (r"\bcompanheiroable housemates\b", "companheiros de casa"),
    (r"\bcompanionable housemates\b", "companheiros de casa"),
    (r"\bdon't mistake\b", "não confunda"),
    (r"\bDon't mistake\b", "Não confunda"),
    (r"\beasygoing personality\b", "personalidade tranquila"),
    (r"\bfor low energy\b", "com baixa energia"),
    (r"\bsocialize well\b", "socializam bem"),
    (r"\bhumans alike\b", "humanos também"),
    (r"\band humans alike\b", "e humanos também"),
    
    # Socialization
    (r"\bEarly socialization\b", "A socialização precoce"),
    (r"\bearly socialization\b", "a socialização precoce"),
    (r"\bare recommended\b", "são recomendados"),
    (r"\bis recommended\b", "é recomendado"),
    
    # Adjectives
    (r"\bamigável\b", "amigável"),  # Keep Portuguese
    (r"\bfriendly\b", "amigável"),
    (r"\btolerant\b", "tolerante"),
    (r"\bfabulous\b", "fabulosos"),
    (r"\bintelligent\b", "inteligente"),
    (r"\bhighly capable\b", "muito capazes"),
    (r"\boutgoing\b", "extrovertidos"),
    (r"\btrustworthy\b", "confiáveis"),
    (r"\beager to please\b", "ansiosos para agradar"),
    (r"\bansioso to please\b", "ansiosos para agradar"),
    (r"\bwonderful\b", "maravilhosos"),
    (r"\bpatient\b", "pacientes"),
    (r"\bpaciente\b", "pacientes"),
    (r"\bgentil\b", "gentis"),
    (r"\bgentle\b", "gentis"),
    (r"\bexcellent\b", "excelentes"),
    (r"\bfun-loving\b", "que gostam de se divertir"),
    (r"\bplayful\b", "brincalhões"),
    (r"\bloyal\b", "leais"),
    (r"\bprotective\b", "protetores"),
    (r"\baffectionate\b", "afetuosos"),
    (r"\balert\b", "alertas"),
    (r"\bbrave\b", "corajosos"),
    (r"\bcalm\b", "calmos"),
    (r"\bconfident\b", "confiantes"),
    (r"\bcurioso\b", "curioso"),  # Keep Portuguese
    (r"\bcurious\b", "curioso"),
    (r"\bdetermined\b", "determinados"),
    (r"\bdignified\b", "dignos"),
    (r"\benergetic\b", "energéticos"),
    (r"\bindependent\b", "independentes"),
    (r"\bstubborn\b", "teimosos"),
    (r"\bsensitive\b", "sensíveis"),
    (r"\breserved\b", "reservados"),
    (r"\bspirited\b", "animados"),
    (r"\bsweet\b", "doces"),
    (r"\bversatile\b", "versáteis"),
    (r"\bactive\b", "ativos"),
    (r"\bstrong\b", "fortes"),
    (r"\bathletic\b", "atléticos"),
    (r"\bgraceful\b", "graciosos"),
    (r"\belegant\b", "elegantes"),
    (r"\bwary\b", "cautelosos"),
    (r"\bclever\b", "inteligentes"),
    (r"\bsmart\b", "inteligentes"),
    (r"\bbold\b", "ousados"),
    (r"\bfearless\b", "destemidos"),
    (r"\bnoble\b", "nobres"),
    (r"\bdevoted\b", "devotados"),
    (r"\bsociable\b", "sociáveis"),
    (r"\bfrisky\b", "vívidos"),
    (r"\blively\b", "vívidos"),
    (r"\bquiet\b", "quietos"),
    (r"\bmellow\b", "tranquilos"),
    (r"\brelaxed\b", "relaxados"),
    (r"\bcheerful\b", "alegres"),
    (r"\bhappy\b", "felizes"),
    (r"\bcharming\b", "charmosos"),
    (r"\bcourageous\b", "corajosos"),
    (r"\badaptable\b", "adaptáveis"),
    (r"\bobedient\b", "obedientes"),
    (r"\bresponsive\b", "responsivos"),
    (r"\bperfect\b", "perfeitos"),
    (r"\bentertaining\b", "divertidos"),
    (r"\bbrincalhão\b", "brincalhão"),  # Keep Portuguese
    (r"\bfamously\b", "são conhecidos por serem"),
    
    # Common verbs
    (r"\bmaintain\b", "mantêm"),
    (r"\bcan be\b", "pode ser"),
    
    # Dog-related terms
    (r"\bdogs\b", "cães"),
    (r"\bdog\b", "cão"),
    (r"\bcãos\b", "cães"),  # Fix malformed plural
    (r"\bpuppies\b", "filhotes"),
    (r"\bpuppy-like\b", "de filhote"),
    (r"\bpuppy\b", "filhote"),
    (r"\bpups\b", "filhotes"),
    (r"\bpup\b", "filhote"),
    (r"\bguncão\b", "cão de caça"),
    (r"\bgundog\b", "cão de caça"),
    (r"\braça\b", "raça"),  # Keep Portuguese
    (r"\bbreed\b", "raça"),
    (r"\braças\b", "raças"),  # Keep Portuguese
    (r"\bbreeds\b", "raças"),
    
    # Common words
    (r"\birresistible\b", "irresistíveis"),
    (r"\bcompanion\b", "companheiro"),
    (r"\bcompanions\b", "companheiros"),
    (r"\bcompanheiros\b", "companheiros"),  # Keep Portuguese
    (r"\battitude\b", "atitude"),
    (r"\bfaces\b", "rostos"),
    (r"\bexpressive\b", "expressivos"),
    (r"\bintelligence\b", "inteligência"),
    (r"\bnature\b", "natureza"),
    (r"\bsocialization\b", "socialização"),
    (r"\btraining\b", "treinamento"),
    (r"\bfamilies\b", "famílias"),
    (r"\bchildren\b", "crianças"),
    (r"\byears\b", "anos"),
    (r"\bcentury\b", "século"),
    (r"\bduring\b", "durante"),
    (r"\btherapy\b", "terapia"),
    (r"\bworking\b", "de trabalho"),
    (r"\bterritorial\b", "territorial"),
    (r"\baffection\b", "afeto"),
    
    # Function words
    (r"\bmany\b", "muitos"),
    (r"\bwith a\b", "com uma"),
    (r"\bwith\b", "com"),
    (r"\band\b", "e"),
    (r"\bfor\b", "para"),
    (r"\bof\b", "de"),
    (r"\bor\b", "ou"),
    (r"\bin\b", "em"),
    (r"\bon\b", "em"),
    (r"\bas\b", "como"),
    (r"\bbut\b", "mas"),
    (r"\bfrom\b", "de"),
    (r"\bby\b", "por"),
    (r"\bhave\b", "têm"),
    (r"\bhas\b", "tem"),
    (r"\bare\b", "são"),
    (r"\bis\b", "é"),
    (r"\btheir\b", "seu"),
    (r"\bits\b", "sua"),
    (r"\ba medium-to-large\b", "um cão de porte médio a grande"),
    (r"\bmedium-to-large\b", "médio a grande"),
    
    # Additional words/phrases
    (r"\bform\b", "formam"),
    (r"\bfamily\b", "família"),
    (r"\bcan cause\b", "pode causar"),
    (r"\benjoy\b", "gostam de"),
    (r"\bgames\b", "jogos"),
    (r"\bideal\b", "ideal"),
    (r"\brace\b", "raça"),
    (r"\bsmall\b", "pequeno"),
    (r"\bshort\b", "curta"),
    (r"\bdaily\b", "diário"),
    (r"\bwalks\b", "passeios"),
    (r"\bAmerica's\b", "da América"),
    (r"\bLord Tweedmouth\b", "Lord Tweedmouth"),
    (r"\byellow retriever\b", "retriever amarelo"),
    (r"\bTweed Water Spaniel\b", "Tweed Water Spaniel"),
    (r"\bGoldens are\b", "Os Golden são"),
    (r"\bLabs are\b", "Os Labs são"),
]

def translate_text(text: str) -> str:
    """Apply all translations to text."""
    result = text
    
    for pattern, replacement in TRANSLATIONS:
        result = re.sub(pattern, replacement, result)
    
    # Post-processing fixes for common issues
    post_fixes = [
        (r"\bde de\b", "de"),
        (r"\bé um um\b", "é um"),
        (r"'s\b", ""),  # Remove possessive 's
        (r"\bUm Um\b", "Um"),
        (r"\bpara Um\b", "para um"),
        (r"\bcom Um\b", "com um"),
        (r"\bé Um\b", "é um"),
        (r"\bO O\b", "O"),
        (r"\bem em\b", "em"),
        (r"\bcom com\b", "com"),
        (r"\be e\b", "e"),
        (r"\bpor por\b", "por"),
        # Fix double spaces
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
    html_files = list(PT_BREEDS_DIR.glob("*.html"))
    print(f"Found {len(html_files)} HTML files in pt/breeds/")
    
    fixed = 0
    for filepath in sorted(html_files):
        if fix_jsonld_in_file(filepath):
            print(f"  Fixed: {filepath.name}")
            fixed += 1
    
    print(f"\nFixed {fixed} files")

if __name__ == "__main__":
    main()
