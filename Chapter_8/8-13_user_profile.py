# Python Crash Course — original exercise solution
# Chapter exercise implementation; examples use Python 3.

def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

profile = build_profile("Favour", "Ajiri", location="Port Harcourt",
                        field="Mechatronics Engineering", learning="Python")
print(profile)
