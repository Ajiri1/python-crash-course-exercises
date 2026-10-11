"""Exercise 6-12: Extensions — extend the favorite-languages polling example."""
favorite_languages = {
    "jen": {"language": "python", "years": 4},
    "sarah": {"language": "c", "years": 2},
    "edward": {"language": "ruby", "years": 5},
    "phil": {"language": "python", "years": 3},
}

for name, details in favorite_languages.items():
    print(
        f"{name.title()} prefers {details['language'].title()} "
        f"and has studied it for {details['years']} year(s)."
    )
