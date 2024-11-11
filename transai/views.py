from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .detector import detect_lang
from .convert_target_lang import convert_to_accept

from .audio_detect import AudioDetector

# Create your views here.
tokenizer_nllb = AutoTokenizer.from_pretrained('facebook/nllb-200-distilled-600M')
model_nllb = AutoModelForSeq2SeqLM.from_pretrained('facebook/nllb-200-distilled-600M')
translation_pipeline = pipeline('translation', model=model_nllb, tokenizer=tokenizer_nllb, max_length=200)

def translator(source, source_lang, target_lang):
    source_text = source
    source_lang = source_lang
    target_lang = target_lang

    output = translation_pipeline(source_text, src_lang=source_lang, tgt_lang=target_lang)[0]['translation_text']
    return output

def audiotext(audio_file):
    # Create an instance of the AudioDetect class
    audio_detector = AudioDetector()

    # Provide the path to the audio file
    audio_file_input = audio_file

    # Transcribe the audio file
    transcription = audio_detector.transcribe_audio(audio_file_input)

    # Print the transcription result
    print("Transcription:", transcription)
    return transcription
# class TestConnection(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         message = 'connection success'
#         return Response(message)

# defin api
@method_decorator(csrf_exempt, name='dispatch')
class TranslateView(GenericAPIView):
    # only authenticated user can access
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        user_lang = request.META.get('HTTP_ACCEPT_LANGUAGE')

        if user_lang:
            target_lang_from_request = user_lang.split(",")[0]
            print('Language header detected: ', target_lang_from_request)
            target_lang_input = convert_to_accept(target_lang_from_request)
            print('convert request lang to accept format: ', target_lang_input)

        else:
            print("language header not found")
            target_lang_input = request.data.get('target_lang', 'eng_Latn')
            print('target_lang set to input: ', target_lang_input)
        
        # Check if the request contains an audio file
        audio_file = request.FILES.get('audio')  # Assuming the field name is 'audio'

        if audio_file:
            # If an audio file is provided, use the AudioDetector class to get transcription
            print('Audio file detected, transcribing...')
            audio_detector = AudioDetector()
            source_text_input = audio_detector.transcribe_audio(audio_file)
            print(f"Transcription from audio: {source_text_input}")
        else:
            # If no audio file is provided, get the text from request data
            source_text_input = request.data.get('source_text')
            print(f"Source text from request: {source_text_input}")

        if not source_text_input:
            return Response({'error':'Source text is required'}, status=status.HTTP_400_BAD_REQUEST)
                  
        source_lang_input = detect_lang(source_text_input)

        print('detecting input lang...')
        print('detecting input lang...')
        print('detecting input lang...')
        print('input lang: ', source_lang_input)
        # source_lang_input = request.data.get('source_lang', 'zho_Hans')

        translated =  translator(source_text_input, source_lang_input, target_lang_input)
        print('translating result: ', translated)

        return Response({
            "source_text" : source_text_input,
            "source_lang" : source_lang_input,
            "target_lang" : target_lang_input,
            "trans_text" : translated
                     
        }, status=status.HTTP_201_CREATED)    


@method_decorator(csrf_exempt, name='dispatch')
class AdminView(GenericAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        output = audiotext("/Users/harryy/vscode/vue/untitled folder/untitled folder/trans_ai_api/trans_ai_api/transai/audiosamples/audio.mp3")

        return Response({
            "message" : "hi admin user",
            "output" : output
        }, status=status.HTTP_200_OK)
    

