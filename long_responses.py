import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_HELP = "What can I help you with today!"
R_JOKE = "Why did the scarecrow win an award? Because he was outstanding in his field!"
R_GENDER = "I'm a bot and we don't have gender"
R_JPNCE = "JPNCE was established in the year 1997 by experienced academicians and industrialists. The college is continuously supported by a group of technocrats and is guided by renowned professors and administrators. The basic aim is not only to impart quality in technical education but also to follow the principles, morals, ethics, and ideals of “Bharatha Ratna” Sri Jaya Prakash Narayan, hence the college name. JPNCE is located in beautiful lush green environs surrounded by scenic mountains and is at an accessible distance from Hyderabad."

def unknown():
    responses = [
        "Could you please re-phrase that?",
        "...",
        "Sounds about right.",
        "What does that mean?",
    ]
    return random.choice(responses)
