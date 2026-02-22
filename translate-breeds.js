#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const breedsDir = path.join(__dirname, 'it/breeds');
const files = fs.readdirSync(breedsDir).filter(f => f.endsWith('.html'));

// Translation mappings for common phrases
const translations = {
  // Verdict section
  "The ultimate family dog": "Il cane ideale per la famiglia",
  "Best suited for experienced owners": "Ideale per proprietari esperti",
  "Not ideal for first-time owners": "Non ideale per proprietari alle prime armi",
  "apartment living": "vita in appartamento",
  "Experienced dog owners": "Proprietari esperti",
  "Active families": "Famiglie attive",
  "Those wanting a protective dog": "Chi cerca un cane protettivo",
  "People with time for training": "Persone con tempo per l'addestramento",
  "Small apartments": "Piccoli appartamenti",
  // Common phrases
  "Generally healthy": "Generalmente sano",
  "prone to": "predisposto a",
  "High energy breed": "Razza ad alta energia",
  "requiring vigorous daily exercise": "che richiede esercizio quotidiano vigoroso",
  "at least an hour of activity": "almeno un'ora di attività",
  "Mental stimulation": "Stimolazione mentale",
  "training and puzzle toys": "addestramento e giochi puzzle",
  "behavioral issues": "problemi comportamentali",
  "Without adequate exercise": "Senza esercizio adeguato",
};

// Function to translate text - uses simple pattern matching for common phrases
// For full translation, we output what needs to be translated
function processFile(filename) {
  const filepath = path.join(breedsDir, filename);
  const content = fs.readFileSync(filepath, 'utf-8');
  
  // Check if there's English content to translate
  const hasEnglish = /content="[A-Z][a-z]+ [a-z]+ [a-z]+/.test(content) || 
                     /<p class="text-slate-600">[A-Z][a-z]+/.test(content);
  
  if (hasEnglish) {
    console.log(filename);
  }
}

files.forEach(processFile);
console.log(`\nTotal: ${files.length} files`);
