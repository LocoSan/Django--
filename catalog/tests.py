from django.test import SimpleTestCase
from django.urls import reverse


class CatalogTests(SimpleTestCase):
    def setUp(self):
        self.url = reverse("catalog")

    def test_catalog_shows_items_and_form(self):
        response = self.client.get(self.url)
        self.assertContains(response, "Льняная рубашка")
        self.assertContains(response, 'name="style"')
        self.assertContains(response, 'name="size"')

    def test_preferences_are_saved_and_used_on_next_visit(self):
        response = self.client.post(self.url, {"style": "sport", "size": "M"})
        self.assertRedirects(response, self.url)
        self.assertEqual(response.cookies["style"].value, "sport")
        self.assertEqual(response.cookies["size"].value, "M")
        next_page = self.client.get(self.url)
        self.assertContains(next_page, "Спортивная футболка")
        self.assertNotContains(next_page, "Льняная рубашка")
        self.assertEqual(next_page.context["form"]["size"].value(), "M")

    def test_invalid_preferences_are_not_saved(self):
        response = self.client.post(self.url, {"style": "unknown", "size": "42"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("style", response.context["form"].errors)
        self.assertIn("size", response.context["form"].errors)
        self.assertNotIn("style", response.cookies)

    def test_reset_returns_the_full_catalog(self):
        self.client.post(self.url, {"style": "sport", "size": "M"})
        response = self.client.post(reverse("reset"))
        self.assertRedirects(response, self.url)
        self.assertEqual(response.cookies["style"]["max-age"], 0)
        page = self.client.get(self.url)
        self.assertContains(page, "Льняная рубашка")
        self.assertContains(page, "Спортивная футболка")
