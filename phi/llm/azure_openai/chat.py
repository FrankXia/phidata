from typing import Optional, Dict, Any, Callable
from phi.utils.log import logger
from phi.llm.openai.like import OpenAILike

try:
    from openai import AzureOpenAI as AzureOpenAIClient
except ImportError:
    logger.error("`azure openai` not installed")
    raise

AzureADTokenProvider = Callable[[], str]


class AzureOpenAIChat(OpenAILike):
    name: str = "AzureOpenAIChat"
    model: str = "esri-gpt4-dev"
    api_key: Optional[str] = None
    api_version: Optional[str] = None
    azure_endpoint: Optional[str] = None
    azure_deployment: Optional[str] = None
    base_url: Optional[str] = None
    azure_ad_token: Optional[str] = None
    azure_ad_token_provider: Optional[AzureADTokenProvider] = None
    openai_client: AzureOpenAIClient = None

    @property
    def client(self) -> AzureOpenAIClient:
        if self.openai_client:
            return self.openai_client

        _openai_params: Dict[str, Any] = {}
        if self.api_key:
            _openai_params["api_key"] = self.api_key
        if self.api_version:
            _openai_params["api_version"] = self.api_version
        if self.organization:
            _openai_params["organization"] = self.organization
        if self.azure_endpoint:
            _openai_params["azure_endpoint"] = self.azure_endpoint
        if self.azure_deployment:
            _openai_params["azure_deployment"] = self.azure_deployment
        if self.base_url:
            _openai_params["base_url"] = self.base_url
        if self.azure_ad_token:
            _openai_params["azure_ad_token"] = self.azure_ad_token
        if self.azure_ad_token_provider:
            _openai_params["azure_ad_token_provider"] = self.azure_ad_token_provider
        if self.client_kwargs:
            _openai_params.update(self.client_kwargs)

        return AzureOpenAIClient(**_openai_params)
