# docassemble-googleTTS

A docassemble interview that performs text to speech with Google Cloud

## What you need

1. Install this interview 
2. Go to the Configuration and set the `tts account credentials` subdirective 
   under the `google` directive. 
   Set it to a service account. 
   ([See here for details](https://docassemble.org/docs/functions.html#google%20sheets%20example) 
   how to do it, but note the different subdirective.)
3. Run interview. Make your text talk!

## Limitations

* Only Wavenet US voices can be selected.