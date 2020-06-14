from flask import url_for


class TestPage(object):
    def test_store_page(self, client):
        """ Cart page should respond with a success 200. """
        response = client.get(url_for('cart.cart_summary'))
        assert response.status_code == 200

    def test_store_page_title(self, client):
        """ Cart page should have title. """
        response = client.get(url_for('cart.cart_summary'))

        assert '<title>' in str(response.data)
