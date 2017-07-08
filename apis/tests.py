from rest_framework import status
from rest_framework.test import APITestCase
base_url = '/api/v1/'
class LocationTests(APITestCase):
    def test_location_crud(self):
        """
        Ensure location crud working
        """

        url = base_url+'location'
        data = {'name':'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])
        lid = str(response.data['id'])
        url = base_url+'location/'+lid
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['id'], int(lid))
        data['name'] = 'test1'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

class DepartmentTests(APITestCase):
    def test_department_crud(self):
        """
        Ensure department crud working
        """

        url = base_url+'location'
        data = {'name':'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        url = base_url+'department'
        data = {'name':'test', 'location': response.data['id']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])
        did = str(response.data['id'])
        url = base_url+'department/'+did
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['id'], int(did))
        self.assertEqual(response.data['location']['id'], data['location'])
        data['name'] = 'test1'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

class CategoryTests(APITestCase):
    def test_category_crud(self):
        """
        Ensure category crud working
        """

        url = base_url+'location'
        data = {'name':'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        url = base_url+'department'
        data = {'name':'test', 'location': response.data['id']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        url = base_url+'category'
        data = {'name':'test', 'department': response.data['id']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])
        cid = str(response.data['id'])
        url = base_url+'category/'+cid
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['id'], int(cid))
        self.assertEqual(response.data['department']['id'], data['department'])
        data['name'] = 'test1'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)        

class SubcategoryTests(APITestCase):
    def test_subcategory_crud(self):
        """
        Ensure subcategory crud working
        """

        url = base_url+'location'
        data = {'name':'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        url = base_url+'department'
        data = {'name':'test', 'location': response.data['id']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        url = base_url+'category'
        data = {'name':'test', 'department': response.data['id']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        url = base_url+'subcategory'
        data = {'name':'test', 'category': response.data['id']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])
        sid = str(response.data['id'])
        url = base_url+'subcategory/'+sid
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['id'], int(sid))
        self.assertEqual(response.data['category']['id'], data['category'])
        data['name'] = 'test1'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)


class ProductTests(APITestCase):
    def test_product_crud(self):
        """
        Ensure product crud working
        """

        url = base_url+'location'
        data = {'name':'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        url = base_url+'department'
        data = {'name':'test', 'location': response.data['id']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        url = base_url+'category'
        data = {'name':'test', 'department': response.data['id']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        url = base_url+'subcategory'
        data = {'name':'test', 'category': response.data['id']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        url = base_url+'flatdata'
        data = {'name':'test', 'subcategory': response.data['id']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])
        pid = str(response.data['id'])
        url = base_url+'flatdata/'+pid
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['id'], int(pid))
        self.assertEqual(response.data['subcategory']['id'], data['subcategory'])
        data['name'] = 'test1'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)


