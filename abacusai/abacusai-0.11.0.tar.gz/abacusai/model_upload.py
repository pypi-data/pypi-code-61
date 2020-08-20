

class ModelUpload():
    '''

    '''

    def __init__(self, client, modelId=None, modelInstanceId=None, status=None, createdAt=None, modelUploadId=None, embeddingsUploadId=None, verificationsUploadId=None):
        self.client = client
        self.id = modelUploadId
        self.model_id = modelId
        self.model_instance_id = modelInstanceId
        self.status = status
        self.created_at = createdAt
        self.model_upload_id = modelUploadId
        self.embeddings_upload_id = embeddingsUploadId
        self.verifications_upload_id = verificationsUploadId

    def __repr__(self):
        return f"ModelUpload(model_id={repr(self.model_id)}, model_instance_id={repr(self.model_instance_id)}, status={repr(self.status)}, created_at={repr(self.created_at)}, model_upload_id={repr(self.model_upload_id)}, embeddings_upload_id={repr(self.embeddings_upload_id)}, verifications_upload_id={repr(self.verifications_upload_id)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'model_id': self.model_id, 'model_instance_id': self.model_instance_id, 'status': self.status, 'created_at': self.created_at, 'model_upload_id': self.model_upload_id, 'embeddings_upload_id': self.embeddings_upload_id, 'verifications_upload_id': self.verifications_upload_id}
