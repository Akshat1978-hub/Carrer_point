from src.forecasting import forecast_demand
from src.careers import recommend_careers, CAREERS
from src.quiz import QUESTIONS, score_quiz

def test_forecast_length():
    assert len(forecast_demand([10, 11, 12, 13], 3)["forecast"]) == 3

def test_forecast_invalid_horizon():
    try:
        forecast_demand([10, 11], 4)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_recommender_returns_careers():
    results = recommend_careers(["Computers"], ["Building apps"], ["Logical thinking"], 4)
    assert results and results[0]["career"] in CAREERS

def test_quiz_perfect_score():
    answers = {i:q["options"][q["correct"]] for i,q in enumerate(QUESTIONS)}
    assert score_quiz(answers)[0] == len(QUESTIONS)
