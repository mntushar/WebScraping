from Handler import *


def data_extract():
    # Extract article information
    for article in soup.find_all('article'):
        # Initialize variables
        title = ""
        url = ""
        summary = ""
        categories = []

        # Find title and URL
        title_tag = article.find('h2', class_='entry-title')
        if title_tag:
            title_link = title_tag.find('a')
            if title_link:
                title = title_link.text.strip()
                url = title_link.get('href', '')

        # Find summary
        entry_summary = article.find('div', class_='entry-summary')
        if entry_summary:
            summary_tag = entry_summary.find('p')
            if summary_tag:
                summary = summary_tag.text.strip()

        # Find categories
        footer_tag = article.find('footer', class_='entry-meta')
        if footer_tag:
            categories = [cat.text for cat in footer_tag.find_all('a', rel='category tag')]

        # Append article information to the list
        data.append({
            'title': title,
            'url': url,
            'summary': summary,
            'categories': ', '.join(categories)
        })


if __name__ == '__main__':
    url = 'https://blogs.findermaster.com/'
    response_handler = ResponseHandler()
    response = response_handler.request(url)
    scarping_handler = ScarpingHandler()
    soup = scarping_handler.beautiful_soup(response)
    if not soup:
        exit()

    # List to store article data 
    data = []

    data_extract()
    url = url + 'page/'
    for i in range(2, 4):
        changeUrl = url + str(i) + '/'
        print(changeUrl)
        response = response_handler.request(changeUrl)
        soup = scarping_handler.beautiful_soup(response)
        if not soup:
            pass
        data_extract()

    fileHandler = FileHandler()
    fileHandler.append_datas_csv('Data', data, ['title', 'url', 'summary', 'categories'])
