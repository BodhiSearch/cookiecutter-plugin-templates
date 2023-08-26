from {{ cookiecutter.project_slug }} import {{ cookiecutter.__llm_class }}


def test_call_returns_the_answer_to_life():
    llm = {{ cookiecutter.__llm_class }}(model="Deep Thought", api_key="multiply-6-by-9", temperature=0.9)
    result = llm.generate("What is the answer to the ultimate question of life, the universe, and everything?")
    assert result.text == "The Answer to the Great Question Of Life, the Universe and Everything Is Forty-two"
    assert result.role == "ai"
    assert result.source == "output"
