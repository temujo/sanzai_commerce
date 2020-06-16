from flask_wtf import Form
from wtforms import TextAreaField, TextField
from wtforms_components import Email
from wtforms.validators import DataRequired, Length


class ContactForm(Form):
    email = TextField("Таны E-mail хаяг юу бэ?",
                      [
                          Email(message="E-mail хаяг буруу формат-нд байна."),
                          DataRequired(message="Энэ талбар шаардлагтай."),
                          Length(3, 254)
                      ]
                      )
    message = TextAreaField("Таны асуулт/санал юу бэ?",
                            [
                                DataRequired(message="Энэ талбар шаардлагтай."),
                                Length(1, 8192)
                            ]
                            )
