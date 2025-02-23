import pytest

class Test_Navigation:
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
    
    def test_navigation_assertion(self):        
        page = self.page        
        page.goto("https://www.google.com")
        page.wait_for_load_state()
        assert "google" in page.url