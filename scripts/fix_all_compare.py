#!/usr/bin/env python3
"""Fix all compare pages: images, translations for all languages"""

import re
import os

# === TRANSLATION DATA ===

LANGUAGES = {
    "de": {
        "lang_name": "German",
        "sizes": {"Tiny": "Winzig", "Small": "Klein", "Medium": "Mittel", "Large": "Groß", "Giant": "Riesig"},
        "shedding": {"Low": "Gering", "Moderate": "Mäßig", "High": "Hoch", "Minimal": "Minimal", "Seasonal": "Saisonal", "Heavy": "Stark", "None": "Keine"},
        "years": "Jahre",
        "attrs": {
            "Size": "Größe", "Height": "Höhe", "Weight": "Gewicht", "Lifespan": "Lebenserwartung",
            "Origin": "Herkunft", "Energy": "Energie", "Grooming": "Pflege", "Trainability": "Trainierbarkeit",
            "Kid Friendly": "Kinderfreundlich", "Apartment": "Wohnung"
        },
        "ui": {
            "Select a breed...": "Rasse auswählen...",
            "Breed 1": "Rasse 1", "Breed 2": "Rasse 2", "Breed 3 (optional)": "Rasse 3 (optional)",
            "Select up to 3 breeds to compare side by side": "Wähle bis zu 3 Rassen zum Vergleichen",
            "Attribute": "Merkmal"
        },
        "countries": {
            "Germany": "Deutschland", "Afghanistan": "Afghanistan", "England": "England", "Japan": "Japan",
            "United States": "Vereinigte Staaten", "France": "Frankreich", "Scotland": "Schottland",
            "Ireland": "Irland", "China": "China", "Russia": "Russland", "Belgium": "Belgien",
            "Australia": "Australien", "Canada": "Kanada", "Wales": "Wales", "Switzerland": "Schweiz",
            "Italy": "Italien", "Spain": "Spanien", "Portugal": "Portugal", "Hungary": "Ungarn",
            "Poland": "Polen", "Netherlands": "Niederlande", "Mexico": "Mexiko", "Cuba": "Kuba",
            "Malta": "Malta", "Croatia": "Kroatien", "Tibet": "Tibet", "Central Africa": "Zentralafrika",
            "Congo": "Kongo", "Turkey": "Türkei", "Greece": "Griechenland", "Norway": "Norwegen",
            "Sweden": "Schweden", "Finland": "Finnland", "Denmark": "Dänemark", "Unknown": "Unbekannt", "Ancient": "Antik"
        },
        "breeds": {
            "Afghan Hound": "Afghanischer Windhund", "Airedale Terrier": "Airedale Terrier",
            "Alaskan Malamute": "Alaskan Malamute", "American Bulldog": "Amerikanische Bulldogge",
            "Australian Shepherd": "Australian Shepherd", "Basset Hound": "Basset Hound",
            "Beagle": "Beagle", "Bernese Mountain Dog": "Berner Sennenhund",
            "Border Collie": "Border Collie", "Boxer": "Boxer", "Bulldog": "Englische Bulldogge",
            "Cavalier King Charles Spaniel": "Cavalier King Charles Spaniel", "Chihuahua": "Chihuahua",
            "Cocker Spaniel": "Englischer Cocker Spaniel", "Dachshund": "Dackel", "Dalmatian": "Dalmatiner",
            "Doberman Pinscher": "Dobermann", "French Bulldog": "Französische Bulldogge",
            "German Shepherd": "Deutscher Schäferhund", "Golden Retriever": "Golden Retriever",
            "Great Dane": "Deutsche Dogge", "Labrador Retriever": "Labrador Retriever",
            "Maltese": "Malteser", "Pomeranian": "Zwergspitz", "Poodle": "Pudel", "Pug": "Mops",
            "Rottweiler": "Rottweiler", "Shih Tzu": "Shih Tzu", "Siberian Husky": "Sibirischer Husky",
            "Yorkshire Terrier": "Yorkshire Terrier"
        }
    },
    "fr": {
        "lang_name": "French",
        "sizes": {"Tiny": "Minuscule", "Small": "Petit", "Medium": "Moyen", "Large": "Grand", "Giant": "Géant"},
        "shedding": {"Low": "Faible", "Moderate": "Modéré", "High": "Élevé", "Minimal": "Minimal", "Seasonal": "Saisonnier", "Heavy": "Important", "None": "Aucun"},
        "years": "ans",
        "attrs": {
            "Size": "Taille", "Height": "Hauteur", "Weight": "Poids", "Lifespan": "Espérance de vie",
            "Origin": "Origine", "Energy": "Énergie", "Grooming": "Toilettage", "Trainability": "Éducabilité",
            "Kid Friendly": "Enfants", "Apartment": "Appartement"
        },
        "ui": {
            "Select a breed...": "Sélectionner une race...",
            "Breed 1": "Race 1", "Breed 2": "Race 2", "Breed 3 (optional)": "Race 3 (optionnel)",
            "Select up to 3 breeds to compare side by side": "Sélectionnez jusqu'à 3 races à comparer",
            "Attribute": "Attribut"
        },
        "countries": {
            "Germany": "Allemagne", "Afghanistan": "Afghanistan", "England": "Angleterre", "Japan": "Japon",
            "United States": "États-Unis", "France": "France", "Scotland": "Écosse", "Ireland": "Irlande",
            "China": "Chine", "Russia": "Russie", "Belgium": "Belgique", "Australia": "Australie",
            "Canada": "Canada", "Wales": "Pays de Galles", "Switzerland": "Suisse", "Italy": "Italie",
            "Spain": "Espagne", "Portugal": "Portugal", "Hungary": "Hongrie", "Poland": "Pologne",
            "Netherlands": "Pays-Bas", "Mexico": "Mexique", "Cuba": "Cuba", "Malta": "Malte",
            "Tibet": "Tibet", "Turkey": "Turquie", "Greece": "Grèce", "Norway": "Norvège",
            "Sweden": "Suède", "Finland": "Finlande", "Denmark": "Danemark", "Unknown": "Inconnu", "Ancient": "Ancien"
        },
        "breeds": {
            "Afghan Hound": "Lévrier Afghan", "Bernese Mountain Dog": "Bouvier Bernois",
            "Bulldog": "Bouledogue Anglais", "Dachshund": "Teckel", "Doberman Pinscher": "Dobermann",
            "French Bulldog": "Bouledogue Français", "German Shepherd": "Berger Allemand",
            "Great Dane": "Dogue Allemand", "Maltese": "Bichon Maltais", "Poodle": "Caniche",
            "Pug": "Carlin", "Siberian Husky": "Husky Sibérien"
        }
    },
    "it": {
        "lang_name": "Italian",
        "sizes": {"Tiny": "Minuscolo", "Small": "Piccolo", "Medium": "Medio", "Large": "Grande", "Giant": "Gigante"},
        "shedding": {"Low": "Basso", "Moderate": "Moderato", "High": "Alto", "Minimal": "Minimo", "Seasonal": "Stagionale", "Heavy": "Abbondante", "None": "Nessuno"},
        "years": "anni",
        "attrs": {
            "Size": "Taglia", "Height": "Altezza", "Weight": "Peso", "Lifespan": "Aspettativa di vita",
            "Origin": "Origine", "Energy": "Energia", "Grooming": "Toelettatura", "Trainability": "Addestrabilità",
            "Kid Friendly": "Bambini", "Apartment": "Appartamento"
        },
        "ui": {
            "Select a breed...": "Seleziona una razza...",
            "Breed 1": "Razza 1", "Breed 2": "Razza 2", "Breed 3 (optional)": "Razza 3 (opzionale)",
            "Select up to 3 breeds to compare side by side": "Seleziona fino a 3 razze da confrontare",
            "Attribute": "Attributo"
        },
        "countries": {
            "Germany": "Germania", "Afghanistan": "Afghanistan", "England": "Inghilterra", "Japan": "Giappone",
            "United States": "Stati Uniti", "France": "Francia", "Scotland": "Scozia", "Ireland": "Irlanda",
            "China": "Cina", "Russia": "Russia", "Belgium": "Belgio", "Australia": "Australia",
            "Canada": "Canada", "Wales": "Galles", "Switzerland": "Svizzera", "Italy": "Italia",
            "Spain": "Spagna", "Portugal": "Portogallo", "Hungary": "Ungheria", "Poland": "Polonia",
            "Netherlands": "Paesi Bassi", "Mexico": "Messico", "Cuba": "Cuba", "Malta": "Malta",
            "Tibet": "Tibet", "Turkey": "Turchia", "Greece": "Grecia", "Norway": "Norvegia",
            "Sweden": "Svezia", "Finland": "Finlandia", "Denmark": "Danimarca", "Unknown": "Sconosciuto", "Ancient": "Antico"
        },
        "breeds": {
            "Bernese Mountain Dog": "Bovaro del Bernese", "Bulldog": "Bulldog Inglese",
            "Dachshund": "Bassotto", "French Bulldog": "Bulldog Francese",
            "German Shepherd": "Pastore Tedesco", "Great Dane": "Alano", "Maltese": "Maltese",
            "Poodle": "Barboncino", "Pug": "Carlino", "Siberian Husky": "Siberian Husky"
        }
    },
    "pt": {
        "lang_name": "Portuguese",
        "sizes": {"Tiny": "Minúsculo", "Small": "Pequeno", "Medium": "Médio", "Large": "Grande", "Giant": "Gigante"},
        "shedding": {"Low": "Baixo", "Moderate": "Moderado", "High": "Alto", "Minimal": "Mínimo", "Seasonal": "Sazonal", "Heavy": "Abundante", "None": "Nenhum"},
        "years": "anos",
        "attrs": {
            "Size": "Tamanho", "Height": "Altura", "Weight": "Peso", "Lifespan": "Expectativa de vida",
            "Origin": "Origem", "Energy": "Energia", "Grooming": "Higiene", "Trainability": "Treinabilidade",
            "Kid Friendly": "Crianças", "Apartment": "Apartamento"
        },
        "ui": {
            "Select a breed...": "Selecione uma raça...",
            "Breed 1": "Raça 1", "Breed 2": "Raça 2", "Breed 3 (optional)": "Raça 3 (opcional)",
            "Select up to 3 breeds to compare side by side": "Selecione até 3 raças para comparar",
            "Attribute": "Atributo"
        },
        "countries": {
            "Germany": "Alemanha", "Afghanistan": "Afeganistão", "England": "Inglaterra", "Japan": "Japão",
            "United States": "Estados Unidos", "France": "França", "Scotland": "Escócia", "Ireland": "Irlanda",
            "China": "China", "Russia": "Rússia", "Belgium": "Bélgica", "Australia": "Austrália",
            "Canada": "Canadá", "Wales": "País de Gales", "Switzerland": "Suíça", "Italy": "Itália",
            "Spain": "Espanha", "Portugal": "Portugal", "Hungary": "Hungria", "Poland": "Polónia",
            "Netherlands": "Países Baixos", "Mexico": "México", "Cuba": "Cuba", "Malta": "Malta",
            "Tibet": "Tibete", "Turkey": "Turquia", "Greece": "Grécia", "Norway": "Noruega",
            "Sweden": "Suécia", "Finland": "Finlândia", "Denmark": "Dinamarca", "Unknown": "Desconhecido", "Ancient": "Antigo"
        },
        "breeds": {
            "Bulldog": "Buldogue Inglês", "Dachshund": "Teckel", "French Bulldog": "Buldogue Francês",
            "German Shepherd": "Pastor Alemão", "Great Dane": "Dogue Alemão", "Poodle": "Poodle",
            "Pug": "Pug", "Siberian Husky": "Husky Siberiano"
        }
    },
    "nl": {
        "lang_name": "Dutch",
        "sizes": {"Tiny": "Minuscuul", "Small": "Klein", "Medium": "Middel", "Large": "Groot", "Giant": "Reus"},
        "shedding": {"Low": "Laag", "Moderate": "Matig", "High": "Hoog", "Minimal": "Minimaal", "Seasonal": "Seizoensgebonden", "Heavy": "Veel", "None": "Geen"},
        "years": "jaar",
        "attrs": {
            "Size": "Grootte", "Height": "Hoogte", "Weight": "Gewicht", "Lifespan": "Levensverwachting",
            "Origin": "Herkomst", "Energy": "Energie", "Grooming": "Verzorging", "Trainability": "Traineerbaarheid",
            "Kid Friendly": "Kindvriendelijk", "Apartment": "Appartement"
        },
        "ui": {
            "Select a breed...": "Selecteer een ras...",
            "Breed 1": "Ras 1", "Breed 2": "Ras 2", "Breed 3 (optional)": "Ras 3 (optioneel)",
            "Select up to 3 breeds to compare side by side": "Selecteer tot 3 rassen om te vergelijken",
            "Attribute": "Kenmerk"
        },
        "countries": {
            "Germany": "Duitsland", "Afghanistan": "Afghanistan", "England": "Engeland", "Japan": "Japan",
            "United States": "Verenigde Staten", "France": "Frankrijk", "Scotland": "Schotland",
            "Ireland": "Ierland", "China": "China", "Russia": "Rusland", "Belgium": "België",
            "Australia": "Australië", "Canada": "Canada", "Wales": "Wales", "Switzerland": "Zwitserland",
            "Italy": "Italië", "Spain": "Spanje", "Portugal": "Portugal", "Hungary": "Hongarije",
            "Poland": "Polen", "Netherlands": "Nederland", "Mexico": "Mexico", "Unknown": "Onbekend", "Ancient": "Oud"
        },
        "breeds": {
            "Dachshund": "Teckel", "German Shepherd": "Duitse Herder", "Poodle": "Poedel"
        }
    },
    "sv": {
        "lang_name": "Swedish",
        "sizes": {"Tiny": "Pytteliten", "Small": "Liten", "Medium": "Medel", "Large": "Stor", "Giant": "Jätte"},
        "shedding": {"Low": "Låg", "Moderate": "Måttlig", "High": "Hög", "Minimal": "Minimal", "Seasonal": "Säsongsbunden", "Heavy": "Riklig", "None": "Ingen"},
        "years": "år",
        "attrs": {
            "Size": "Storlek", "Height": "Höjd", "Weight": "Vikt", "Lifespan": "Livslängd",
            "Origin": "Ursprung", "Energy": "Energi", "Grooming": "Pälsvård", "Trainability": "Träningsbarhet",
            "Kid Friendly": "Barnvänlig", "Apartment": "Lägenhet"
        },
        "ui": {
            "Select a breed...": "Välj en ras...",
            "Breed 1": "Ras 1", "Breed 2": "Ras 2", "Breed 3 (optional)": "Ras 3 (valfritt)",
            "Select up to 3 breeds to compare side by side": "Välj upp till 3 raser att jämföra",
            "Attribute": "Attribut"
        },
        "countries": {
            "Germany": "Tyskland", "Afghanistan": "Afghanistan", "England": "England", "Japan": "Japan",
            "United States": "USA", "France": "Frankrike", "Scotland": "Skottland", "Ireland": "Irland",
            "China": "Kina", "Russia": "Ryssland", "Belgium": "Belgien", "Australia": "Australien",
            "Canada": "Kanada", "Wales": "Wales", "Switzerland": "Schweiz", "Italy": "Italien",
            "Spain": "Spanien", "Portugal": "Portugal", "Hungary": "Ungern", "Poland": "Polen",
            "Netherlands": "Nederländerna", "Mexico": "Mexiko", "Norway": "Norge", "Sweden": "Sverige",
            "Finland": "Finland", "Denmark": "Danmark", "Unknown": "Okänt", "Ancient": "Forntida"
        },
        "breeds": {
            "Dachshund": "Tax", "German Shepherd": "Schäfer", "Poodle": "Pudel"
        }
    },
    "da": {
        "lang_name": "Danish",
        "sizes": {"Tiny": "Bittesmå", "Small": "Lille", "Medium": "Mellem", "Large": "Stor", "Giant": "Kæmpe"},
        "shedding": {"Low": "Lav", "Moderate": "Moderat", "High": "Høj", "Minimal": "Minimal", "Seasonal": "Sæsonbetonet", "Heavy": "Kraftig", "None": "Ingen"},
        "years": "år",
        "attrs": {
            "Size": "Størrelse", "Height": "Højde", "Weight": "Vægt", "Lifespan": "Levetid",
            "Origin": "Oprindelse", "Energy": "Energi", "Grooming": "Pelspleje", "Trainability": "Trænbarhed",
            "Kid Friendly": "Børnevenlig", "Apartment": "Lejlighed"
        },
        "ui": {
            "Select a breed...": "Vælg en race...",
            "Breed 1": "Race 1", "Breed 2": "Race 2", "Breed 3 (optional)": "Race 3 (valgfri)",
            "Select up to 3 breeds to compare side by side": "Vælg op til 3 racer at sammenligne",
            "Attribute": "Attribut"
        },
        "countries": {
            "Germany": "Tyskland", "England": "England", "Japan": "Japan", "United States": "USA",
            "France": "Frankrig", "Scotland": "Skotland", "Ireland": "Irland", "China": "Kina",
            "Russia": "Rusland", "Belgium": "Belgien", "Australia": "Australien", "Canada": "Canada",
            "Switzerland": "Schweiz", "Italy": "Italien", "Spain": "Spanien", "Portugal": "Portugal",
            "Hungary": "Ungarn", "Poland": "Polen", "Netherlands": "Holland", "Mexico": "Mexico",
            "Norway": "Norge", "Sweden": "Sverige", "Finland": "Finland", "Denmark": "Danmark",
            "Unknown": "Ukendt", "Ancient": "Gammel"
        },
        "breeds": {}
    },
    "no": {
        "lang_name": "Norwegian",
        "sizes": {"Tiny": "Bittesmå", "Small": "Liten", "Medium": "Middels", "Large": "Stor", "Giant": "Kjempe"},
        "shedding": {"Low": "Lav", "Moderate": "Moderat", "High": "Høy", "Minimal": "Minimal", "Seasonal": "Sesongbasert", "Heavy": "Kraftig", "None": "Ingen"},
        "years": "år",
        "attrs": {
            "Size": "Størrelse", "Height": "Høyde", "Weight": "Vekt", "Lifespan": "Levealder",
            "Origin": "Opprinnelse", "Energy": "Energi", "Grooming": "Pelsstell", "Trainability": "Trenbarhet",
            "Kid Friendly": "Barnevennlig", "Apartment": "Leilighet"
        },
        "ui": {
            "Select a breed...": "Velg en rase...",
            "Breed 1": "Rase 1", "Breed 2": "Rase 2", "Breed 3 (optional)": "Rase 3 (valgfritt)",
            "Select up to 3 breeds to compare side by side": "Velg opptil 3 raser å sammenligne",
            "Attribute": "Attributt"
        },
        "countries": {
            "Germany": "Tyskland", "England": "England", "Japan": "Japan", "United States": "USA",
            "France": "Frankrike", "Scotland": "Skottland", "Ireland": "Irland", "China": "Kina",
            "Russia": "Russland", "Belgium": "Belgia", "Australia": "Australia", "Canada": "Canada",
            "Switzerland": "Sveits", "Italy": "Italia", "Spain": "Spania", "Portugal": "Portugal",
            "Hungary": "Ungarn", "Poland": "Polen", "Netherlands": "Nederland", "Mexico": "Mexico",
            "Norway": "Norge", "Sweden": "Sverige", "Finland": "Finland", "Denmark": "Danmark",
            "Unknown": "Ukjent", "Ancient": "Gammel"
        },
        "breeds": {}
    },
    "pl": {
        "lang_name": "Polish",
        "sizes": {"Tiny": "Malutki", "Small": "Mały", "Medium": "Średni", "Large": "Duży", "Giant": "Olbrzymi"},
        "shedding": {"Low": "Niskie", "Moderate": "Umiarkowane", "High": "Wysokie", "Minimal": "Minimalne", "Seasonal": "Sezonowe", "Heavy": "Obfite", "None": "Brak"},
        "years": "lat",
        "attrs": {
            "Size": "Rozmiar", "Height": "Wzrost", "Weight": "Waga", "Lifespan": "Długość życia",
            "Origin": "Pochodzenie", "Energy": "Energia", "Grooming": "Pielęgnacja", "Trainability": "Szkolenie",
            "Kid Friendly": "Dzieci", "Apartment": "Mieszkanie"
        },
        "ui": {
            "Select a breed...": "Wybierz rasę...",
            "Breed 1": "Rasa 1", "Breed 2": "Rasa 2", "Breed 3 (optional)": "Rasa 3 (opcjonalnie)",
            "Select up to 3 breeds to compare side by side": "Wybierz do 3 ras do porównania",
            "Attribute": "Atrybut"
        },
        "countries": {
            "Germany": "Niemcy", "Afghanistan": "Afganistan", "England": "Anglia", "Japan": "Japonia",
            "United States": "Stany Zjednoczone", "France": "Francja", "Scotland": "Szkocja",
            "Ireland": "Irlandia", "China": "Chiny", "Russia": "Rosja", "Belgium": "Belgia",
            "Australia": "Australia", "Canada": "Kanada", "Wales": "Walia", "Switzerland": "Szwajcaria",
            "Italy": "Włochy", "Spain": "Hiszpania", "Portugal": "Portugalia", "Hungary": "Węgry",
            "Poland": "Polska", "Netherlands": "Holandia", "Mexico": "Meksyk",
            "Unknown": "Nieznane", "Ancient": "Starożytne"
        },
        "breeds": {
            "German Shepherd": "Owczarek Niemiecki", "Dachshund": "Jamnik"
        }
    },
    "ru": {
        "lang_name": "Russian",
        "sizes": {"Tiny": "Крошечный", "Small": "Маленький", "Medium": "Средний", "Large": "Большой", "Giant": "Гигантский"},
        "shedding": {"Low": "Низкая", "Moderate": "Умеренная", "High": "Высокая", "Minimal": "Минимальная", "Seasonal": "Сезонная", "Heavy": "Обильная", "None": "Отсутствует"},
        "years": "лет",
        "attrs": {
            "Size": "Размер", "Height": "Рост", "Weight": "Вес", "Lifespan": "Продолжительность жизни",
            "Origin": "Происхождение", "Energy": "Энергия", "Grooming": "Уход", "Trainability": "Обучаемость",
            "Kid Friendly": "Дети", "Apartment": "Квартира"
        },
        "ui": {
            "Select a breed...": "Выберите породу...",
            "Breed 1": "Порода 1", "Breed 2": "Порода 2", "Breed 3 (optional)": "Порода 3 (необязательно)",
            "Select up to 3 breeds to compare side by side": "Выберите до 3 пород для сравнения",
            "Attribute": "Атрибут"
        },
        "countries": {
            "Germany": "Германия", "Afghanistan": "Афганистан", "England": "Англия", "Japan": "Япония",
            "United States": "США", "France": "Франция", "Scotland": "Шотландия", "Ireland": "Ирландия",
            "China": "Китай", "Russia": "Россия", "Belgium": "Бельгия", "Australia": "Австралия",
            "Canada": "Канада", "Wales": "Уэльс", "Switzerland": "Швейцария", "Italy": "Италия",
            "Spain": "Испания", "Portugal": "Португалия", "Hungary": "Венгрия", "Poland": "Польша",
            "Netherlands": "Нидерланды", "Mexico": "Мексика", "Unknown": "Неизвестно", "Ancient": "Древний"
        },
        "breeds": {
            "German Shepherd": "Немецкая Овчарка", "Dachshund": "Такса", "Poodle": "Пудель"
        }
    },
    "tr": {
        "lang_name": "Turkish",
        "sizes": {"Tiny": "Minik", "Small": "Küçük", "Medium": "Orta", "Large": "Büyük", "Giant": "Dev"},
        "shedding": {"Low": "Az", "Moderate": "Orta", "High": "Yüksek", "Minimal": "Minimal", "Seasonal": "Mevsimsel", "Heavy": "Yoğun", "None": "Hiç"},
        "years": "yıl",
        "attrs": {
            "Size": "Boyut", "Height": "Yükseklik", "Weight": "Ağırlık", "Lifespan": "Ömür",
            "Origin": "Köken", "Energy": "Enerji", "Grooming": "Bakım", "Trainability": "Eğitilebilirlik",
            "Kid Friendly": "Çocuk Dostu", "Apartment": "Daire"
        },
        "ui": {
            "Select a breed...": "Bir ırk seçin...",
            "Breed 1": "Irk 1", "Breed 2": "Irk 2", "Breed 3 (optional)": "Irk 3 (isteğe bağlı)",
            "Select up to 3 breeds to compare side by side": "Karşılaştırmak için 3 ırk seçin",
            "Attribute": "Özellik"
        },
        "countries": {
            "Germany": "Almanya", "Afghanistan": "Afganistan", "England": "İngiltere", "Japan": "Japonya",
            "United States": "ABD", "France": "Fransa", "Scotland": "İskoçya", "Ireland": "İrlanda",
            "China": "Çin", "Russia": "Rusya", "Belgium": "Belçika", "Australia": "Avustralya",
            "Canada": "Kanada", "Wales": "Galler", "Switzerland": "İsviçre", "Italy": "İtalya",
            "Spain": "İspanya", "Portugal": "Portekiz", "Hungary": "Macaristan", "Poland": "Polonya",
            "Netherlands": "Hollanda", "Mexico": "Meksika", "Turkey": "Türkiye",
            "Unknown": "Bilinmiyor", "Ancient": "Antik"
        },
        "breeds": {
            "German Shepherd": "Alman Çoban Köpeği"
        }
    },
    "ja": {
        "lang_name": "Japanese",
        "sizes": {"Tiny": "極小", "Small": "小型", "Medium": "中型", "Large": "大型", "Giant": "超大型"},
        "shedding": {"Low": "少ない", "Moderate": "普通", "High": "多い", "Minimal": "最小", "Seasonal": "季節的", "Heavy": "多量", "None": "なし"},
        "years": "年",
        "attrs": {
            "Size": "サイズ", "Height": "体高", "Weight": "体重", "Lifespan": "寿命",
            "Origin": "原産国", "Energy": "活動量", "Grooming": "お手入れ", "Trainability": "しつけやすさ",
            "Kid Friendly": "子供との相性", "Apartment": "マンション適性"
        },
        "ui": {
            "Select a breed...": "犬種を選択...",
            "Breed 1": "犬種 1", "Breed 2": "犬種 2", "Breed 3 (optional)": "犬種 3 (任意)",
            "Select up to 3 breeds to compare side by side": "最大3犬種を選んで比較",
            "Attribute": "特性"
        },
        "countries": {
            "Germany": "ドイツ", "Afghanistan": "アフガニスタン", "England": "イングランド", "Japan": "日本",
            "United States": "アメリカ", "France": "フランス", "Scotland": "スコットランド", "Ireland": "アイルランド",
            "China": "中国", "Russia": "ロシア", "Belgium": "ベルギー", "Australia": "オーストラリア",
            "Canada": "カナダ", "Wales": "ウェールズ", "Switzerland": "スイス", "Italy": "イタリア",
            "Spain": "スペイン", "Portugal": "ポルトガル", "Hungary": "ハンガリー", "Poland": "ポーランド",
            "Netherlands": "オランダ", "Mexico": "メキシコ", "Unknown": "不明", "Ancient": "古代"
        },
        "breeds": {
            "German Shepherd": "ジャーマン・シェパード", "Labrador Retriever": "ラブラドール・レトリバー",
            "Golden Retriever": "ゴールデン・レトリバー", "Poodle": "プードル", "Shiba Inu": "柴犬"
        }
    },
    "zh": {
        "lang_name": "Chinese",
        "sizes": {"Tiny": "超小型", "Small": "小型", "Medium": "中型", "Large": "大型", "Giant": "巨型"},
        "shedding": {"Low": "少", "Moderate": "适中", "High": "多", "Minimal": "极少", "Seasonal": "季节性", "Heavy": "大量", "None": "无"},
        "years": "年",
        "attrs": {
            "Size": "体型", "Height": "身高", "Weight": "体重", "Lifespan": "寿命",
            "Origin": "原产地", "Energy": "活力", "Grooming": "美容", "Trainability": "可训练性",
            "Kid Friendly": "儿童友好", "Apartment": "公寓适应"
        },
        "ui": {
            "Select a breed...": "选择品种...",
            "Breed 1": "品种 1", "Breed 2": "品种 2", "Breed 3 (optional)": "品种 3 (可选)",
            "Select up to 3 breeds to compare side by side": "选择最多3个品种进行比较",
            "Attribute": "属性"
        },
        "countries": {
            "Germany": "德国", "Afghanistan": "阿富汗", "England": "英格兰", "Japan": "日本",
            "United States": "美国", "France": "法国", "Scotland": "苏格兰", "Ireland": "爱尔兰",
            "China": "中国", "Russia": "俄罗斯", "Belgium": "比利时", "Australia": "澳大利亚",
            "Canada": "加拿大", "Wales": "威尔士", "Switzerland": "瑞士", "Italy": "意大利",
            "Spain": "西班牙", "Portugal": "葡萄牙", "Hungary": "匈牙利", "Poland": "波兰",
            "Netherlands": "荷兰", "Mexico": "墨西哥", "Unknown": "未知", "Ancient": "古代"
        },
        "breeds": {
            "German Shepherd": "德国牧羊犬", "Labrador Retriever": "拉布拉多犬",
            "Golden Retriever": "金毛寻回犬", "Poodle": "贵宾犬"
        }
    }
}

def fix_compare_page(lang_code, data, base_dir):
    filepath = os.path.join(base_dir, lang_code, "compare", "index.html")
    if not os.path.exists(filepath):
        print(f"SKIP: {filepath} not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix image paths
    content = content.replace('image: "../images/heads/', 'image: "../../images/heads/')
    
    # 2. Translate breeds (if any defined)
    for en_name, tr_name in data.get("breeds", {}).items():
        content = re.sub(rf'name: "{re.escape(en_name)}"', f'name: "{tr_name}"', content)
    
    # 3. Translate sizes
    for en, tr in data.get("sizes", {}).items():
        content = re.sub(rf'size: "{en}"', f'size: "{tr}"', content)
    
    # 4. Translate shedding
    for en, tr in data.get("shedding", {}).items():
        content = re.sub(rf'shedding: "{en}"', f'shedding: "{tr}"', content)
    
    # 5. Translate countries
    for en, tr in data.get("countries", {}).items():
        content = re.sub(rf'origin: "{re.escape(en)}"', f'origin: "{tr}"', content)
    
    # 6. Translate years
    if data.get("years"):
        content = re.sub(r'(\d+-\d+) years', rf'\1 {data["years"]}', content)
    
    # 7. Translate row labels
    attrs = data.get("attrs", {})
    if attrs.get("Size"):
        content = content.replace("['Size', 'size']", f"['{attrs['Size']}', 'size']")
    if attrs.get("Height"):
        content = content.replace("['Height', 'height']", f"['{attrs['Height']}', 'height']")
    if attrs.get("Weight"):
        content = content.replace("['Weight', 'weight']", f"['{attrs['Weight']}', 'weight']")
    if attrs.get("Lifespan"):
        content = content.replace("['Lifespan', 'lifespan']", f"['{attrs['Lifespan']}', 'lifespan']")
    if attrs.get("Origin"):
        content = content.replace("['Origin', 'origin']", f"['{attrs['Origin']}', 'origin']")
    if attrs.get("Energy"):
        content = content.replace("['Energy', 'energy', true]", f"['{attrs['Energy']}', 'energy', true]")
    if attrs.get("Grooming"):
        content = content.replace("['Grooming', 'grooming', true]", f"['{attrs['Grooming']}', 'grooming', true]")
    if attrs.get("Trainability"):
        content = content.replace("['Trainability', 'trainability', true]", f"['{attrs['Trainability']}', 'trainability', true]")
    if attrs.get("Kid Friendly"):
        content = content.replace("['Kid Friendly', 'kidFriendly', true]", f"['{attrs['Kid Friendly']}', 'kidFriendly', true]")
    if attrs.get("Apartment"):
        content = content.replace("['Apartment', 'apartment', true]", f"['{attrs['Apartment']}', 'apartment', true]")
    
    # 8. UI translations
    ui = data.get("ui", {})
    if ui.get("Select a breed..."):
        content = content.replace('>Select a breed...</option>', f'>{ui["Select a breed..."]}</option>')
        content = content.replace('<option value="">Select a breed...', f'<option value="">{ui["Select a breed..."]}')
    if ui.get("Breed 1"):
        content = content.replace('class="block text-sm font-medium text-slate-600 mb-2">Breed 1</label>', f'class="block text-sm font-medium text-slate-600 mb-2">{ui["Breed 1"]}</label>')
    if ui.get("Breed 2"):
        content = content.replace('class="block text-sm font-medium text-slate-600 mb-2">Breed 2</label>', f'class="block text-sm font-medium text-slate-600 mb-2">{ui["Breed 2"]}</label>')
    if ui.get("Breed 3 (optional)"):
        content = content.replace('class="block text-sm font-medium text-slate-600 mb-2">Breed 3 (optional)</label>', f'class="block text-sm font-medium text-slate-600 mb-2">{ui["Breed 3 (optional)"]}</label>')
    if ui.get("Select up to 3 breeds to compare side by side"):
        content = content.replace('>Select up to 3 breeds to compare side by side<', f'>{ui["Select up to 3 breeds to compare side by side"]}<')
    if ui.get("Attribute"):
        content = content.replace('>Attribute<', f'>{ui["Attribute"]}<')
    
    # 9. Fix comparison links
    content = content.replace('href="comparisons/', 'href="/compare/comparisons/')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {lang_code} ({data['lang_name']})")

if __name__ == "__main__":
    base_dir = "/Users/juhaporraskorpi/clawd/breedfinder.org"
    
    for lang_code, data in LANGUAGES.items():
        fix_compare_page(lang_code, data, base_dir)
    
    print("\n✅ All compare pages fixed!")
