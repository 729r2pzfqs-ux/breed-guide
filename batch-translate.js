#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const breedsDir = path.join(__dirname, 'it/breeds');

// Common English to Italian translations for recurring phrases
const commonTranslations = {
  // Exercise section common phrases
  "High energy breed requiring vigorous daily exercise—at least an hour of activity. They thrive with active families who enjoy outdoor activities. Mental stimulation through training and puzzle toys is equally important. Without adequate exercise, they may develop behavioral issues.":
    "Razza ad alta energia che richiede esercizio quotidiano vigoroso—almeno un'ora di attività. Prosperano con famiglie attive che amano le attività all'aperto. La stimolazione mentale attraverso l'addestramento e i giochi puzzle è altrettanto importante. Senza esercizio adeguato, possono sviluppare problemi comportamentali.",
  
  "Moderate exercise needs with short daily walks and indoor play sessions. They enjoy interactive toys and mental stimulation games. Despite their small size, they have bursts of energy and love to play. A fenced yard is ideal as they can be escape artists.":
    "Esigenze di esercizio moderate con brevi passeggiate quotidiane e sessioni di gioco in casa. Amano i giocattoli interattivi e i giochi di stimolazione mentale. Nonostante le piccole dimensioni, hanno momenti di energia e adorano giocare. Un giardino recintato è ideale perché possono essere artisti della fuga.",
  
  "High exercise needs requiring daily runs in a secure, fenced area.":
    "Elevate esigenze di esercizio che richiedono corse quotidiane in un'area sicura e recintata.",
  
  // Ideal For phrases
  "Experienced dog owners": "Proprietari esperti",
  "Active families": "Famiglie attive",
  "Those wanting a protective dog": "Chi cerca un cane protettivo",
  "People with time for training": "Persone con tempo per l'addestramento",
  "Adults only": "Solo adulti",
  "Those wanting a character": "Chi cerca un cane con carattere",
  "Those appreciating elegant, independent dogs": "Chi apprezza cani eleganti e indipendenti",
  "Owners committed to grooming": "Proprietari dedicati alla toelettatura",
  "Homes with secure yards": "Case con giardini recintati",
  "Families with children": "Famiglie con bambini",
  "Active individuals": "Persone attive",
  "Those seeking a loyal companion": "Chi cerca un compagno fedele",
  "Hunters and outdoor enthusiasts": "Cacciatori e appassionati outdoor",
  "Runners and joggers": "Corridori e jogger",
  
  // Not Ideal For phrases
  "Families with young children": "Famiglie con bambini piccoli",
  "Those wanting an obedient dog": "Chi cerca un cane obbediente",
  "Owners unwilling to groom regularly": "Proprietari non disposti a toelettare regolarmente",
  "Off-leash situations": "Situazioni senza guinzaglio",
  "Small apartments": "Piccoli appartamenti",
  "Sedentary lifestyles": "Stili di vita sedentari",
  "First-time owners": "Proprietari alle prime armi",
  "Apartment dwellers": "Residenti in appartamento",
  "Those often away from home": "Chi è spesso fuori casa",
  "Hot climates": "Climi caldi",
  "Cold climates": "Climi freddi",
  
  // Temperament tags
  "aloof": "riservato",
  "clownish": "buffo",
  "funny": "divertente",
  "courageous": "coraggioso",
  "playful": "giocherellone",
  "alert": "vigile",
  "energetic": "energico",
  "loyal": "leale",
  "affectionate": "affettuoso",
  "protective": "protettivo",
  "friendly": "amichevole",
  "intelligent": "intelligente",
  "stubborn": "testardo",
  "independent": "indipendente",
  "gentle": "gentile",
  "calm": "calmo",
  "active": "attivo",
  "spirited": "vivace",
  "bold": "audace",
  "confident": "sicuro",
  "devoted": "devoto",
  "eager": "desideroso",
  "loving": "amorevole",
  "patient": "paziente",
  "reserved": "riservato",
  "sensitive": "sensibile",
  "sweet": "dolce",
  "watchful": "attento",
  "wilful": "volitivo",
  "outgoing": "estroverso",
  "mischievous": "birichino",
  "curious": "curioso",
  "fearless": "impavido",
  "feisty": "combattivo",
  "lively": "vivace",
  "proud": "fiero",
  "dignified": "dignitoso",
  "brave": "coraggioso",
  "cheerful": "allegro",
  "determined": "determinato",
  "agile": "agile",
  "athletic": "atletico",
  "keen": "acuto",
  "obedient": "obbediente",
  "responsive": "reattivo",
  "trainable": "addestrabile",
  "sociable": "socievole",
  "trusting": "fiducioso",
  "happy": "felice",
  "hardworking": "lavoratore",
  "versatile": "versatile",
  "adaptable": "adattabile",
  "powerful": "potente",
  "regal": "regale",
  "noble": "nobile",
  "majestic": "maestoso",
  "serene": "sereno",
  "placid": "placido",
  "docile": "docile",
  "even-tempered": "equilibrato",
  "good-natured": "di buon carattere",
  "companionable": "socievole",
  "devoted": "devoto",
  "people-oriented": "orientato alle persone",
  "family-oriented": "orientato alla famiglia",
  "kid-friendly": "adatto ai bambini",
  "dog-friendly": "va d'accordo con altri cani",
  "cat-friendly": "va d'accordo con i gatti"
};

function translateFile(filename) {
  const filepath = path.join(breedsDir, filename);
  let content = fs.readFileSync(filepath, 'utf-8');
  
  // Apply common translations
  for (const [en, it] of Object.entries(commonTranslations)) {
    content = content.replace(new RegExp(escapeRegex(en), 'g'), it);
  }
  
  fs.writeFileSync(filepath, content);
  console.log(`Processed: ${filename}`);
}

function escapeRegex(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

const files = fs.readdirSync(breedsDir).filter(f => f.endsWith('.html'));
files.forEach(translateFile);
console.log(`\nProcessed ${files.length} files`);
