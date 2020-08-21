class CheckServiceResult():
    def __init__(self, model):
        self.__user_has_Certificates = model.get("userHasCertificates", None)

    def get_user_has_Certificates(self):
        return self.__user_has_Certificates

    def set_user_has_Certificates(self, user_has_Certificates):
        self.__user_has_Certificates = user_has_Certificates

    user_has_Certificates = property(get_user_has_Certificates, set_user_has_Certificates)


__all__ = [
    'CheckServiceResult'
]