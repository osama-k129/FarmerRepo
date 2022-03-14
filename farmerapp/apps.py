from django.apps import AppConfig


class FarmerappConfig(AppConfig):
    name = 'farmerapp'


    def ready(self):
        import farmerapp.mysignal