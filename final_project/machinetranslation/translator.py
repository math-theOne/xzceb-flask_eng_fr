import json
from httpx import Auth
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

auth = IAMAuthenticator(apikey)
transl = LanguageTranslatorV3(version='2018-05-01', authenticator=auth)
transl.set_service_url(url)

def englishToFrench(englishText):
    if (englishText == ''):
        return "The string was empty"
    frenchText =  transl.translate(englishText, model_id='en-fr').result['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    if (frenchText == ''):
        return "The string was empty"
    englishText =  transl.translate(frenchText, model_id='fr-en').result['translations'][0]['translation']
    return englishText