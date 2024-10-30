from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Central",
            ciudad="Ciudad de México",
            pais="México"
        )

    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, "Laboratorio Central")
        self.assertEqual(self.laboratorio.ciudad, "Ciudad de México")
        self.assertEqual(self.laboratorio.pais, "México")

    def test_url_exists_at_correct_location(self):
        response = self.client.get('/insertar/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Actualizar los detalles del Laboratorio")

