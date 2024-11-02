from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from shop.models import Category

class TestCategory(APITestCase):
    url = reverse_lazy('category-list')

    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        # Créer des catégories de test
        category = Category.objects.create(
            name='Fruits',
            active=True,
            description=''  # Ajout du champ description
        )
        Category.objects.create(
            name='Legumes',
            active=False,
            description=''
        )

        # Faire la requête GET
        response = self.client.get(self.url)

        # Vérifier le status code
        self.assertEqual(response.status_code, 200)

        # Préparer les données attendues
        expected = [{
            'id': category.id,
            'name': category.name,
            'description': category.description,
            'active': category.active,
            'date_created': self.format_datetime(category.date_created),
            'date_updated': self.format_datetime(category.date_updated),
        }]

        # Comparer les résultats
        self.assertEqual(expected, response.json())

    def test_create(self):
        # Vérifier qu'aucune catégorie n'existe au début
        self.assertFalse(Category.objects.exists())

        # Tenter de créer une nouvelle catégorie
        response = self.client.post(self.url, data={'name': 'Nouvelle categorie'})

        # Vérifier le status code
        self.assertEqual(response.status_code, 405)

        # Vérifier qu'aucune catégorie n'a été créée
        self.assertFalse(Category.objects.exists())



