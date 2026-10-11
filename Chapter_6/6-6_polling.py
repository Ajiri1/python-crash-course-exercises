"""Exercise 6-6: Polling — thank people who responded and invite others."""
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
people_to_poll = ["jen", "mike", "sarah", "anna", "phil", "chidi"]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"{person.title()}, thank you for responding to the poll.")
    else:
        print(f"{person.title()}, please take our favorite-language poll.")
