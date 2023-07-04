from django.db import models
sex = (
    ('ayol','ayol'),
    ('erkak','erkak')
)
class IELTS(models.Model):
    image = models.ImageField(upload_to='img')
    candidate_id = models.IntegerField()
    date = models.DateField()
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=200 , choices=sex)
    rigion_address = models.CharField(max_length=200)
    nationally = models.CharField(max_length=200)
    first_language = models.CharField(max_length=200)
    speaking = models.FloatField()
    writeng = models.FloatField()
    reading = models.FloatField()
    listening = models.FloatField()
    admission = models.TextField(null=True,blank=True)
    test_number = models.IntegerField()
    date_number = models.IntegerField()

    def __str__(self):
        return f"{self.image} | {self.candidate_id} | {self.date} | {self.last_name} | {self.first_name} | {self.date_of_birth} | " \
               f"{self.rigion_address} | {self.nationally} | {self.first_language} | {self.speaking} | {self.writeng} | {self.reading} | " \
               f"{self.listening} | {self.admission} | {self.test_number} | {self.date_number}"


    class Meta:
        verbose_name = "IELTS"
        verbose_name_plural = 'IELTS'
