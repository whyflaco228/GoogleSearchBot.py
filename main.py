from icrawler.builtin import GoogleImageCrawler


def google_img_downloader():
    filters = dict(
        type='photo',
        color='',
        size='large',
        license='noncommercial'
    )

    keyword = input('Введите то, что хотите найти: ')
    blackwhite = input('Хотите черное-белое изображение? Да/Нет: ')
    max_num = input('Введите число, сколько фотографий вы хотите найти: ')
    if int(max_num) > 10:
        print('Вы ввели чесло больше 10!Введите число сначала!')
        max_num = input('Введите число, сколько фотографий вы хотите найти: ')
    if (blackwhite == 'Да'):
        filters['color'] = 'blackandwhite'
    else:
        filters['color'] = 'color'
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    crawler.crawl(keyword=keyword, max_num=int(max_num), overwrite=True, filters=filters)



def main():
    google_img_downloader()


if __name__ == '__main__':
    main()
