from django.test import TestCase
from movies.models import Villans, Categories

class TestModels(TestCase):

    def setUp(self):
        self.categories = Categories(category="Superhuman")
        self.categories.save()


    def test_Categores_model(self):

        self.assertEquals(1,Categories.objects.count())

    def test_Categories_can_save(self):


        result = Categories.objects.all()
        self.assertIsInstance(self.categories,Categories)
        self.assertEquals(len(result),1)
        self.assertEquals("Superhuman",result.first().category)


    def test_Villans_model_saves(self  ):

        villan = Villans(name="destroyer", category=self.categories)
        villan.save()
        result = Villans.objects.all()
        self.assertIsInstance(villan, Villans)
        self.assertEquals(len(result), 1)
        self.assertEquals("destroyer", result.first().name)
