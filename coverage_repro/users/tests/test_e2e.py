import os
from channels.testing import ChannelsLiveServerTestCase
from django.test import tag, LiveServerTestCase
from playwright.sync_api import sync_playwright, expect


@tag("channels-live-server-test-case")
class TestUsingChannelsTest(ChannelsLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.close()
        cls.playwright.stop()

    def test_example(self):
        context = self.browser.new_context()
        page = context.new_page()
        page.goto(self.live_server_url + "/about/")
        expect(page.locator("text=On about page")).to_be_visible()

    def test_example_2(self):
        context = self.browser.new_context()
        page = context.new_page()
        page.goto(self.live_server_url + "/about/")
        expect(page.locator("text=On about")).to_be_visible()


@tag("live-server-test-case")
class TestUsingLiveServerTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.close()
        cls.playwright.stop()

    def test_example(self):
        context = self.browser.new_context()
        page = context.new_page()
        page.goto(self.live_server_url + "/about/")
        expect(page.locator("text=On about page")).to_be_visible()

    def test_example_2(self):
        context = self.browser.new_context()
        page = context.new_page()
        page.goto(self.live_server_url + "/about/")
        expect(page.locator("text=On about")).to_be_visible()
