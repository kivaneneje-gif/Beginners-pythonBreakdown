def create_profile(**details):
    return details
profile = create_profile(
    name="John Doe", 
    age=30,
    occupation="Engineer",
    bio="Loves coding and outdoor activities.",
    hometown="San Francisco",
    sex="Male",
    height=180,
    weight=75,
    hobbies=["reading", "cycling", "traveling"],
    religion="None",
    marital_status="Single",
    )

print(profile)