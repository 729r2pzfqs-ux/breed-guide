#!/usr/bin/env python3
"""Generate breed pages for breeds 111-150"""

import os
import json

# Breed data for 111-150
NEW_BREEDS = [
    # Terriers 111-115
    {
        "id": "glen-of-imaal-terrier", "name": "Glen of Imaal Terrier",
        "group": "terrier", "origin": "Ireland", "lifespan": "10-14 years",
        "size": {"height_cm": "32-36", "weight_kg": "14-16", "category": "small"},
        "ratings": {"size": 2, "energy": 3, "grooming": 2, "sociability": 3, "trainability": 3, "barking": 2, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Medium, harsh", "coat_colors": ["wheaten", "blue", "brindle"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["spirited", "gentle", "loyal", "brave", "patient"],
        "description": {
            "overview": "A sturdy, low-to-ground terrier from Ireland's Wicklow Mountains, bred for hunting badgers and foxes.",
            "temperament": "Gentler than most terriers, Glens are patient and less excitable. They're brave and loyal family companions.",
            "health": "Watch for hip dysplasia and PRA (progressive retinal atrophy). Generally healthy breed.",
            "exercise": "Moderate exercise needs. Enjoys walks and play but doesn't require intense activity."
        },
        "verdict": {
            "best_for": ["Families wanting a calmer terrier", "Apartment dwellers", "Those wanting a loyal companion", "Owners seeking a low-bark dog"],
            "not_for": ["Those wanting a high-energy terrier", "Homes with small pets", "Those not committed to training"],
            "summary": "A sturdy, gentle terrier that's calmer than most. Great for families wanting terrier spirit without terrier intensity."
        }
    },
    {
        "id": "kerry-blue-terrier", "name": "Kerry Blue Terrier",
        "group": "terrier", "origin": "Ireland", "lifespan": "12-15 years",
        "size": {"height_cm": "44-51", "weight_kg": "15-18", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 4, "sociability": 3, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Soft, wavy, non-shedding", "coat_colors": ["blue-gray"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["spirited", "alert", "determined", "loyal", "playful"],
        "description": {
            "overview": "Ireland's national terrier, known for its distinctive blue-gray coat that develops with age.",
            "temperament": "Spirited and alert with strong hunting instincts. Loyal to family but can be dog-aggressive.",
            "health": "Prone to hip dysplasia, eye problems, and skin issues. Relatively healthy overall.",
            "exercise": "High energy requiring daily vigorous exercise. Excels in dog sports."
        },
        "verdict": {
            "best_for": ["Active families", "Experienced dog owners", "Those wanting a non-shedding dog", "Homes without other dogs"],
            "not_for": ["First-time owners", "Multi-dog households", "Those unwilling to groom regularly"],
            "summary": "A spirited Irish terrier with a stunning blue coat. Needs experienced handling and regular grooming."
        }
    },
    {
        "id": "manchester-terrier", "name": "Manchester Terrier",
        "group": "terrier", "origin": "England", "lifespan": "14-16 years",
        "size": {"height_cm": "38-41", "weight_kg": "5-10", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 1, "sociability": 3, "trainability": 4, "barking": 3, "kid_friendly": 3, "apartment_ok": 4},
        "characteristics": {"coat_type": "Short, smooth, glossy", "coat_colors": ["black and tan"], "shedding": "low", "hypoallergenic": False},
        "temperament": ["spirited", "alert", "keen", "devoted", "athletic"],
        "description": {
            "overview": "An elegant, athletic terrier originally bred for rat hunting in Manchester, England.",
            "temperament": "Alert and spirited with strong prey drive. Devoted to owners, can be reserved with strangers.",
            "health": "Generally healthy. Watch for von Willebrand's disease and patellar luxation.",
            "exercise": "Needs regular exercise and mental stimulation. Excellent at agility and obedience."
        },
        "verdict": {
            "best_for": ["Active owners", "Apartment dwellers wanting a low-maintenance coat", "Those interested in dog sports", "Experienced terrier owners"],
            "not_for": ["Homes with small pets", "Those wanting a cuddly lap dog", "Families with very young children"],
            "summary": "Sleek, athletic terrier with minimal grooming needs. Alert and devoted but needs socialization."
        }
    },
    {
        "id": "bedlington-terrier", "name": "Bedlington Terrier",
        "group": "terrier", "origin": "England", "lifespan": "12-14 years",
        "size": {"height_cm": "38-44", "weight_kg": "8-10", "category": "small"},
        "ratings": {"size": 2, "energy": 3, "grooming": 4, "sociability": 3, "trainability": 3, "barking": 2, "kid_friendly": 4, "apartment_ok": 4},
        "characteristics": {"coat_type": "Curly, woolly, non-shedding", "coat_colors": ["blue", "liver", "sandy"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["gentle", "loyal", "spirited", "affectionate", "courageous"],
        "description": {
            "overview": "A unique lamb-like terrier that's gentler than most, originally bred for hunting vermin in English mines.",
            "temperament": "Gentle and affectionate at home but retains terrier courage. Good with children.",
            "health": "Prone to copper toxicosis (liver disease). Reputable breeders test for this.",
            "exercise": "Moderate exercise needs. Enjoys walks and playtime but not overly demanding."
        },
        "verdict": {
            "best_for": ["Families with children", "Allergy sufferers", "Apartment dwellers", "Those wanting a gentler terrier"],
            "not_for": ["Those unwilling to groom regularly", "Homes with small pets", "Those wanting a guard dog"],
            "summary": "A lamb-like terrier that's gentler than most. Great family dog but requires regular professional grooming."
        }
    },
    {
        "id": "border-terrier", "name": "Border Terrier",
        "group": "terrier", "origin": "England/Scotland", "lifespan": "12-15 years",
        "size": {"height_cm": "28-40", "weight_kg": "5-7", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 2, "sociability": 4, "trainability": 4, "barking": 3, "kid_friendly": 5, "apartment_ok": 4},
        "characteristics": {"coat_type": "Wiry, weather-resistant", "coat_colors": ["red", "wheaten", "grizzle and tan", "blue and tan"], "shedding": "low", "hypoallergenic": False},
        "temperament": ["affectionate", "alert", "obedient", "fearless", "good-natured"],
        "description": {
            "overview": "A small, tough working terrier from the border country between England and Scotland.",
            "temperament": "One of the most good-natured terriers. Affectionate, adaptable, and great with children.",
            "health": "Generally healthy. Watch for hip dysplasia, heart defects, and seizures.",
            "exercise": "Active breed needing daily walks and play. Loves outdoor adventures."
        },
        "verdict": {
            "best_for": ["Families with children", "Active individuals", "First-time terrier owners", "Those wanting an adaptable dog"],
            "not_for": ["Homes with small pets", "Those wanting a couch potato", "Off-leash walking without training"],
            "summary": "One of the friendliest terriers—great with kids and adaptable to most living situations."
        }
    },
    
    # Hounds 116-130
    {
        "id": "borzoi", "name": "Borzoi",
        "group": "hound", "origin": "Russia", "lifespan": "9-14 years",
        "size": {"height_cm": "68-85", "weight_kg": "27-48", "category": "giant"},
        "ratings": {"size": 5, "energy": 3, "grooming": 3, "sociability": 2, "trainability": 2, "barking": 1, "kid_friendly": 3, "apartment_ok": 3},
        "characteristics": {"coat_type": "Long, silky, wavy", "coat_colors": ["any color"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["gentle", "dignified", "independent", "quiet", "affectionate"],
        "description": {
            "overview": "An elegant Russian sighthound bred for hunting wolves, known for its grace and aristocratic bearing.",
            "temperament": "Gentle and quiet indoors but has strong chase instincts. Independent and cat-like.",
            "health": "Prone to bloat, heart problems, and bone cancer. Sensitive to anesthesia.",
            "exercise": "Needs space to run but calm indoors. Must be in securely fenced areas."
        },
        "verdict": {
            "best_for": ["Quiet households", "Those appreciating elegant dogs", "Experienced sighthound owners", "Homes with secure fencing"],
            "not_for": ["Homes with small pets", "Those wanting an obedient dog", "Active families with young children"],
            "summary": "Elegant, quiet giants that are gentle at home but have strong prey drive. Need secure fencing."
        }
    },
    {
        "id": "irish-wolfhound", "name": "Irish Wolfhound",
        "group": "hound", "origin": "Ireland", "lifespan": "6-8 years",
        "size": {"height_cm": "71-90", "weight_kg": "40-69", "category": "giant"},
        "ratings": {"size": 5, "energy": 3, "grooming": 2, "sociability": 5, "trainability": 3, "barking": 1, "kid_friendly": 5, "apartment_ok": 2},
        "characteristics": {"coat_type": "Rough, wiry", "coat_colors": ["gray", "brindle", "red", "black", "white", "fawn"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["gentle", "dignified", "patient", "loyal", "courageous"],
        "description": {
            "overview": "The tallest of all dog breeds, originally bred to hunt wolves in Ireland. Known as gentle giants.",
            "temperament": "Despite their size, Irish Wolfhounds are gentle, patient, and excellent with children.",
            "health": "Short lifespan due to size. Prone to heart disease, bone cancer, and bloat.",
            "exercise": "Moderate exercise needs. Daily walks and space to stretch their legs."
        },
        "verdict": {
            "best_for": ["Families wanting a gentle giant", "Those with space for a large dog", "Patient owners prepared for shorter lifespan", "Those wanting a calm companion"],
            "not_for": ["Small living spaces", "Those wanting a long-lived dog", "Budget-conscious owners (food costs)"],
            "summary": "The ultimate gentle giant. Wonderful family dogs but have short lifespans and need space."
        }
    },
    {
        "id": "scottish-deerhound", "name": "Scottish Deerhound",
        "group": "hound", "origin": "Scotland", "lifespan": "8-11 years",
        "size": {"height_cm": "71-81", "weight_kg": "34-50", "category": "giant"},
        "ratings": {"size": 5, "energy": 3, "grooming": 2, "sociability": 4, "trainability": 2, "barking": 1, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Harsh, wiry", "coat_colors": ["dark blue-gray", "gray", "brindle", "yellow", "red fawn"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["gentle", "dignified", "friendly", "docile", "eager"],
        "description": {
            "overview": "An ancient Scottish breed once used to hunt red deer, prized for its speed and endurance.",
            "temperament": "Gentle and dignified with a friendly, docile nature. Quiet and well-mannered indoors.",
            "health": "Prone to heart disease, bone cancer, and bloat. Sensitive to anesthesia.",
            "exercise": "Needs daily exercise and room to run. Must be leashed or in secure areas."
        },
        "verdict": {
            "best_for": ["Those appreciating noble, quiet dogs", "Rural homes with space", "Experienced sighthound owners", "Those wanting a dignified companion"],
            "not_for": ["Apartment dwellers", "Homes with small pets", "Those wanting an obedient dog"],
            "summary": "Dignified, gentle giants that are quiet indoors but need space to run. Strong prey drive."
        }
    },
    {
        "id": "petit-basset-griffon-vendeen", "name": "Petit Basset Griffon Vendéen",
        "group": "hound", "origin": "France", "lifespan": "14-16 years",
        "size": {"height_cm": "34-38", "weight_kg": "14-18", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 2, "sociability": 5, "trainability": 2, "barking": 4, "kid_friendly": 5, "apartment_ok": 3},
        "characteristics": {"coat_type": "Rough, long, harsh", "coat_colors": ["white with lemon", "orange", "tricolor", "grizzle"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["happy", "extroverted", "independent", "curious", "vivacious"],
        "description": {
            "overview": "A cheerful French scent hound known as PBGV, bred to hunt rabbits in the Vendée region.",
            "temperament": "Happy, outgoing, and friendly to everyone. Independent but loves company. Quite vocal.",
            "health": "Generally healthy. Watch for hip dysplasia, eye problems, and epilepsy.",
            "exercise": "Active breed needing daily exercise. Loves to follow scents—keep leashed."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a happy, social dog", "Experienced hound owners", "Those tolerant of barking"],
            "not_for": ["Noise-sensitive neighbors", "Those wanting an obedient dog", "Off-leash situations"],
            "summary": "Happy, extroverted little hounds that love everyone. Independent and vocal—true hound character."
        }
    },
    {
        "id": "otterhound", "name": "Otterhound",
        "group": "hound", "origin": "England", "lifespan": "10-13 years",
        "size": {"height_cm": "61-69", "weight_kg": "36-54", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 3, "sociability": 4, "trainability": 2, "barking": 4, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Dense, rough, double coat", "coat_colors": ["all hound colors"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["amiable", "boisterous", "even-tempered", "friendly", "independent"],
        "description": {
            "overview": "A rare, shaggy British hound bred to hunt otters, known for its webbed feet and love of water.",
            "temperament": "Friendly and boisterous with a deep, melodious bark. Independent but good-natured.",
            "health": "Prone to hip dysplasia and bloat. One of the rarest breeds—fewer than 1,000 worldwide.",
            "exercise": "Needs plenty of exercise and loves swimming. Must be secured—strong tracking instinct."
        },
        "verdict": {
            "best_for": ["Active families with space", "Those near water for swimming", "Those wanting a rare breed", "Patient trainers"],
            "not_for": ["Apartment dwellers", "Noise-sensitive neighbors", "Those wanting an obedient dog"],
            "summary": "Rare, lovable shaggy hounds that adore water. Independent and vocal but friendly and even-tempered."
        }
    },
    {
        "id": "black-and-tan-coonhound", "name": "Black and Tan Coonhound",
        "group": "hound", "origin": "United States", "lifespan": "10-12 years",
        "size": {"height_cm": "58-69", "weight_kg": "25-34", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 1, "sociability": 4, "trainability": 3, "barking": 5, "kid_friendly": 4, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short, dense", "coat_colors": ["black and tan"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["easygoing", "friendly", "mellow", "independent", "determined"],
        "description": {
            "overview": "An American scent hound bred to track raccoons and larger game, known for its distinctive bay.",
            "temperament": "Easygoing and friendly but independent when on a scent. Mellow at home.",
            "health": "Prone to hip dysplasia and ear infections. Generally healthy breed.",
            "exercise": "Needs regular exercise and mental stimulation through scent work."
        },
        "verdict": {
            "best_for": ["Rural homes", "Hunters and outdoor enthusiasts", "Those tolerant of baying", "Families wanting an easygoing dog"],
            "not_for": ["Apartment or suburban living", "Noise-sensitive neighbors", "Those wanting off-leash reliability"],
            "summary": "Easygoing American hounds that are mellow at home but loud when excited. Best for rural settings."
        }
    },
    {
        "id": "bluetick-coonhound", "name": "Bluetick Coonhound",
        "group": "hound", "origin": "United States", "lifespan": "11-12 years",
        "size": {"height_cm": "53-69", "weight_kg": "20-36", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 1, "sociability": 4, "trainability": 3, "barking": 5, "kid_friendly": 4, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short, glossy", "coat_colors": ["blue mottled"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["friendly", "intelligent", "devoted", "tenacious", "athletic"],
        "description": {
            "overview": "A striking American coonhound with a distinctive blue-mottled coat, bred for tracking game.",
            "temperament": "Friendly and devoted to family. Intelligent but single-minded when tracking.",
            "health": "Prone to hip dysplasia and bloat. Keep ears clean to prevent infections.",
            "exercise": "High exercise needs. Excels at scent work and needs room to run."
        },
        "verdict": {
            "best_for": ["Active rural families", "Hunters", "Those who appreciate hound baying", "Experienced hound owners"],
            "not_for": ["Apartment living", "Suburban neighborhoods", "Those wanting a quiet dog"],
            "summary": "Beautiful, devoted hounds with striking coats. Very vocal—truly meant for country living."
        }
    },
    {
        "id": "redbone-coonhound", "name": "Redbone Coonhound",
        "group": "hound", "origin": "United States", "lifespan": "12-15 years",
        "size": {"height_cm": "53-69", "weight_kg": "20-32", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 1, "sociability": 5, "trainability": 3, "barking": 5, "kid_friendly": 5, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short, smooth", "coat_colors": ["solid red"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["easygoing", "affectionate", "eager to please", "mellow", "sociable"],
        "description": {
            "overview": "A beautiful red American coonhound known for its even temper and affectionate nature.",
            "temperament": "One of the most easygoing coonhounds. Affectionate, great with kids, and eager to please.",
            "health": "Generally healthy. Watch for hip dysplasia and ear infections.",
            "exercise": "Needs daily exercise and loves outdoor adventures. Strong prey drive."
        },
        "verdict": {
            "best_for": ["Families with children", "Active outdoor enthusiasts", "Those wanting an affectionate hound", "Rural homes"],
            "not_for": ["Apartment living", "Noise-sensitive areas", "Those wanting a quiet dog"],
            "summary": "Sweet, affectionate hounds great with kids. Vocal like all coonhounds—best for country living."
        }
    },
    {
        "id": "treeing-walker-coonhound", "name": "Treeing Walker Coonhound",
        "group": "hound", "origin": "United States", "lifespan": "12-13 years",
        "size": {"height_cm": "51-69", "weight_kg": "20-32", "category": "large"},
        "ratings": {"size": 4, "energy": 5, "grooming": 1, "sociability": 4, "trainability": 3, "barking": 5, "kid_friendly": 4, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short, dense, smooth", "coat_colors": ["tricolor", "bicolor"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["intelligent", "confident", "loving", "competitive", "energetic"],
        "description": {
            "overview": "A fast, competitive American coonhound descended from English Foxhounds, popular in field trials.",
            "temperament": "Intelligent and confident with high energy. Loving with family but focused when hunting.",
            "health": "Generally healthy breed. Watch for hip dysplasia and ear infections.",
            "exercise": "Very high energy—needs lots of exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Hunters and field trialers", "Very active families", "Rural homes", "Experienced hound owners"],
            "not_for": ["Apartment living", "Sedentary owners", "Those wanting a quiet dog"],
            "summary": "High-energy, competitive hounds that excel in the field. Need lots of exercise and rural space."
        }
    },
    {
        "id": "plott-hound", "name": "Plott Hound",
        "group": "hound", "origin": "United States", "lifespan": "12-14 years",
        "size": {"height_cm": "51-64", "weight_kg": "18-27", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 1, "sociability": 3, "trainability": 3, "barking": 4, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Short, smooth, glossy", "coat_colors": ["brindle"], "shedding": "low", "hypoallergenic": False},
        "temperament": ["bold", "loyal", "intelligent", "alert", "confident"],
        "description": {
            "overview": "North Carolina's state dog, a unique brindle hound descended from German Hanover Hounds.",
            "temperament": "Bold and confident, more aggressive than other coonhounds. Loyal and protective of family.",
            "health": "Generally healthy. Watch for hip dysplasia and gastric torsion.",
            "exercise": "High energy requiring daily vigorous exercise. Excels at tracking."
        },
        "verdict": {
            "best_for": ["Experienced hound owners", "Active hunters", "Those wanting a loyal protector", "Rural homes"],
            "not_for": ["First-time owners", "Apartment living", "Multi-pet households"],
            "summary": "Bold, loyal hounds that are more protective than other coonhounds. Need experienced handling."
        }
    },
    {
        "id": "harrier", "name": "Harrier",
        "group": "hound", "origin": "England", "lifespan": "12-15 years",
        "size": {"height_cm": "48-53", "weight_kg": "20-27", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 1, "sociability": 5, "trainability": 3, "barking": 4, "kid_friendly": 5, "apartment_ok": 2},
        "characteristics": {"coat_type": "Short, dense, glossy", "coat_colors": ["all hound colors"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["outgoing", "friendly", "people-oriented", "active", "pack-minded"],
        "description": {
            "overview": "A medium-sized pack hound from England, essentially a smaller version of the English Foxhound.",
            "temperament": "Extremely friendly and outgoing. Loves people and other dogs. Pack-oriented.",
            "health": "Generally healthy breed. Watch for hip dysplasia and ear infections.",
            "exercise": "High energy needing daily vigorous exercise. Loves to run and track scents."
        },
        "verdict": {
            "best_for": ["Active families", "Multi-dog households", "Those wanting a friendly, social dog", "Runners and hikers"],
            "not_for": ["Apartment living", "Those wanting a quiet dog", "Sedentary owners"],
            "summary": "Friendly, pack-oriented hounds that love everyone. Need lots of exercise and companionship."
        }
    },
    {
        "id": "english-foxhound", "name": "English Foxhound",
        "group": "hound", "origin": "England", "lifespan": "10-13 years",
        "size": {"height_cm": "58-64", "weight_kg": "25-34", "category": "large"},
        "ratings": {"size": 4, "energy": 5, "grooming": 1, "sociability": 5, "trainability": 2, "barking": 4, "kid_friendly": 4, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short, dense, glossy", "coat_colors": ["tricolor", "bicolor"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["gentle", "sociable", "tolerant", "active", "pack-minded"],
        "description": {
            "overview": "A classic English pack hound bred for fox hunting, known for stamina and gentle nature.",
            "temperament": "Extremely sociable and gentle. Bred to work in packs, needs canine companionship.",
            "health": "Generally healthy. Watch for hip dysplasia and ear infections.",
            "exercise": "Very high energy—bred to run all day. Needs extensive exercise."
        },
        "verdict": {
            "best_for": ["Active rural families", "Multi-dog households", "Hunters", "Those with large properties"],
            "not_for": ["Apartment or suburban living", "Single-dog households", "Sedentary owners"],
            "summary": "Classic pack hounds needing canine companions and extensive exercise. Best for rural homes."
        }
    },
    {
        "id": "american-foxhound", "name": "American Foxhound",
        "group": "hound", "origin": "United States", "lifespan": "11-13 years",
        "size": {"height_cm": "53-64", "weight_kg": "27-32", "category": "large"},
        "ratings": {"size": 4, "energy": 5, "grooming": 1, "sociability": 4, "trainability": 2, "barking": 4, "kid_friendly": 4, "apartment_ok": 1},
        "characteristics": {"coat_type": "Medium length, hard", "coat_colors": ["any color"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["easygoing", "sweet", "independent", "loving", "determined"],
        "description": {
            "overview": "America's own foxhound, bred from English stock but taller and lighter.",
            "temperament": "Sweet and easygoing but independent. Musical voice—loves to bay.",
            "health": "Generally healthy breed. Watch for hip dysplasia and ear infections.",
            "exercise": "Extremely high energy. Needs hours of daily exercise."
        },
        "verdict": {
            "best_for": ["Very active rural families", "Hunters", "Multi-dog households", "Those with large properties"],
            "not_for": ["Apartment or suburban living", "Sedentary owners", "Noise-sensitive neighbors"],
            "summary": "Sweet, easygoing hounds that need extensive exercise and space. Very vocal."
        }
    },
    {
        "id": "ibizan-hound", "name": "Ibizan Hound",
        "group": "hound", "origin": "Spain (Ibiza)", "lifespan": "11-14 years",
        "size": {"height_cm": "56-74", "weight_kg": "20-29", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 1, "sociability": 3, "trainability": 3, "barking": 2, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Short or wire-haired", "coat_colors": ["red", "white", "red and white"], "shedding": "low", "hypoallergenic": False},
        "temperament": ["clownish", "family-oriented", "sensitive", "independent", "athletic"],
        "description": {
            "overview": "An ancient sighthound from the Balearic Islands, known for its deer-like elegance and jumping ability.",
            "temperament": "Playful and clownish at home, athletic outdoors. Sensitive and family-oriented.",
            "health": "Generally healthy. Watch for hip dysplasia and eye problems. Sensitive to anesthesia.",
            "exercise": "Needs daily running in a secure area. Exceptional jumpers—need high fences."
        },
        "verdict": {
            "best_for": ["Active families", "Those appreciating elegant, athletic dogs", "Experienced sighthound owners", "Homes with very high fences"],
            "not_for": ["Homes with small pets", "Those without secure fencing", "First-time sighthound owners"],
            "summary": "Elegant, athletic hounds that are clownish at home. Need secure, high fencing—amazing jumpers."
        }
    },
    {
        "id": "cirneco-delletna", "name": "Cirneco dell'Etna",
        "group": "hound", "origin": "Italy (Sicily)", "lifespan": "12-14 years",
        "size": {"height_cm": "42-52", "weight_kg": "8-12", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 1, "sociability": 3, "trainability": 3, "barking": 2, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Short, glossy", "coat_colors": ["tan", "chestnut"], "shedding": "low", "hypoallergenic": False},
        "temperament": ["affectionate", "friendly", "independent", "alert", "athletic"],
        "description": {
            "overview": "An ancient Sicilian sighthound bred to hunt rabbits on Mount Etna's volcanic slopes.",
            "temperament": "Affectionate with family, friendly but independent. Alert and athletic.",
            "health": "Very healthy breed with few genetic issues. Hardy constitution.",
            "exercise": "Moderate to high exercise needs. Loves to run but calmer than many sighthounds."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a healthier sighthound", "Apartment dwellers with exercise commitment", "Those wanting a unique breed"],
            "not_for": ["Homes with small pets", "Sedentary owners", "Those wanting an off-leash dog"],
            "summary": "A healthy, elegant Sicilian hound that's more manageable than larger sighthounds."
        }
    },
    
    # Working/Herding 131-150
    {
        "id": "giant-schnauzer", "name": "Giant Schnauzer",
        "group": "working", "origin": "Germany", "lifespan": "12-15 years",
        "size": {"height_cm": "60-70", "weight_kg": "25-48", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 4, "sociability": 3, "trainability": 4, "barking": 3, "kid_friendly": 3, "apartment_ok": 2},
        "characteristics": {"coat_type": "Dense, wiry, weather-resistant", "coat_colors": ["black", "salt and pepper"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["loyal", "intelligent", "bold", "territorial", "trainable"],
        "description": {
            "overview": "The largest Schnauzer, bred as a versatile working dog for guarding and driving cattle.",
            "temperament": "Loyal and protective with high intelligence. Needs firm, consistent leadership.",
            "health": "Prone to hip dysplasia, cancer, and autoimmune issues. Regular health screening important.",
            "exercise": "High energy requiring vigorous daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Experienced dog owners", "Those wanting a protective companion", "Active individuals", "Those committed to training"],
            "not_for": ["First-time owners", "Those unable to provide leadership", "Sedentary families"],
            "summary": "Impressive, loyal guardians requiring experienced handling and extensive exercise."
        }
    },
    {
        "id": "standard-schnauzer", "name": "Standard Schnauzer",
        "group": "working", "origin": "Germany", "lifespan": "13-16 years",
        "size": {"height_cm": "44-50", "weight_kg": "14-23", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 3, "sociability": 3, "trainability": 4, "barking": 3, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Wiry, tight-fitting", "coat_colors": ["black", "salt and pepper"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["spirited", "reliable", "intelligent", "playful", "protective"],
        "description": {
            "overview": "The original Schnauzer, a versatile German farm dog bred for guarding and ratting.",
            "temperament": "Spirited and reliable with a playful streak. Protective of family.",
            "health": "Generally healthy. Watch for hip dysplasia and eye problems.",
            "exercise": "Needs regular exercise and mental challenges. Versatile in dog sports."
        },
        "verdict": {
            "best_for": ["Active families", "Those wanting a versatile dog", "Experienced owners", "Those interested in dog sports"],
            "not_for": ["First-time owners", "Those wanting a laid-back dog", "Owners unable to groom regularly"],
            "summary": "Spirited, versatile dogs that excel at many activities. Need consistent training and grooming."
        }
    },
    {
        "id": "bouvier-des-flandres", "name": "Bouvier des Flandres",
        "group": "herding", "origin": "Belgium", "lifespan": "10-12 years",
        "size": {"height_cm": "59-68", "weight_kg": "27-40", "category": "large"},
        "ratings": {"size": 4, "energy": 3, "grooming": 4, "sociability": 3, "trainability": 4, "barking": 2, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Rough, tousled, double coat", "coat_colors": ["fawn to black", "brindle"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["loyal", "protective", "calm", "rational", "gentle"],
        "description": {
            "overview": "A powerful Belgian herding dog originally used for cattle driving and farm work.",
            "temperament": "Calm and rational with strong protective instincts. Gentle with family.",
            "health": "Prone to hip dysplasia and bloat. Generally healthy with proper care.",
            "exercise": "Moderate exercise needs. Enjoys work and activities but calm at home."
        },
        "verdict": {
            "best_for": ["Experienced dog owners", "Families wanting a calm protector", "Rural homes", "Those committed to grooming"],
            "not_for": ["First-time owners", "Those unwilling to groom", "Apartment dwellers"],
            "summary": "Calm, powerful guardians that are gentle with family. Need regular grooming."
        }
    },
    {
        "id": "old-english-sheepdog", "name": "Old English Sheepdog",
        "group": "herding", "origin": "England", "lifespan": "10-12 years",
        "size": {"height_cm": "54-61", "weight_kg": "27-45", "category": "large"},
        "ratings": {"size": 4, "energy": 3, "grooming": 5, "sociability": 5, "trainability": 3, "barking": 3, "kid_friendly": 5, "apartment_ok": 2},
        "characteristics": {"coat_type": "Profuse, shaggy", "coat_colors": ["gray and white", "blue and white"], "shedding": "high", "hypoallergenic": False},
        "temperament": ["adaptable", "gentle", "intelligent", "social", "playful"],
        "description": {
            "overview": "The iconic shaggy dog, originally bred to drive cattle to market in England.",
            "temperament": "Gentle and adaptable, great with children. Social and playful nature.",
            "health": "Prone to hip dysplasia, eye problems, and autoimmune diseases.",
            "exercise": "Moderate exercise needs. Enjoys playtime and walks but not hyperactive."
        },
        "verdict": {
            "best_for": ["Families with children", "Those committed to extensive grooming", "Those wanting a social, gentle dog"],
            "not_for": ["Those unable to groom extensively", "Hot climates", "Those wanting a low-maintenance dog"],
            "summary": "Iconic gentle giants great with kids. Require extensive grooming commitment."
        }
    },
    {
        "id": "polish-lowland-sheepdog", "name": "Polish Lowland Sheepdog",
        "group": "herding", "origin": "Poland", "lifespan": "12-14 years",
        "size": {"height_cm": "42-50", "weight_kg": "14-23", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 4, "sociability": 3, "trainability": 3, "barking": 3, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Long, thick, shaggy", "coat_colors": ["all colors"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["confident", "clever", "perceptive", "self-confident", "lively"],
        "description": {
            "overview": "A medium-sized Polish herding dog known as PON, with a shaggy coat and bright expression.",
            "temperament": "Confident and clever with excellent memory. Perceptive and independent.",
            "health": "Generally healthy. Watch for hip dysplasia and eye problems.",
            "exercise": "Moderate to high exercise needs. Enjoys herding activities and agility."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Those wanting a clever companion", "Active families", "Allergy sufferers"],
            "not_for": ["First-time owners", "Those wanting an easy-to-train dog", "Those unwilling to groom"],
            "summary": "Clever, confident herders that need mental stimulation. Good for allergy sufferers."
        }
    },
    {
        "id": "bergamasco-sheepdog", "name": "Bergamasco Sheepdog",
        "group": "herding", "origin": "Italy", "lifespan": "13-15 years",
        "size": {"height_cm": "54-62", "weight_kg": "26-38", "category": "large"},
        "ratings": {"size": 4, "energy": 3, "grooming": 2, "sociability": 4, "trainability": 3, "barking": 2, "kid_friendly": 5, "apartment_ok": 2},
        "characteristics": {"coat_type": "Felted mats (flocks)", "coat_colors": ["gray or gray merle"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["intelligent", "patient", "protective", "calm", "eager to please"],
        "description": {
            "overview": "An ancient Italian herder with a unique matted coat that forms naturally into 'flocks'.",
            "temperament": "Patient and intelligent with a calm demeanor. Excellent with children.",
            "health": "Very healthy breed with few genetic issues. Hardy constitution.",
            "exercise": "Moderate exercise needs. Enjoys outdoor activities but calm indoors."
        },
        "verdict": {
            "best_for": ["Families with children", "Those wanting a unique, healthy breed", "Patient owners", "Rural homes"],
            "not_for": ["Those preferring traditional grooming", "Hot climates", "Apartment dwellers"],
            "summary": "Unique, patient herders with distinctive coats. Great with kids, surprisingly easy to care for."
        }
    },
    {
        "id": "canaan-dog", "name": "Canaan Dog",
        "group": "herding", "origin": "Israel", "lifespan": "12-15 years",
        "size": {"height_cm": "48-61", "weight_kg": "16-25", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 2, "sociability": 2, "trainability": 3, "barking": 4, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Double coat, medium length", "coat_colors": ["sand to red-brown", "white", "black"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["alert", "vigilant", "devoted", "docile", "territorial"],
        "description": {
            "overview": "Israel's national dog, an ancient pariah dog breed used for herding and guarding.",
            "temperament": "Alert and territorial, devoted to family but reserved with strangers.",
            "health": "Very healthy breed with few genetic issues. Hardy and robust.",
            "exercise": "Moderate to high exercise needs. Versatile in many dog sports."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Those wanting a watchdog", "Active families", "Those interested in a natural breed"],
            "not_for": ["First-time owners", "Those wanting a social butterfly", "Multi-pet homes"],
            "summary": "Alert, healthy natural breed that bonds closely with family. Reserved with strangers."
        }
    },
    {
        "id": "icelandic-sheepdog", "name": "Icelandic Sheepdog",
        "group": "herding", "origin": "Iceland", "lifespan": "12-14 years",
        "size": {"height_cm": "42-46", "weight_kg": "9-14", "category": "medium"},
        "ratings": {"size": 2, "energy": 4, "grooming": 3, "sociability": 5, "trainability": 4, "barking": 4, "kid_friendly": 5, "apartment_ok": 3},
        "characteristics": {"coat_type": "Double coat, long or short", "coat_colors": ["various with white markings"], "shedding": "high", "hypoallergenic": False},
        "temperament": ["friendly", "inquisitive", "playful", "cheerful", "alert"],
        "description": {
            "overview": "Iceland's only native dog breed, a hardy spitz-type herder with a cheerful disposition.",
            "temperament": "Exceptionally friendly and cheerful. Loves everyone and is playful.",
            "health": "Generally healthy. Watch for hip dysplasia and eye problems.",
            "exercise": "Moderate to high exercise needs. Enjoys herding activities."
        },
        "verdict": {
            "best_for": ["Families with children", "Those wanting a friendly companion", "Active owners", "Those tolerant of barking"],
            "not_for": ["Those wanting a quiet dog", "Those disliking shedding", "Very hot climates"],
            "summary": "Cheerful, friendly herders that love everyone. Can be vocal and shed heavily."
        }
    },
    {
        "id": "swedish-vallhund", "name": "Swedish Vallhund",
        "group": "herding", "origin": "Sweden", "lifespan": "12-15 years",
        "size": {"height_cm": "30-35", "weight_kg": "9-14", "category": "small"},
        "ratings": {"size": 2, "energy": 4, "grooming": 2, "sociability": 4, "trainability": 4, "barking": 4, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Medium length, harsh", "coat_colors": ["gray", "red", "sable"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["friendly", "energetic", "watchful", "alert", "intelligent"],
        "description": {
            "overview": "An ancient Viking herding dog, similar to Corgis, known as the 'Swedish Cow Dog'.",
            "temperament": "Friendly and energetic with a watchful nature. Intelligent and eager to please.",
            "health": "Generally healthy. Watch for hip dysplasia and eye problems.",
            "exercise": "High energy needing daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Active families", "Those interested in dog sports", "Those wanting a compact herder", "Experienced dog owners"],
            "not_for": ["Sedentary owners", "Those wanting a quiet dog", "First-time herding breed owners"],
            "summary": "Viking herding dogs with big personalities in compact bodies. Active and vocal."
        }
    },
    {
        "id": "mudi", "name": "Mudi",
        "group": "herding", "origin": "Hungary", "lifespan": "12-14 years",
        "size": {"height_cm": "38-47", "weight_kg": "8-13", "category": "medium"},
        "ratings": {"size": 2, "energy": 5, "grooming": 2, "sociability": 3, "trainability": 5, "barking": 4, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Wavy to curly", "coat_colors": ["black", "white", "brown", "gray", "merle"], "shedding": "low", "hypoallergenic": False},
        "temperament": ["versatile", "intelligent", "alert", "active", "biddable"],
        "description": {
            "overview": "A rare Hungarian herding dog known for exceptional versatility and trainability.",
            "temperament": "Extremely versatile and intelligent. Alert and active, bonds strongly with owner.",
            "health": "Generally healthy breed with few genetic issues.",
            "exercise": "Very high energy requiring lots of exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Experienced owners wanting a versatile dog", "Active competitors in dog sports", "Those wanting an intelligent partner", "Rural homes"],
            "not_for": ["First-time owners", "Sedentary families", "Apartment living"],
            "summary": "Highly versatile Hungarian herders excelling at everything. Need experienced, active owners."
        }
    },
    {
        "id": "spanish-water-dog", "name": "Spanish Water Dog",
        "group": "working", "origin": "Spain", "lifespan": "12-14 years",
        "size": {"height_cm": "40-50", "weight_kg": "14-22", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 2, "sociability": 3, "trainability": 4, "barking": 3, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Curly, woolly (cords naturally)", "coat_colors": ["black", "brown", "white", "bicolor"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["loyal", "affectionate", "diligent", "athletic", "versatile"],
        "description": {
            "overview": "A rustic Spanish breed used for herding and water work, with a distinctive curly coat.",
            "temperament": "Loyal and affectionate with family. Diligent worker and versatile athlete.",
            "health": "Generally healthy. Watch for hip dysplasia and eye problems.",
            "exercise": "High energy requiring daily exercise. Loves water activities."
        },
        "verdict": {
            "best_for": ["Active families", "Water sports enthusiasts", "Allergy sufferers", "Those wanting a versatile dog"],
            "not_for": ["Sedentary owners", "Those wanting traditional grooming", "First-time owners"],
            "summary": "Versatile, athletic dogs that love water. Low-shedding coats but unique grooming needs."
        }
    },
    {
        "id": "lagotto-romagnolo", "name": "Lagotto Romagnolo",
        "group": "working", "origin": "Italy", "lifespan": "15-17 years",
        "size": {"height_cm": "41-48", "weight_kg": "11-16", "category": "medium"},
        "ratings": {"size": 3, "energy": 4, "grooming": 3, "sociability": 4, "trainability": 4, "barking": 2, "kid_friendly": 5, "apartment_ok": 3},
        "characteristics": {"coat_type": "Dense, curly, woolly", "coat_colors": ["off-white", "brown", "orange", "roan"], "shedding": "minimal", "hypoallergenic": True},
        "temperament": ["affectionate", "keen", "undemanding", "loyal", "trainable"],
        "description": {
            "overview": "An Italian water retriever now famous as the world's premier truffle-hunting dog.",
            "temperament": "Affectionate and loyal without being demanding. Keen worker, easy to train.",
            "health": "Generally healthy with good longevity. Watch for hip dysplasia.",
            "exercise": "Moderate to high exercise needs. Loves scent work and swimming."
        },
        "verdict": {
            "best_for": ["Families with children", "Allergy sufferers", "Those interested in scent work", "Active owners"],
            "not_for": ["Those wanting a guard dog", "Sedentary families", "Those disliking curly coats"],
            "summary": "Charming Italian truffle dogs that are wonderful family companions. Long-lived and hypoallergenic."
        }
    },
    {
        "id": "dutch-shepherd", "name": "Dutch Shepherd",
        "group": "herding", "origin": "Netherlands", "lifespan": "11-14 years",
        "size": {"height_cm": "55-62", "weight_kg": "23-32", "category": "large"},
        "ratings": {"size": 4, "energy": 5, "grooming": 2, "sociability": 3, "trainability": 5, "barking": 3, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Short, long, or wire-haired", "coat_colors": ["brindle (gold or silver)"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["reliable", "obedient", "alert", "faithful", "active"],
        "description": {
            "overview": "A versatile Dutch herding dog increasingly popular in police and military work.",
            "temperament": "Reliable and obedient with strong work drive. Faithful to family.",
            "health": "Generally healthy. Watch for hip dysplasia.",
            "exercise": "Very high energy requiring extensive daily exercise and work."
        },
        "verdict": {
            "best_for": ["Experienced working dog handlers", "Active families", "Those interested in dog sports", "Those wanting a versatile working dog"],
            "not_for": ["First-time owners", "Sedentary families", "Those unable to provide work"],
            "summary": "Versatile, reliable working dogs excelling in many fields. Need experienced handlers."
        }
    },
    {
        "id": "white-swiss-shepherd", "name": "White Swiss Shepherd",
        "group": "herding", "origin": "Switzerland", "lifespan": "12-14 years",
        "size": {"height_cm": "55-66", "weight_kg": "25-40", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 3, "sociability": 4, "trainability": 4, "barking": 3, "kid_friendly": 5, "apartment_ok": 2},
        "characteristics": {"coat_type": "Medium or long, double coat", "coat_colors": ["white"], "shedding": "high", "hypoallergenic": False},
        "temperament": ["gentle", "intelligent", "loyal", "alert", "eager to please"],
        "description": {
            "overview": "A white-coated cousin of the German Shepherd, known for a gentler temperament.",
            "temperament": "Gentler and less intense than German Shepherds. Loyal, intelligent, eager to please.",
            "health": "Prone to hip dysplasia and some digestive issues. Generally healthy.",
            "exercise": "High energy requiring daily exercise and mental stimulation."
        },
        "verdict": {
            "best_for": ["Families with children", "Those wanting a gentler shepherd", "Active owners", "Those committed to training"],
            "not_for": ["Those disliking heavy shedding", "Apartment dwellers", "Sedentary owners"],
            "summary": "Gentler white shepherds great for families. Need exercise and shed heavily."
        }
    },
    {
        "id": "chinook", "name": "Chinook",
        "group": "working", "origin": "United States", "lifespan": "12-15 years",
        "size": {"height_cm": "53-66", "weight_kg": "25-41", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 2, "sociability": 5, "trainability": 4, "barking": 2, "kid_friendly": 5, "apartment_ok": 2},
        "characteristics": {"coat_type": "Medium, double coat", "coat_colors": ["tawny"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["patient", "smart", "devoted", "gentle", "versatile"],
        "description": {
            "overview": "New Hampshire's state dog, bred for sled racing and known for gentle temperament.",
            "temperament": "Patient and gentle, excellent with children. Smart and devoted to family.",
            "health": "Generally healthy. Watch for hip dysplasia and seizures.",
            "exercise": "High energy needing regular exercise. Loves pulling and outdoor activities."
        },
        "verdict": {
            "best_for": ["Families with children", "Those wanting a gentle working dog", "Active outdoors families", "Those interested in mushing"],
            "not_for": ["Apartment dwellers", "Sedentary owners", "Hot climates"],
            "summary": "Gentle, devoted working dogs perfect for active families. Great with kids."
        }
    },
    {
        "id": "eurasier", "name": "Eurasier",
        "group": "working", "origin": "Germany", "lifespan": "12-16 years",
        "size": {"height_cm": "48-60", "weight_kg": "18-32", "category": "medium"},
        "ratings": {"size": 3, "energy": 3, "grooming": 3, "sociability": 2, "trainability": 3, "barking": 1, "kid_friendly": 4, "apartment_ok": 3},
        "characteristics": {"coat_type": "Medium length, double coat", "coat_colors": ["all colors except liver and white"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["calm", "confident", "reserved", "loyal", "even-tempered"],
        "description": {
            "overview": "A modern German breed combining Chow, Wolfspitz, and Samoyed, bred as a companion.",
            "temperament": "Calm and even-tempered, reserved with strangers but devoted to family.",
            "health": "Generally healthy. Watch for hip dysplasia and thyroid issues.",
            "exercise": "Moderate exercise needs. Calm indoors but enjoys outdoor activities."
        },
        "verdict": {
            "best_for": ["Quiet households", "Those wanting a calm companion", "Families with older children", "Experienced dog owners"],
            "not_for": ["Those wanting a social butterfly", "Highly active families", "First-time owners"],
            "summary": "Calm, dignified companions devoted to family. Reserved with strangers, quiet."
        }
    },
    {
        "id": "hovawart", "name": "Hovawart",
        "group": "working", "origin": "Germany", "lifespan": "10-14 years",
        "size": {"height_cm": "58-70", "weight_kg": "25-40", "category": "large"},
        "ratings": {"size": 4, "energy": 4, "grooming": 2, "sociability": 3, "trainability": 4, "barking": 3, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Long, wavy", "coat_colors": ["black and gold", "black", "blonde"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["devoted", "self-confident", "good-natured", "vigilant", "reserved"],
        "description": {
            "overview": "An ancient German estate guardian breed, revived in the 20th century.",
            "temperament": "Devoted and self-confident. Good-natured but vigilant guardian.",
            "health": "Generally healthy. Watch for hip dysplasia and thyroid issues.",
            "exercise": "High energy requiring regular exercise and activities."
        },
        "verdict": {
            "best_for": ["Experienced owners", "Families wanting a guardian", "Active homes", "Rural properties"],
            "not_for": ["First-time owners", "Apartment dwellers", "Those wanting immediate obedience"],
            "summary": "Loyal, self-confident guardians that mature slowly. Need patient, experienced owners."
        }
    },
    {
        "id": "landseer", "name": "Landseer",
        "group": "working", "origin": "Germany/Switzerland", "lifespan": "8-10 years",
        "size": {"height_cm": "67-80", "weight_kg": "50-70", "category": "giant"},
        "ratings": {"size": 5, "energy": 3, "grooming": 4, "sociability": 5, "trainability": 3, "barking": 2, "kid_friendly": 5, "apartment_ok": 1},
        "characteristics": {"coat_type": "Long, dense, slightly wavy", "coat_colors": ["white with black patches"], "shedding": "high", "hypoallergenic": False},
        "temperament": ["gentle", "generous", "serene", "patient", "sociable"],
        "description": {
            "overview": "A giant breed similar to Newfoundland, known for its distinctive black and white coat.",
            "temperament": "Exceptionally gentle and patient. Loves children and water. Serene disposition.",
            "health": "Prone to hip dysplasia, heart issues, and bloat. Shorter lifespan.",
            "exercise": "Moderate exercise needs. Loves swimming but not overly active."
        },
        "verdict": {
            "best_for": ["Families with children", "Those with pools or lake access", "Patient owners", "Those prepared for giant breed costs"],
            "not_for": ["Apartment dwellers", "Hot climates", "Those wanting a long-lived dog"],
            "summary": "Gentle giants exceptional with children and in water. Need space and acceptance of shorter lifespan."
        }
    },
    {
        "id": "greater-swiss-mountain-dog", "name": "Greater Swiss Mountain Dog",
        "group": "working", "origin": "Switzerland", "lifespan": "8-11 years",
        "size": {"height_cm": "60-72", "weight_kg": "45-64", "category": "giant"},
        "ratings": {"size": 5, "energy": 3, "grooming": 2, "sociability": 4, "trainability": 3, "barking": 3, "kid_friendly": 5, "apartment_ok": 1},
        "characteristics": {"coat_type": "Short, dense, double coat", "coat_colors": ["tricolor (black, red, white)"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["faithful", "dependable", "alert", "vigilant", "good-natured"],
        "description": {
            "overview": "The largest Swiss mountain dog, bred for draft work, herding, and guarding.",
            "temperament": "Faithful and dependable with a good-natured disposition. Alert watchdog.",
            "health": "Prone to hip dysplasia, bloat, and some eye issues. Shorter lifespan.",
            "exercise": "Moderate exercise needs. Enjoys activities but not overly demanding."
        },
        "verdict": {
            "best_for": ["Families with children", "Those wanting a faithful guardian", "Rural homes", "Those accepting shorter lifespan"],
            "not_for": ["Apartment dwellers", "Hot climates", "Budget-conscious owners"],
            "summary": "Faithful, dependable family dogs great with kids. Need space and have giant breed costs."
        }
    },
    {
        "id": "appenzeller-sennenhund", "name": "Appenzeller Sennenhund",
        "group": "working", "origin": "Switzerland", "lifespan": "12-15 years",
        "size": {"height_cm": "47-58", "weight_kg": "22-32", "category": "medium"},
        "ratings": {"size": 3, "energy": 5, "grooming": 2, "sociability": 3, "trainability": 4, "barking": 4, "kid_friendly": 4, "apartment_ok": 2},
        "characteristics": {"coat_type": "Short, thick, double coat", "coat_colors": ["tricolor (black, tan, white)", "Havana brown"], "shedding": "moderate", "hypoallergenic": False},
        "temperament": ["lively", "reliable", "fearless", "self-assured", "suspicious of strangers"],
        "description": {
            "overview": "A medium-sized Swiss mountain dog, the most energetic of the four Swiss breeds.",
            "temperament": "Lively and fearless with high energy. Reliable but suspicious of strangers.",
            "health": "Generally healthy breed. Watch for hip dysplasia.",
            "exercise": "Very high energy requiring extensive daily exercise and work."
        },
        "verdict": {
            "best_for": ["Very active families", "Those wanting a versatile working dog", "Experienced owners", "Rural homes"],
            "not_for": ["Sedentary families", "Apartment dwellers", "First-time owners"],
            "summary": "The athletic Swiss mountain dog—lively and hardworking. Need experienced, active owners."
        }
    },
]

# Page template (simplified)
PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="../favicon.ico" type="image/x-icon">
    <title>{name}: Breed Guide, Temperament & Care | BreedFinder</title>
    <meta name="description" content="Complete guide to the {name}: temperament, exercise needs, grooming, health issues, and whether this breed is right for you.">
    <link rel="canonical" href="https://breedfinder.org/breeds/{id}">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .rating-bar {{ background: #e2e8f0; position: relative; overflow: hidden; }}
        .rating-bar::after {{ content: ''; position: absolute; left: 0; top: 0; height: 100%; width: var(--rating); background: linear-gradient(90deg, #0ea5e9, #8b5cf6); border-radius: 9999px; }}
    </style>
</head>
<body class="bg-gradient-to-b from-slate-50 to-white min-h-screen text-slate-800">
    <header class="bg-white/80 backdrop-blur-md border-b border-slate-200/60 sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-4 py-4 flex items-center justify-between">
            <a href="../" class="flex items-center gap-3">
                <img src="../logo-192.png" class="w-10 h-10" alt="BreedFinder">
                <span class="text-xl font-bold">BreedFinder</span>
            </a>
            <nav class="flex items-center gap-6 text-sm font-medium">
                <a href="../quiz" class="text-slate-600 hover:text-sky-600">Breed Quiz</a>
            </nav>
        </div>
    </header>

    <main class="max-w-5xl mx-auto px-4 py-8">
        <nav class="text-sm text-slate-500 mb-6 flex items-center gap-2">
            <a href="../" class="hover:text-sky-600">Home</a>
            <i data-lucide="chevron-right" class="w-4 h-4"></i>
            <span class="text-slate-700 font-medium">{name}</span>
        </nav>

        <div class="bg-white rounded-3xl p-8 mb-8 shadow-sm border border-slate-100">
            <div class="flex flex-col md:flex-row gap-8">
                <div class="md:w-2/5">
                    <img src="../images/breeds/{id}.webp" alt="{name}" class="rounded-2xl w-full aspect-[4/5] object-cover border border-slate-200/50">
                </div>
                <div class="md:w-3/5">
                    <div class="flex items-center gap-2 mb-2">
                        <span class="bg-slate-100 text-slate-600 px-3 py-1 rounded-full text-sm">{group}</span>
                    </div>
                    <h1 class="text-4xl font-bold mb-3">{name}</h1>
                    <p class="text-slate-600 mb-6">{overview}</p>
                    
                    <div class="grid grid-cols-3 gap-4 mb-6">
                        <div class="text-center p-3 bg-slate-50 rounded-xl">
                            <div class="text-2xl mb-1">📏</div>
                            <div class="text-sm text-slate-500">Height</div>
                            <div class="font-semibold">{height} cm</div>
                        </div>
                        <div class="text-center p-3 bg-slate-50 rounded-xl">
                            <div class="text-2xl mb-1">⚖️</div>
                            <div class="text-sm text-slate-500">Weight</div>
                            <div class="font-semibold">{weight} kg</div>
                        </div>
                        <div class="text-center p-3 bg-slate-50 rounded-xl">
                            <div class="text-2xl mb-1">❤️</div>
                            <div class="text-sm text-slate-500">Lifespan</div>
                            <div class="font-semibold">{lifespan}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Ratings -->
        <div class="bg-white rounded-2xl p-6 mb-8 shadow-sm border border-slate-100">
            <h2 class="text-xl font-bold mb-4">Breed Ratings</h2>
            <div class="grid md:grid-cols-2 gap-4">
                {ratings_html}
            </div>
        </div>

        <!-- Temperament -->
        <div class="bg-white rounded-2xl p-6 mb-8 shadow-sm border border-slate-100">
            <h2 class="text-xl font-bold mb-4">Temperament</h2>
            <div class="flex flex-wrap gap-2">
                {temperament_html}
            </div>
            <p class="mt-4 text-slate-600">{temperament_desc}</p>
        </div>

        <!-- Health & Exercise -->
        <div class="grid md:grid-cols-2 gap-6 mb-8">
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
                <h2 class="text-xl font-bold mb-3">🏥 Health</h2>
                <p class="text-slate-600">{health}</p>
            </div>
            <div class="bg-white rounded-2xl p-6 shadow-sm border border-slate-100">
                <h2 class="text-xl font-bold mb-3">🏃 Exercise</h2>
                <p class="text-slate-600">{exercise}</p>
            </div>
        </div>

        <!-- Verdict -->
        <div class="bg-gradient-to-r from-sky-50 to-violet-50 rounded-2xl p-6 mb-8 border border-sky-100">
            <h2 class="text-xl font-bold mb-4">Is This Breed Right for You?</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <div>
                    <h3 class="font-semibold text-emerald-700 mb-2">✅ Best For</h3>
                    <ul class="space-y-1 text-slate-600">{best_for_html}</ul>
                </div>
                <div>
                    <h3 class="font-semibold text-rose-700 mb-2">❌ Not Ideal For</h3>
                    <ul class="space-y-1 text-slate-600">{not_for_html}</ul>
                </div>
            </div>
            <p class="mt-4 text-slate-700 font-medium">{summary}</p>
        </div>

        <div class="flex gap-4">
            <a href="../quiz" class="bg-sky-600 hover:bg-sky-700 text-white px-6 py-3 rounded-xl font-semibold">Take Breed Quiz</a>
            <a href="../compare" class="bg-slate-200 hover:bg-slate-300 px-6 py-3 rounded-xl font-semibold">Compare Breeds</a>
        </div>
    </main>

    <footer class="bg-slate-900 text-white py-8 px-4 mt-12">
        <div class="max-w-5xl mx-auto text-center text-slate-400 text-sm">
            <p>© 2026 BreedFinder</p>
        </div>
    </footer>
    <script>lucide.createIcons();</script>
</body>
</html>'''

def generate_page(breed):
    ratings = breed['ratings']
    rating_labels = {
        'energy': 'Energy Level',
        'grooming': 'Grooming Needs',
        'trainability': 'Trainability',
        'kid_friendly': 'Kid Friendly',
        'apartment_ok': 'Apartment Friendly',
        'barking': 'Barking Level',
        'sociability': 'Sociability'
    }
    
    ratings_html = ""
    for key, label in rating_labels.items():
        if key in ratings:
            val = ratings[key]
            pct = val * 20
            ratings_html += f'''<div>
                    <div class="flex justify-between text-sm mb-1"><span>{label}</span><span>{val}/5</span></div>
                    <div class="rating-bar h-2 rounded-full" style="--rating: {pct}%"></div>
                </div>\n'''
    
    temperament_html = "".join([f'<span class="bg-emerald-50 text-emerald-700 px-3 py-1 rounded-full text-sm">{t.title()}</span>' for t in breed['temperament']])
    
    best_for_html = "".join([f'<li>• {item}</li>' for item in breed['verdict']['best_for']])
    not_for_html = "".join([f'<li>• {item}</li>' for item in breed['verdict']['not_for']])
    
    return PAGE_TEMPLATE.format(
        id=breed['id'],
        name=breed['name'],
        group=breed['group'].title(),
        overview=breed['description']['overview'],
        height=breed['size']['height_cm'],
        weight=breed['size']['weight_kg'],
        lifespan=breed['lifespan'],
        ratings_html=ratings_html,
        temperament_html=temperament_html,
        temperament_desc=breed['description']['temperament'],
        health=breed['description']['health'],
        exercise=breed['description']['exercise'],
        best_for_html=best_for_html,
        not_for_html=not_for_html,
        summary=breed['verdict']['summary']
    )

# Generate pages
breeds_dir = os.path.expanduser("~/clawd/dog-breed-guide/breeds")
os.makedirs(breeds_dir, exist_ok=True)

for breed in NEW_BREEDS:
    html = generate_page(breed)
    filepath = os.path.join(breeds_dir, f"{breed['id']}.html")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ {breed['name']}")

print(f"\n🎉 Generated {len(NEW_BREEDS)} breed pages!")
