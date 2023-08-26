import pytest

from bodhilib.llm import get_llm


@pytest.mark.live
def test_generate():
    llm = get_llm(service_name="{{ cookiecutter.__service_name }}", model="Deep Thought", api_key="multiple-6-by-9", temperature=0.9)
    result = llm.generate("What day comes after Monday?")
    assert result.role == "ai"
    assert result.source == "output"
    assert "forty-two" in result.text.strip().lower()
