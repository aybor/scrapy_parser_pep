import csv
import datetime as dt

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:

    def open_spider(self, spider):
        self.result_dic = {}

    def process_item(self, item, spider):
        if item['status'] in self.result_dic.keys():
            self.result_dic[item['status']] += 1
        else:
            self.result_dic[item['status']] = 1
        return item

    def close_spider(self, spider):
        results = [('Статус', 'Количество')]
        for status, qty in self.result_dic.items():
            results.append((status, qty))
        results.append(('Total', sum(self.result_dic.values())))

        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_name = (f'status_summary_'
                     f'{dt.datetime.now().strftime(DATETIME_FORMAT)}.csv')
        file_path = results_dir / file_name

        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(
                f,
                dialect='unix',
                delimiter=',',
                quoting=csv.QUOTE_NONE
            )
            writer.writerows(results)
