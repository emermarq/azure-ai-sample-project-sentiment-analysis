from gtts import gTTS

text = """
Azure AI is a comprehensive suite of artificial intelligence services offered by Microsoft through its Azure cloud platform.
It enables developers and organizations to build intelligent applications with powerful tools like Azure OpenAI, Cognitive Services, and Azure Machine Learning.
These services support tasks such as natural language processing, computer vision, and predictive analytics.
Azure AI is scalable, secure, and designed to integrate easily with existing systems.
With its robust infrastructure, companies can streamline operations, gain insights from data, and enhance customer experiences.
Azure AI empowers innovation by providing accessible, enterprise-grade AI solutions for businesses of all sizes across various industries.
"""

tts = gTTS(text)
tts.save("azure_ai.mp3")