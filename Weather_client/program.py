import requests
import bs4
import collections

weatherReport = collections.namedtuple('weatherReport', 'cond, temp, unit, loc')


def main():
    print_header()
    zipcode = input('What zipcode do you want to get the weather from?(i.e.79705)')
    html = get_html_from_web(zipcode)
    report = get_weather_from_html(html)
    print('The weather in {} is currently {} with a temperature of {} {}'.format(
        report.loc, report.cond, report.temp, report.unit))


def get_weather_from_html(html):
    # cityCss = 'div#location h1'
    # weatherConditionCss = 'div#curCond span.wx-value'
    # weatherTempCss = 'div#curTemp span.wx-data span.wx-value'
    # weatherScaleCss = 'div#curTemp span.wx-data span.wx-unit'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    unit = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = clean_up_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = clean_up_text(condition)
    temp = clean_up_text(temp)
    unit = clean_up_text(unit)

    # print(condition, temp, unit, loc)
    # return condition, temp, unit, loc
    report = weatherReport(cond=condition, temp=temp, unit=unit, loc=loc)
    return report


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def clean_up_text(text):
    if not text:
        return text

    text = text.strip()
    return text


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}'.format(zipcode)

    response = requests.get(url)

    # print (response.status_code)
    # print(response.text[0:250])

    return response.text


def print_header():
    print('---------------------------------------------------------------------------')
    print('                               Weather App')
    print('---------------------------------------------------------------------------')
    print()


if __name__ == '__main__':
    main()
