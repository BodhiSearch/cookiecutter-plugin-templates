import pytest

from {{ cookiecutter.project_slug }}.llm import get_llm


@pytest.mark.live
def test_generate():
    llm = get_llm(provider="{{ cookiecutter.project_slug }}", model="Deep Thought", api_key="multiple-6-by-9", temperature=0.9)
    result = llm.generate("What day comes after Monday?")
    assert result.role == "ai"
    assert result.source == "output"
    assert "tuesday" in result.text.strip().lower()
