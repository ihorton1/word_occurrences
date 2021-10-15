from app.word_occurrences_blueprint.views import _remove_nonwords_from_list, _trim_punctuation_from_strings, _get_url_response, _parse_html_text
from app.word_occurrences_blueprint.utils.regex import leading_punctuation, trailing_punctuation

def test_parse_html_text():
    test_html = '<p><b>RMS <i>Titanic</i></b> was a British passenger <a href="/wiki/Ocean_liner" title="Ocean liner">liner</a> operated by the <a href="/wiki/White_Star_Line" title="White Star Line">White Star Line</a> that <a href="/wiki/Sinking_of_the_Titanic" title="Sinking of the Titanic">sank in the North Atlantic Ocean</a> on 15 April 1912, after striking an <a href="/wiki/Iceberg" title="Iceberg">iceberg</a> during her <a href="/wiki/Maiden_voyage" class="mw-redirect" title="Maiden voyage">maiden voyage</a> from <a href="/wiki/Southampton" title="Southampton">Southampton</a> to <a href="/wiki/New_York_City" title="New York City">New York City</a>.</p>'
    correct_result = 'RMS  Titanic  was a British passenger  liner  operated by the  White Star Line  that  sank in the North Atlantic Ocean  on 15 April 1912, after striking an  iceberg  during her  maiden voyage  from  Southampton  to  New York City .'
    test_result = _parse_html_text(test_html)
    assert test_result == correct_result

def test_remove_nonwords_from_list():
    test_list = ['test', 'test.', 'test123', '123', '.']
    correct_result = ['test', 'test.', 'test123']
    test_result = _remove_nonwords_from_list(test_list)
    assert test_result == correct_result

def test_trim_punctuation_from_strings_front():
    test_list = ['.test', '.!test', 'test']
    correct_result = ['test', 'test', 'test']
    test_result = _trim_punctuation_from_strings(test_list, leading_punctuation)
    assert test_result == correct_result

def test_trim_punctuation_from_strings_back():
    test_list = ['test.', 'test.!', "test's", 'test']
    correct_result = ['test', 'test', "test's", 'test']
    test_result = _trim_punctuation_from_strings(test_list, trailing_punctuation)
    print(test_result)
    assert test_result == correct_result


