from flask import url_for, jsonify

from lib.tests import assert_status_with_message


class TestContact(object):
    def test_contact_page(self, client):
        """ Contact page should respond with a success 200. """
        response = client.get(url_for('contact.index'))
        assert response.status_code == 200
