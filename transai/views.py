from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline



# Create your views here.

# init translation model
# Initialize translation model once
tokenizer_nllb = AutoTokenizer.from_pretrained('facebook/nllb-200-distilled-600M')
model_nllb = AutoModelForSeq2SeqLM.from_pretrained('facebook/nllb-200-distilled-600M')
translation_pipeline = pipeline('translation', model=model_nllb, tokenizer=tokenizer_nllb, max_length=200)

# defin api
class TranslateView(APIView):

    def post(self, request):
        source_text = request.data.get('source_text')
        source_lang = request.data.get('source_lang', 'zho_Hans')
        target_lang = request.data.get('target_lang', 'eng_Latn')

        if not source_text:
            return Response({'error':'Source text is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        translated = translation_pipeline(source_text, src_lang=source_lang, tgt_lang=target_lang)[0]['translation_text']

        return Response({

            'source_text': source_text,
            'translated_text': translated,
        }, status=status.HTTP_201_CREATED)