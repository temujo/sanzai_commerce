from sanzai.extensions import mail
from sanzai.blueprints.contact.tasks import deliver_contact_email


class TestTasks(object):
    def test_deliver_support_email(self):
        """ Deliver a contact email. """
        form = {
          'email': 'foo@bar.com',
          'message': 'Test message from Sanzai.'
        }

        with mail.record_messages() as outbox:
            deliver_contact_email(form['email'], form['message'])

            assert len(outbox) == 1
            assert form['email'] in outbox[0].body
