CAREERS = {
    "AI & Machine Learning Engineer": {"icon":"🤖","subjects":["Maths","Computers","Science"],"activities":["Solving puzzles","Building apps","Finding patterns in data"],"strengths":["Logical thinking","Research"],"why":"You enjoy patterns, logic, and technology.","first_step":"Learn Python and build a tiny prediction model.","skills":["Python","Statistics","Machine learning","Problem solving"],"base_scenario":112,"tech_weight":1.2,"automation_weight":0.4},
    "Data Scientist": {"icon":"📊","subjects":["Maths","Computers","Business"],"activities":["Finding patterns in data","Solving puzzles","Exploring nature"],"strengths":["Logical thinking","Research","Attention to detail"],"why":"You may enjoy turning data into useful explanations.","first_step":"Explore a small dataset and make three charts.","skills":["Python","Statistics","SQL","Data storytelling"],"base_scenario":108,"tech_weight":0.9,"automation_weight":0.3},
    "Software Developer": {"icon":"💻","subjects":["Computers","Maths"],"activities":["Building apps","Solving puzzles"],"strengths":["Logical thinking","Teamwork"],"why":"You like building things and solving problems.","first_step":"Create a small website or Python utility.","skills":["Programming","Debugging","Git","Software design"],"base_scenario":106,"tech_weight":0.8,"automation_weight":0.5},
    "Cybersecurity Analyst": {"icon":"🛡️","subjects":["Computers","Maths","Science"],"activities":["Investigating security","Solving puzzles"],"strengths":["Attention to detail","Logical thinking","Research"],"why":"You may enjoy investigation, systems, and protecting information.","first_step":"Learn networking basics and practise in a legal cyber lab.","skills":["Networking","Linux","Security basics","Scripting"],"base_scenario":110,"tech_weight":0.9,"automation_weight":0.2},
    "Robotics Engineer": {"icon":"🦾","subjects":["Maths","Science","Computers"],"activities":["Building machines","Solving puzzles"],"strengths":["Logical thinking","Creativity","Research"],"why":"You enjoy combining software with physical systems.","first_step":"Try a simple simulator or beginner microcontroller project.","skills":["Electronics","Programming","Control systems","Maths"],"base_scenario":105,"tech_weight":1.0,"automation_weight":0.4},
    "Game Developer": {"icon":"🎮","subjects":["Computers","Maths","Art & Design"],"activities":["Building apps","Designing visuals","Solving puzzles"],"strengths":["Creativity","Logical thinking"],"why":"You may enjoy interactive worlds and technical creativity.","first_step":"Build a tiny 2D game with a score counter.","skills":["Programming","Game design","2D/3D assets","Debugging"],"base_scenario":103,"tech_weight":0.7,"automation_weight":0.6},
    "Doctor / Health Technology": {"icon":"🩺","subjects":["Biology","Science"],"activities":["Helping people","Exploring nature"],"strengths":["Communication","Attention to detail","Teamwork"],"why":"You may be interested in health, biology, and helping people.","first_step":"Explore biology and learn how health technology supports clinicians.","skills":["Biology","Communication","Research","Ethics"],"base_scenario":107,"tech_weight":0.6,"automation_weight":0.2},
    "Environmental Scientist": {"icon":"🌱","subjects":["Environment","Science","Maths"],"activities":["Exploring nature","Finding patterns in data"],"strengths":["Research","Logical thinking"],"why":"You may enjoy understanding ecosystems and environmental problems.","first_step":"Collect local observations and visualize them responsibly.","skills":["Environmental science","Statistics","GIS","Communication"],"base_scenario":104,"tech_weight":0.7,"automation_weight":0.2},
    "Space Scientist": {"icon":"🪐","subjects":["Maths","Science","Computers"],"activities":["Solving puzzles","Finding patterns in data","Exploring nature"],"strengths":["Research","Logical thinking"],"why":"You may enjoy scientific questions about space and the universe.","first_step":"Explore astronomy data and learn basic Python plotting.","skills":["Physics","Maths","Programming","Scientific method"],"base_scenario":102,"tech_weight":0.7,"automation_weight":0.2},
    "Renewable Energy Engineer": {"icon":"☀️","subjects":["Maths","Science","Environment"],"activities":["Building machines","Exploring nature"],"strengths":["Research","Logical thinking","Teamwork"],"why":"You may like engineering solutions for cleaner energy.","first_step":"Compare solar output at different times using sample data.","skills":["Electrical basics","Energy systems","Data analysis","Design"],"base_scenario":106,"tech_weight":0.8,"automation_weight":0.3},
    "UI/UX Designer": {"icon":"🎨","subjects":["Art & Design","Computers","Writing & Communication"],"activities":["Designing visuals","Helping people","Building apps"],"strengths":["Creativity","Communication","Teamwork"],"why":"You may enjoy making technology easier and more pleasant to use.","first_step":"Redesign one app screen and ask someone to test it.","skills":["User research","Wireframing","Prototyping","Accessibility"],"base_scenario":101,"tech_weight":0.6,"automation_weight":0.6},
    "Digital Marketing Analyst": {"icon":"📣","subjects":["Business","Maths","Writing & Communication"],"activities":["Finding patterns in data","Designing visuals"],"strengths":["Communication","Creativity","Logical thinking"],"why":"You may enjoy combining communication, experiments, and data.","first_step":"Analyse a sample campaign dataset and compare click rates.","skills":["Analytics","Communication","Experiment design","Spreadsheets"],"base_scenario":103,"tech_weight":0.6,"automation_weight":0.7}
}

def recommend_careers(subjects, activities, strengths, comfort=3):
    selected = set(subjects or []) | set(activities or []) | set(strengths or [])
    results = []
    for name, info in CAREERS.items():
        features = set(info["subjects"] + info["activities"] + info["strengths"])
        overlap = len(selected & features)
        raw = 35 + (overlap / max(1, len(features))) * 55
        if "Maths" in info["subjects"] or "Computers" in info["subjects"]:
            raw += (comfort - 3) * 2
        match = int(max(25, min(96, round(raw))))
        why = info["why"]
        if overlap:
            why += " Your answers overlap with " + ", ".join(sorted(selected & features)[:3]) + "."
        results.append({"career":name,"icon":info["icon"],"match":match,"why":why,"first_step":info["first_step"]})
    return sorted(results, key=lambda x:x["match"], reverse=True)

def career_demand_history(career):
    # Synthetic demonstration values only; replace with verified data before factual claims.
    base = CAREERS[career]["base_scenario"]
    return [round(base*x, 1) for x in [0.70,0.73,0.75,0.79,0.82,0.84,0.88,0.91,0.95,1.00]]
