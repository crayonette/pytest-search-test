from selene.support.shared import browser
from selene import have, be


def test_google_good_search(open_browser):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests'))


def test_google_bad_search(open_browser):
    browser.element('[name=q]').should(be.blank).type('fjghdfbdsnfvshdsjhskdf').press_enter()
    browser.element('[id=topstuff]').should(
        have.text('Your search - fjghdfbdsnfvshdsjhskdf - did not match any documents.'))
