# Offline speech recognition

Vosk-Browser 0.0.8: https://github.com/ccoreilly/vosk-browser (Apache-2.0).
Vosk speech recognition: https://github.com/alphacep/vosk-api (Apache-2.0).
English model: vosk-model-en-us-0.22-lgraph (Apache-2.0), copied from the supplied Clavis Android project's speech/english-model.zip and repackaged as model.tar.gz for Vosk-Browser.
Official model: https://alphacephei.com/vosk/models/vosk-model-en-us-0.22-lgraph.zip

Transcription runs on the computer. No microphone, API key or speech upload is used. Recognition can contain errors. Desktop recognition follows current playback rather than Android's text-ahead prefetch.

# Offline narration

sherpa-onnx 1.13.8: https://github.com/k2-fsa/sherpa-onnx (Apache-2.0).
KittenTTS v0.8 (kitten-micro-en): https://github.com/KittenML/KittenTTS (Apache-2.0), converted for sherpa-onnx; downloaded from the sherpa-onnx model releases on first use and verified by SHA-256.

Narration is synthesized on the computer and cached locally. The voice is downloaded once; no text is sent to a service.
