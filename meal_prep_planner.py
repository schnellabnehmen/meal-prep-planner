"""
Meal-Prep-Planer für gesundes Abnehmen 🥗

Dieses Open-Source-Tool hilft dir, Mahlzeiten für mehrere Tage zu planen 
und eine Einkaufsliste zu erstellen.

👉 Mehr Abnehm-Tipps findest du hier: https://www.schnellabnehmen.at
"""
import random

# Beispielrezepte für verschiedene Mahlzeiten
recipes = {
    "Frühstück": [
        {"name": "Haferflocken mit Beeren", "zutaten": ["Haferflocken", "Beeren", "Milch"]},
        {"name": "Rührei mit Gemüse", "zutaten": ["Eier", "Paprika", "Tomaten"]},
        {"name": "Griechischer Joghurt mit Nüssen", "zutaten": ["Joghurt", "Honig", "Nüsse"]}
    ],
    "Mittagessen": [
        {"name": "Hähnchen mit Brokkoli und Reis", "zutaten": ["Hähnchenbrust", "Brokkoli", "Reis"]},
        {"name": "Linsensuppe", "zutaten": ["Linsen", "Karotten", "Zwiebeln"]},
        {"name": "Salat mit Thunfisch", "zutaten": ["Blattsalat", "Thunfisch", "Olivenöl"]}
    ],
    "Abendessen": [
        {"name": "Gegrillter Lachs mit Gemüse", "zutaten": ["Lachs", "Zucchini", "Spargel"]},
        {"name": "Quinoa-Bowl mit Avocado", "zutaten": ["Quinoa", "Avocado", "Tomaten"]},
        {"name": "Omelette mit Spinat", "zutaten": ["Eier", "Spinat", "Käse"]}
    ],
    "Snacks": [
        {"name": "Mandelbutter mit Apfelscheiben", "zutaten": ["Mandeln", "Apfel"]},
        {"name": "Hüttenkäse mit Gurken", "zutaten": ["Hüttenkäse", "Gurke"]},
        {"name": "Proteinriegel", "zutaten": ["Haferflocken", "Proteinpulver", "Erdnussbutter"]}
    ]
}

def generate_meal_prep_plan(days):
    meal_plan = []
    shopping_list = {}
    
    for day in range(1, days + 1):
        day_plan = {"Tag": day}
        for meal_type, meal_options in recipes.items():
            meal = random.choice(meal_options)
            day_plan[meal_type] = meal["name"]
            for zutat in meal["zutaten"]:
                shopping_list[zutat] = shopping_list.get(zutat, 0) + 1
        meal_plan.append(day_plan)
    
    return meal_plan, shopping_list

def main():
    print("Willkommen beim Meal-Prep-Planer!\n")
    try:
        days = int(input("Für wie viele Tage möchtest du einen Plan erstellen? "))
        if days <= 0:
            print("Bitte gib eine gültige Anzahl von Tagen ein.")
            return
    
        plan, einkaufsliste = generate_meal_prep_plan(days)
        
        print("\nDein Meal-Prep-Plan:")
        for day in plan:
            print(f"\nTag {day['Tag']}: ")
            for key, value in day.items():
                if key != "Tag":
                    print(f"  {key}: {value}")
        
        print("\nEinkaufsliste:")
        for item, count in einkaufsliste.items():
            print(f"- {item}: {count}")
        
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")

if __name__ == "__main__":
    main()
