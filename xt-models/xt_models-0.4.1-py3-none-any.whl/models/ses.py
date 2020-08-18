import torch
import torch.nn as nn
from torch.nn import BCEWithLogitsLoss
from transformers import BertPreTrainedModel, BertModel

class BertForSES(BertPreTrainedModel):
    """BERT model for span extraction.
    This module is composed of the BERT model with a (multiple) linear(s) layer on top of
    the sequence output that computes start_logits and end_logits for all ans_types
    Params:
        `config`: a BertConfig class instance with the configuration to build a new model.
    Inputs:
        `input_ids`: a torch.LongTensor of shape [batch_size, sequence_length]
            with the word token indices in the vocabulary(see the tokens preprocessing logic in the scripts
            `extract_features.py`, `run_classifier.py` and `run_squad.py`)
        `token_type_ids`: an optional torch.LongTensor of shape [batch_size, sequence_length] with the token
            types indices selected in [0, 1]. Type 0 corresponds to a `sentence A` and type 1 corresponds to
            a `sentence B` token (see BERT paper for more details).
        `attention_mask`: an optional torch.LongTensor of shape [batch_size, sequence_length] with indices
            selected in [0, 1]. It's a mask to be used if the input sequence length is smaller than the max
            input sequence length in the current batch. It's the mask that we typically use for attention when
            a batch has varying length sentences.
        `start_positions`: 
            sparse vector of size (batch_size * max_sequence_length * num_ans_types))
            a '1.0' is where all start logits are. '0' elsewhere
        `end_positions`: 
            sparse vector of size (batch_size * max_sequence_length * num_ans_types))
             a '1.0' is where all end logits are. '0' elsewhere  
    Outputs:
        'start_logits': 
            a list (len of ans_types) of tensors. Each tensor is (batch_size * max_sequence_length * 1)
        'end_logits':
            a list (len of ans_types) of tensors. Each tensor is (batch_size * max_sequence_length * 1)
    """
    def __init__(self, config, num_ans_types):
        super().__init__(config)
        self.bert = BertModel(config)
        # self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.num_classes = num_ans_types
        self.qa_outputs = nn.Linear(config.hidden_size, 2*num_ans_types) # 2 For start/end positions
        self.init_weights()

    def forward(self, x):

        input_ids, attention_mask, token_type_ids = x

        outputs = self.bert(input_ids, token_type_ids, attention_mask)
        sequence_output = outputs[0]
        logits = self.qa_outputs(sequence_output)
        start_logits, end_logits = logits.reshape(logits.shape[0], logits.shape[1], self.num_classes, 2).split(1, dim=-1)
        start_logits = start_logits.squeeze(-1)
        end_logits = end_logits.squeeze(-1)
        outputs = (start_logits, end_logits,)

        return outputs