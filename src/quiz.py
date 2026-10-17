QUESTIONS = [
    {"question":"A robot stops working. What would you do first?","options":["Check clues step by step","Redesign its look","Ask how it affects people","Explore the environment around it"],"correct":0},
    {"question":"Which challenge sounds most exciting?","options":["Find patterns in data","Create a character or poster","Explain a discovery to others","Build something with moving parts"],"correct":0},
    {"question":"A team has several possible ideas. How should it choose?","options":["Compare evidence and test ideas","Choose the most colourful one","Choose without checking","Avoid trying anything new"],"correct":0},
    {"question":"A good way to test a prediction is to…","options":["Compare it with data not used to build it","Show only the best-looking chart","Assume it must be correct","Hide errors"],"correct":0},
    {"question":"What should a responsible AI system do when uncertain?","options":["Explain uncertainty and limitations","Pretend to know the answer","Invent missing facts","Promise a perfect result"],"correct":0}
]

def score_quiz(answers):
    score = sum(1 for i,q in enumerate(QUESTIONS) if answers.get(i)==q["options"][q["correct"]])
    if score >= 4:
        return score, {"title":"🔭 Future Explorer","message":"You think carefully about evidence and testing. Keep asking questions and exploring new ideas!"}
    if score >= 2:
        return score, {"title":"🧩 Curious Thinker","message":"You are building your investigation skills. Compare evidence, test ideas, and learn from mistakes."}
    return score, {"title":"🌱 Idea Starter","message":"Every expert starts by asking questions. Keep exploring, testing, and learning!"}
