from .groq import Groq

services = {
    'openai': Groq,
    'openrouter': Groq,
    'anthropic': Groq,
    'togetherai': Groq,
    'mistralai': Groq,
    'groq': Groq,
    'perplexity': Groq,
    'gemini': Groq,
}

def get_service_class(service_name):
    return services.get(service_name)