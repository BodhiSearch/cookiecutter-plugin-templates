"""LLM implementation for {{ cookiecutter.project_name }}."""
from typing import Any, Dict, Optional

from bodhilib.llm import LLM
from bodhilib.logging import logger
from bodhilib.models import Prompt, PromptInput, parse_prompts, prompt_output


class {{ cookiecutter.__llm_class }}(LLM):
    """{{ cookiecutter.project_name }} LLM Service implementation."""

    def __init__(self, model: Optional[str] = None, api_key: Optional[str] = None, **kwargs: Dict[str, Any]) -> None:
        """Initialize the LLM service.

        Args:
            model: model name to use for the LLM service
            api_key: API key to use for the LLM service
            kwargs: additional configs to pass to the LLM service
        """
        self.model = model
        self.api_key = api_key
        self.kwargs = kwargs

    def generate(self, prompts: PromptInput, **kwargs: Dict[str, Any]) -> Prompt:
        """Generate a response to the given prompt.

        Args:
            prompts: input prompt(s) to LLM to generate a reply
            kwargs: additional configs to pass to the LLM
        Returns:
            Prompt: generated response from the LLM service
        """
        parsed_prompts = parse_prompts(prompts)
        single_prompt = "\n".join([p.text for p in parsed_prompts])
        logger.info(f"Received prompt: {single_prompt}")
        return prompt_output("The Answer to the Great Question Of Life, the Universe and Everything Is Forty-two")
