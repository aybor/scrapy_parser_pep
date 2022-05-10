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
        results = [('Статус', 'Количество')]
        for status, qty in result_dic.items():
            results.append((status, qty))
        results.append(('Total', sum(result_dic.values())))
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_name = f'status_summary_{dt.datetime.now().strftime(DATETIME_FORMAT)}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
