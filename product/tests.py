from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .models import Category, Product, Favorite, User
from .views import product, search, substitute, \
    save, delete, favorite, redirect


class TestProductUrls(SimpleTestCase):

    def test_search_url(self):
        url = reverse('product:search')
        self.assertEquals(resolve(url).func, search)

    def test_product_url(self):
        url = reverse('product:product', args=['1'])
        self.assertEquals(resolve(url).func, product)

    def test_substitute_url(self):
        url = reverse('product:substitute', args=['1'])
        self.assertEquals(resolve(url).func, substitute)

    def test_save_url(self):
        url = reverse('product:save', args=['1', '2'])
        self.assertEquals(resolve(url).func, save)

    def test_favorite_url(self):
        url = reverse('product:favorite')
        self.assertEquals(resolve(url).func, favorite)

    def test_delete_url(self):
        url = reverse('product:delete', args=['1'])
        self.assertEquals(resolve(url).func, delete)


class TestProductViews(TestCase):

    def setUp(self):
        user = User.objects.create(username='name',
                                   password='abdcef123')
        cat = Category.objects.create(name='name')
        prod = Product.objects.create(name='name',
                                      brands='brand',
                                      link='http://url.com',
                                      nutriscore='B',
                                      image='http://imageurl.com',
                                      fat=1,
                                      saturated_fat=1,
                                      sugars=1,
                                      salt=1)

        sub = Product.objects.create(name='nametest',
                                     brands='testbrand',
                                     link='http://testurl.com',
                                     nutriscore='A',
                                     image='http://testimageurl.com',
                                     fat=0,
                                     saturated_fat=0,
                                     sugars=0,
                                     salt=0)
        cat.products.add(prod)
        cat.products.add(sub)
        cat.save()
        Favorite.objects.create(user_id=user.id,
                                sub_id=sub.id,
                                prod_id=prod.id)

    def test_bad_search_view(self):
        response = self.client.get(reverse('product:search'))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(redirect('index.html'))

    def test_good_search_view(self):
        response = self.client.get(reverse('product:search'),
                                   {'query': 'name'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/search.html')

    def test_product_view(self):
        prod_id = Product.objects.first().id
        response = self.client.get(reverse('product:product',
                                           args=[prod_id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product.html')

    def test_substitute_view(self):
        sub_id = Product.objects.last().id
        response = self.client.get(reverse('product:substitute',
                                           args=[sub_id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/substitute.html')

    def test_save_logged_in_view(self):
        user = User.objects.first()
        self.client.force_login(user)
        prod = Product.objects.first().id
        sub_id = Product.objects.last().id
        response = self.client.get(reverse('product:save',
                                           args=[prod, sub_id]))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(redirect('index.html'))

    def test_favorite_logged_in_view(self):
        user = User.objects.first()
        self.client.force_login(user)
        response = self.client.get(reverse('product:favorite'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorite.html')

    def test_delete_logged_in_view(self):
        user = User.objects.first()
        self.client.force_login(user)
        fav = Favorite.objects.first().id
        response = self.client.get(reverse('product:delete',
                                           args=[fav]))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(redirect('index.html'))

    def test_save_logged_out_view(self):
        prod = Product.objects.first().id
        sub_id = Product.objects.last().id
        response = self.client.get(reverse('product:save',
                                           args=[prod, sub_id]))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(redirect('user/login.html'))

    def test_favorite_logged_out_view(self):
        response = self.client.get(reverse('product:favorite'))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(redirect('user/login.html'))

    def test_delete_logged_out_view(self):
        fav = Favorite.objects.first().id
        response = self.client.get(reverse('product:delete',
                                           args=[fav]))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(redirect('user/login.html'))


class TestStringModels(TestCase):

    def setUp(self):
        Category.objects.create(name='name')

    def test_string(self):
        cat = Category.objects.first()
        self.assertEqual(str(cat), 'name')
