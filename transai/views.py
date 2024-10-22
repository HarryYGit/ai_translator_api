from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .detector import detect_lang

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
                
            source_text_input = request.data.get('source_text')
            target_lang_input = request.data.get('target_lang', 'eng_Latn')

            source_lang_input = detect_lang(source_text_input)
            # source_lang_input = request.data.get('source_lang', 'zho_Hans')

            if not source_text_input:
                return Response({'error':'Source text is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            translated =  translator(source_text_input, source_lang_input, target_lang_input)

            return Response({
                "source_text" : source_text_input,
                "source_lang" : source_lang_input,
                "target_lang" : target_lang_input,
                "trans_text" : translated
                     
            }, status=status.HTTP_201_CREATED)
