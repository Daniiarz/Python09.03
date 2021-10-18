import tempfile
from math import sqrt

from django.test import TestCase

from blog.models import Blog


def a_b(a, b):
    return a + b + sqrt(a * b)


class ABTestCase(TestCase):

    def test_a_b_return_value(self):
        a, b = 2, 2
        expected_result = 6
        test_result = a_b(a, b)
        self.assertEqual(expected_result, test_result)
        self.assertIn(2, [2, 3, 4])

    def test_2_not_in_list(self):
        test_list = [3, 4, 5, 6]
        self.assertNotIn(2, test_list)


class BlogPostTestCase(TestCase):

    def test_blog_change_view(self):
        blog = Blog.objects.create(title="test blog", description="test desc")

        new_title = "new title"
        data = {
            "title": new_title
        }
        self.client.post(f"/blog/{blog.id}/change", data=data)
        blog.refresh_from_db()

        self.assertEqual(blog.title, new_title)

    def test_blog_change_desc_view(self):
        blog = Blog.objects.create(title="test blog", description="test desc")

        new_desc = "new desc"
        data = {
            "description": new_desc
        }
        self.client.post(f"/blog/{blog.id}/change", data=data)
        blog.refresh_from_db()

        self.assertEqual(blog.description, new_desc)
