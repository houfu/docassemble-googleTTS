def get_text_to_speech(text_to_synthesize, voice, speaking_rate, pitch):
  from google.cloud import texttospeech
  import json
  from docassemble.base.util import get_config
  from oauth2client.service_account import ServiceAccountCredentials
  
  credential_info = json.loads(get_config('google').get('TTS service account'), strict=False)
  creds = ServiceAccountCredentials.from_json_keyfile_dict(credential_info)
  
  client = texttospeech.TextToSpeechClient(creds)
  
  input_text = texttospeech.SynthesisInput(text=text_to_synthesize)
  
  voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name=voice,
  )
  
  audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=speaking_rate,
    pitch=pitch,
  )
  
  response = client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config }
  )
  
  return response.audio_content
