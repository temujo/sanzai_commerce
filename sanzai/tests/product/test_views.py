from flask import url_for


class TestPage(object):
    def test_store_page(self, client):
        """ Store page should respond with a success 200. """
        response = client.get(url_for('product.store'))
        assert response.status_code == 200

    def test_store_page_title(self, client):
        """ Store page should have title. """
        response = client.get(url_for('product.store'))

        assert '<title>' in str(response.data)
