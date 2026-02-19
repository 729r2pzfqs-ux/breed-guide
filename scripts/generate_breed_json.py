#!/usr/bin/env python3
"""Generate JSON files for breeds 51-110"""

import json
import os

BREEDS = {
    51: {
        "id": "american-staffordshire-terrier",
        "name": "American Staffordshire Terrier",
        "aliases": ["AmStaff", "Staffie"],
        "group": "terrier",
        "origin": "United States",
        "lifespan": "12-16 years",
        "size": {"height_cm": "43-48", "weight_kg": "25-32", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 1, "sociability": 3, "trainability": 4, "barking": 2, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Short, stiff, glossy", "coat_colors": ["any color", "solid", "parti", "patched"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["confident", "smart", "good-natured", "loyal", "courageous", "affectionate"],
        "description": {
            "overview": "The American Staffordshire Terrier is a muscular, stocky dog with a confident disposition. Despite their tough appearance, they're affectionate family companions.",
            "temperament": "AmStaffs are loyal, trustworthy, and good with children when properly trained. They're intelligent and eager to please.",
            "health": "Prone to hip dysplasia, heart disease, and skin allergies. Regular vet checkups recommended.",
            "exercise": "High energy dogs needing vigorous daily exercise. Love interactive play and mental challenges."
        },
        "verdict": {
            "best_for": ["Active families", "Experienced dog owners", "Those wanting a loyal companion", "Homes with yards"],
            "not_for": ["First-time owners", "Areas with breed restrictions", "Those away from home often", "Multi-pet households without proper introduction"],
            "summary": "Loyal, affectionate family dogs with a muscular build. AmStaffs need experienced owners, proper training, and plenty of exercise."
        }
    },
    52: {
        "id": "staffordshire-bull-terrier",
        "name": "Staffordshire Bull Terrier",
        "aliases": ["Staffie", "Staffy", "SBT"],
        "group": "terrier",
        "origin": "England",
        "lifespan": "12-14 years",
        "size": {"height_cm": "36-41", "weight_kg": "11-17", "category": "medium"},
        "ratings": {"size": 2, "energy": 4, "grooming": 1, "sociability": 4, "trainability": 4, "barking": 2, "kid_friendly": 5, "apartment_ok": 4},
        "characteristics": {"coat_type": "Smooth, short, close", "coat_colors": ["red", "fawn", "white", "black", "blue", "brindle"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["clever", "brave", "tenacious", "affectionate", "loyal", "playful"],
        "description": {
            "overview": "Known as the 'nanny dog' in England, the Staffordshire Bull Terrier is beloved for its affection toward children and family.",
            "temperament": "Staffies are incredibly people-oriented, especially with children. They're brave but not aggressive toward people.",
            "health": "Generally healthy but prone to hip dysplasia and certain eye conditions.",
            "exercise": "Energetic dogs needing regular exercise. Love interactive play and short training sessions."
        },
        "verdict": {
            "best_for": ["Families with children", "Active households", "Those wanting an affectionate companion", "Apartment dwellers with exercise commitment"],
            "not_for": ["Those wanting a guard dog", "Homes with small pets", "Sedentary lifestyles", "Areas with breed restrictions"],
            "summary": "The ultimate 'nanny dog' - incredibly affectionate with children and family. Staffies are brave, loyal, and love being part of family activities."
        }
    },
    53: {
        "id": "cane-corso",
        "name": "Cane Corso",
        "aliases": ["Italian Mastiff", "Cane Corso Italiano"],
        "group": "working",
        "origin": "Italy",
        "lifespan": "9-12 years",
        "size": {"height_cm": "60-70", "weight_kg": "40-50", "category": "giant"},
        "ratings": {"size": 5, "energy": 3, "grooming": 2, "sociability": 2, "trainability": 4, "barking": 2, "kid_friendly": 3, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short, stiff, dense", "coat_colors": ["black", "gray", "fawn", "red", "brindle"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["intelligent", "loyal", "protective", "noble", "confident", "trainable"],
        "description": {
            "overview": "The Cane Corso is a large Italian mastiff breed known for its protective instincts and impressive physique.",
            "temperament": "Corsos are intelligent and trainable but need experienced handling. Loyal and protective of family.",
            "health": "Prone to hip dysplasia, bloat, and eye problems. Regular health screening important.",
            "exercise": "Moderate exercise needs but requires mental stimulation. Daily walks and play sessions."
        },
        "verdict": {
            "best_for": ["Experienced dog owners", "Those wanting a protective companion", "Rural homes with space", "Active individuals"],
            "not_for": ["First-time owners", "Apartment dwellers", "Families with very young children", "Those unable to provide training"],
            "summary": "A noble Italian guardian breed. Cane Corsos are intelligent and loyal but need experienced owners who can provide firm, consistent training."
        }
    },
    54: {
        "id": "chow-chow",
        "name": "Chow Chow",
        "aliases": ["Chow", "Songshi Quan"],
        "group": "non-sporting",
        "origin": "China",
        "lifespan": "8-12 years",
        "size": {"height_cm": "46-56", "weight_kg": "20-32", "category": "medium"},
        "ratings": {"size": 3, "energy": 2, "grooming": 4, "sociability": 1, "trainability": 2, "barking": 2, "kid_friendly": 2, "apartment_ok": 3},
        "characteristics": {"coat_type": "Dense double coat, rough or smooth", "coat_colors": ["red", "black", "blue", "cinnamon", "cream"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["dignified", "aloof", "loyal", "independent", "quiet", "serious"],
        "description": {
            "overview": "The Chow Chow is an ancient breed from China, known for its lion-like mane and blue-black tongue.",
            "temperament": "Chows are fiercely loyal to family but aloof with strangers. They're independent and cat-like in personality.",
            "health": "Prone to hip dysplasia, eye problems, and skin issues. Heat sensitive due to thick coat.",
            "exercise": "Moderate exercise needs. Short daily walks. Avoid exercise in hot weather."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Those wanting a quiet, dignified companion", "People who respect independence", "Cool climates"],
            "not_for": ["First-time owners", "Families with young children", "Hot climates", "Those wanting an outgoing, social dog"],
            "summary": "A dignified, ancient breed with a cat-like personality. Chows are loyal to family but independent and aloof. Best for experienced owners."
        }
    },
    55: {
        "id": "dalmatian",
        "name": "Dalmatian",
        "aliases": ["Dal", "Spotted Coach Dog", "Firehouse Dog"],
        "group": "non-sporting",
        "origin": "Croatia",
        "lifespan": "11-13 years",
        "size": {"height_cm": "48-61", "weight_kg": "20-32", "category": "large"},
        "ratings": {"size": 4, "energy": 5, "grooming": 2, "sociability": 4, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Short, dense, fine", "coat_colors": ["white with black spots", "white with liver spots"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["outgoing", "playful", "dignified", "intelligent", "energetic", "sensitive"],
        "description": {
            "overview": "The Dalmatian is known worldwide for its unique spotted coat and association with firehouses.",
            "temperament": "Dalmatians are energetic, playful, and sensitive. They bond closely with family and need plenty of activity.",
            "health": "Prone to deafness (8% deaf in both ears), urinary stones, and skin allergies.",
            "exercise": "Very high energy. Need extensive daily exercise - running, hiking, or vigorous play."
        },
        "verdict": {
            "best_for": ["Very active families", "Runners and hikers", "Homes with yards", "Those with time for extensive exercise"],
            "not_for": ["Sedentary households", "Apartment dwellers", "Those away from home often", "First-time owners"],
            "summary": "Energetic, athletic dogs with iconic spotted coats. Dalmatians need very active owners who can provide extensive daily exercise."
        }
    },
    56: {
        "id": "basenji",
        "name": "Basenji",
        "aliases": ["African Barkless Dog", "Congo Dog"],
        "group": "hound",
        "origin": "Central Africa",
        "lifespan": "13-14 years",
        "size": {"height_cm": "41-43", "weight_kg": "9-11", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 1, "sociability": 2, "trainability": 2, "barking": 1, "kid_friendly": 3, "apartment_ok": 4},
        "characteristics": {"coat_type": "Short, fine", "coat_colors": ["red", "black", "tricolor", "brindle"], "shedding": "minimal", "hypoallergenic": False},
        "temperament": ["independent", "intelligent", "alert", "curious", "affectionate", "energetic"],
        "description": {
            "overview": "The Basenji is an ancient African breed known for being 'barkless' - instead they make a unique yodel-like sound.",
            "temperament": "Basenjis are independent and cat-like. They're intelligent but can be stubborn and mischievous.",
            "health": "Prone to Fanconi syndrome, hip dysplasia, and eye problems. Health testing important.",
            "exercise": "High energy dogs needing daily exercise. Love to run and explore but should be kept on leash."
        },
        "verdict": {
            "best_for": ["Experienced dog owners", "Those wanting a unique, quiet dog", "Active individuals", "Apartments (due to minimal barking)"],
            "not_for": ["First-time owners", "Those wanting an obedient dog", "Homes with small pets", "Those who want off-leash reliability"],
            "summary": "A unique, ancient breed that doesn't bark but yodels. Basenjis are intelligent and cat-like in independence. Best for experienced owners."
        }
    },
    57: {
        "id": "irish-setter",
        "name": "Irish Setter",
        "aliases": ["Red Setter", "Irish Red Setter"],
        "group": "sporting",
        "origin": "Ireland",
        "lifespan": "12-15 years",
        "size": {"height_cm": "64-69", "weight_kg": "27-32", "category": "large"},
        "ratings": {"size": 4, "energy": 5, "grooming": 4, "sociability": 5, "trainability": 4, "barking": 3, "kid_friendly": 5, "apartment_ok": 2},
        "characteristics": {"coat_type": "Long, silky, feathered", "coat_colors": ["mahogany red", "chestnut red"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["outgoing", "sweet-natured", "active", "playful", "loving", "friendly"],
        "description": {
            "overview": "The Irish Setter is a beautiful, athletic sporting dog with a stunning mahogany coat and outgoing personality.",
            "temperament": "Irish Setters are famously friendly and outgoing. They love everyone and are great with children.",
            "health": "Prone to hip dysplasia, epilepsy, and bloat. Regular vet care important.",
            "exercise": "Very high energy. Need extensive daily exercise - at least 2 hours of activity."
        },
        "verdict": {
            "best_for": ["Active families", "Homes with children", "Those wanting a social, friendly dog", "Runners and outdoor enthusiasts"],
            "not_for": ["Sedentary households", "Those wanting a guard dog", "Apartment dwellers", "Those away from home often"],
            "summary": "Gorgeous, outgoing athletes with hearts of gold. Irish Setters are fantastic family dogs but need extensive exercise and companionship."
        }
    },
    58: {
        "id": "english-setter",
        "name": "English Setter",
        "aliases": ["Laverack Setter", "Llewellin Setter"],
        "group": "sporting",
        "origin": "England",
        "lifespan": "12 years",
        "size": {"height_cm": "61-69", "weight_kg": "20-36", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 4, "sociability": 5, "trainability": 4, "barking": 3, "kid_friendly": 5, "apartment_ok": 2},
        "characteristics": {"coat_type": "Long, flat, silky with feathering", "coat_colors": ["white with blue", "lemon", "orange", "liver belton"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["gentle", "friendly", "merry", "affectionate", "willing to please", "calm"],
        "description": {
            "overview": "The English Setter is an elegant bird dog known for its gentle temperament and beautiful speckled coat.",
            "temperament": "English Setters are gentle, friendly, and wonderful with children. They're people-oriented and aim to please.",
            "health": "Prone to hip dysplasia, deafness, and thyroid issues.",
            "exercise": "High energy dogs needing regular exercise. Love running and outdoor activities."
        },
        "verdict": {
            "best_for": ["Families with children", "Active households", "Those wanting a gentle companion", "Hunters and outdoor enthusiasts"],
            "not_for": ["Apartment dwellers", "Sedentary households", "Those wanting a guard dog", "Owners gone for long periods"],
            "summary": "Gentle, elegant bird dogs with beautiful coats. English Setters are wonderful family companions who need regular exercise and human companionship."
        }
    },
    59: {
        "id": "afghan-hound",
        "name": "Afghan Hound",
        "aliases": ["Tazi", "Baluchi Hound"],
        "group": "hound",
        "origin": "Afghanistan",
        "lifespan": "12-14 years",
        "size": {"height_cm": "63-74", "weight_kg": "23-27", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 5, "sociability": 2, "trainability": 2, "barking": 2, "kid_friendly": 3, "apartment_ok": 3},
        "characteristics": {"coat_type": "Long, thick, silky", "coat_colors": ["all colors"], "shedding": "moderate", "hypoallergenic": True},
        "temperament": ["dignified", "aloof", "independent", "sweet", "clownish", "loyal"],
        "description": {
            "overview": "The Afghan Hound is an ancient, elegant sighthound known for its stunning flowing coat and aristocratic bearing.",
            "temperament": "Afghans are dignified and aloof but can be clownish at home. They're independent and sometimes stubborn.",
            "health": "Prone to hip dysplasia, cataracts, and hypothyroidism. Sensitive to anesthesia.",
            "exercise": "Need daily exercise and room to run. Love to sprint in safe, enclosed areas."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Those appreciating elegant, independent dogs", "Owners committed to grooming", "Homes with secure yards"],
            "not_for": ["First-time owners", "Those wanting an obedient dog", "Owners unwilling to groom regularly", "Off-leash situations"],
            "summary": "Elegant, aristocratic sighthounds with stunning coats. Afghans are independent and aloof but loyal to family. Require extensive grooming."
        }
    },
    60: {
        "id": "scottish-terrier",
        "name": "Scottish Terrier",
        "aliases": ["Scottie", "Aberdeen Terrier"],
        "group": "terrier",
        "origin": "Scotland",
        "lifespan": "12 years",
        "size": {"height_cm": "25-28", "weight_kg": "8-10", "category": "small"},
        "ratings": {"size": 2, "energy": 3, "grooming": 3, "sociability": 2, "trainability": 3, "barking": 3, "kid_friendly": 3, "apartment_ok": 5},
        "characteristics": {"coat_type": "Hard, wiry outer coat with soft undercoat", "coat_colors": ["black", "wheaten", "brindle"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["confident", "independent", "spirited", "dignified", "loyal", "feisty"],
        "description": {
            "overview": "The Scottish Terrier is a small but confident terrier with a distinctive silhouette and independent spirit.",
            "temperament": "Scotties are independent, dignified, and sometimes stubborn. Loyal to family but reserved with strangers.",
            "health": "Prone to von Willebrand's disease, craniomandibular osteopathy, and certain cancers.",
            "exercise": "Moderate exercise needs. Daily walks and play sessions. Love to dig."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Those wanting a dignified companion", "Owners who respect independence", "Singles or couples"],
            "not_for": ["Families with young children", "Those wanting an eager-to-please dog", "Multi-dog households", "First-time owners"],
            "summary": "Dignified, independent terriers with distinctive looks. Scotties are loyal but stubborn. Perfect for apartments and owners who appreciate their spirit."
        }
    },
    61: {
        "id": "american-bulldog",
        "name": "American Bulldog",
        "aliases": ["AmBull", "Old Country Bulldog"],
        "group": "working",
        "origin": "United States",
        "lifespan": "10-12 years",
        "size": {"height_cm": "52-70", "weight_kg": "27-54", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 1, "sociability": 3, "trainability": 4, "barking": 2, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Short, harsh", "coat_colors": ["white", "white with patches of red", "brown", "brindle", "fawn"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["loyal", "confident", "friendly", "assertive", "energetic", "protective"],
        "description": {
            "overview": "The American Bulldog is a powerful, athletic breed that descended from working bulldogs brought to America by immigrants.",
            "temperament": "American Bulldogs are loyal, confident, and protective. Good with children but need socialization.",
            "health": "Prone to hip dysplasia, elbow dysplasia, and cherry eye.",
            "exercise": "High energy. Need vigorous daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Active families", "Those wanting a protective companion", "Homes with yards"],
            "not_for": ["First-time owners", "Apartment dwellers", "Sedentary households", "Areas with breed restrictions"],
            "summary": "Powerful, loyal working dogs with a friendly disposition. American Bulldogs need experienced owners, proper training, and plenty of exercise."
        }
    },
    62: {
        "id": "belgian-tervuren",
        "name": "Belgian Tervuren",
        "aliases": ["Tervuren", "Terv"],
        "group": "herding",
        "origin": "Belgium",
        "lifespan": "12-14 years",
        "size": {"height_cm": "56-66", "weight_kg": "20-30", "category": "large"},
        "ratings": {"size": 4, "energy": 5, "grooming": 4, "sociability": 3, "trainability": 5, "barking": 3, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Long, straight, abundant", "coat_colors": ["fawn to mahogany with black overlay"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["intelligent", "alert", "protective", "confident", "hardworking", "devoted"],
        "description": {
            "overview": "The Belgian Tervuren is an elegant herding dog with a long mahogany coat and exceptional intelligence.",
            "temperament": "Tervurens are highly intelligent, protective, and devoted to family. They excel in obedience and herding.",
            "health": "Prone to hip dysplasia, epilepsy, and eye problems.",
            "exercise": "Very high energy. Need extensive daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Active households", "Those interested in dog sports", "Homes with secure yards"],
            "not_for": ["First-time owners", "Sedentary households", "Apartment dwellers", "Those away from home often"],
            "summary": "Elegant, highly intelligent herding dogs. Tervurens excel at work and sports but need experienced owners and extensive exercise."
        }
    },
    63: {
        "id": "belgian-sheepdog",
        "name": "Belgian Sheepdog",
        "aliases": ["Groenendael", "Belgian Groenendael"],
        "group": "herding",
        "origin": "Belgium",
        "lifespan": "12-14 years",
        "size": {"height_cm": "56-66", "weight_kg": "20-30", "category": "large"},
        "ratings": {"size": 4, "energy": 5, "grooming": 4, "sociability": 3, "trainability": 5, "barking": 3, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Long, straight, abundant", "coat_colors": ["solid black"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["intelligent", "devoted", "alert", "versatile", "hardworking", "protective"],
        "description": {
            "overview": "The Belgian Sheepdog (Groenendael) is an elegant, all-black herding dog known for its intelligence and versatility.",
            "temperament": "Belgian Sheepdogs are devoted, intelligent, and versatile. They bond closely with family and excel at various tasks.",
            "health": "Prone to hip dysplasia, epilepsy, and eye problems.",
            "exercise": "Very high energy. Need extensive daily exercise and mental challenges."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Active families", "Those interested in dog sports", "People wanting a devoted companion"],
            "not_for": ["First-time owners", "Sedentary households", "Apartment dwellers", "Those without time for training"],
            "summary": "Striking black herding dogs with exceptional intelligence. Belgian Sheepdogs are devoted and versatile but need experienced, active owners."
        }
    },
    64: {
        "id": "belgian-laekenois",
        "name": "Belgian Laekenois",
        "aliases": ["Laeken", "Belgian Shepherd Laekenois"],
        "group": "herding",
        "origin": "Belgium",
        "lifespan": "12-14 years",
        "size": {"height_cm": "56-66", "weight_kg": "20-30", "category": "large"},
        "ratings": {"size": 4, "energy": 5, "grooming": 3, "sociability": 3, "trainability": 5, "barking": 3, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Rough, wiry, tousled", "coat_colors": ["fawn to mahogany with black shading"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["intelligent", "alert", "protective", "devoted", "hardworking", "watchful"],
        "description": {
            "overview": "The Belgian Laekenois is the rarest of the four Belgian Shepherd varieties, with a distinctive rough, wiry coat.",
            "temperament": "Laekenois are intelligent, protective, and devoted. They're slightly more reserved than other Belgian varieties.",
            "health": "Prone to hip dysplasia, epilepsy, and eye problems.",
            "exercise": "Very high energy. Need extensive daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Active households", "Those wanting a unique breed", "People interested in dog sports"],
            "not_for": ["First-time owners", "Sedentary households", "Apartment dwellers", "Those wanting an outgoing dog"],
            "summary": "The rarest Belgian Shepherd with a unique wiry coat. Laekenois are intelligent and devoted but need experienced, active owners."
        }
    },
    65: {
        "id": "bloodhound",
        "name": "Bloodhound",
        "aliases": ["St. Hubert Hound", "Chien de Saint-Hubert"],
        "group": "hound",
        "origin": "Belgium/France",
        "lifespan": "10-12 years",
        "size": {"height_cm": "58-69", "weight_kg": "36-50", "category": "large"},
        "ratings": {"size": 5, "energy": 3, "grooming": 2, "sociability": 4, "trainability": 3, "barking": 4, "kid_friendly": 4, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short, dense", "coat_colors": ["black and tan", "liver and tan", "red"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["gentle", "patient", "noble", "affectionate", "stubborn", "inquisitive"],
        "description": {
            "overview": "The Bloodhound has the most powerful nose of any dog breed, able to follow trails over 300 hours old.",
            "temperament": "Bloodhounds are gentle, patient, and affectionate but can be stubborn when on a scent.",
            "health": "Prone to bloat, hip dysplasia, and ear infections. Drool significantly.",
            "exercise": "Moderate exercise needs but need secure areas - will follow scents."
        },
        "verdict": {
            "best_for": ["Families wanting a gentle giant", "Those with secure, fenced yards", "Patient owners", "Search and rescue enthusiasts"],
            "not_for": ["Apartment dwellers", "Neat freaks (they drool)", "Those wanting off-leash reliability", "Owners wanting an obedient dog"],
            "summary": "Gentle giants with legendary noses. Bloodhounds are patient and affectionate but stubborn when tracking. Need secure yards and patient owners."
        }
    },
    66: {
        "id": "whippet",
        "name": "Whippet",
        "aliases": ["English Whippet", "Snap Dog"],
        "group": "hound",
        "origin": "England",
        "lifespan": "12-15 years",
        "size": {"height_cm": "44-51", "weight_kg": "11-21", "category": "medium"},
        "ratings": {"size": 3, "energy": 3, "grooming": 1, "sociability": 4, "trainability": 4, "barking": 1, "kid_friendly": 4, "apartment_ok": 5},
        "characteristics": {"coat_type": "Short, smooth, fine", "coat_colors": ["any color"], "shedding": "minimal", "hypoallergenic": False},
        "temperament": ["affectionate", "playful", "calm", "gentle", "athletic", "quiet"],
        "description": {
            "overview": "The Whippet is a medium-sized sighthound that combines elegance with athleticism and a sweet temperament.",
            "temperament": "Whippets are gentle, affectionate couch potatoes indoors but lightning-fast athletes outside.",
            "health": "Generally healthy. May be prone to eye problems and heart conditions.",
            "exercise": "Need daily exercise but are calm indoors. Love to run in secure areas."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Those wanting a quiet dog", "Families with older children", "Owners who can provide running time"],
            "not_for": ["Homes with small pets", "Cold climates without coat", "Those wanting off-leash reliability", "Very young children"],
            "summary": "Elegant, gentle sighthounds perfect for apartments. Whippets are calm indoors but need secure areas to run. Quiet and affectionate."
        }
    },
    67: {
        "id": "italian-greyhound",
        "name": "Italian Greyhound",
        "aliases": ["Iggy", "IG", "Piccolo Levriero Italiano"],
        "group": "toy",
        "origin": "Italy",
        "lifespan": "14-15 years",
        "size": {"height_cm": "33-38", "weight_kg": "3-5", "category": "tiny"},
        "ratings": {"size": 1, "energy": 3, "grooming": 1, "sociability": 3, "trainability": 3, "barking": 2, "kid_friendly": 2, "apartment_ok": 5},
        "characteristics": {"coat_type": "Short, glossy, soft", "coat_colors": ["any color except brindle or tan markings"], "shedding": "minimal", "hypoallergenic": False},
        "temperament": ["affectionate", "playful", "alert", "sensitive", "athletic", "mischievous"],
        "description": {
            "overview": "The Italian Greyhound is a miniature sighthound that combines elegance with a playful, affectionate personality.",
            "temperament": "IGs are affectionate and playful but sensitive. They bond closely with owners and can be mischievous.",
            "health": "Prone to dental issues, leg fractures, and eye problems. Fragile bones.",
            "exercise": "Moderate exercise needs. Short bursts of speed but also love lounging."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Those wanting an elegant companion", "Singles or couples", "Owners who can provide warmth (coats/blankets)"],
            "not_for": ["Families with young children", "Cold climates without protection", "Rough households", "Those wanting a sturdy dog"],
            "summary": "Elegant miniature sighthounds with big personalities. IGs are affectionate but fragile. Perfect for gentle owners in apartments."
        }
    },
    68: {
        "id": "greyhound",
        "name": "Greyhound",
        "aliases": ["English Greyhound"],
        "group": "hound",
        "origin": "England/Egypt",
        "lifespan": "10-13 years",
        "size": {"height_cm": "68-76", "weight_kg": "27-40", "category": "large"},
        "ratings": {"size": 4, "energy": 2, "grooming": 1, "sociability": 3, "trainability": 3, "barking": 1, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Short, smooth", "coat_colors": ["any color"], "shedding": "minimal", "hypoallergenic": False},
        "temperament": ["gentle", "independent", "noble", "affectionate", "calm", "quiet"],
        "description": {
            "overview": "The Greyhound is the fastest dog breed, capable of reaching 45 mph, yet surprisingly calm and gentle at home.",
            "temperament": "Greyhounds are gentle, quiet couch potatoes. Despite their racing heritage, they're calm indoors.",
            "health": "Prone to bloat, dental issues, and sensitivity to anesthesia.",
            "exercise": "Surprisingly low exercise needs. Short daily walks and occasional sprints."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Those wanting a quiet dog", "Families", "Those interested in adopting retired racers"],
            "not_for": ["Homes with small pets", "Those wanting off-leash reliability", "Very cold climates", "Those wanting an active outdoor companion"],
            "summary": "The world's fastest couch potato. Greyhounds are gentle, quiet, and surprisingly apartment-friendly. Many retired racers need homes."
        }
    },
    69: {
        "id": "saluki",
        "name": "Saluki",
        "aliases": ["Persian Greyhound", "Royal Dog of Egypt"],
        "group": "hound",
        "origin": "Middle East",
        "lifespan": "10-17 years",
        "size": {"height_cm": "58-71", "weight_kg": "18-27", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 2, "sociability": 2, "trainability": 2, "barking": 1, "kid_friendly": 3, "apartment_ok": 3},
        "characteristics": {"coat_type": "Smooth or feathered, silky", "coat_colors": ["white", "cream", "fawn", "red", "grizzle", "black and tan", "tricolor"], "shedding": "minimal", "hypoallergenic": False},
        "temperament": ["gentle", "dignified", "independent", "aloof", "devoted", "quiet"],
        "description": {
            "overview": "The Saluki is one of the oldest dog breeds, treasured by pharaohs and nomadic tribes for thousands of years.",
            "temperament": "Salukis are gentle and devoted to family but aloof with strangers. Independent and cat-like.",
            "health": "Generally healthy but prone to heart conditions and certain cancers.",
            "exercise": "Need daily exercise and secure areas to run. Strong prey drive."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Those appreciating elegant, independent dogs", "Runners (with leash)", "Quiet households"],
            "not_for": ["First-time owners", "Homes with small pets", "Those wanting an obedient dog", "Off-leash environments"],
            "summary": "Ancient, elegant sighthounds with independent spirits. Salukis are gentle and devoted but aloof. Need experienced owners and secure running areas."
        }
    },
    70: {
        "id": "pharaoh-hound",
        "name": "Pharaoh Hound",
        "aliases": ["Kelb tal-Fenek", "Rabbit Dog"],
        "group": "hound",
        "origin": "Malta",
        "lifespan": "12-14 years",
        "size": {"height_cm": "53-63", "weight_kg": "20-25", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 1, "sociability": 4, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Short, glossy", "coat_colors": ["tan", "rich tan", "chestnut"], "shedding": "minimal", "hypoallergenic": False},
        "temperament": ["affectionate", "playful", "intelligent", "noble", "friendly", "active"],
        "description": {
            "overview": "The Pharaoh Hound is Malta's national dog, known for 'blushing' (nose and ears turn deep rose when excited).",
            "temperament": "Pharaoh Hounds are friendly, affectionate, and playful. They're good with children and other dogs.",
            "health": "Generally healthy. May be prone to sensitivity to anesthesia.",
            "exercise": "High energy. Need daily exercise and secure areas to run."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a unique, friendly dog", "Homes with older children", "Owners who can provide exercise"],
            "not_for": ["Homes with small pets", "Cold climates", "Those wanting off-leash reliability", "Sedentary households"],
            "summary": "Elegant, friendly sighthounds that actually blush! Pharaoh Hounds are playful and affectionate. Need active owners and secure running space."
        }
    },
    71: {
        "id": "keeshond",
        "name": "Keeshond",
        "aliases": ["Dutch Barge Dog", "Smiling Dutchman", "Wolfspitz"],
        "group": "non-sporting",
        "origin": "Netherlands",
        "lifespan": "12-15 years",
        "size": {"height_cm": "43-46", "weight_kg": "16-20", "category": "medium"},
        "ratings": {"size": 3, "energy": 3, "grooming": 4, "sociability": 5, "trainability": 4, "barking": 4, "kid_friendly": 5, "apartment_ok": 4},
        "characteristics": {"coat_type": "Long, straight, harsh outer coat with thick undercoat", "coat_colors": ["mixture of gray, black, and cream"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["friendly", "lively", "outgoing", "intelligent", "alert", "affectionate"],
        "description": {
            "overview": "The Keeshond is known as the 'smiling Dutchman' for its distinctive facial markings and friendly expression.",
            "temperament": "Keeshonden are outgoing, friendly, and excellent with everyone. They're nicknamed 'velcro dogs' for their devotion.",
            "health": "Prone to hip dysplasia, heart problems, and thyroid issues.",
            "exercise": "Moderate exercise needs. Daily walks and play sessions."
        },
        "verdict": {
            "best_for": ["Families with children", "Those wanting a friendly companion", "Apartment dwellers (with exercise)", "First-time owners"],
            "not_for": ["Those wanting a guard dog", "Owners disliking barking", "Those unwilling to groom", "Hot climates"],
            "summary": "The smiling, friendly spitz that loves everyone. Keeshonden are excellent family dogs but need regular grooming and can be vocal."
        }
    },
    72: {
        "id": "finnish-lapphund",
        "name": "Finnish Lapphund",
        "aliases": ["Lapinkoira", "Lappie"],
        "group": "herding",
        "origin": "Finland",
        "lifespan": "12-15 years",
        "size": {"height_cm": "41-52", "weight_kg": "15-24", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 4, "sociability": 4, "trainability": 4, "barking": 4, "kid_friendly": 5, "apartment_ok": 3},
        "characteristics": {"coat_type": "Long, straight, dense double coat", "coat_colors": ["all colors allowed"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["friendly", "calm", "faithful", "courageous", "keen", "gentle"],
        "description": {
            "overview": "The Finnish Lapphund was bred by the Sami people to herd reindeer in the harsh Arctic climate.",
            "temperament": "Lappies are friendly, calm, and excellent with children. They're eager to please and adaptable.",
            "health": "Generally healthy. May be prone to hip dysplasia and eye problems.",
            "exercise": "Moderate to high exercise needs. Love outdoor activities, especially in cold weather."
        },
        "verdict": {
            "best_for": ["Families with children", "Active households", "Cold climates", "Those wanting a friendly, trainable dog"],
            "not_for": ["Hot climates", "Those unwilling to groom", "Owners bothered by barking", "Sedentary households"],
            "summary": "Friendly Arctic herders perfect for families. Finnish Lapphunds are gentle, trainable, and great with kids. Need grooming and tolerate cold well."
        }
    },
    73: {
        "id": "norwegian-elkhound",
        "name": "Norwegian Elkhound",
        "aliases": ["Norsk Elghund", "Elkhound"],
        "group": "hound",
        "origin": "Norway",
        "lifespan": "12-15 years",
        "size": {"height_cm": "49-52", "weight_kg": "20-23", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 3, "sociability": 4, "trainability": 3, "barking": 4, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Thick, hard outer coat with soft undercoat", "coat_colors": ["gray with black tips"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["bold", "playful", "loyal", "alert", "independent", "friendly"],
        "description": {
            "overview": "The Norwegian Elkhound is an ancient spitz breed that hunted moose and bears alongside Vikings.",
            "temperament": "Elkhounds are bold, loyal, and playful. They're good watchdogs and family companions.",
            "health": "Prone to hip dysplasia, kidney problems, and eye issues.",
            "exercise": "High energy. Need vigorous daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a loyal companion", "Cold climates", "Homes with secure yards"],
            "not_for": ["Apartment dwellers", "Hot climates", "Those bothered by barking", "Sedentary households"],
            "summary": "Bold Viking hunting dogs with loyal hearts. Norwegian Elkhounds are great family dogs but need exercise and can be vocal."
        }
    },
    74: {
        "id": "alaskan-klee-kai",
        "name": "Alaskan Klee Kai",
        "aliases": ["Klee Kai", "Mini Husky"],
        "group": "non-sporting",
        "origin": "United States",
        "lifespan": "12-16 years",
        "size": {"height_cm": "33-43", "weight_kg": "4-10", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 3, "sociability": 2, "trainability": 4, "barking": 3, "kid_friendly": 3, "apartment_ok": 4},
        "characteristics": {"coat_type": "Double coat, medium length", "coat_colors": ["black and white", "gray and white", "red and white"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["intelligent", "curious", "alert", "loyal", "reserved", "energetic"],
        "description": {
            "overview": "The Alaskan Klee Kai looks like a miniature Husky but is a distinct breed developed in Alaska in the 1970s.",
            "temperament": "Klee Kai are intelligent and loyal to family but reserved with strangers. They can be vocal.",
            "health": "Generally healthy. May be prone to heart problems and thyroid issues.",
            "exercise": "Moderate to high energy. Need daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Those wanting a small, Husky-like dog", "Active individuals", "Homes without small children"],
            "not_for": ["First-time owners", "Those wanting a social dog", "Families with very young children", "Those bothered by shedding"],
            "summary": "Mini Husky look-alikes with big personalities. Klee Kai are loyal and intelligent but reserved with strangers. Need experienced owners."
        }
    },
    75: {
        "id": "chinese-crested",
        "name": "Chinese Crested",
        "aliases": ["Crested", "Puff"],
        "group": "toy",
        "origin": "China/Africa",
        "lifespan": "13-18 years",
        "size": {"height_cm": "28-33", "weight_kg": "2-5", "category": "tiny"},
        "ratings": {"size": 1, "energy": 2, "grooming": 3, "sociability": 4, "trainability": 4, "barking": 2, "kid_friendly": 3, "apartment_ok": 5},
        "characteristics": {"coat_type": "Hairless variety or Powderpuff with soft double coat", "coat_colors": ["any color or combination"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["affectionate", "playful", "alert", "lively", "devoted", "happy"],
        "description": {
            "overview": "Chinese Crested come in two varieties: Hairless (with hair on head, feet, and tail) and Powderpuff (fully coated).",
            "temperament": "Chinese Crested are affectionate, playful, and devoted. They love being with their people.",
            "health": "Hairless variety prone to skin issues and dental problems. Need sun protection.",
            "exercise": "Low to moderate exercise needs. Short walks and indoor play."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Allergy sufferers (hairless)", "Those wanting a devoted lap dog", "Owners who enjoy grooming/skincare"],
            "not_for": ["Outdoor-focused owners", "Very cold climates (without protection)", "Rough households", "Those wanting a sturdy dog"],
            "summary": "Unique, devoted companions in hairless or fluffy varieties. Chinese Crested are affectionate and apartment-perfect but need skin/dental care."
        }
    },
    76: {
        "id": "lhasa-apso",
        "name": "Lhasa Apso",
        "aliases": ["Lhasa", "Bark Lion Sentinel Dog"],
        "group": "non-sporting",
        "origin": "Tibet",
        "lifespan": "12-15 years",
        "size": {"height_cm": "25-28", "weight_kg": "5-8", "category": "small"},
        "ratings": {"size": 2, "energy": 3, "grooming": 5, "sociability": 2, "trainability": 3, "barking": 4, "kid_friendly": 2, "apartment_ok": 5},
        "characteristics": {"coat_type": "Long, heavy, straight", "coat_colors": ["all colors"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["confident", "smart", "comical", "aloof", "loyal", "stubborn"],
        "description": {
            "overview": "The Lhasa Apso served as sentinels in Tibetan monasteries and palaces for over a thousand years.",
            "temperament": "Lhasas are confident, sometimes stubborn, and loyal to family. Reserved with strangers.",
            "health": "Prone to eye problems, kidney issues, and hip dysplasia.",
            "exercise": "Moderate exercise needs. Daily walks and play sessions."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Those wanting a loyal watchdog", "Owners committed to grooming", "Adults and older children"],
            "not_for": ["Families with young children", "Those wanting an eager-to-please dog", "Owners unwilling to groom", "First-time owners"],
            "summary": "Confident Tibetan sentinels in a small package. Lhasas are loyal and make good watchdogs but need extensive grooming and patient training."
        }
    },
    77: {
        "id": "tibetan-terrier",
        "name": "Tibetan Terrier",
        "aliases": ["TT", "Tsang Apso", "Holy Dog of Tibet"],
        "group": "non-sporting",
        "origin": "Tibet",
        "lifespan": "15-16 years",
        "size": {"height_cm": "36-43", "weight_kg": "8-14", "category": "medium"},
        "ratings": {"size": 3, "energy": 3, "grooming": 5, "sociability": 4, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Long, fine, double coat", "coat_colors": ["all colors except chocolate or liver"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["affectionate", "sensitive", "clever", "loyal", "gentle", "playful"],
        "description": {
            "overview": "Despite its name, the Tibetan Terrier is not a terrier but a herding breed kept as good luck charms in Tibet.",
            "temperament": "TTs are affectionate, clever, and adaptable. They bond closely with family.",
            "health": "Prone to hip dysplasia, eye problems, and some neurological conditions.",
            "exercise": "Moderate exercise needs. Enjoy walks and playtime."
        },
        "verdict": {
            "best_for": ["Families", "Apartment dwellers (with exercise)", "Those wanting a devoted companion", "Allergy sufferers"],
            "not_for": ["Those unwilling to groom regularly", "Owners wanting a low-maintenance dog", "Very active households", "Those wanting an independent dog"],
            "summary": "Gentle, devoted 'good luck' dogs from Tibet. Tibetan Terriers are affectionate family companions but require extensive grooming."
        }
    },
    78: {
        "id": "tibetan-mastiff",
        "name": "Tibetan Mastiff",
        "aliases": ["TM", "Do-Khyi"],
        "group": "working",
        "origin": "Tibet",
        "lifespan": "10-12 years",
        "size": {"height_cm": "61-76", "weight_kg": "34-73", "category": "giant"},
        "ratings": {"size": 5, "energy": 2, "grooming": 4, "sociability": 1, "trainability": 2, "barking": 4, "kid_friendly": 3, "apartment_ok": 1},
        "characteristics": {"coat_type": "Long, thick double coat", "coat_colors": ["black", "brown", "blue/gray", "gold"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["independent", "reserved", "protective", "intelligent", "stubborn", "loyal"],
        "description": {
            "overview": "The Tibetan Mastiff is an ancient guardian breed that protected Himalayan monasteries and nomadic camps.",
            "temperament": "TMs are independent, protective, and reserved with strangers. Loyal but can be stubborn.",
            "health": "Prone to hip dysplasia, thyroid issues, and eye problems.",
            "exercise": "Moderate exercise needs. More active at night due to guardian instincts."
        },
        "verdict": {
            "best_for": ["Experienced large breed owners", "Rural properties", "Those wanting a guardian", "Cold climates"],
            "not_for": ["First-time owners", "Apartment dwellers", "Hot climates", "Those wanting an obedient, social dog"],
            "summary": "Majestic Himalayan guardians with independent spirits. Tibetan Mastiffs need experienced owners, space, and respect for their protective nature."
        }
    },
    79: {
        "id": "leonberger",
        "name": "Leonberger",
        "aliases": ["Leo", "Gentle Giant"],
        "group": "working",
        "origin": "Germany",
        "lifespan": "9 years",
        "size": {"height_cm": "65-80", "weight_kg": "41-77", "category": "giant"},
        "ratings": {"size": 5, "energy": 3, "grooming": 4, "sociability": 5, "trainability": 4, "barking": 2, "kid_friendly": 5, "apartment_ok": 1},
        "characteristics": {"coat_type": "Medium to long, water-resistant double coat", "coat_colors": ["lion-yellow", "golden", "red-brown", "sand"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["friendly", "playful", "gentle", "loyal", "patient", "confident"],
        "description": {
            "overview": "The Leonberger was bred to resemble a lion and serve as a versatile working dog and family companion.",
            "temperament": "Leos are gentle giants - friendly, patient, and wonderful with children. They love water.",
            "health": "Prone to hip dysplasia, bloat, and some heart conditions. Shorter lifespan.",
            "exercise": "Moderate exercise needs. Love swimming and family activities."
        },
        "verdict": {
            "best_for": ["Families with children", "Those with space for a giant breed", "Water enthusiasts", "Those wanting a gentle giant"],
            "not_for": ["Apartment dwellers", "Those wanting a long-lived dog", "Neat freaks (drool and shedding)", "Hot climates"],
            "summary": "Majestic, lion-like gentle giants. Leonbergers are patient, friendly family dogs but need space and have shorter lifespans."
        }
    },
    80: {
        "id": "anatolian-shepherd",
        "name": "Anatolian Shepherd",
        "aliases": ["Kangal Dog", "Karabash", "Anatolian Karabash"],
        "group": "working",
        "origin": "Turkey",
        "lifespan": "11-13 years",
        "size": {"height_cm": "71-81", "weight_kg": "41-68", "category": "giant"},
        "ratings": {"size": 5, "energy": 3, "grooming": 2, "sociability": 2, "trainability": 3, "barking": 3, "kid_friendly": 3, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short to medium, dense", "coat_colors": ["fawn with black mask", "brindle", "white", "pinto"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["independent", "protective", "loyal", "intelligent", "patient", "territorial"],
        "description": {
            "overview": "The Anatolian Shepherd is an ancient Turkish breed used to protect livestock from predators like wolves and bears.",
            "temperament": "Anatolians are independent, protective guardians. Loyal to family but territorial with strangers.",
            "health": "Generally healthy. May be prone to hip dysplasia and entropion.",
            "exercise": "Moderate exercise needs. Need space to patrol and protect."
        },
        "verdict": {
            "best_for": ["Rural properties", "Livestock owners", "Experienced large breed owners", "Those wanting a working guardian"],
            "not_for": ["Apartment dwellers", "First-time owners", "Urban environments", "Those wanting a social dog"],
            "summary": "Powerful Turkish guardians bred to protect livestock. Anatolians are independent and territorial - best for rural properties with experienced owners."
        }
    },
    81: {
        "id": "kuvasz",
        "name": "Kuvasz",
        "aliases": ["Hungarian Kuvasz"],
        "group": "working",
        "origin": "Hungary",
        "lifespan": "10-12 years",
        "size": {"height_cm": "66-76", "weight_kg": "32-52", "category": "giant"},
        "ratings": {"size": 5, "energy": 3, "grooming": 3, "sociability": 2, "trainability": 3, "barking": 3, "kid_friendly": 3, "apartment_ok": 1},
        "characteristics": {"coat_type": "Medium length, wavy to straight double coat", "coat_colors": ["white"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["loyal", "protective", "patient", "independent", "intelligent", "courageous"],
        "description": {
            "overview": "The Kuvasz is an ancient Hungarian flock guardian known for its striking white coat and fierce loyalty.",
            "temperament": "Kuvasz are loyal and protective but independent. They're patient with family but wary of strangers.",
            "health": "Prone to hip dysplasia, osteochondritis, and thyroid issues.",
            "exercise": "Moderate exercise needs. Need space and a job to do."
        },
        "verdict": {
            "best_for": ["Experienced large breed owners", "Rural properties", "Those wanting a guardian", "Active families with older children"],
            "not_for": ["First-time owners", "Apartment dwellers", "Urban environments", "Those wanting an easy-to-train dog"],
            "summary": "Majestic white Hungarian guardians. Kuvasz are fiercely loyal and protective but need experienced owners who understand livestock guardians."
        }
    },
    82: {
        "id": "komondor",
        "name": "Komondor",
        "aliases": ["Hungarian Komondor", "Mop Dog"],
        "group": "working",
        "origin": "Hungary",
        "lifespan": "10-12 years",
        "size": {"height_cm": "64-76", "weight_kg": "36-61", "category": "giant"},
        "ratings": {"size": 5, "energy": 2, "grooming": 5, "sociability": 2, "trainability": 3, "barking": 3, "kid_friendly": 3, "apartment_ok": 1},
        "characteristics": {"coat_type": "Long, corded (natural cords)", "coat_colors": ["white"], "shedding": "minimal", "hypoallergenic": False},
        "temperament": ["loyal", "dignified", "protective", "independent", "calm", "fearless"],
        "description": {
            "overview": "The Komondor's distinctive corded coat helped it blend in with sheep and protected it from predators and weather.",
            "temperament": "Komondorok are calm, dignified guardians. Protective and loyal but independent.",
            "health": "Prone to hip dysplasia and bloat. Coat requires special care.",
            "exercise": "Moderate exercise needs. Need space to guard and patrol."
        },
        "verdict": {
            "best_for": ["Experienced large breed owners", "Rural properties", "Those dedicated to coat care", "Livestock owners"],
            "not_for": ["First-time owners", "Apartment dwellers", "Those unwilling to maintain cords", "Urban environments"],
            "summary": "The iconic corded Hungarian guardian. Komondorok are loyal protectors but their unique coat requires dedicated care."
        }
    },
    83: {
        "id": "puli",
        "name": "Puli",
        "aliases": ["Hungarian Puli", "Pulik (plural)"],
        "group": "herding",
        "origin": "Hungary",
        "lifespan": "10-15 years",
        "size": {"height_cm": "36-45", "weight_kg": "10-15", "category": "medium"},
        "ratings": {"size": 2, "energy": 4, "grooming": 5, "sociability": 3, "trainability": 4, "barking": 4, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Long, corded", "coat_colors": ["black", "white", "gray", "cream"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["intelligent", "agile", "loyal", "energetic", "alert", "playful"],
        "description": {
            "overview": "The Puli is a small Hungarian herding dog with a distinctive corded coat, often described as a 'mop on springs.'",
            "temperament": "Pulik are intelligent, energetic, and playful. They're quick learners but can be independent.",
            "health": "Generally healthy. May be prone to hip dysplasia and eye problems.",
            "exercise": "High energy. Need daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Active families", "Those interested in dog sports", "Owners dedicated to coat care", "Allergy sufferers"],
            "not_for": ["Those wanting low-maintenance grooming", "Sedentary households", "Owners bothered by barking", "First-time owners"],
            "summary": "Energetic Hungarian herders with iconic corded coats. Pulik are intelligent and playful but require dedicated coat maintenance."
        }
    },
    84: {
        "id": "pumi",
        "name": "Pumi",
        "aliases": ["Hungarian Pumi"],
        "group": "herding",
        "origin": "Hungary",
        "lifespan": "12-13 years",
        "size": {"height_cm": "38-47", "weight_kg": "8-15", "category": "medium"},
        "ratings": {"size": 2, "energy": 5, "grooming": 3, "sociability": 3, "trainability": 5, "barking": 4, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Medium length, curly, wavy", "coat_colors": ["black", "white", "gray", "fawn"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["intelligent", "active", "lively", "alert", "vocal", "ready to work"],
        "description": {
            "overview": "The Pumi is an energetic Hungarian herding breed known for its corkscrew curls and terrier-like ears.",
            "temperament": "Pumik are highly intelligent, energetic, and vocal. They excel at herding and dog sports.",
            "health": "Generally healthy. May be prone to hip dysplasia and patellar luxation.",
            "exercise": "Very high energy. Need extensive daily exercise and mental challenges."
        },
        "verdict": {
            "best_for": ["Active owners", "Those interested in dog sports", "Experienced dog owners", "Rural or suburban homes"],
            "not_for": ["Sedentary households", "Those bothered by barking", "Apartment dwellers without exercise plan", "First-time owners"],
            "summary": "Energetic Hungarian herders with distinctive curly coats. Pumik are intelligent and excel at sports but need lots of exercise and bark readily."
        }
    },
    85: {
        "id": "beauceron",
        "name": "Beauceron",
        "aliases": ["Berger de Beauce", "French Shorthaired Shepherd", "Bas Rouge"],
        "group": "herding",
        "origin": "France",
        "lifespan": "10-12 years",
        "size": {"height_cm": "61-70", "weight_kg": "30-45", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 2, "sociability": 3, "trainability": 4, "barking": 3, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Short, dense double coat", "coat_colors": ["black and tan", "harlequin"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["intelligent", "loyal", "protective", "versatile", "confident", "gentle"],
        "description": {
            "overview": "The Beauceron is France's largest sheepdog, known for double dewclaws and versatile working ability.",
            "temperament": "Beaucerons are intelligent, loyal, and protective. They're versatile workers and devoted family dogs.",
            "health": "Prone to hip dysplasia and bloat.",
            "exercise": "High energy. Need vigorous daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Active families", "Those interested in working dogs", "Rural or suburban homes with yards"],
            "not_for": ["First-time owners", "Apartment dwellers", "Sedentary households", "Those wanting a low-energy dog"],
            "summary": "France's versatile, powerful sheepdogs. Beaucerons are intelligent and loyal but need experienced owners and plenty of activity."
        }
    },
    86: {
        "id": "briard",
        "name": "Briard",
        "aliases": ["Berger de Brie", "Chien Berger de Brie"],
        "group": "herding",
        "origin": "France",
        "lifespan": "12 years",
        "size": {"height_cm": "56-68", "weight_kg": "25-45", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 5, "sociability": 3, "trainability": 4, "barking": 3, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Long, wavy, dry", "coat_colors": ["black", "gray", "tawny"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["loyal", "protective", "intelligent", "obedient", "fearless", "gentle"],
        "description": {
            "overview": "The Briard is a French herding breed known for its long, flowing coat and devotion to family.",
            "temperament": "Briards are loyal protectors with gentle hearts. They're intelligent and devoted to their families.",
            "health": "Prone to hip dysplasia, bloat, and eye problems.",
            "exercise": "High energy. Need daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a protective companion", "Owners committed to grooming", "Homes with yards"],
            "not_for": ["Those unwilling to groom extensively", "Apartment dwellers", "Sedentary households", "First-time owners"],
            "summary": "Loyal French sheepdogs with flowing coats and protective hearts. Briards are devoted family dogs but need extensive grooming and exercise."
        }
    },
    87: {
        "id": "airedale-terrier",
        "name": "Airedale Terrier",
        "aliases": ["King of Terriers", "Bingley Terrier", "Waterside Terrier"],
        "group": "terrier",
        "origin": "England",
        "lifespan": "11-14 years",
        "size": {"height_cm": "56-61", "weight_kg": "20-30", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 3, "sociability": 3, "trainability": 4, "barking": 3, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Dense, wiry", "coat_colors": ["tan with black saddle"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["confident", "courageous", "friendly", "intelligent", "outgoing", "versatile"],
        "description": {
            "overview": "The Airedale is the largest terrier breed, earning the nickname 'King of Terriers' for its size and versatility.",
            "temperament": "Airedales are confident, intelligent, and versatile. They're good with children and make excellent family dogs.",
            "health": "Prone to hip dysplasia and skin allergies.",
            "exercise": "High energy. Need daily vigorous exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a versatile dog", "Homes with yards", "Experienced dog owners"],
            "not_for": ["Apartment dwellers", "Sedentary households", "Multi-dog homes (may be dog-aggressive)", "First-time owners"],
            "summary": "The King of Terriers - versatile, intelligent, and confident. Airedales are great family dogs but need exercise and experienced handling."
        }
    },
    88: {
        "id": "soft-coated-wheaten-terrier",
        "name": "Soft Coated Wheaten Terrier",
        "aliases": ["Wheaten", "Irish Soft-Coated Wheaten Terrier"],
        "group": "terrier",
        "origin": "Ireland",
        "lifespan": "12-14 years",
        "size": {"height_cm": "43-48", "weight_kg": "14-20", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 4, "sociability": 5, "trainability": 3, "barking": 3, "kid_friendly": 5, "apartment_ok": 4},
        "characteristics": {"coat_type": "Soft, silky, wavy", "coat_colors": ["wheaten (pale beige to shimmering gold)"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["happy", "friendly", "deeply devoted", "spirited", "playful", "affectionate"],
        "description": {
            "overview": "The Wheaten is an Irish farm dog known for its soft, silky coat and exuberant 'Wheaten greeting' (jumping).",
            "temperament": "Wheatens are friendly, happy dogs that love everyone. They're enthusiastic greeters and devoted companions.",
            "health": "Prone to protein-losing diseases, hip dysplasia, and allergies.",
            "exercise": "Moderate to high energy. Need daily exercise and play."
        },
        "verdict": {
            "best_for": ["Families with children", "Those wanting a friendly companion", "Allergy sufferers", "Active households"],
            "not_for": ["Those bothered by jumping", "Owners wanting a calm dog", "Those unwilling to groom", "Very young children (due to exuberance)"],
            "summary": "Happy, friendly Irish terriers with signature soft coats. Wheatens love everyone and make great family dogs but can be exuberant greeters."
        }
    },
    89: {
        "id": "jack-russell-terrier",
        "name": "Jack Russell Terrier",
        "aliases": ["JRT", "Jack Russell"],
        "group": "terrier",
        "origin": "England",
        "lifespan": "12-14 years",
        "size": {"height_cm": "25-30", "weight_kg": "6-8", "category": "small"},
        "ratings": {"size": 2, "energy": 5, "grooming": 1, "sociability": 3, "trainability": 3, "barking": 4, "kid_friendly": 3, "apartment_ok": 3},
        "characteristics": {"coat_type": "Smooth, rough, or broken", "coat_colors": ["white with black", "tan", "or both"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["energetic", "clever", "athletic", "fearless", "vocal", "stubborn"],
        "description": {
            "overview": "The Jack Russell Terrier is a small but mighty hunting terrier with boundless energy and fearless spirit.",
            "temperament": "JRTs are incredibly energetic, clever, and fearless. They're athletic and need lots of mental and physical stimulation.",
            "health": "Generally healthy. May be prone to patellar luxation and eye problems.",
            "exercise": "Extremely high energy. Need extensive daily exercise and mental challenges."
        },
        "verdict": {
            "best_for": ["Very active owners", "Those wanting a spirited companion", "Experienced terrier owners", "Homes without small pets"],
            "not_for": ["Sedentary households", "First-time owners", "Homes with small pets", "Those wanting a calm lap dog"],
            "summary": "Small dogs with huge personalities and endless energy. JRTs are clever and athletic but need experienced owners and extensive exercise."
        }
    },
    90: {
        "id": "parson-russell-terrier",
        "name": "Parson Russell Terrier",
        "aliases": ["PRT", "Parson Jack Russell"],
        "group": "terrier",
        "origin": "England",
        "lifespan": "13-15 years",
        "size": {"height_cm": "33-36", "weight_kg": "6-8", "category": "small"},
        "ratings": {"size": 2, "energy": 5, "grooming": 1, "sociability": 3, "trainability": 3, "barking": 4, "kid_friendly": 3, "apartment_ok": 3},
        "characteristics": {"coat_type": "Smooth or broken", "coat_colors": ["white with tan", "black", "or both"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["bold", "friendly", "athletic", "clever", "tenacious", "independent"],
        "description": {
            "overview": "The Parson Russell is slightly larger and more square than the Jack Russell, bred to the original breed standard.",
            "temperament": "PRTs are bold, athletic, and clever. They're friendly but independent and need confident handling.",
            "health": "Generally healthy. May be prone to eye problems and deafness.",
            "exercise": "Extremely high energy. Need extensive daily exercise and activities."
        },
        "verdict": {
            "best_for": ["Very active owners", "Those interested in terrier sports", "Experienced owners", "Homes without small pets"],
            "not_for": ["Sedentary households", "First-time owners", "Homes with small pets", "Those wanting a calm dog"],
            "summary": "Athletic, bold terriers with endless energy. Parson Russells are clever and tenacious - perfect for active, experienced terrier enthusiasts."
        }
    },
    91: {
        "id": "toy-fox-terrier",
        "name": "Toy Fox Terrier",
        "aliases": ["TFT", "American Toy Terrier", "Amertoy"],
        "group": "toy",
        "origin": "United States",
        "lifespan": "13-15 years",
        "size": {"height_cm": "22-29", "weight_kg": "1.5-3", "category": "tiny"},
        "ratings": {"size": 1, "energy": 4, "grooming": 1, "sociability": 4, "trainability": 5, "barking": 3, "kid_friendly": 3, "apartment_ok": 5},
        "characteristics": {"coat_type": "Short, fine, smooth", "coat_colors": ["tri-color", "white and black", "white and tan", "white, chocolate and tan"], "shedding": "minimal", "hypoallergenic": False},
        "temperament": ["intelligent", "alert", "friendly", "loyal", "spirited", "athletic"],
        "description": {
            "overview": "The Toy Fox Terrier is a true American breed that combines terrier tenacity with toy-dog charm.",
            "temperament": "TFTs are intelligent, loyal, and spirited. They're athletic for their size and excel at tricks and agility.",
            "health": "Prone to patellar luxation and Legg-Calve-Perthes disease.",
            "exercise": "Moderate energy for a terrier. Need daily play and mental stimulation."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Those wanting a trainable toy dog", "Active seniors", "Owners interested in tricks and agility"],
            "not_for": ["Families with young children", "Those wanting a cuddly lap dog only", "Cold climates without protection", "Rough households"],
            "summary": "Tiny athletes with big terrier personalities. Toy Fox Terriers are intelligent, trainable, and perfect for apartments."
        }
    },
    92: {
        "id": "rat-terrier",
        "name": "Rat Terrier",
        "aliases": ["Ratting Terrier", "Decker Giant"],
        "group": "terrier",
        "origin": "United States",
        "lifespan": "12-18 years",
        "size": {"height_cm": "25-46", "weight_kg": "4-11", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 1, "sociability": 4, "trainability": 4, "barking": 3, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Short, smooth, dense", "coat_colors": ["any variation of pied patterning"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["intelligent", "alert", "loving", "inquisitive", "lively", "fearless"],
        "description": {
            "overview": "The Rat Terrier is an American farm dog bred to control vermin, valued for its intelligence and versatility.",
            "temperament": "Rat Terriers are intelligent, loving, and lively. They bond closely with family and are good with children.",
            "health": "Generally healthy. May be prone to patellar luxation and hip dysplasia.",
            "exercise": "Moderate to high energy. Need daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Families", "Active households", "Those wanting a versatile companion", "Farm and rural homes"],
            "not_for": ["Homes with small pets", "Those wanting a calm lap dog", "Owners away from home often", "First-time owners wanting an easy dog"],
            "summary": "Versatile American farm dogs with loving personalities. Rat Terriers are intelligent, family-friendly, and adaptable to various living situations."
        }
    },
    93: {
        "id": "dogo-argentino",
        "name": "Dogo Argentino",
        "aliases": ["Argentine Dogo", "Argentine Mastiff"],
        "group": "working",
        "origin": "Argentina",
        "lifespan": "9-15 years",
        "size": {"height_cm": "60-68", "weight_kg": "35-45", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 1, "sociability": 2, "trainability": 4, "barking": 2, "kid_friendly": 3, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short, smooth", "coat_colors": ["white (small dark patch near eye allowed)"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["loyal", "courageous", "protective", "friendly", "cheerful", "athletic"],
        "description": {
            "overview": "The Dogo Argentino was bred in Argentina for big-game hunting, including wild boar and puma.",
            "temperament": "Dogos are loyal, courageous, and protective. They're friendly with family but need early socialization.",
            "health": "Prone to deafness (especially pigment-related) and hip dysplasia.",
            "exercise": "High energy. Need vigorous daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Experienced large breed owners", "Active households", "Those wanting a loyal protector", "Homes with secure yards"],
            "not_for": ["First-time owners", "Apartment dwellers", "Multi-dog households", "Areas with breed restrictions"],
            "summary": "Powerful Argentine hunting dogs with loyal hearts. Dogos are athletic and protective but need experienced owners and proper socialization."
        }
    },
    94: {
        "id": "boerboel",
        "name": "Boerboel",
        "aliases": ["South African Mastiff", "South African Boerboel"],
        "group": "working",
        "origin": "South Africa",
        "lifespan": "9-11 years",
        "size": {"height_cm": "59-70", "weight_kg": "50-90", "category": "giant"},
        "ratings": {"size": 5, "energy": 3, "grooming": 1, "sociability": 2, "trainability": 3, "barking": 2, "kid_friendly": 4, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short, dense, smooth", "coat_colors": ["brown", "red", "fawn", "brindle"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["confident", "intelligent", "calm", "protective", "loyal", "obedient"],
        "description": {
            "overview": "The Boerboel is a powerful South African mastiff bred to protect homesteads from predators.",
            "temperament": "Boerboels are confident, calm, and deeply protective. They're gentle with family but formidable guardians.",
            "health": "Prone to hip dysplasia, elbow dysplasia, and heart problems.",
            "exercise": "Moderate exercise needs. Daily walks and play but not highly active."
        },
        "verdict": {
            "best_for": ["Experienced large breed owners", "Rural properties", "Those wanting a guardian", "Families with older children"],
            "not_for": ["First-time owners", "Apartment dwellers", "Novice large breed handlers", "Areas with breed restrictions"],
            "summary": "Powerful South African guardians with calm confidence. Boerboels are protective and loyal but need experienced handlers and space."
        }
    },
    95: {
        "id": "american-eskimo-dog",
        "name": "American Eskimo Dog",
        "aliases": ["Eskie", "American Spitz"],
        "group": "non-sporting",
        "origin": "Germany/United States",
        "lifespan": "13-15 years",
        "size": {"height_cm": "38-48", "weight_kg": "8-16", "category": "medium"},
        "ratings": {"size": 2, "energy": 4, "grooming": 4, "sociability": 4, "trainability": 5, "barking": 4, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Dense, fluffy double coat", "coat_colors": ["white", "white and biscuit"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["intelligent", "alert", "friendly", "eager to please", "playful", "protective"],
        "description": {
            "overview": "Despite its name, the American Eskimo Dog descended from German Spitz dogs and was popular in circus acts.",
            "temperament": "Eskies are intelligent, eager to please, and love to perform. They're friendly but alert watchdogs.",
            "health": "Prone to hip dysplasia, eye problems, and patellar luxation.",
            "exercise": "Moderate to high energy. Need daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Families", "Those wanting a trainable companion", "Trick and agility enthusiasts", "First-time owners"],
            "not_for": ["Those bothered by shedding or barking", "Owners away from home often", "Hot climates", "Those wanting a quiet dog"],
            "summary": "Brilliant, fluffy performers that love to learn. American Eskimo Dogs are highly trainable and friendly but shed heavily and can be vocal."
        }
    },
    96: {
        "id": "shikoku",
        "name": "Shikoku",
        "aliases": ["Shikoku Ken", "Kochi Ken", "Japanese Wolfdog"],
        "group": "hound",
        "origin": "Japan",
        "lifespan": "10-12 years",
        "size": {"height_cm": "43-55", "weight_kg": "16-25", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 3, "sociability": 2, "trainability": 3, "barking": 2, "kid_friendly": 3, "apartment_ok": 2},
        "characteristics": {"coat_type": "Double coat, harsh outer, soft under", "coat_colors": ["sesame", "black sesame", "red sesame"], "shedding": "heavy", "hypoallergenic": False},
        "temperament": ["loyal", "alert", "cautious", "brave", "agile", "intelligent"],
        "description": {
            "overview": "The Shikoku is a rare Japanese hunting dog from the mountains of Shikoku island, used to hunt wild boar.",
            "temperament": "Shikoku are loyal, alert, and cautious with strangers. They're brave hunters and devoted companions.",
            "health": "Generally healthy. May be prone to hip dysplasia and allergies.",
            "exercise": "High energy. Need vigorous daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Experienced dog owners", "Active households", "Those appreciating rare breeds", "Homes with secure yards"],
            "not_for": ["First-time owners", "Apartment dwellers", "Multi-pet households", "Those wanting a social dog"],
            "summary": "Rare Japanese hunting dogs with wolf-like appearance. Shikoku are loyal and agile but need experienced owners and plenty of exercise."
        }
    },
    97: {
        "id": "thai-ridgeback",
        "name": "Thai Ridgeback",
        "aliases": ["TRD", "Mah Thai Lang Ahn"],
        "group": "hound",
        "origin": "Thailand",
        "lifespan": "12-13 years",
        "size": {"height_cm": "51-61", "weight_kg": "16-34", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 1, "sociability": 2, "trainability": 3, "barking": 2, "kid_friendly": 3, "apartment_ok": 2},
        "characteristics": {"coat_type": "Short, smooth with distinctive ridge", "coat_colors": ["solid red", "black", "blue", "fawn"], "shedding": "minimal", "hypoallergenic": False},
        "temperament": ["loyal", "independent", "intelligent", "protective", "athletic", "aloof"],
        "description": {
            "overview": "The Thai Ridgeback is an ancient pariah dog with a distinctive hair ridge running along its back.",
            "temperament": "TRDs are loyal and protective but independent and reserved. They bond closely with one person or family.",
            "health": "Generally healthy. May be prone to dermoid sinus.",
            "exercise": "High energy. Need daily vigorous exercise and secure areas."
        },
        "verdict": {
            "best_for": ["Experienced dog owners", "Those wanting a unique breed", "Active individuals", "Warm climates"],
            "not_for": ["First-time owners", "Multi-pet households", "Cold climates", "Those wanting an outgoing dog"],
            "summary": "Ancient Thai dogs with distinctive ridges and independent spirits. Thai Ridgebacks are loyal but need experienced, patient owners."
        }
    },
    98: {
        "id": "xoloitzcuintli",
        "name": "Xoloitzcuintli",
        "aliases": ["Xolo", "Mexican Hairless Dog"],
        "group": "non-sporting",
        "origin": "Mexico",
        "lifespan": "13-18 years",
        "size": {"height_cm": "25-60", "weight_kg": "4-25", "category": "medium"},
        "ratings": {"size": 3, "energy": 3, "grooming": 2, "sociability": 3, "trainability": 4, "barking": 2, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Hairless or coated variety", "coat_colors": ["black", "gray", "bronze", "red", "liver"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["loyal", "alert", "calm", "intelligent", "affectionate", "attentive"],
        "description": {
            "overview": "The Xoloitzcuintli is an ancient Mexican breed dating back 3,000 years, considered sacred by the Aztecs.",
            "temperament": "Xolos are loyal, calm, and affectionate with family. They're alert watchdogs but not aggressive.",
            "health": "Generally healthy. Hairless variety needs skin protection.",
            "exercise": "Moderate exercise needs. Daily walks and play sessions."
        },
        "verdict": {
            "best_for": ["Those wanting a unique, ancient breed", "Allergy sufferers (hairless)", "Apartment dwellers", "Warm climates"],
            "not_for": ["Cold climates without protection", "Those wanting a fluffy dog", "Outdoor-focused owners", "Those unwanting skincare routine"],
            "summary": "Ancient Aztec dogs in hairless or coated varieties. Xolos are loyal, calm companions perfect for apartments but need skin care."
        }
    },
    99: {
        "id": "peruvian-inca-orchid",
        "name": "Peruvian Inca Orchid",
        "aliases": ["PIO", "Peruvian Hairless Dog", "Perro Sin Pelo del Perú"],
        "group": "hound",
        "origin": "Peru",
        "lifespan": "12-14 years",
        "size": {"height_cm": "25-65", "weight_kg": "4-25", "category": "medium"},
        "ratings": {"size": 3, "energy": 3, "grooming": 2, "sociability": 3, "trainability": 3, "barking": 2, "kid_friendly": 3, "apartment_ok": 4},
        "characteristics": {"coat_type": "Hairless or coated", "coat_colors": ["all colors including mottled"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["affectionate", "loyal", "alert", "lively", "protective", "intelligent"],
        "description": {
            "overview": "The Peruvian Inca Orchid is an ancient sighthound that comes in hairless and coated varieties.",
            "temperament": "PIOs are affectionate with family but wary of strangers. They're loyal and make good watchdogs.",
            "health": "Generally healthy. Hairless variety prone to skin issues and dental problems.",
            "exercise": "Moderate energy. Need daily exercise and enjoy running."
        },
        "verdict": {
            "best_for": ["Those wanting a unique breed", "Allergy sufferers", "Apartment dwellers", "Warm climates"],
            "not_for": ["Cold climates", "Very social households", "Those wanting low-maintenance", "Rough play environments"],
            "summary": "Elegant Peruvian sighthounds in hairless or coated varieties. PIOs are loyal and affectionate but need skin care and sun protection."
        }
    },
    100: {
        "id": "entlebucher-mountain-dog",
        "name": "Entlebucher Mountain Dog",
        "aliases": ["Entlebucher", "Entlebucher Sennenhund", "Entle"],
        "group": "herding",
        "origin": "Switzerland",
        "lifespan": "11-13 years",
        "size": {"height_cm": "42-52", "weight_kg": "20-30", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 2, "sociability": 4, "trainability": 4, "barking": 3, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Short, dense, harsh", "coat_colors": ["tricolor - black with tan and white markings"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["loyal", "smart", "enthusiastic", "independent", "self-assured", "agile"],
        "description": {
            "overview": "The Entlebucher is the smallest of the four Swiss Mountain Dogs, bred for herding cattle in the Alps.",
            "temperament": "Entles are loyal, smart, and enthusiastic. They're devoted to family and excel at various dog sports.",
            "health": "Prone to hip dysplasia and eye problems (PRA).",
            "exercise": "High energy. Need vigorous daily exercise and mental challenges."
        },
        "verdict": {
            "best_for": ["Active families", "Those interested in dog sports", "Experienced herding breed owners", "Homes with yards"],
            "not_for": ["Sedentary households", "Apartment dwellers without exercise plan", "First-time owners", "Those wanting a low-energy dog"],
            "summary": "The smallest Swiss Mountain Dog with big energy and loyalty. Entles are smart, athletic, and devoted - perfect for active families."
        }
    },
    # 101-110 Terriers
    101: {
        "id": "cairn-terrier",
        "name": "Cairn Terrier",
        "aliases": ["Cairn"],
        "group": "terrier",
        "origin": "Scotland",
        "lifespan": "13-15 years",
        "size": {"height_cm": "23-33", "weight_kg": "6-8", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 3, "sociability": 4, "trainability": 3, "barking": 4, "kid_friendly": 4, "apartment_ok": 5},
        "characteristics": {"coat_type": "Harsh, weather-resistant double coat", "coat_colors": ["cream", "wheaten", "red", "gray", "nearly black"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["alert", "cheerful", "busy", "independent", "hardy", "fearless"],
        "description": {
            "overview": "The Cairn Terrier is one of Scotland's oldest terriers, made famous by Toto in The Wizard of Oz.",
            "temperament": "Cairns are cheerful, busy little dogs with typical terrier spirit. They're friendly but independent.",
            "health": "Prone to liver shunt, eye problems, and hip dysplasia.",
            "exercise": "Moderate to high energy. Need daily walks and play."
        },
        "verdict": {
            "best_for": ["Families", "Apartment dwellers", "Those wanting a spirited companion", "Active seniors"],
            "not_for": ["Those wanting a calm lap dog", "Homes with small pets", "Those bothered by digging", "First-time owners wanting easy training"],
            "summary": "Cheerful Scottish terriers with big personalities. Cairns are friendly and adaptable but have typical terrier independence."
        }
    },
    102: {
        "id": "norfolk-terrier",
        "name": "Norfolk Terrier",
        "aliases": ["Norfolk"],
        "group": "terrier",
        "origin": "England",
        "lifespan": "12-16 years",
        "size": {"height_cm": "23-25", "weight_kg": "5-6", "category": "small"},
        "ratings": {"size": 1, "energy": 4, "grooming": 3, "sociability": 5, "trainability": 4, "barking": 3, "kid_friendly": 5, "apartment_ok": 5},
        "characteristics": {"coat_type": "Hard, wiry, straight", "coat_colors": ["red", "wheaten", "black and tan", "grizzle"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["alert", "fearless", "fun-loving", "loyal", "confident", "affectionate"],
        "description": {
            "overview": "The Norfolk Terrier is one of the smallest working terriers, with folded ears distinguishing it from the Norwich.",
            "temperament": "Norfolks are friendly, confident, and love everyone. Less scrappy than many terriers.",
            "health": "Generally healthy. May be prone to hip dysplasia and heart problems.",
            "exercise": "Moderate energy. Daily walks and play sessions."
        },
        "verdict": {
            "best_for": ["Families with children", "Apartment dwellers", "First-time terrier owners", "Active seniors"],
            "not_for": ["Homes with small pets", "Those wanting an independent dog", "Those unwilling to groom", "Sedentary households"],
            "summary": "Friendly, portable terriers perfect for families. Norfolk Terriers are less scrappy than many terriers and great with kids."
        }
    },
    103: {
        "id": "norwich-terrier",
        "name": "Norwich Terrier",
        "aliases": ["Norwich"],
        "group": "terrier",
        "origin": "England",
        "lifespan": "12-15 years",
        "size": {"height_cm": "24-25", "weight_kg": "5-6", "category": "small"},
        "ratings": {"size": 1, "energy": 4, "grooming": 3, "sociability": 4, "trainability": 4, "barking": 3, "kid_friendly": 4, "apartment_ok": 5},
        "characteristics": {"coat_type": "Hard, wiry, straight", "coat_colors": ["red", "wheaten", "black and tan", "grizzle"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["alert", "curious", "fearless", "loyal", "affectionate", "spirited"],
        "description": {
            "overview": "The Norwich Terrier has pricked ears (unlike the folded-ear Norfolk) and was bred to hunt vermin.",
            "temperament": "Norwich are alert, curious, and affectionate. They're spirited but generally good-natured.",
            "health": "Generally healthy. May be prone to upper airway syndrome and hip dysplasia.",
            "exercise": "Moderate energy. Need daily walks and mental stimulation."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Families", "Those wanting a small, spirited dog", "Active individuals"],
            "not_for": ["Homes with small pets", "Those wanting a quiet dog", "Sedentary households", "Very young children"],
            "summary": "Small but mighty terriers with pricked ears. Norwich are curious, affectionate, and adapt well to various living situations."
        }
    },
    104: {
        "id": "wire-fox-terrier",
        "name": "Wire Fox Terrier",
        "aliases": ["Wire", "WFT"],
        "group": "terrier",
        "origin": "England",
        "lifespan": "12-15 years",
        "size": {"height_cm": "36-41", "weight_kg": "7-9", "category": "small"},
        "ratings": {"size": 2, "energy": 5, "grooming": 4, "sociability": 4, "trainability": 3, "barking": 4, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Dense, wiry", "coat_colors": ["white with black", "tan", "or both"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["alert", "confident", "fearless", "friendly", "energetic", "keen"],
        "description": {
            "overview": "The Wire Fox Terrier is a classic British terrier that has won more Best in Show titles at Westminster than any other breed.",
            "temperament": "Wire Fox Terriers are confident, fearless, and full of energy. They're friendly but independent.",
            "health": "Prone to eye problems, hip dysplasia, and skin allergies.",
            "exercise": "Very high energy. Need extensive daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a show-quality terrier", "Experienced terrier owners", "Homes with secure yards"],
            "not_for": ["Sedentary households", "Homes with small pets", "First-time owners", "Those wanting a quiet dog"],
            "summary": "Classic show-ring champions with terrier spirit. Wire Fox Terriers are confident and energetic - perfect for active, experienced owners."
        }
    },
    105: {
        "id": "smooth-fox-terrier",
        "name": "Smooth Fox Terrier",
        "aliases": ["Smooth", "SFT"],
        "group": "terrier",
        "origin": "England",
        "lifespan": "12-15 years",
        "size": {"height_cm": "36-41", "weight_kg": "7-9", "category": "small"},
        "ratings": {"size": 2, "energy": 5, "grooming": 1, "sociability": 4, "trainability": 3, "barking": 4, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Smooth, flat, dense", "coat_colors": ["white with black", "tan", "or both"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["alert", "fearless", "friendly", "energetic", "playful", "independent"],
        "description": {
            "overview": "The Smooth Fox Terrier is the older of the two Fox Terrier varieties, with a sleek, easy-care coat.",
            "temperament": "Smooth Fox Terriers are fearless, energetic, and playful. They're friendly but have strong hunting instincts.",
            "health": "Prone to deafness, eye problems, and patellar luxation.",
            "exercise": "Very high energy. Need extensive daily exercise and activities."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a lower-maintenance coat", "Experienced terrier owners", "Homes with yards"],
            "not_for": ["Sedentary households", "Homes with small pets", "Those wanting a quiet dog", "First-time owners"],
            "summary": "Sleek, athletic terriers with boundless energy. Smooth Fox Terriers are easier to groom than Wires but equally spirited."
        }
    },
    106: {
        "id": "lakeland-terrier",
        "name": "Lakeland Terrier",
        "aliases": ["Lakie"],
        "group": "terrier",
        "origin": "England",
        "lifespan": "12-15 years",
        "size": {"height_cm": "33-38", "weight_kg": "7-8", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 4, "sociability": 3, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Dense, wiry double coat", "coat_colors": ["black and tan", "blue and tan", "red", "wheaten", "grizzle"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["bold", "confident", "friendly", "independent", "intelligent", "tenacious"],
        "description": {
            "overview": "The Lakeland Terrier was bred to protect sheep from foxes in England's Lake District.",
            "temperament": "Lakelands are bold, confident, and friendly. They're independent but less scrappy than some terriers.",
            "health": "Generally healthy. May be prone to eye problems and Legg-Calve-Perthes disease.",
            "exercise": "Moderate to high energy. Need daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Active families", "Apartment dwellers (with exercise)", "Allergy sufferers", "Experienced terrier owners"],
            "not_for": ["Homes with small pets", "Those wanting an eager-to-please dog", "Sedentary households", "First-time owners"],
            "summary": "Bold, confident terriers from England's Lake District. Lakelands are friendly and hypoallergenic but have typical terrier independence."
        }
    },
    107: {
        "id": "welsh-terrier",
        "name": "Welsh Terrier",
        "aliases": ["Welshie"],
        "group": "terrier",
        "origin": "Wales",
        "lifespan": "12-15 years",
        "size": {"height_cm": "36-39", "weight_kg": "9-10", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 3, "sociability": 4, "trainability": 4, "barking": 3, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Dense, wiry double coat", "coat_colors": ["black and tan", "grizzle and tan"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["friendly", "spirited", "alert", "intelligent", "game", "cheerful"],
        "description": {
            "overview": "The Welsh Terrier is one of the oldest terrier breeds, resembling a smaller Airedale.",
            "temperament": "Welsh Terriers are friendly, spirited, and intelligent. They're more easygoing than many terriers.",
            "health": "Generally healthy. May be prone to eye problems and allergies.",
            "exercise": "Moderate to high energy. Need daily exercise and play."
        },
        "verdict": {
            "best_for": ["Families", "Apartment dwellers", "First-time terrier owners", "Active households"],
            "not_for": ["Homes with small pets", "Sedentary households", "Those wanting a calm dog", "Off-leash environments"],
            "summary": "Friendly Welsh terriers that are more easygoing than most. Welsh Terriers are great family dogs with typical terrier spirit."
        }
    },
    108: {
        "id": "skye-terrier",
        "name": "Skye Terrier",
        "aliases": ["Skye"],
        "group": "terrier",
        "origin": "Scotland",
        "lifespan": "12-14 years",
        "size": {"height_cm": "24-27", "weight_kg": "16-20", "category": "small"},
        "ratings": {"size": 2, "energy": 3, "grooming": 5, "sociability": 2, "trainability": 3, "barking": 3, "kid_friendly": 3, "apartment_ok": 4},
        "characteristics": {"coat_type": "Long, straight, flat", "coat_colors": ["black", "blue", "gray", "cream", "fawn"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["loyal", "good-tempered", "canny", "dignified", "fearless", "reserved"],
        "description": {
            "overview": "The Skye Terrier is a rare Scottish breed known for its long, flowing coat and devotion to one person.",
            "temperament": "Skyes are loyal and devoted to their person but reserved with strangers. They're dignified and fearless.",
            "health": "Prone to orthopedic problems (don't let puppies jump) and certain cancers.",
            "exercise": "Moderate exercise needs. Daily walks but not highly active."
        },
        "verdict": {
            "best_for": ["Singles or couples", "Those wanting a loyal one-person dog", "Owners committed to grooming", "Quiet households"],
            "not_for": ["Families with young children", "Multi-dog households", "Those wanting a social dog", "Active households"],
            "summary": "Rare, dignified terriers devoted to one person. Skye Terriers are loyal but reserved - perfect for quiet homes with dedicated owners."
        }
    },
    109: {
        "id": "sealyham-terrier",
        "name": "Sealyham Terrier",
        "aliases": ["Sealy"],
        "group": "terrier",
        "origin": "Wales",
        "lifespan": "12-14 years",
        "size": {"height_cm": "27-30", "weight_kg": "8-11", "category": "small"},
        "ratings": {"size": 2, "energy": 3, "grooming": 4, "sociability": 3, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 5},
        "characteristics": {"coat_type": "Long, hard, wiry outer coat", "coat_colors": ["all white", "white with lemon", "tan", "or badger markings"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["outgoing", "calm", "fearless", "adaptable", "friendly", "alert"],
        "description": {
            "overview": "The Sealyham Terrier is a rare Welsh breed that was once the darling of Hollywood celebrities.",
            "temperament": "Sealyhams are calmer than most terriers. They're friendly, adaptable, and make excellent companions.",
            "health": "Prone to eye problems (lens luxation) and deafness.",
            "exercise": "Moderate exercise needs. Daily walks and play."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Those wanting a calmer terrier", "Allergy sufferers", "Families"],
            "not_for": ["Those wanting a highly active dog", "Homes with small pets", "Owners unwilling to groom", "Those wanting a common breed"],
            "summary": "Rare, calm terriers perfect for apartments. Sealyhams are friendlier and more adaptable than most terriers."
        }
    },
    110: {
        "id": "dandie-dinmont-terrier",
        "name": "Dandie Dinmont Terrier",
        "aliases": ["Dandie"],
        "group": "terrier",
        "origin": "Scotland",
        "lifespan": "12-15 years",
        "size": {"height_cm": "20-28", "weight_kg": "8-11", "category": "small"},
        "ratings": {"size": 2, "energy": 3, "grooming": 3, "sociability": 3, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 5},
        "characteristics": {"coat_type": "Crisp outer coat with soft undercoat", "coat_colors": ["pepper (bluish-black to silver)", "mustard (reddish-brown to fawn)"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["independent", "determined", "dignified", "affectionate", "fun", "intelligent"],
        "description": {
            "overview": "The Dandie Dinmont is a rare Scottish terrier, the only breed named after a fictional character (from a Sir Walter Scott novel).",
            "temperament": "Dandies are independent but affectionate. They're dignified and less hyperactive than many terriers.",
            "health": "Prone to intervertebral disc disease (due to long back) and glaucoma.",
            "exercise": "Moderate exercise needs. Daily walks and play sessions."
        },
        "verdict": {
            "best_for": ["Apartment dwellers", "Those wanting a unique terrier", "Calm households", "Allergy sufferers"],
            "not_for": ["Those wanting a highly active dog", "Rough-play households (back issues)", "Those wanting a common breed", "Off-leash environments"],
            "summary": "Unique, dignified terriers with a literary heritage. Dandies are calmer than most terriers and adapt well to apartment life."
        }
    }
}

OUTPUT_DIR = "/Users/juhaporraskorpi/clawd/dog-breed-guide/data/breeds"

for num, breed_data in BREEDS.items():
    filepath = f"{OUTPUT_DIR}/{breed_data['id']}.json"
    with open(filepath, 'w') as f:
        json.dump(breed_data, f, indent=2)
    print(f"Created: {breed_data['id']}.json")

print(f"\nTotal: {len(BREEDS)} breed files created")
