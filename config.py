from dataclasses import dataclass
import os

@dataclass
class openai_config:
    api_key:str
    organization:str
    language:str = 'python'
    model:str = "gpt-3.5-turbo-0301"

    @classmethod
    def from_file(cls, language = 'python'):
        assert os.path.exists('openai_config')
        with open('openai_config') as f:
            kwargs = {}
            for line in f.readlines():
                texts = [text.strip() for text in line.split("=")]
                if texts[0] == 'organization':
                    kwargs['organization'] = texts[1]
                elif texts[0] == 'api_key':
                    kwargs['api_key'] = texts[1]
        kwargs['language'] = language
        return cls(**kwargs)
