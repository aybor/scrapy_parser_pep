import csv
import datetime as dt

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT

result_dic = {}


class PepParsePipeline:

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if item['status'] in result_dic.keys():
            result_dic[item['status']] += 1
        else:
            result_dic[item['status']] = 1
        return item

    def close_spider(self, spider):
        fieldnames = ['Статус', 'Количество']
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_name = (f'status_summary_'
                     f'{dt.datetime.now().strftime(DATETIME_FORMAT)}.csv')
        file_path = results_dir / file_name

        with open(file_path, 'w') as f:
            writer = csv.DictWriter(
                f,
                dialect='unix',
                fieldnames=fieldnames,
                delimiter=',',
                quoting=csv.QUOTE_NONE
            )
            writer.writeheader()
            for status, qty in result_dic.items():
                writer.writerow({'Статус': status, 'Количество': qty})
