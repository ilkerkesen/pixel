"""
    Register PIXEL models for the AutoClass interface.
    https://huggingface.co/docs/transformers/en/model_doc/auto
"""

from transformers import (
    AutoConfig,
    AutoModel,
    AutoModelForPreTraining,
    AutoModelForQuestionAnswering,
    AutoModelForSequenceClassification,
    AutoModelForTokenClassification,
)

from .models import (
    PIXELConfig,
    PIXELModel,
    PIXELForPreTraining,
    PIXELForQuestionAnswering,
    PIXELForSequenceClassification,
    PIXELForTokenClassification,
)


AutoConfig.register("pixel", PIXELConfig)
AutoModel.register(PIXELConfig, PIXELModel)
AutoModelForPreTraining.register(PIXELConfig, PIXELForPreTraining)
AutoModelForQuestionAnswering.register(PIXELConfig, PIXELForQuestionAnswering)
AutoModelForSequenceClassification.register(PIXELConfig, PIXELForSequenceClassification)
AutoModelForTokenClassification.register(PIXELConfig, PIXELForTokenClassification)