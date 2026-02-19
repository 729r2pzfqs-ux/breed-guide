#!/usr/bin/env python3
"""Generate breed pages 51-100 for BreedFinder.org"""

import os
import json

# Breed data for breeds 51-100
BREEDS = [
    {
        "id": "american-staffordshire-terrier",
        "name": "American Staffordshire Terrier",
        "group": "Terrier",
        "size_category": "Medium",
        "origin": "United States",
        "lifespan": "12-16 years",
        "height": "43-48 cm",
        "weight": "25-32 kg",
        "energy": 4, "grooming": 1, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 2,
        "temperament": ["Confident", "Loyal", "Courageous", "Good-natured"],
        "description": "The American Staffordshire Terrier is a confident, smart, and good-natured companion. Despite their muscular build, they're known for being loving family dogs who are great with children.",
        "best_for": ["Active families", "Experienced dog owners", "Those wanting a loyal companion"],
        "not_for": ["First-time owners", "Those away from home often", "Apartments without exercise access"],
        "verdict": "A loving, loyal family dog that thrives with proper training and socialization. Great for active families who can provide consistent leadership."
    },
    {
        "id": "staffordshire-bull-terrier",
        "name": "Staffordshire Bull Terrier",
        "group": "Terrier",
        "size_category": "Medium",
        "origin": "England",
        "lifespan": "12-14 years",
        "height": "36-41 cm",
        "weight": "11-17 kg",
        "energy": 4, "grooming": 1, "sociability": 5, "trainability": 4, "kid_friendly": 5, "barking": 2,
        "temperament": ["Brave", "Tenacious", "Affectionate", "Playful"],
        "description": "Known as the 'nanny dog' in Britain, Staffordshire Bull Terriers are incredibly affectionate with family, especially children. They're muscular but gentle souls.",
        "best_for": ["Families with children", "Active individuals", "Those wanting an affectionate pet"],
        "not_for": ["Multi-pet households without supervision", "Sedentary lifestyles", "First-time owners"],
        "verdict": "An exceptional family dog with a heart of gold. Perfect for families wanting a loyal, affectionate companion who loves children."
    },
    {
        "id": "cane-corso",
        "name": "Cane Corso",
        "group": "Working",
        "size_category": "Large",
        "origin": "Italy",
        "lifespan": "9-12 years",
        "height": "60-70 cm",
        "weight": "40-50 kg",
        "energy": 3, "grooming": 1, "sociability": 3, "trainability": 4, "kid_friendly": 3, "barking": 2,
        "temperament": ["Intelligent", "Loyal", "Protective", "Noble"],
        "description": "The Cane Corso is an Italian mastiff breed known for its imposing appearance and loyal nature. They're intelligent guardians who bond deeply with their families.",
        "best_for": ["Experienced owners", "Those wanting protection", "Homes with space"],
        "not_for": ["First-time owners", "Apartments", "Families with very young children"],
        "verdict": "A majestic guardian for experienced owners. Requires early socialization and firm, consistent training but rewards with unwavering loyalty."
    },
    {
        "id": "chow-chow",
        "name": "Chow Chow",
        "group": "Non-Sporting",
        "size_category": "Medium",
        "origin": "China",
        "lifespan": "8-12 years",
        "height": "46-56 cm",
        "weight": "20-32 kg",
        "energy": 2, "grooming": 5, "sociability": 2, "trainability": 2, "kid_friendly": 2, "barking": 2,
        "temperament": ["Dignified", "Loyal", "Independent", "Aloof"],
        "description": "The Chow Chow is a dignified, serious-minded breed known for its lion-like mane and blue-black tongue. They're fiercely loyal to their family but aloof with strangers.",
        "best_for": ["Experienced owners", "Those respecting independence", "Quiet households"],
        "not_for": ["First-time owners", "Families with young children", "Those wanting a cuddly dog"],
        "verdict": "A noble, cat-like companion for those who appreciate an independent spirit. Not for everyone, but deeply loyal to their chosen person."
    },
    {
        "id": "dalmatian",
        "name": "Dalmatian",
        "group": "Non-Sporting",
        "size_category": "Large",
        "origin": "Croatia",
        "lifespan": "11-13 years",
        "height": "56-61 cm",
        "weight": "23-27 kg",
        "energy": 5, "grooming": 2, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 3,
        "temperament": ["Energetic", "Playful", "Intelligent", "Outgoing"],
        "description": "Famous for their unique spotted coat, Dalmatians are athletic, energetic dogs originally bred to run alongside carriages. They need lots of exercise and mental stimulation.",
        "best_for": ["Very active families", "Runners and cyclists", "Homes with large yards"],
        "not_for": ["Sedentary lifestyles", "Small apartments", "Those without time for exercise"],
        "verdict": "A stunning, athletic companion for active owners who can match their endless energy. Perfect for runners and outdoor enthusiasts."
    },
    {
        "id": "basenji",
        "name": "Basenji",
        "group": "Hound",
        "size_category": "Small",
        "origin": "Central Africa",
        "lifespan": "13-14 years",
        "height": "41-43 cm",
        "weight": "9-12 kg",
        "energy": 4, "grooming": 1, "sociability": 3, "trainability": 2, "kid_friendly": 3, "barking": 1,
        "temperament": ["Independent", "Intelligent", "Alert", "Curious"],
        "description": "Known as the 'barkless dog,' Basenjis make a unique yodel-like sound instead of barking. They're cat-like in their independence and cleanliness.",
        "best_for": ["Experienced owners", "Those who appreciate independence", "Apartment dwellers wanting quiet"],
        "not_for": ["First-time owners", "Off-leash situations", "Those wanting eager-to-please dogs"],
        "verdict": "A unique, cat-like companion for experienced owners. Their quiet nature makes them great for apartments, but their independence requires patience."
    },
    {
        "id": "irish-setter",
        "name": "Irish Setter",
        "group": "Sporting",
        "size_category": "Large",
        "origin": "Ireland",
        "lifespan": "12-15 years",
        "height": "64-69 cm",
        "weight": "27-32 kg",
        "energy": 5, "grooming": 4, "sociability": 5, "trainability": 4, "kid_friendly": 5, "barking": 3,
        "temperament": ["Energetic", "Affectionate", "Outgoing", "Sweet-natured"],
        "description": "The Irish Setter is a gorgeous, mahogany-red sporting dog known for its friendly, outgoing personality. They're eternally youthful and full of enthusiasm.",
        "best_for": ["Active families", "Homes with children", "Those wanting an affectionate companion"],
        "not_for": ["Sedentary lifestyles", "Those wanting a guard dog", "Small living spaces"],
        "verdict": "A beautiful, joyful family dog that brings energy and love to any home. Perfect for active families who appreciate their playful, affectionate nature."
    },
    {
        "id": "english-setter",
        "name": "English Setter",
        "group": "Sporting",
        "size_category": "Large",
        "origin": "England",
        "lifespan": "10-12 years",
        "height": "61-69 cm",
        "weight": "25-36 kg",
        "energy": 4, "grooming": 4, "sociability": 5, "trainability": 4, "kid_friendly": 5, "barking": 3,
        "temperament": ["Gentle", "Friendly", "Mellow", "Affectionate"],
        "description": "The English Setter is known as the 'gentleman of the dog world.' They're elegant, gentle dogs with beautiful speckled coats and sweet dispositions.",
        "best_for": ["Families", "Those wanting a gentle companion", "Homes with other pets"],
        "not_for": ["Very small spaces", "Those wanting a guard dog", "Owners often away"],
        "verdict": "An elegant, gentle soul perfect for families. Their calm indoor demeanor and love of people make them wonderful companions."
    },
    {
        "id": "afghan-hound",
        "name": "Afghan Hound",
        "group": "Hound",
        "size_category": "Large",
        "origin": "Afghanistan",
        "lifespan": "12-14 years",
        "height": "63-74 cm",
        "weight": "23-27 kg",
        "energy": 4, "grooming": 5, "sociability": 3, "trainability": 2, "kid_friendly": 3, "barking": 2,
        "temperament": ["Dignified", "Independent", "Aloof", "Clownish"],
        "description": "The Afghan Hound is an ancient breed known for its stunning, flowing coat and regal appearance. Behind that dignified exterior lies a surprisingly silly personality.",
        "best_for": ["Experienced owners", "Those who enjoy grooming", "Fenced properties"],
        "not_for": ["First-time owners", "Those wanting easy training", "Small apartments"],
        "verdict": "A stunning, aristocratic companion for those willing to invest in grooming. Their unique mix of dignity and silliness makes them truly special."
    },
    {
        "id": "scottish-terrier",
        "name": "Scottish Terrier",
        "group": "Terrier",
        "size_category": "Small",
        "origin": "Scotland",
        "lifespan": "11-13 years",
        "height": "25-28 cm",
        "weight": "8-10 kg",
        "energy": 3, "grooming": 4, "sociability": 2, "trainability": 3, "kid_friendly": 3, "barking": 3,
        "temperament": ["Independent", "Confident", "Dignified", "Spirited"],
        "description": "The Scottish Terrier, or 'Scottie,' is a small but mighty terrier with a distinctive silhouette. They're confident, independent dogs with big personalities.",
        "best_for": ["Those appreciating independence", "Apartment dwellers", "Adults or older children"],
        "not_for": ["Families with young children", "Multi-dog households", "Those wanting a lap dog"],
        "verdict": "A dignified, spirited companion with a mind of their own. Perfect for those who appreciate a dog with independent character."
    },
    {
        "id": "american-bulldog",
        "name": "American Bulldog",
        "group": "Working",
        "size_category": "Large",
        "origin": "United States",
        "lifespan": "10-15 years",
        "height": "51-71 cm",
        "weight": "27-58 kg",
        "energy": 4, "grooming": 1, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 3,
        "temperament": ["Confident", "Loyal", "Friendly", "Assertive"],
        "description": "The American Bulldog is a powerful, athletic breed that's both a working dog and family companion. They're confident and loyal with a gentle side for family.",
        "best_for": ["Active families", "Experienced owners", "Those wanting protection"],
        "not_for": ["First-time owners", "Apartment living", "Sedentary lifestyles"],
        "verdict": "A powerful, loyal family protector with a heart of gold. Great for active families who can provide training and exercise."
    },
    {
        "id": "belgian-tervuren",
        "name": "Belgian Tervuren",
        "group": "Herding",
        "size_category": "Large",
        "origin": "Belgium",
        "lifespan": "12-14 years",
        "height": "56-66 cm",
        "weight": "20-30 kg",
        "energy": 5, "grooming": 4, "sociability": 4, "trainability": 5, "kid_friendly": 4, "barking": 4,
        "temperament": ["Intelligent", "Alert", "Devoted", "Energetic"],
        "description": "The Belgian Tervuren is an elegant herding dog with a beautiful mahogany coat. They're highly intelligent and excel in various dog sports and work.",
        "best_for": ["Active owners", "Dog sport enthusiasts", "Those wanting a trainable dog"],
        "not_for": ["Sedentary lifestyles", "First-time owners", "Those away often"],
        "verdict": "An elegant, brilliant working dog that thrives with a job to do. Perfect for active owners interested in dog sports or training."
    },
    {
        "id": "belgian-sheepdog",
        "name": "Belgian Sheepdog",
        "group": "Herding",
        "size_category": "Large",
        "origin": "Belgium",
        "lifespan": "12-14 years",
        "height": "56-66 cm",
        "weight": "20-30 kg",
        "energy": 5, "grooming": 4, "sociability": 4, "trainability": 5, "kid_friendly": 4, "barking": 4,
        "temperament": ["Intelligent", "Versatile", "Devoted", "Alert"],
        "description": "Also known as the Groenendael, this elegant black-coated Belgian breed is known for its intelligence and versatility. They excel in obedience, herding, and protection work.",
        "best_for": ["Experienced owners", "Active families", "Those wanting a versatile dog"],
        "not_for": ["First-time owners", "Sedentary lifestyles", "Small apartments"],
        "verdict": "A stunning, intelligent companion for active, experienced owners. Their devotion and trainability make them excellent working partners."
    },
    {
        "id": "belgian-laekenois",
        "name": "Belgian Laekenois",
        "group": "Herding",
        "size_category": "Large",
        "origin": "Belgium",
        "lifespan": "10-12 years",
        "height": "56-66 cm",
        "weight": "20-30 kg",
        "energy": 5, "grooming": 3, "sociability": 3, "trainability": 5, "kid_friendly": 3, "barking": 4,
        "temperament": ["Alert", "Intelligent", "Protective", "Devoted"],
        "description": "The rarest of the Belgian shepherds, the Laekenois has a distinctive rough, tousled coat. They're watchful guardians with strong protective instincts.",
        "best_for": ["Experienced owners", "Those wanting a rare breed", "Active households"],
        "not_for": ["First-time owners", "Families with young children", "Sedentary lifestyles"],
        "verdict": "A rare, devoted guardian for experienced owners. Their protective nature and intelligence make them excellent working dogs."
    },
    {
        "id": "bloodhound",
        "name": "Bloodhound",
        "group": "Hound",
        "size_category": "Large",
        "origin": "Belgium/France",
        "lifespan": "10-12 years",
        "height": "58-69 cm",
        "weight": "36-50 kg",
        "energy": 3, "grooming": 2, "sociability": 4, "trainability": 2, "kid_friendly": 4, "barking": 4,
        "temperament": ["Gentle", "Patient", "Noble", "Stubborn"],
        "description": "The Bloodhound has the most powerful nose in the dog world. They're gentle giants known for their tracking abilities and patient, affectionate nature.",
        "best_for": ["Patient owners", "Those with large yards", "Families"],
        "not_for": ["Neat freaks", "Those wanting easy training", "Small spaces"],
        "verdict": "A gentle, noble scent hound for patient owners. Their drool and stubbornness are worth it for their loving, docile nature."
    },
    {
        "id": "whippet",
        "name": "Whippet",
        "group": "Hound",
        "size_category": "Medium",
        "origin": "England",
        "lifespan": "12-15 years",
        "height": "44-51 cm",
        "weight": "9-14 kg",
        "energy": 3, "grooming": 1, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 1,
        "temperament": ["Gentle", "Quiet", "Affectionate", "Playful"],
        "description": "The Whippet is a medium-sized sighthound that's like a smaller Greyhound. They're gentle couch potatoes indoors but love to sprint outdoors.",
        "best_for": ["Apartment dwellers", "Families", "Those wanting a quiet dog"],
        "not_for": ["Off-leash in unfenced areas", "Very cold climates", "Those without comfy furniture"],
        "verdict": "The perfect couch companion that can also zoom. Ideal for those wanting a gentle, quiet, low-maintenance dog."
    },
    {
        "id": "italian-greyhound",
        "name": "Italian Greyhound",
        "group": "Toy",
        "size_category": "Small",
        "origin": "Italy",
        "lifespan": "14-15 years",
        "height": "33-38 cm",
        "weight": "3-5 kg",
        "energy": 3, "grooming": 1, "sociability": 4, "trainability": 3, "kid_friendly": 2, "barking": 2,
        "temperament": ["Affectionate", "Playful", "Sensitive", "Alert"],
        "description": "The Italian Greyhound is a miniature sighthound with an elegant, slender build. They're affectionate lap dogs who love warmth and cuddles.",
        "best_for": ["Apartment dwellers", "Adults", "Those wanting an affectionate lap dog"],
        "not_for": ["Families with young children", "Cold climates without sweaters", "Rough play"],
        "verdict": "An elegant, affectionate miniature companion. Perfect for adults seeking a devoted, cuddly lap dog."
    },
    {
        "id": "greyhound",
        "name": "Greyhound",
        "group": "Hound",
        "size_category": "Large",
        "origin": "Egypt/England",
        "lifespan": "10-13 years",
        "height": "68-76 cm",
        "weight": "27-40 kg",
        "energy": 2, "grooming": 1, "sociability": 4, "trainability": 3, "kid_friendly": 4, "barking": 1,
        "temperament": ["Gentle", "Quiet", "Independent", "Noble"],
        "description": "Despite being the fastest dog breed, Greyhounds are calm, gentle couch potatoes. Many retired racing Greyhounds make wonderful, low-key family pets.",
        "best_for": ["Apartment dwellers", "Those wanting a calm dog", "Families"],
        "not_for": ["Off-leash in unfenced areas", "Homes with small pets", "Cold climates without coats"],
        "verdict": "The ultimate couch potato athlete. Surprisingly perfect for apartments due to their calm, gentle nature."
    },
    {
        "id": "saluki",
        "name": "Saluki",
        "group": "Hound",
        "size_category": "Large",
        "origin": "Middle East",
        "lifespan": "10-17 years",
        "height": "58-71 cm",
        "weight": "18-27 kg",
        "energy": 4, "grooming": 2, "sociability": 3, "trainability": 2, "kid_friendly": 3, "barking": 1,
        "temperament": ["Gentle", "Dignified", "Independent", "Reserved"],
        "description": "One of the oldest dog breeds, Salukis are elegant, cat-like sighthounds. They're gentle and devoted to family but reserved with strangers.",
        "best_for": ["Experienced owners", "Those appreciating elegance", "Fenced properties"],
        "not_for": ["First-time owners", "Off-leash areas", "Homes with small pets"],
        "verdict": "An ancient, elegant companion for those who appreciate their dignified, independent nature. Requires secure fencing."
    },
    {
        "id": "pharaoh-hound",
        "name": "Pharaoh Hound",
        "group": "Hound",
        "size_category": "Medium",
        "origin": "Malta",
        "lifespan": "12-14 years",
        "height": "53-64 cm",
        "weight": "18-27 kg",
        "energy": 4, "grooming": 1, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 3,
        "temperament": ["Affectionate", "Playful", "Intelligent", "Noble"],
        "description": "The Pharaoh Hound is known for its unique ability to 'blush' - their nose and ears turn rosy when excited. They're athletic, playful, and affectionate.",
        "best_for": ["Active families", "Those wanting a unique breed", "Warm climates"],
        "not_for": ["Cold climates", "Off-leash in unfenced areas", "First-time owners"],
        "verdict": "A unique, affectionate sighthound that actually blushes! Perfect for active families in warmer climates."
    },
    {
        "id": "keeshond",
        "name": "Keeshond",
        "group": "Non-Sporting",
        "size_category": "Medium",
        "origin": "Netherlands",
        "lifespan": "12-15 years",
        "height": "43-46 cm",
        "weight": "16-20 kg",
        "energy": 3, "grooming": 4, "sociability": 5, "trainability": 4, "kid_friendly": 5, "barking": 4,
        "temperament": ["Friendly", "Outgoing", "Alert", "Playful"],
        "description": "The Keeshond is a fluffy spitz-type dog known for its spectacular 'spectacles' - markings around the eyes. They're friendly, outgoing family dogs.",
        "best_for": ["Families", "Those wanting a friendly dog", "Those who enjoy grooming"],
        "not_for": ["Those wanting a quiet dog", "Hot climates", "Low-maintenance seekers"],
        "verdict": "A friendly, fluffy companion that loves everyone. Perfect for families wanting an outgoing, people-oriented dog."
    },
    {
        "id": "finnish-lapphund",
        "name": "Finnish Lapphund",
        "group": "Herding",
        "size_category": "Medium",
        "origin": "Finland",
        "lifespan": "12-15 years",
        "height": "41-52 cm",
        "weight": "15-24 kg",
        "energy": 3, "grooming": 4, "sociability": 5, "trainability": 4, "kid_friendly": 5, "barking": 4,
        "temperament": ["Friendly", "Calm", "Courageous", "Faithful"],
        "description": "Originally bred to herd reindeer, the Finnish Lapphund is a gentle, friendly spitz breed. They're great with families and adapt well to various lifestyles.",
        "best_for": ["Families", "Active households", "Cold climates"],
        "not_for": ["Hot climates", "Those wanting minimal grooming", "Very small apartments"],
        "verdict": "A wonderful, friendly family dog from the Arctic. Perfect for families wanting a gentle, adaptable companion."
    },
    {
        "id": "norwegian-elkhound",
        "name": "Norwegian Elkhound",
        "group": "Hound",
        "size_category": "Medium",
        "origin": "Norway",
        "lifespan": "12-15 years",
        "height": "49-52 cm",
        "weight": "20-25 kg",
        "energy": 4, "grooming": 3, "sociability": 4, "trainability": 3, "kid_friendly": 4, "barking": 5,
        "temperament": ["Bold", "Energetic", "Loyal", "Friendly"],
        "description": "The Norwegian Elkhound is an ancient Nordic breed that hunted moose and bears. They're bold, friendly dogs with a distinctive silver-gray coat.",
        "best_for": ["Active families", "Those appreciating independence", "Cold climates"],
        "not_for": ["Hot climates", "Those wanting a quiet dog", "Apartment dwellers"],
        "verdict": "A bold, ancient Viking dog for active families. Their loyalty and friendliness make them great companions."
    },
    {
        "id": "alaskan-klee-kai",
        "name": "Alaskan Klee Kai",
        "group": "Non-Sporting",
        "size_category": "Small",
        "origin": "United States",
        "lifespan": "13-16 years",
        "height": "33-43 cm",
        "weight": "4-10 kg",
        "energy": 4, "grooming": 3, "sociability": 2, "trainability": 4, "kid_friendly": 3, "barking": 4,
        "temperament": ["Alert", "Intelligent", "Curious", "Reserved"],
        "description": "The Alaskan Klee Kai looks like a miniature Husky but has its own distinct personality. They're intelligent but can be reserved with strangers.",
        "best_for": ["Experienced owners", "Active individuals", "Those appreciating a watchful dog"],
        "not_for": ["Families with young children", "Those wanting a social butterfly", "First-time owners"],
        "verdict": "A mini-Husky with a big personality. Best for experienced owners who can handle their intelligence and wariness of strangers."
    },
    {
        "id": "chinese-crested",
        "name": "Chinese Crested",
        "group": "Toy",
        "size_category": "Small",
        "origin": "China/Africa",
        "lifespan": "13-18 years",
        "height": "28-33 cm",
        "weight": "3-5 kg",
        "energy": 3, "grooming": 2, "sociability": 4, "trainability": 3, "kid_friendly": 3, "barking": 2,
        "temperament": ["Affectionate", "Alert", "Playful", "Devoted"],
        "description": "The Chinese Crested comes in two varieties: hairless and powderpuff. Both are loving, playful companions that bond strongly with their owners.",
        "best_for": ["Apartment dwellers", "Those with allergies", "Singles or couples"],
        "not_for": ["Cold climates without protection", "Rough play", "Those wanting a robust dog"],
        "verdict": "A unique, devoted lap dog that's great for allergy sufferers. They need sun protection and sweaters but reward with endless affection."
    },
    {
        "id": "lhasa-apso",
        "name": "Lhasa Apso",
        "group": "Non-Sporting",
        "size_category": "Small",
        "origin": "Tibet",
        "lifespan": "12-15 years",
        "height": "25-28 cm",
        "weight": "5-8 kg",
        "energy": 3, "grooming": 5, "sociability": 3, "trainability": 3, "kid_friendly": 3, "barking": 4,
        "temperament": ["Confident", "Smart", "Loyal", "Aloof"],
        "description": "The Lhasa Apso was bred as a sentinel dog in Tibetan monasteries. They're confident, sometimes stubborn dogs with a regal air.",
        "best_for": ["Adults", "Apartment dwellers", "Those appreciating independence"],
        "not_for": ["Families with young children", "Those wanting easy grooming", "First-time owners"],
        "verdict": "A regal, confident companion from Tibet. Best for patient owners who appreciate their independent, watchful nature."
    },
    {
        "id": "tibetan-terrier",
        "name": "Tibetan Terrier",
        "group": "Non-Sporting",
        "size_category": "Medium",
        "origin": "Tibet",
        "lifespan": "15-16 years",
        "height": "36-41 cm",
        "weight": "8-14 kg",
        "energy": 3, "grooming": 5, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 3,
        "temperament": ["Affectionate", "Sensitive", "Gentle", "Reserved"],
        "description": "Despite the name, Tibetan Terriers aren't terriers at all. They're gentle, affectionate dogs bred as companions and good luck charms in Tibet.",
        "best_for": ["Families", "Those wanting a loyal companion", "Apartment dwellers"],
        "not_for": ["Those wanting minimal grooming", "Very active households", "Rough play"],
        "verdict": "A gentle, loyal companion with a long lifespan. Great for families wanting an affectionate, adaptable dog."
    },
    {
        "id": "tibetan-mastiff",
        "name": "Tibetan Mastiff",
        "group": "Working",
        "size_category": "Giant",
        "origin": "Tibet",
        "lifespan": "10-12 years",
        "height": "61-76 cm",
        "weight": "32-68 kg",
        "energy": 2, "grooming": 4, "sociability": 2, "trainability": 2, "kid_friendly": 2, "barking": 4,
        "temperament": ["Independent", "Reserved", "Protective", "Intelligent"],
        "description": "The Tibetan Mastiff is an ancient guardian breed known for its imposing size and protective nature. They're independent thinkers who take guarding seriously.",
        "best_for": ["Very experienced owners", "Rural properties", "Those wanting a guardian"],
        "not_for": ["First-time owners", "Apartments", "Families with young children"],
        "verdict": "A majestic guardian for very experienced owners only. Requires space, patience, and understanding of guardian breeds."
    },
    {
        "id": "leonberger",
        "name": "Leonberger",
        "group": "Working",
        "size_category": "Giant",
        "origin": "Germany",
        "lifespan": "7-9 years",
        "height": "65-80 cm",
        "weight": "41-77 kg",
        "energy": 3, "grooming": 4, "sociability": 5, "trainability": 4, "kid_friendly": 5, "barking": 3,
        "temperament": ["Gentle", "Friendly", "Playful", "Patient"],
        "description": "The Leonberger is a gentle giant bred to resemble a lion. Despite their imposing size, they're known as 'gentle giants' who are wonderful with children.",
        "best_for": ["Families with space", "Those wanting a gentle giant", "Experienced large-dog owners"],
        "not_for": ["Small apartments", "Those with limited space", "First-time owners"],
        "verdict": "The ultimate gentle giant - a lion-like dog with a heart of gold. Perfect for families with space who want a loving, patient companion."
    },
    {
        "id": "anatolian-shepherd",
        "name": "Anatolian Shepherd",
        "group": "Working",
        "size_category": "Giant",
        "origin": "Turkey",
        "lifespan": "11-13 years",
        "height": "71-81 cm",
        "weight": "41-68 kg",
        "energy": 3, "grooming": 2, "sociability": 2, "trainability": 2, "kid_friendly": 3, "barking": 4,
        "temperament": ["Independent", "Loyal", "Protective", "Reserved"],
        "description": "The Anatolian Shepherd is an ancient livestock guardian with powerful protective instincts. They're independent, intelligent, and fiercely loyal to their family.",
        "best_for": ["Rural properties", "Livestock owners", "Very experienced owners"],
        "not_for": ["First-time owners", "Apartments", "Those wanting an obedient dog"],
        "verdict": "A serious guardian for experienced owners with livestock or rural property. Not a casual pet - they need a job."
    },
    {
        "id": "kuvasz",
        "name": "Kuvasz",
        "group": "Working",
        "size_category": "Large",
        "origin": "Hungary",
        "lifespan": "10-12 years",
        "height": "66-76 cm",
        "weight": "32-52 kg",
        "energy": 3, "grooming": 3, "sociability": 3, "trainability": 3, "kid_friendly": 4, "barking": 4,
        "temperament": ["Loyal", "Patient", "Independent", "Protective"],
        "description": "The Kuvasz is a majestic white Hungarian guardian breed. They're deeply loyal and protective but also patient and gentle with their family.",
        "best_for": ["Experienced owners", "Families with older children", "Those wanting a guardian"],
        "not_for": ["First-time owners", "Apartments", "Those wanting easy training"],
        "verdict": "A loyal, majestic guardian for experienced owners. Their protective nature requires early socialization but rewards with devoted companionship."
    },
    {
        "id": "komondor",
        "name": "Komondor",
        "group": "Working",
        "size_category": "Large",
        "origin": "Hungary",
        "lifespan": "10-12 years",
        "height": "65-80 cm",
        "weight": "36-50 kg",
        "energy": 2, "grooming": 5, "sociability": 2, "trainability": 2, "kid_friendly": 3, "barking": 4,
        "temperament": ["Independent", "Calm", "Protective", "Devoted"],
        "description": "Known for their unique corded coat, Komondors are powerful livestock guardians. They're calm and devoted but serious about protecting their family.",
        "best_for": ["Rural properties", "Experienced owners", "Those wanting a unique breed"],
        "not_for": ["First-time owners", "Apartments", "Those wanting easy grooming"],
        "verdict": "A unique, powerful guardian with an unforgettable appearance. Best for experienced owners who can manage their cords and independent nature."
    },
    {
        "id": "puli",
        "name": "Puli",
        "group": "Herding",
        "size_category": "Medium",
        "origin": "Hungary",
        "lifespan": "10-15 years",
        "height": "38-44 cm",
        "weight": "11-16 kg",
        "energy": 4, "grooming": 5, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 4,
        "temperament": ["Intelligent", "Energetic", "Faithful", "Agile"],
        "description": "The Puli is a mop-like Hungarian herding dog known for its distinctive corded coat. They're lively, intelligent, and surprisingly agile.",
        "best_for": ["Active owners", "Those who appreciate unique coats", "Dog sport enthusiasts"],
        "not_for": ["Those wanting low maintenance", "Sedentary lifestyles", "Hot climates"],
        "verdict": "A bouncy, intelligent mop-dog that's full of life. Perfect for active owners who enjoy their unique appearance and lively personality."
    },
    {
        "id": "pumi",
        "name": "Pumi",
        "group": "Herding",
        "size_category": "Medium",
        "origin": "Hungary",
        "lifespan": "12-13 years",
        "height": "38-47 cm",
        "weight": "8-15 kg",
        "energy": 5, "grooming": 3, "sociability": 4, "trainability": 5, "kid_friendly": 4, "barking": 5,
        "temperament": ["Energetic", "Intelligent", "Alert", "Lively"],
        "description": "The Pumi is a Hungarian herding terrier with distinctive curly ears. They're incredibly energetic, intelligent, and excel at dog sports.",
        "best_for": ["Very active owners", "Dog sport enthusiasts", "Those wanting a trainable dog"],
        "not_for": ["Sedentary lifestyles", "Those wanting a quiet dog", "First-time owners"],
        "verdict": "A tireless, intelligent athlete in a cute package. Perfect for active owners who want a dog sport partner."
    },
    {
        "id": "beauceron",
        "name": "Beauceron",
        "group": "Herding",
        "size_category": "Large",
        "origin": "France",
        "lifespan": "10-12 years",
        "height": "61-70 cm",
        "weight": "30-45 kg",
        "energy": 4, "grooming": 2, "sociability": 3, "trainability": 4, "kid_friendly": 3, "barking": 3,
        "temperament": ["Loyal", "Protective", "Intelligent", "Watchful"],
        "description": "The Beauceron is a powerful French herding dog with distinctive double dewclaws. They're intelligent, versatile, and deeply loyal to their family.",
        "best_for": ["Experienced owners", "Active households", "Those wanting a versatile dog"],
        "not_for": ["First-time owners", "Apartments", "Sedentary lifestyles"],
        "verdict": "A powerful, intelligent working dog for experienced owners. Their versatility and loyalty make them excellent companions for the right person."
    },
    {
        "id": "briard",
        "name": "Briard",
        "group": "Herding",
        "size_category": "Large",
        "origin": "France",
        "lifespan": "12 years",
        "height": "58-69 cm",
        "weight": "25-45 kg",
        "energy": 4, "grooming": 5, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 3,
        "temperament": ["Loyal", "Protective", "Intelligent", "Loving"],
        "description": "The Briard is a large French herding dog with a distinctive long, wavy coat. They're known for their loyalty and are often called 'a heart wrapped in fur.'",
        "best_for": ["Active families", "Those who enjoy grooming", "Experienced owners"],
        "not_for": ["Those wanting minimal grooming", "Sedentary lifestyles", "First-time owners"],
        "verdict": "A 'heart wrapped in fur' - loyal, loving, and intelligent. Perfect for active families who don't mind the grooming commitment."
    },
    {
        "id": "airedale-terrier",
        "name": "Airedale Terrier",
        "group": "Terrier",
        "size_category": "Large",
        "origin": "England",
        "lifespan": "11-14 years",
        "height": "56-61 cm",
        "weight": "18-29 kg",
        "energy": 4, "grooming": 4, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 3,
        "temperament": ["Confident", "Courageous", "Friendly", "Intelligent"],
        "description": "The 'King of Terriers' is the largest terrier breed. They're confident, versatile dogs that excel in many activities and make loyal family companions.",
        "best_for": ["Active families", "Those wanting a versatile dog", "Experienced owners"],
        "not_for": ["Sedentary lifestyles", "Those wanting minimal grooming", "Multi-pet homes"],
        "verdict": "The King of Terriers - versatile, confident, and full of personality. Great for active families who want an all-around companion."
    },
    {
        "id": "soft-coated-wheaten-terrier",
        "name": "Soft Coated Wheaten Terrier",
        "group": "Terrier",
        "size_category": "Medium",
        "origin": "Ireland",
        "lifespan": "12-14 years",
        "height": "43-48 cm",
        "weight": "14-20 kg",
        "energy": 4, "grooming": 5, "sociability": 5, "trainability": 3, "kid_friendly": 5, "barking": 3,
        "temperament": ["Happy", "Friendly", "Devoted", "Playful"],
        "description": "The Wheaten Terrier is known for its silky, wheat-colored coat and exuberant 'Wheaten greeting.' They're less scrappy than most terriers and love everyone.",
        "best_for": ["Families", "Those wanting a friendly dog", "Allergy sufferers"],
        "not_for": ["Those wanting minimal grooming", "Those disliking jumping", "Neat freaks"],
        "verdict": "An exuberant, friendly family dog that greets everyone with joy. Perfect for families wanting an affectionate, hypoallergenic companion."
    },
    {
        "id": "jack-russell-terrier",
        "name": "Jack Russell Terrier",
        "group": "Terrier",
        "size_category": "Small",
        "origin": "England",
        "lifespan": "13-16 years",
        "height": "25-30 cm",
        "weight": "5-8 kg",
        "energy": 5, "grooming": 1, "sociability": 4, "trainability": 4, "kid_friendly": 3, "barking": 5,
        "temperament": ["Energetic", "Fearless", "Intelligent", "Athletic"],
        "description": "The Jack Russell is a small but mighty terrier with endless energy. They're intelligent, athletic, and need plenty of mental and physical exercise.",
        "best_for": ["Very active owners", "Those wanting a trainable small dog", "Rural properties"],
        "not_for": ["Sedentary lifestyles", "Apartments without exercise", "First-time owners"],
        "verdict": "A small dog with a big personality and endless energy. Perfect for active owners who can match their intensity."
    },
    {
        "id": "parson-russell-terrier",
        "name": "Parson Russell Terrier",
        "group": "Terrier",
        "size_category": "Small",
        "origin": "England",
        "lifespan": "13-15 years",
        "height": "33-36 cm",
        "weight": "6-8 kg",
        "energy": 5, "grooming": 2, "sociability": 4, "trainability": 4, "kid_friendly": 3, "barking": 4,
        "temperament": ["Bold", "Clever", "Athletic", "Friendly"],
        "description": "Similar to the Jack Russell but slightly taller, the Parson Russell is an athletic, intelligent terrier. They excel in earthdog trials and agility.",
        "best_for": ["Active owners", "Dog sport enthusiasts", "Those wanting a small athletic dog"],
        "not_for": ["Sedentary lifestyles", "First-time owners", "Homes with small pets"],
        "verdict": "An athletic, clever terrier for active owners. Great for dog sports and owners who can provide plenty of exercise and mental stimulation."
    },
    {
        "id": "toy-fox-terrier",
        "name": "Toy Fox Terrier",
        "group": "Toy",
        "size_category": "Toy",
        "origin": "United States",
        "lifespan": "13-15 years",
        "height": "22-29 cm",
        "weight": "1.5-3.5 kg",
        "energy": 4, "grooming": 1, "sociability": 4, "trainability": 4, "kid_friendly": 3, "barking": 4,
        "temperament": ["Intelligent", "Alert", "Friendly", "Spirited"],
        "description": "The Toy Fox Terrier is a tiny but tenacious companion. They have all the terrier spirit packed into a portable package.",
        "best_for": ["Apartment dwellers", "Seniors", "Those wanting a small trainable dog"],
        "not_for": ["Families with very young children", "Cold climates", "Rough play"],
        "verdict": "A pocket-sized terrier with a big personality. Perfect for those wanting terrier spirit in a compact, trainable package."
    },
    {
        "id": "rat-terrier",
        "name": "Rat Terrier",
        "group": "Terrier",
        "size_category": "Small",
        "origin": "United States",
        "lifespan": "12-18 years",
        "height": "25-46 cm",
        "weight": "4-11 kg",
        "energy": 4, "grooming": 1, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 3,
        "temperament": ["Intelligent", "Alert", "Loving", "Inquisitive"],
        "description": "The Rat Terrier is an American farm dog that's both a ratter and companion. They come in two sizes and are known for their intelligence and affection.",
        "best_for": ["Families", "Active individuals", "Those wanting a versatile small dog"],
        "not_for": ["Homes with small pets", "Those wanting a couch potato", "Very cold climates"],
        "verdict": "An intelligent, affectionate American terrier. Great for families wanting an adaptable, loving small dog."
    },
    {
        "id": "dogo-argentino",
        "name": "Dogo Argentino",
        "group": "Working",
        "size_category": "Large",
        "origin": "Argentina",
        "lifespan": "9-15 years",
        "height": "60-68 cm",
        "weight": "35-45 kg",
        "energy": 4, "grooming": 1, "sociability": 3, "trainability": 4, "kid_friendly": 3, "barking": 2,
        "temperament": ["Loyal", "Courageous", "Friendly", "Cheerful"],
        "description": "The Dogo Argentino was bred for big-game hunting. They're powerful, athletic dogs that are surprisingly affectionate with their families.",
        "best_for": ["Experienced owners", "Active families", "Those wanting a loyal companion"],
        "not_for": ["First-time owners", "Apartments", "Multi-pet households"],
        "verdict": "A powerful, loyal athlete for experienced owners. Their affectionate nature with family makes them devoted companions."
    },
    {
        "id": "boerboel",
        "name": "Boerboel",
        "group": "Working",
        "size_category": "Giant",
        "origin": "South Africa",
        "lifespan": "9-11 years",
        "height": "61-70 cm",
        "weight": "68-90 kg",
        "energy": 3, "grooming": 1, "sociability": 3, "trainability": 4, "kid_friendly": 4, "barking": 2,
        "temperament": ["Confident", "Calm", "Intelligent", "Protective"],
        "description": "The Boerboel is a powerful South African mastiff bred to protect homesteads. They're confident, intelligent, and devoted to their families.",
        "best_for": ["Very experienced owners", "Rural properties", "Those wanting a guardian"],
        "not_for": ["First-time owners", "Apartments", "Those unable to provide leadership"],
        "verdict": "A massive, confident guardian for very experienced owners. Their devotion to family is unmatched, but they need firm, fair leadership."
    },
    {
        "id": "american-eskimo-dog",
        "name": "American Eskimo Dog",
        "group": "Non-Sporting",
        "size_category": "Small",
        "origin": "Germany/United States",
        "lifespan": "13-15 years",
        "height": "23-48 cm",
        "weight": "3-18 kg",
        "energy": 4, "grooming": 4, "sociability": 4, "trainability": 5, "kid_friendly": 4, "barking": 5,
        "temperament": ["Intelligent", "Alert", "Friendly", "Eager to please"],
        "description": "Despite the name, American Eskimos are German spitz dogs. They come in three sizes and are known for their brilliant white coats and trainability.",
        "best_for": ["Families", "Those wanting a trainable dog", "Dog sport enthusiasts"],
        "not_for": ["Those wanting a quiet dog", "Hot climates", "Minimal grooming seekers"],
        "verdict": "A beautiful, brilliant companion that loves to learn. Perfect for families wanting an intelligent, trainable dog."
    },
    {
        "id": "shikoku",
        "name": "Shikoku",
        "group": "Hound",
        "size_category": "Medium",
        "origin": "Japan",
        "lifespan": "10-12 years",
        "height": "43-55 cm",
        "weight": "15-25 kg",
        "energy": 4, "grooming": 3, "sociability": 3, "trainability": 3, "kid_friendly": 3, "barking": 3,
        "temperament": ["Brave", "Alert", "Loyal", "Cautious"],
        "description": "The Shikoku is a rare Japanese breed originally used for hunting boar. They're athletic, intelligent, and form strong bonds with their owners.",
        "best_for": ["Experienced owners", "Active individuals", "Those wanting a rare breed"],
        "not_for": ["First-time owners", "Multi-pet households", "Those wanting a social butterfly"],
        "verdict": "A rare, athletic Japanese hunting dog for experienced owners. Their loyalty and intelligence reward those who earn their trust."
    },
    {
        "id": "thai-ridgeback",
        "name": "Thai Ridgeback",
        "group": "Hound",
        "size_category": "Medium",
        "origin": "Thailand",
        "lifespan": "12-13 years",
        "height": "51-61 cm",
        "weight": "23-34 kg",
        "energy": 4, "grooming": 1, "sociability": 2, "trainability": 3, "kid_friendly": 3, "barking": 2,
        "temperament": ["Independent", "Intelligent", "Loyal", "Protective"],
        "description": "The Thai Ridgeback is an ancient, primitive breed with a distinctive ridge of hair along its back. They're independent and bond strongly with one person.",
        "best_for": ["Experienced owners", "Warm climates", "Those wanting a unique breed"],
        "not_for": ["First-time owners", "Multi-pet households", "Cold climates"],
        "verdict": "A rare, primitive breed for experienced owners who appreciate their independence. Their loyalty to their person is absolute."
    },
    {
        "id": "xoloitzcuintli",
        "name": "Xoloitzcuintli",
        "group": "Non-Sporting",
        "size_category": "Medium",
        "origin": "Mexico",
        "lifespan": "13-18 years",
        "height": "25-60 cm",
        "weight": "4-25 kg",
        "energy": 3, "grooming": 1, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 2,
        "temperament": ["Loyal", "Alert", "Calm", "Affectionate"],
        "description": "The ancient Aztec dog, the Xolo comes in three sizes and two varieties (hairless and coated). They're calm, loyal companions with a long history.",
        "best_for": ["Allergy sufferers", "Those wanting a unique breed", "Apartment dwellers"],
        "not_for": ["Very cold climates", "Harsh sun without protection", "Those wanting a fluffy dog"],
        "verdict": "An ancient, unique companion that's perfect for allergy sufferers. Their calm, loyal nature makes them excellent apartment dogs."
    },
    {
        "id": "peruvian-inca-orchid",
        "name": "Peruvian Inca Orchid",
        "group": "Hound",
        "size_category": "Medium",
        "origin": "Peru",
        "lifespan": "12-14 years",
        "height": "25-65 cm",
        "weight": "4-25 kg",
        "energy": 3, "grooming": 1, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 3,
        "temperament": ["Affectionate", "Loyal", "Alert", "Noble"],
        "description": "The Peruvian Inca Orchid is an ancient hairless breed from Peru. They come in three sizes and are known for their affectionate, gentle nature.",
        "best_for": ["Allergy sufferers", "Those wanting a gentle companion", "Mild climates"],
        "not_for": ["Extreme climates", "Those wanting a rugged outdoor dog", "Rough play"],
        "verdict": "A gentle, ancient hairless breed perfect for allergy sufferers. They need sun protection but reward with devoted, affectionate companionship."
    },
    {
        "id": "entlebucher-mountain-dog",
        "name": "Entlebucher Mountain Dog",
        "group": "Herding",
        "size_category": "Medium",
        "origin": "Switzerland",
        "lifespan": "11-13 years",
        "height": "42-52 cm",
        "weight": "20-30 kg",
        "energy": 4, "grooming": 2, "sociability": 4, "trainability": 4, "kid_friendly": 4, "barking": 3,
        "temperament": ["Loyal", "Smart", "Energetic", "Confident"],
        "description": "The smallest of the Swiss mountain dogs, the Entlebucher is an energetic, intelligent herding breed. They're loyal companions who excel at dog sports.",
        "best_for": ["Active families", "Dog sport enthusiasts", "Those wanting a loyal companion"],
        "not_for": ["Sedentary lifestyles", "Apartment dwellers", "First-time owners"],
        "verdict": "The smallest Swiss mountain dog with a big personality. Perfect for active families wanting a loyal, athletic companion."
    }
]

def generate_paw_rating(count):
    """Generate paw SVG rating icons"""
    filled = '<span class="text-amber-500">🐾</span>'
    empty = '<span class="text-slate-200">🐾</span>'
    return (filled * count) + (empty * (5 - count))

def generate_breed_page(breed):
    """Generate HTML for a single breed page"""
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{breed["name"]}: Breed Guide, Temperament & Care | BreedFinder</title>
    <meta name="description" content="Complete guide to the {breed["name"]}: temperament, exercise needs, grooming, health issues, and whether this breed is right for you.">
    <link rel="canonical" href="https://breedfinder.org/breeds/{breed["id"]}">
    
    <link rel="icon" href="../favicon.svg?v=4" type="image/svg+xml">
    
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://breedfinder.org/breeds/{breed["id"]}">
    <meta property="og:title" content="{breed["name"]}: Complete Breed Guide">
    <meta property="og:description" content="{breed["description"][:150]}...">
    <meta property="og:site_name" content="BreedFinder">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Plus Jakarta Sans', 'sans-serif'] }}
                }}
            }}
        }}
    </script>
    <style>
        .card-shadow {{
            box-shadow: 0 1px 3px rgba(0,0,0,0.05), 0 4px 12px rgba(0,0,0,0.04);
        }}
    </style>
</head>
<body class="bg-gradient-to-b from-slate-50 to-white min-h-screen text-slate-800">
    <!-- Header -->
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-200/60 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../" class="flex items-center gap-3">
                <div class="w-10 h-10 bg-gradient-to-br from-sky-500 to-violet-500 rounded-xl flex items-center justify-center text-white shadow-lg shadow-sky-500/20">
                    <img src="../favicon.svg?v=4" class="w-5 h-5" alt="BreedFinder">
                </div>
                <span class="text-xl font-bold bg-gradient-to-r from-slate-800 to-slate-600 bg-clip-text text-transparent">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="../breeds/" class="text-slate-600 hover:text-sky-600 transition">All Breeds</a>
                <a href="../quiz/" class="text-slate-600 hover:text-sky-600 transition">Breed Quiz</a>
            </nav>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-4 py-8">
        <!-- Breadcrumb -->
        <nav class="text-sm text-slate-500 mb-6 flex items-center gap-2">
            <a href="../" class="hover:text-sky-600 transition">Home</a>
            <i data-lucide="chevron-right" class="w-4 h-4 text-slate-300"></i>
            <a href="../breeds/" class="hover:text-sky-600 transition">Breeds</a>
            <i data-lucide="chevron-right" class="w-4 h-4 text-slate-300"></i>
            <span class="text-slate-700 font-medium">{breed["name"]}</span>
        </nav>

        <!-- Hero Card -->
        <div class="bg-white rounded-3xl p-8 mb-8 card-shadow border border-slate-100">
            <div class="flex flex-col md:flex-row gap-8">
                <!-- Image -->
                <div class="md:w-2/5">
                    <div class="bg-gradient-to-br from-slate-100 to-slate-50 rounded-2xl aspect-[4/5] flex items-center justify-center border border-slate-200/50">
                        <i data-lucide="dog" class="w-24 h-24 text-slate-300"></i>
                    </div>
                </div>
                
                <!-- Info -->
                <div class="md:w-3/5">
                    <div class="flex items-center gap-2 mb-3">
                        <span class="bg-sky-100 text-sky-700 text-xs font-semibold px-3 py-1 rounded-full">{breed["group"]}</span>
                        <span class="bg-violet-100 text-violet-700 text-xs font-semibold px-3 py-1 rounded-full">{breed["size_category"]}</span>
                    </div>
                    
                    <h1 class="text-4xl font-bold text-slate-900 mb-3">{breed["name"]}</h1>
                    <p class="text-lg text-slate-600 mb-6 leading-relaxed">{breed["description"]}</p>
                    
                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                                <i data-lucide="map-pin" class="w-3 h-3"></i> Origin
                            </div>
                            <div class="text-slate-800 font-semibold">{breed["origin"]}</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                                <i data-lucide="heart" class="w-3 h-3"></i> Lifespan
                            </div>
                            <div class="text-slate-800 font-semibold">{breed["lifespan"]}</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                                <i data-lucide="ruler" class="w-3 h-3"></i> Height
                            </div>
                            <div class="text-slate-800 font-semibold">{breed["height"]}</div>
                        </div>
                        <div class="bg-slate-50 rounded-xl p-4">
                            <div class="text-xs font-medium text-slate-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                                <i data-lucide="scale" class="w-3 h-3"></i> Weight
                            </div>
                            <div class="text-slate-800 font-semibold">{breed["weight"]}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Ratings Card -->
        <div class="bg-white rounded-3xl p-8 mb-8 card-shadow border border-slate-100">
            <h2 class="text-2xl font-bold text-slate-900 mb-6 flex items-center gap-3">
                <span class="w-10 h-10 bg-gradient-to-br from-amber-400 to-orange-500 rounded-xl flex items-center justify-center text-white shadow-lg shadow-amber-500/20">
                    🐾
                </span>
                Breed Ratings
            </h2>
            <div class="grid grid-cols-2 md:grid-cols-3 gap-6">
                <div class="text-center p-4 bg-slate-50 rounded-xl">
                    <div class="text-sm font-medium text-slate-600 mb-2">Energy Level</div>
                    <div class="text-xl">{generate_paw_rating(breed["energy"])}</div>
                </div>
                <div class="text-center p-4 bg-slate-50 rounded-xl">
                    <div class="text-sm font-medium text-slate-600 mb-2">Grooming</div>
                    <div class="text-xl">{generate_paw_rating(breed["grooming"])}</div>
                </div>
                <div class="text-center p-4 bg-slate-50 rounded-xl">
                    <div class="text-sm font-medium text-slate-600 mb-2">Sociability</div>
                    <div class="text-xl">{generate_paw_rating(breed["sociability"])}</div>
                </div>
                <div class="text-center p-4 bg-slate-50 rounded-xl">
                    <div class="text-sm font-medium text-slate-600 mb-2">Trainability</div>
                    <div class="text-xl">{generate_paw_rating(breed["trainability"])}</div>
                </div>
                <div class="text-center p-4 bg-slate-50 rounded-xl">
                    <div class="text-sm font-medium text-slate-600 mb-2">Kid Friendly</div>
                    <div class="text-xl">{generate_paw_rating(breed["kid_friendly"])}</div>
                </div>
                <div class="text-center p-4 bg-slate-50 rounded-xl">
                    <div class="text-sm font-medium text-slate-600 mb-2">Barking</div>
                    <div class="text-xl">{generate_paw_rating(breed["barking"])}</div>
                </div>
            </div>
        </div>

        <!-- Temperament -->
        <div class="bg-white rounded-3xl p-8 mb-8 card-shadow border border-slate-100">
            <h2 class="text-2xl font-bold text-slate-900 mb-6">Temperament</h2>
            <div class="flex flex-wrap gap-2">
                {"".join([f'<span class="bg-gradient-to-r from-sky-100 to-violet-100 text-slate-700 px-4 py-2 rounded-full text-sm font-medium">{t}</span>' for t in breed["temperament"]])}
            </div>
        </div>

        <!-- Is This Breed Right for You? -->
        <div class="bg-gradient-to-r from-sky-500 to-violet-500 rounded-3xl p-8 mb-8 text-white">
            <h2 class="text-2xl font-bold mb-6 flex items-center gap-3">
                <span class="text-3xl">🤔</span>
                Is This Breed Right for You?
            </h2>
            
            <div class="grid md:grid-cols-2 gap-6 mb-6">
                <div class="bg-white/20 backdrop-blur rounded-2xl p-6">
                    <h3 class="font-bold text-lg mb-3 flex items-center gap-2">
                        <span>✅</span> Best For
                    </h3>
                    <ul class="space-y-2">
                        {"".join([f'<li class="flex items-start gap-2"><span class="mt-1">•</span>{item}</li>' for item in breed["best_for"]])}
                    </ul>
                </div>
                <div class="bg-white/20 backdrop-blur rounded-2xl p-6">
                    <h3 class="font-bold text-lg mb-3 flex items-center gap-2">
                        <span>❌</span> Not Ideal For
                    </h3>
                    <ul class="space-y-2">
                        {"".join([f'<li class="flex items-start gap-2"><span class="mt-1">•</span>{item}</li>' for item in breed["not_for"]])}
                    </ul>
                </div>
            </div>
            
            <div class="bg-white/20 backdrop-blur rounded-2xl p-6">
                <h3 class="font-bold text-lg mb-2">The Verdict</h3>
                <p class="text-white/90">{breed["verdict"]}</p>
            </div>
        </div>

        <!-- Back to All Breeds -->
        <div class="text-center">
            <a href="../breeds/" class="inline-flex items-center gap-2 text-sky-600 font-semibold hover:text-sky-700 transition">
                <i data-lucide="arrow-left" class="w-4 h-4"></i>
                View All Breeds
            </a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-100 mt-16 py-8">
        <div class="max-w-5xl mx-auto px-4 text-center text-slate-500 text-sm">
            <p>© 2026 BreedFinder. Helping you find your perfect companion.</p>
        </div>
    </footer>

    <script>lucide.createIcons();</script>
</body>
</html>'''

def get_quiz_entry(breed):
    """Generate quiz breeds array entry"""
    tags = []
    
    # Size tags
    if breed["size_category"] in ["Toy", "Small"]:
        tags.extend(["apartment-friendly", "small"])
    elif breed["size_category"] == "Medium":
        tags.append("medium")
    elif breed["size_category"] in ["Large", "Giant"]:
        tags.extend(["large", "any-size"])
    
    # Energy tags
    if breed["energy"] >= 4:
        tags.extend(["high-energy", "athletic"])
    elif breed["energy"] == 3:
        tags.append("moderate-energy")
    else:
        tags.extend(["low-energy", "calm"])
    
    # Grooming tags
    if breed["grooming"] >= 4:
        tags.append("high-grooming")
    elif breed["grooming"] == 3:
        tags.append("moderate-grooming")
    else:
        tags.append("low-grooming")
    
    # Kid friendly
    if breed["kid_friendly"] >= 4:
        tags.extend(["family-friendly", "gentle", "patient"])
    
    # Trainability
    if breed["trainability"] >= 4:
        tags.extend(["intelligent", "trainable"])
    
    # Temperament based tags
    temperament_lower = [t.lower() for t in breed["temperament"]]
    if "protective" in temperament_lower or "loyal" in temperament_lower:
        tags.extend(["protective", "loyal", "guard"])
    if "playful" in temperament_lower:
        tags.extend(["playful", "fun"])
    if "affectionate" in temperament_lower:
        tags.extend(["affectionate", "lap-dog"])
    
    # Remove duplicates
    tags = list(dict.fromkeys(tags))
    
    return f'{{ name: "{breed["name"]}", slug: "{breed["id"]}", tags: {json.dumps(tags)} }}'

def get_compare_entry(breed):
    """Generate compare breeds array entry"""
    # Map size category to display
    size_map = {
        "Toy": "Toy",
        "Small": "Small", 
        "Medium": "Medium",
        "Large": "Large",
        "Giant": "Giant"
    }
    
    return f'{{ slug: "{breed["id"]}", name: "{breed["name"]}", size: "{size_map.get(breed["size_category"], "Medium")}", weight: "{breed["weight"]}", lifespan: "{breed["lifespan"]}", energy: {breed["energy"]}, grooming: {breed["grooming"]}, family: {breed["kid_friendly"]}, trainability: {breed["trainability"]} }}'

def main():
    breeds_dir = os.path.join(os.path.dirname(__file__), '..', 'breeds')
    
    # Generate breed pages
    print(f"Generating {len(BREEDS)} breed pages...")
    for breed in BREEDS:
        filepath = os.path.join(breeds_dir, f'{breed["id"]}.html')
        with open(filepath, 'w') as f:
            f.write(generate_breed_page(breed))
        print(f"  ✓ {breed['name']}")
    
    print("\n=== Quiz breeds entries (add to quiz/index.html) ===")
    print(",\n".join([get_quiz_entry(b) for b in BREEDS]))
    
    print("\n\n=== Compare breeds entries (add to compare/index.html) ===")
    print(",\n".join([get_compare_entry(b) for b in BREEDS]))
    
    print(f"\n✅ Generated {len(BREEDS)} breed pages!")

if __name__ == "__main__":
    main()
