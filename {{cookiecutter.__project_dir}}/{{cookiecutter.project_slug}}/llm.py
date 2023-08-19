from typing import Any, Dict
import bodhisearch
from bodhisearch import Provider, LLM, logger
from bodhisearch.prompt import Prompt, PromptInput, parse_prompts, prompt_output


@bodhisearch.provider
def bodhisearch_get_providers():
    return [Provider(provider="{{ cookiecutter.project_slug }}", author="{{ cookiecutter.github_username | default('author-here') }}", type="llm", func=get_llm, version="{{ cookiecutter.version }}")]


def get_llm(provider: str, model: str, api_key: str = "", **kwargs: Dict[str, Any]) -> LLM:
    return {{ cookiecutter.__llm_class }}(model=model, api_key=api_key, **kwargs)


class {{ cookiecutter.__llm_class }}(LLM):
    def __init__(self, model: str, api_key: str, **kwargs: Dict[str, Any]) -> None:
        self.model = model
        self.api_key = api_key
        self.kwargs = kwargs

    def generate(self, prompts: PromptInput, **kwargs: Dict[str, Any]) -> Prompt:
        parsed_prompts = parse_prompts(prompts)
        single_prompt = "\n".join([p.text for p in parsed_prompts])
        logger.info(f"Received prompt: {single_prompt}")
        return prompt_output("The Answer to the Great Question Of Life, the Universe and Everything Is Forty-two")
