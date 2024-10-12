from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import serializers
from rest_framework.generics import GenericAPIView

from .models import TransData

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

from rest_framework.permissions import IsAuthenticated

# Create your views here.

# init translation model
# Initialize translation model once
tokenizer_nllb = AutoTokenizer.from_pretrained('facebook/nllb-200-distilled-600M')
model_nllb = AutoModelForSeq2SeqLM.from_pretrained('facebook/nllb-200-distilled-600M')
translation_pipeline = pipeline('translation', model=model_nllb, tokenizer=tokenizer_nllb, max_length=200)

def translator(source, source_lang, target_lang):
    source_text = source
    source_lang = source_lang
    target_lang = target_lang

    output = translation_pipeline(source_text, src_lang=source_lang, tgt_lang=target_lang)[0]['translation_text']

    return output
    
class TransaiSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransData
        fields = "__all__"

# defin api
class TranslateView(GenericAPIView):
    queryset = TransData.objects.all()
    serializer_class = TransaiSerializers

    # only authenticated user can access
    permission_classes = [IsAuthenticated]


    def get(self, request):

        serializer = self.get_serializer(instance=self.get_queryset(), many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = self.get_serializer(data = request.data)

        if serializer.is_valid():
                source_text_input = serializer.validated_data.get('source_text')
                source_lang_input = request.data.get('source_lang', 'zho_Hans')
                target_lang_input = request.data.get('target_lang', 'eng_Latn')

                if not source_text_input:
                    return Response({'error':'Source text is required'}, status=status.HTTP_400_BAD_REQUEST)
        
                translated =  translator(source_text_input, source_lang_input, target_lang_input)

                trans_data = TransData.objects.create(
                     
                     source_text = source_text_input,
                     source_lang = source_lang_input,
                     target_lang = target_lang_input,
                     trans_text = translated
                )

                response_serializer = self.get_serializer(trans_data)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                

