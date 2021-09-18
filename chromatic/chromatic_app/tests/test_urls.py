from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import home, register, upload
from django.contrib.auth.views import LoginView, LogoutView

class TestURLs(SimpleTestCase):
    def assert_url_is_resolved(self, url_name, view, class_based=False):
        if class_based:
            self.assertEquals(resolve(reverse(url_name)).func.view_class, view)
        else:
            self.assertEquals(resolve(reverse(url_name)).func, view)

    def test_home_url_is_resolved(self):
        self.assert_url_is_resolved('chromatic_app_home', home)

    def test_login_url_is_resolved(self):
        self.assert_url_is_resolved('chromatic_app_login', LoginView, class_based=True)

    def test_logout_url_is_resolved(self):
        self.assert_url_is_resolved('chromatic_app_logout', LogoutView, class_based=True)

    def test_register_url_is_resolved(self):
        self.assert_url_is_resolved('chromatic_app_register', register)

    def test_upload_url_is_resolved(self):
        self.assert_url_is_resolved('chromatic_app_upload', upload)